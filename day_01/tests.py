import unittest

from puzzle import extract_number_from_line, improved_extract_number_from_line, process_document

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

    def test_improved_extract_number_from_line(self):
        line = "two1nine"
        self.assertEqual(improved_extract_number_from_line(line), 29)

    def test_improved_extract_number_from_line_with_overlapping_numbers(self):
        line = "eighthree"
        self.assertEqual(improved_extract_number_from_line(line), 83)

    def test_improved_extract_number_from_line_with_digits_only_line(self):
        line = "716"
        self.assertEqual(improved_extract_number_from_line(line), 76)

    def test_process_document(self):
        document = "\n".join(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f",  "treb7uchet"])
        self.assertEqual(process_document(document), 142)

    def test_process_document_improved(self):
        document = (
            "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n"
            "4nineeightseven2\nzoneight234\n7pqrstsixteen"
        )
        self.assertEqual(process_document(document, improved=True), 281)
