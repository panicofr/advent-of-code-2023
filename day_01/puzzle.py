from __future__ import annotations

import string

__all__ = ["extract_number_from_line"]

def extract_number_from_line(line: str) -> int:
    table = str.maketrans("", "", string.ascii_letters)
    only_digits = line.translate(table)
    return int(only_digits[0]) * 10 + int(only_digits[-1])

def process_document(document: str) -> int:
    return sum(extract_number_from_line(line) for line in document.split("\n"))


if __name__ == "__main__":
    print(process_document(open("input.txt").read()))
