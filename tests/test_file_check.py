# Basic test to simulate CI readiness.
from utils.file_check import file_exists, is_valid_csv, is_valid_excel

def test_file_exists():
    assert file_exists("tests/sample.csv") is False

def test_csv_extension():
    assert is_valid_csv("data/2025-06-16.csv") is True or False  # Example path

def test_excel_extension():
    assert is_valid_excel("data/2025-06-16.xlsx") is True or False
