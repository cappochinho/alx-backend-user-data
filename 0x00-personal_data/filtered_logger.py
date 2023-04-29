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

    REDACTION = "***"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        message: str = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)
