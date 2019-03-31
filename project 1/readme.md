# OOP Demonstration Project

This project is an example of OOP programming. The data (data about the avengers) is in CSV format. The data is ingested, processing the data and then writes out Markdown file on the most popular avengers. The project displays a full project which includes unit tests. 

### Script Outputs

The outputs for the processed CSV and the Markdown report.

### OOP
The `avenger.py` module contains the `Avenger` class. It should implement methods for all of the fields found in the input CSV.  In addition to implementing methods for each field, implement the method `to_markdown` which generates the Markdown markup described in the midterm project. 

### Util Package

The `util` package should contain all the utility functions needed for manipulating dates and converting values. 

### Unit tests

The `run_tests.py` script should run all of the unit tests in the `tests` directory.  Here are the requirements for implementing unit tests. 

* Implement unit test for each method in the `Avenger` class to make sure you are returning the expected output.  Make sure to test the `to_markdown` method as well. 
* Each function in the `util` package should have one or more unit tests.  The unit tests should test both valid and invalid inputs. 
* You should not have any failing unit tests when you submit the project. 

### Prerequisites

Python


```nohighlight
msds510-final/
├── README.md
├── data
│   ├── interim
│   ├── processed
│   │   └── avengers_processed.csv
│   └── raw
│       └── avengers.csv
├── reports
└── src
    ├── make_report.py
    ├── msds510
    │   ├── __init__.py
    │   ├── avenger.py
    │   └── utils
    │       ├── __init__.py
    │       ├── conversion.py
    │       └── date.py
    ├── process_csv.py
    ├── run_tests.py
    └── tests
        ├── __init__.py
        ├── test_avenger.py
        ├── test_util_conversion.py
        └── test_util_date.py
```
