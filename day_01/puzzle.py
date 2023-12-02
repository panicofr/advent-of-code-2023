from __future__ import annotations


import string
import sys
import re

__all__ = ["extract_number_from_line", "improved_extract_number_from_line", "process_document"]

def extract_number_from_line(line: str) -> int:
    only_digits = re.findall("\d", line)
    return int(only_digits[0]) * 10 + int(only_digits[-1])


def improved_extract_number_from_line(line: str) -> int:
    keys = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    reg_exp = f"(?=(\d|{'|'.join(keys)}))"
    all_digits = re.findall(reg_exp, line)
    converted_digits = list(map(lambda i : int(i) if i.isdigit() else keys.index(i) + 1, all_digits))
    return int(converted_digits[0]) * 10 + int(converted_digits[-1])


def process_document(document: str, improved: bool = False) -> int:
    repl = lambda line : improved_extract_number_from_line(line) if improved else extract_number_from_line(line)
    return sum(map(repl, document.split("\n")))


if __name__ == "__main__":
    improved = len(sys.argv) > 1 and sys.argv[1] == "--improved"
    print(process_document(open("input.txt").read(), improved))
