import pandas as pd
from abc import ABC, abstractmethod
import csv

class ReportHandler(ABC):
    """Abstract handler in the chain of responsibility."""

    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, file_path):
        if self._next_handler:
            return self._next_handler.handle(file_path)
        return None

class StandardCSVHandler(ReportHandler):
    """Handler for standard CSV format."""

    def handle(self, file_path):
        try:
            data = pd.read_csv(file_path)
            print(f"Processed {file_path} with StandardCSVHandler")
            return data
        except Exception as e:
            return super().handle(file_path)

class KeyValueCSVHandler(ReportHandler):
    """Handler for key-value pair CSV format."""

    def handle(self, file_path):
        try:
            with open(file_path, mode='r') as infile:
                reader = csv.reader(infile, delimiter=';')
                data = {rows[0].strip(): rows[1].strip() for rows in reader}
            df = pd.DataFrame([data])
            print(f"Processed {file_path} with KeyValueCSVHandler")
            return df
        except Exception as e:
            return super().handle(file_path)

class PipeDelimitedCSVHandler(ReportHandler):
    """Handler for pipe-delimited CSV format."""

    def handle(self, file_path):
        try:
            data = pd.read_csv(file_path, sep='|', header=None)
            print(f"Processed {file_path} with PipeDelimitedCSVHandler")
            return data
        except Exception as e:
            return super().handle(file_path)

# Client code
if __name__ == "__main__":
    file_paths = ["data/report1.csv", "data/report2.csv", "data/report3.csv"]

    # Set up the chain
    handler1 = StandardCSVHandler()
    handler2 = KeyValueCSVHandler()
    handler3 = PipeDelimitedCSVHandler()
    handler1.set_next(handler2).set_next(handler3)

    # Process files
    for file_path in file_paths:
        data = handler1.handle(file_path)
        if data is not None:
            # Do something with the data
            print(data)
