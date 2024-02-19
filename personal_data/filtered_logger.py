#!/usr/bin/env python3
"""
0. Regex-ing
"""

import re


def filter_datum(fields, redaction, message, separator):
    return re.sub(fr'({"|".join(fields)})=[^{separator}]+',
                  fr'\1={redaction}',
                  message)
