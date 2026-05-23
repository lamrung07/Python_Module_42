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
            
        
if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===\n")
    
    #TEST NumericProcessor()________________________
    num_proc = NumericProcessor()
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {num_proc.validate([4,5.00,10,9])}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")
    try:
        num_proc.ingest("foo")  # type: ignore[arg-type]
    except Exception as e:
        print(f"{e}")
    data_numeric = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_numeric}")
    num_proc.ingest(data_numeric)
    print("Extracting 3 values...")
    for i in range (3):
        rank, value = num_proc.output()
        print(f"Numeric value {rank}: {value}")
        
    #TEST TextProcessor()______________________
    text_proc = TextProcessor()
    print("\nTesting Text Processor...")
    print(f"Trying to validate input '42': {text_proc.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    data_txt = ['Hello', 'Nexus', 'World']
    text_proc.ingest(data_txt)
    print("Extracting 1 value...")
    rank, value = text_proc.output()
    print(f"Text value {rank}: {value}")
    
    #TEST LOGProcessor()______________________
    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")
    print("Processing data: [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}", end='')
    print(", {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]")
    log_proc.ingest([{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                    {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}])
    print("Extracting 2 values...")
    for i in range(2):
        rank, value = log_proc.output()
        print(f"Log entry {rank}: {value}")