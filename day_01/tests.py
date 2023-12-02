import unittest

from puzzle import extract_number_from_line, process_document

class TestCase(unittest.TestCase):
    def test_extract_number_from_line(self):
        line = "1abc2"
        self.assertEqual(extract_number_from_line(line), 12)

    def test_number_from_line_with_multiple_digits(self):
        line = "a1b2c3d4e5f"
        self.assertEqual(extract_number_from_line(line), 15)

    def test_extract_number_from_line_with_single_digit(self):
        line = "treb7uchet"
        self.assertEqual(extract_number_from_line(line), 77)

    def test_process_document(self):
        document = "\n".join(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f",  "treb7uchet"])
        self.assertEqual(process_document(document), 142)
