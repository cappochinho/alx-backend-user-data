#!/usr/bin/env python3
"""Task 0: Regex-ing"""


from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str):
    """Filters data using a regex"""

    for field in fields:
        pattern = r'({0})=([^{1}]+)'.format(field, re.escape(separator))
        message = re.sub(pattern, r'\1={}'.format(redaction), message)
    return message