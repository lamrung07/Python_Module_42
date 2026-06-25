#!/usr/bin/env python3
import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.storage: list[typing.Any] = []
        self.rank = 0
        self.total_processed = 0
        pass

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self, nb: int) -> list[tuple[int, str]]:
        result = []
        for _ in range(nb):
            if not self.storage:
                break
            value = self.storage.pop(0)
            result.append((self.rank, value))
            self.rank += 1
        return result

    "Data Stream helpers"
    def get_remaining(self) -> int:
        return len(self.storage)

    def get_total_processed(self) -> int:
        return self.total_processed


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if type(data) in (int, float):
            return True
        if type(data) is list:
            for item in data:
                if type(item) not in (int, float):
                    return False
            return True
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper numeric data")
        if type(data) is list:
            for item in data:
                self.storage.append(str(item))
                self.total_processed += 1
        else:
            self.storage.append(str(data))
            self.total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if type(data) is str:
            return True
        if type(data) is list:
            for item in data:
                if type(item) is not str:
                    return False
            return True
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper text data")
        if type(data) is list:
            for item in data:
                self.storage.append(item)
                self.total_processed += 1
        else:
            self.storage.append(data)
            self.total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if type(data) is dict:
            for key, val in data.items():
                if not (type(key) is str and type(val) is str):
                    return False
            return True
        if type(data) is list:
            for item in data:
                for key, val in item.items():
                    if not (type(key) is str and type(val) is str):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper log data")

        # isinstance(obj, type)->bool: checks obj is an instance of type
        if isinstance(data, dict):
            data = [data]
        for item in data:
            self.storage.append(f"{item['log_level']}: {item['log_message']}")
            self.total_processed += 1


# ExportPlugin Protocol
class ExportPlugin(typing.Protocol):
    @abc.abstractmethod
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        i = len(data) - 1
        for rank, value in data:
            print(f"{value}", end='')
            if i:
                print(",", end='')
            i -= 1
        print()


class JSONExportPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        i = len(data) - 1
        print("{", end='')
        for rank, value in data:
            print(f"'item_{rank}': '{value}'", end='')
            if i:
                print(",", end='')
            i -= 1
        print("}")


# Data Stream
class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """This method register a new data processor"""
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        """
        This method analyze each  element of the list
        received as a parameter and send it to the
        appropriate registered data processor
        """
        for element in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - "
                      f"Can't process element in stream: {element}")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """
        Extracts nb outputs from each processor
        Sends them to an export plugin
        """
        for proc in self.processors:
            res = proc.output(nb)
            if res:
                plugin.process_output(res)

    def print_processors_stats(self) -> None:
        """This method print the stream statistics"""
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = type(proc).__name__
            if name == 'NumericProcessor':
                proc_name = 'Numeric Processor'
            elif name == 'TextProcessor':
                proc_name = 'Text Processor'
            elif name == 'LogProcessor':
                proc_name = 'Log Processor'
            print(f"{proc_name}: total "
                  f"{proc.get_total_processed()} items processed,"
                  f"remaining {proc.get_remaining()} on processor")


if __name__ == "__main__":

    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()
    print("")
    print("Registering Processors\n")
    proc_num = NumericProcessor()
    proc_text = TextProcessor()
    proc_log = LogProcessor()

    '''____Register first batch and process the data_____'''
    batch: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING",
             "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO",
             "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}\n")
    stream.register_processor(proc_num)
    stream.register_processor(proc_text)
    stream.register_processor(proc_log)
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExportPlugin())
    print()
    stream.print_processors_stats()

    '''____Register second batch and process the data_____'''
    batch1 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR",
             "log_message": "500 server crash"},
            {"log_level": "NOTICE",
             "log_message": "Certificate expires in 10 days"},
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"\nSend another batch of data: {batch1}\n")

    stream.process_stream(batch1)
    stream.print_processors_stats()
    print()
    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExportPlugin())
    print()
    stream.print_processors_stats()
