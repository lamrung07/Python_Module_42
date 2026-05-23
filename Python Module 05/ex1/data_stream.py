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
        self.manager: dict[str, typing.Any] = {}
    def register_processor(self, proc: DataProcessor) -> None:
        pass
    def process_stream(self, stream: list[typing.Any]) -> None:
        pass
    def print_processors_stats(self) -> None:
        pass
    
if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...\n== DataStream statistics ==")
    