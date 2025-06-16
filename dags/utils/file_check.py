#Helper functions for checking file presence and format.
import os

def file_exists(path: str) -> bool:
    return os.path.isfile(path)

def is_valid_csv(path: str) -> bool:
    return path.endswith(".csv") and file_exists(path)

def is_valid_excel(path: str) -> bool:
    return path.endswith((".xls", ".xlsx")) and file_exists(path)
