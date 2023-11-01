from datetime import datetime
import csv, threading, queue, time

class CsvLogger:
    """
    CsvLogger is a threaded logging utility that writes log entries to a CSV file 
    asynchronously, without blocking the main thread of execution.

    Each log entry includes the current time, a level indicating the type of 
    message, and the message itself.

    Attributes:
        logfile (file): The file object for the log file.
        logwriter (csv.writer): CSV writer object for writing to the log file.
        output_to_console (bool): Whether to also print log messages to the console.
        queue (queue.Queue): Queue to store log messages before they're written to the file.
        thread (threading.Thread): Worker thread that handles writing messages to the file.

    Methods:
        log(level, msg): Logs a message with a specified level.
        close(): Ensures that all log messages are written to the file before the program exits.
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

        self.queue = queue.Queue()
        self.thread = threading.Thread(target=self.write)
        self.thread.daemon = True
        self.thread.start()

    def write(self):
        """
        Continuously writes log entries from the queue to the CSV file.

        The method retrieves log entries from the internal queue and attempts to 
        write them to the file. If writing fails due to an IOError, the method 
        will retry the operation for a maximum of 4 times, using an 
        exponential backoff strategy.

        If the queue contains the sentinel value "TERMINATE", the method will 
        stop processing and exit.
        """

        while True:
            log_entry = self.queue.get()
            if log_entry == "TERMINATE":
                break

            for attempt in range(4):
                try:
                    self.logwriter.writerow(log_entry)
                    self.logfile.flush()
                    break
                except IOError as e:
                    if self.output_to_console:
                        print(f"Failed to write log. Attempt {attempt + 1}/{4}. Error: {e}")
                    time.sleep(2 ** (attempt + 1))

            else:
                if self.output_to_console:
                    print(f"Failed to write log: Dropping log entry.")

    def log(self, level, msg):
        """
        Logs a message with the specified level to the CSV file and, 
        if enabled, prints it to the console.

        Parameters:
            level (str): Level/type of the log message (e.g., 'INFO', 'ERROR').
            msg (str): The actual log message content.
        """

        log_entry = [datetime.now().strftime('%H:%M:%S'), level.upper(), msg]

        self.queue.put(log_entry)
        
        if self.output_to_console:
            padding = ' ' * (4 - len(level.upper()) % 4)
            print('\t'.join([datetime.now().strftime('%H:%M:%S'), level.upper() + padding, msg]))

    def close(self):
        """
        Should be called to ensure that all log messages in the queue 
        are written to the file before the program exits. Also, it gracefully 
        shuts down the worker thread and closes the log file.
        """

        self.queue.put("TERMINATE")
        self.thread.join()
        self.logfile.close()
