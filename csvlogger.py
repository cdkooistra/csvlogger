from datetime import datetime as dt
import csv

class CsvLogger(object):
    def __init__(self, filename):
        self.logfile = open(filename, 'w', newline='')
        self.logwriter = csv.writer(self.logfile)
        self.logwriter.writerow(['Time', 'Level', 'Message'])

    def info(self, msg):
        self.logwriter.writerow([dt.now().strftime('%H:%M:%S'), 'INFO', msg])
        self.logfile.flush()

    def success(self, msg):
        self.logwriter.writerow([dt.now().strftime('%H:%M:%S'), 'SUCCESS', msg])
        self.logfile.flush()

    def error(self, msg):
        self.logwriter.writerow([dt.now().strftime('%H:%M:%S'), 'ERROR', msg])
        self.logfile.flush()

    def warning(self, msg):
        self.logwriter.writerow([dt.now().strftime('%H:%M:%S'), 'WARNING', msg])
        self.logfile.flush()
