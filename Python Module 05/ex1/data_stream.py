#!/usr/bin/env python3
import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.storage: list[typing.Any] = []
        self.rank: int = 0
        self.total_processed: int = 0
        pass

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> typing.Tuple[int, str]:
        rank = self.rank
        self.rank += 1
        value = self.storage[0]
        del (self.storage[0])
        return (rank, value)

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
        if isinstance(data, dict):
            data = [data]
        for item in data:
            self.storage.append(f"{item['log_level']}: {item['log_message']}")
            self.total_processed += 1


class DataStream():
    """
    Receive a stream of data different types
    Route each element to the appropriate data processor using
    polymorphic behavior
    """
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

            # Case if no processor can handle the data element
            if not handled:
                print(f"DataStream error - "
                      f"Can't process element in stream: {element}")

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
    print("=== Code Nexus - Data Stream ===\n")
    stream = DataStream()

    # Initial stats handles input streams correctly. You need now to handle
    print("Initialize Data Stream ...")
    stream.print_processors_stats()
    print()

    # Register only NumericProcessor
    print("Registering Numeric Processor\n")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)

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

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    print('')
    stream.print_processors_stats()
    print('')

    # ── Register remaining processors ─────────
    print("Registering other data processors")
    txt_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(txt_proc)
    stream.register_processor(log_proc)

    print("Send the same batch again")
    stream.process_stream(batch)
    print('')
    stream.print_processors_stats()
    print('')

    # ── Consume elements ──────────────────────
    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for i in range(3):
        rank, value = num_proc.output()
        # print(f"  Numeric value {rank}: {value}")
    for i in range(2):
        rank, value = txt_proc.output()
        # print(f"  Text value {rank}: {value}")
    for i in range(1):
        rank, value = log_proc.output()
        # print(f"  Log entry {rank}: {value}")
    print()
    stream.print_processors_stats()
