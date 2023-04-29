#!/usr/bin/env python3
"""Task 0: Regex-ing"""


from typing import List
import re
import logging


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Filters data using a regex"""

    for field in fields:
        pattern: str = r'({0})=([^{1}]+)'.format(field, re.escape(separator))
        message: str = re.sub(pattern, r'\1={}'.format(redaction), message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION: str = "***"
    FORMAT: str
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR: str = ";"

    def __init__(self, fields: List[str]):
        """Init method: Initializes a new instance of the class"""

        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """Outputs the correct format of the log records"""

        message: str = super().format(record)
        output: tuple = self.fields, self.REDACTION, message, self.SEPARATOR
        return filter_datum(output[0], output[1], output[2])
