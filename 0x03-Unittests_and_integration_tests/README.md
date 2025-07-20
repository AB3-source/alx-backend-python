# 0x03. Unittests and Integration Tests

## 📌 Description

This project is focused on writing unit and integration tests in Python. It demonstrates how to test individual functions, mock external dependencies, and validate the behavior of larger systems. It is designed to improve software reliability and maintainability through test-driven practices.

The key concepts covered include:

- Writing unit tests with the `unittest` module
- Parameterizing test cases using `parameterized`
- Mocking I/O and network calls using `unittest.mock`
- Creating integration tests to verify end-to-end functionality
- Documenting and annotating all modules, classes, and functions

---

## 📂 Project Structure
   0x03-Unittests_and_integration_tests/
    ├── utils.py
    ├── client.py
    ├── fixtures.py
    ├── test_utils.py  ← unit test for utility functions
    └── README.md      ← project documentation
---

## ✅ Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- PEP8 compliant (pycodestyle v2.5)
- All files are executable
- All functions and methods are type-annotated
- All code has proper docstrings

---

## 🧪 Running Tests

To run the tests in this directory, use:

```bash
python3 -m unittest discover

##   run a specific test file
python3 -m unittest test_utils.py
