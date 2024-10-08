
import csv
from collections import namedtuple

class CSVContextManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.headers = None
        self.NamedTuple = None

    def __enter__(self):
        # Open the CSV file and create a reader object
        self.file = open(self.file_name, mode='r', newline='', encoding='utf-8')
        self.reader = csv.reader(self.file)

        # Read the header row
        column_names = next(self.reader)

        #Names with spaces aren't allowed in NamedTuples. So, spaces are eliminated.
        column_names = [name.replace(' ', '_') for name in column_names]

        # Create a named tuple class with the header names
        self.NamedTuple = namedtuple('Row', column_names)

        return self

    def __iter__(self):
        # Iterate through the rows and yield named tuples
        for row in self.reader:
            yield self.NamedTuple(*row)

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the file when exiting the context
        self.file.close()

with CSVContextManager("/content/nyc_parking_tickets_extract.csv") as csv_manager:
      for row in csv_manager:
          print(row)

# Goal2

from contextlib import contextmanager

@contextmanager
def csv_context_manager(file_name):
    """Context manager to read a CSV file and yield rows as named tuples."""
    file = open(file_name, mode='r', newline='', encoding='utf-8')
    reader = csv.reader(file)

    try:
        # Read the header row
        column_names = next(reader)

        # Remove spaces in column names
        column_names = [name.replace(' ', '_') for name in column_names]

        # Create a named tuple class with the header names
        NamedTuple = namedtuple('Row', column_names)


        def iter_rows():
            for row in reader:
                yield NamedTuple(*row)

        # Yield the iterator
        yield iter_rows()
    finally:
        file.close()


csv_file = '/content/nyc_parking_tickets_extract.csv'
with csv_context_manager(csv_file) as rows:
  for row in rows:
    print(row)

