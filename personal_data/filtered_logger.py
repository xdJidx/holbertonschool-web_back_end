#!/usr/bin/env python3
"""
Personal data
"""

import re
import logging
from typing import Tuple
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection
import bcrypt

PII_FIELDS: Tuple[str, ...] = ["name", "email", "phone_number", "address",
                               "social_security_number"]


def filter_datum(fields: Tuple[str, ...], redaction: str, message: str,
                 separator: str) -> str:
    """
    Returns the log message obfuscated
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is
      separating all fields in the log line
    """
    return re.sub(fr'({"|".join(fields)})=[^{separator}]+',
                  fr'\1={redaction}',
                  message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Tuple[str, ...]):
        """Initializes a RedactingFormatter instance with a list
          of fields to obfuscate.

        Args:
            fields (List[str]): A list of strings representing
            the fields to obfuscate in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the log record, obfuscating specified fields
        in the log message.

        Args:
            record (logging.LogRecord): The log record to be formatted.

        Returns:
            str: The formatted log message.
        """
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object named "user_data" with
       specified configurations.

    Returns:
        logging.Logger: The configured logger.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """Returns a connector to the database.

    Returns:
        mysql.connector.connection.MySQLConnection: Database connector object.
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')

    db = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )

    return db


def main():
    # Connectez-vous à la base de données et exécutez un dump SQL depuis user_data.csv
    db = get_db()
    cursor = db.cursor()

    # Remplacez user_data.csv par le chemin réel de votre fichier CSV
    with open('/home/jerome/holbertonschool-web_back_end/personal_data/filtered_logger.py', 'r') :
        cursor.execute("USE my_db;")
        cursor.execute("DROP TABLE IF EXISTS users;")
        cursor.execute("CREATE TABLE users (name VARCHAR(256), email VARCHAR(256), phone_number VARCHAR(16), address VARCHAR(256), social_security_number VARCHAR(16));")
        cursor.execute("LOAD DATA LOCAL INFILE 'user_data.csv' INTO TABLE users FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n' IGNORE 1 ROWS;")

    cursor.close()
    db.close()

    # Exécutez le script avec les variables d'environnement correctement définies
    os.system("PERSONAL_DATA_DB_USERNAME=root_user PERSONAL_DATA_DB_PASSWORD=root_pwd PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py")


if __name__ == "__main__":
    main()
