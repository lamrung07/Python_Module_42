#!/usr/bin/env python3
import typing
import abc

class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.storage = []
        self.rank = 0
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
        del(self.storage[0])
        return (rank, value)
        

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
        else:
            self.storage.append(str(data))


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
        else:
            self.storage.append(data)


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
    def ingest(self, data: dict[str:str] | list[dict[str:str]]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper log data")
        if type(data) is dict:
            data = [data]
        for item in data:
            self.storage.append(f"{item['log_level']}: {item['log_message']}")
            
class DataStream():
    def __init__(self):
        self.processors: list[DataProcessor] = []
    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)
    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            validated = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    validated = True
                    break
            if not validated:
                print(f"DataStream error - Can't process element in stream: {element}")
    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            print(proc.output())
    
if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...\n== DataStream statistics ==")
    stream = DataStream()
    numeric_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    print("Registering Numeric Processor")
    stream.register_processor(numeric_proc)
    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)