import re
from typing import List
import logging
PII_FIELDS=("name","email","phone","ssn","password")
def get_logger()->logging.Logger:
        Logger=logging.get_logger("user_data")
        Logger.setLevel(logging.INFO)
        Logger.propagate=False
        streamHandler=logging.StreamHandler( )# out put in the console 
        streamHandler.setFormatter(RedactingFormatter(PII_FIELDS))
        Logger.addHandler(streamHandler)
        return Logger
class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        # Get the log message using the parent class' format method
        message = super().format(record)
        
        # Redact sensitive fields using filter_datum
        return self.filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)
    
    @staticmethod
    def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
        """Filters the specified fields in the message, replacing their values with the redaction."""
        for field in fields:
            message = re.sub(f"{field}=.*?{separator}", f"{field}={redaction}{separator}", message)
        return message
    
    def get_logger(self):
        Logger=logging.get_logger("user_data")
        Logger.setLevel(logging.INFO)
        Logger.propagate=False
        streamHandler=logging.StreamHandler( )
        Logger.setFormatter(streamHandler)
        return Logger
