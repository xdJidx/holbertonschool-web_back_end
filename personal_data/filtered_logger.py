#!/usr/bin/env python3
"""
0. Regex-ing
(.*?)= value field use motig no gourmand
"""

import re
import os
import logging
from typing import List
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


""" Task O: """


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscate sensitive information in a log message."""
    # Création d'une expression régulière pour rechercher les champs ds le msg
    # Concaténation des champs avec le séparateur '|'
    pattern = "|".join(fields)
    # Expression régulière complète
    regex = f"({pattern})=(.*?){separator}"
    # Remplacement des occurrences des champs/la value de redaction ds le msg
    return re.sub(regex, f"\\1={redaction}{separator}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super().__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Format method to filter sensitive values """
        # Filtrer les values sensibles dans le msg de journal
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        # Call méthode de formatage de la cls parent pr compléter le formatage
        return super().format(record)


'''Task 2 - Create logger '''


def get_logger() -> logging.Logger:
    """ Returns a logging object """
    # Création de l'objet Logger
    logger = logging.getLogger('user_data')
    # Journalise les msg ayant un niveau INFO
    logger.setLevel(logging.INFO)
    # msg du logger non transmis aux loggers parents
    logger.propagate = False
    # Création d'un gestionnaire de flux pour les msg vers la sortie
    handler = logging.StreamHandler()
    # Défir un formateur de message pour masquer les champs sensibles
    formatter = RedactingFormatter(["email", "password"])
    handler.setFormatter(formatter)
    # Ajout du gestionnaire de flux au logger
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to a database"""
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    hosting = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    database = mysql.connector.connect(
        host=hosting,
        user=username,
        password=password,
        database=db_name
    )

    return database