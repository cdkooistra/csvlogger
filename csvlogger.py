from datetime import datetime
import csv

class CsvLogger:
    """
    CsvLogger is a simple logging utility that writes log entries to a CSV file.

    Each log entry includes the current time, a level indicating the type of 
    message, and the message itself.

    Attributes:
        logfile (file): The file object for the log file.
        logwriter (csv.writer): CSV writer object for writing to the log file.
        output_to_console (bool): Whether to also print log messages to the console.

    Methods:
        log(level, msg): Logs a message with level passed as an argument.
    """
    def __init__(self, filename, output_to_console=False):
        """
        Constructs a CsvLogger that writes to the specified file.

        Parameters:
            filename (str): the name of the log file.
            output_to_console (bool, optional): print log messages to console,
                defaults to False.
        """
        self.logfile = open(filename, 'w', newline='')
        self.logwriter = csv.writer(self.logfile)
        self.logwriter.writerow(['Time', 'Level', 'Message'])
        self.output_to_console = output_to_console

    def log(self, level, msg):
        """Logs a message with the specified level."""
        log_entry = [datetime.now().strftime('%H:%M:%S'), level.upper(), msg]
        self.logwriter.writerow(log_entry)
        self.logfile.flush()
        
        if self.output_to_console:
            level_upper = level.upper()
            spaces_needed = 4 - len(level_upper) % 4
            spaces = ' ' * spaces_needed
            formatted_log_entry = [datetime.now().strftime('%H:%M:%S'), level_upper + spaces, msg]
            print('\t'.join(formatted_log_entry))
