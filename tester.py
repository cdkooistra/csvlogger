import time
from csvlogger import CsvLogger

def test_csv_logger():
    # Initializing CsvLogger with console output
    logger = CsvLogger("test_log.csv", output_to_console=True)

    # Simple log entries
    logger.log("INFO", "Starting the logger test.")
    logger.log("WARNING", "This is a warning message.")
    logger.log("ERROR", "An error occurred!")
    logger.log("SUCCESS", "A successful event occurred!")

    # Simulating a high frequency of logs
    for i in range(1000):
        logger.log("INFO", f"High frequency log message {i}")
        time.sleep(0.001)  # Introducing a tiny sleep to simulate some processing

    logger.log("INFO", "Ending the logger test.")

    # Ensure that all logs are written and worker thread is shut down
    logger.close()

    print("\nTest completed! Check test_log.csv and console for logs.")

if __name__ == "__main__":
    test_csv_logger()
