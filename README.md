# S13_EPAI_Context_Managers
The following objectives were implemented in this assignment. Most of it can be done with any AI code tool, but they fail to understand that Named Tuples can't be initiated with spaces between column names. A simple list comprehension can fix that issue.

# Context Manager Creation
Create a context manager that produces data from each CSV file as named tuples. The field names in the named tuples should correspond to the headers in the CSV files.

# CSV Parsing
Utilize the csv module's reader function to parse the CSV data.

# Generic Implementation
Ensure that the context manager is generic, requiring only the file name as input, without any additional configuration or hardcoding.

# Lazy Iteration
Design the context manager to produce lazy iterators, allowing for efficient row-wise access to the data.

# Generator Function Usage
Reproduce the previous work using a generator function combined with the contextlib.contextmanager decorator to simplify context management.
