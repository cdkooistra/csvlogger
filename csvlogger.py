from datetime import datetime as dt
import csv

class CsvLogger(object):
    """
    CsvLogger is a simple logging utility that writes log entries to a CSV file.

    Each log entry includes the current time, a level indicating the type of 
    message, and the message itself.

    Attributes:
        logfile (file): The file object for the log file.
        logwriter (csv.writer): CSV writer object for writing to the log file.

    Methods:
        info(msg): Logs an informational message.
        success(msg): Logs a success message.
        error(msg): Logs an error message.
        warning(msg): Logs a warning message.
    """
    def __init__(self, filename):
        """
        Constructs a CsvLogger that writes to the specified csv file.

        Parameters:
            filename (str): The name of the log file.
        """
        self.logfile = open(filename, 'w', newline='')
        self.logwriter = csv.writer(self.logfile)
        self.logwriter.writerow(['Time', 'Level', 'Message'])

    def info(self, msg):
        """Logs an informational message."""
        self.logwriter.writerow([dt.now().strftime('%H:%M:%S'), 'INFO', msg])
        self.logfile.flush()

    def success(self, msg):
        """Logs a success message."""
        self.logwriter.writerow([dt.now().strftime('%H:%M:%S'), 'SUCCESS', msg])
        self.logfile.flush()

    def error(self, msg):
        """Logs an error message."""
        self.logwriter.writerow([dt.now().strftime('%H:%M:%S'), 'ERROR', msg])
        self.logfile.flush()

    def warning(self, msg):
        """Logs a warning message."""
        self.logwriter.writerow([dt.now().strftime('%H:%M:%S'), 'WARNING', msg])
        self.logfile.flush()
