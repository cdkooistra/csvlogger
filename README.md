# CSV Logger
A short Python script that enables logging output into a .csv file.
Uses Python Standard Library, so does not require any additional installation.

## Usage
To use in any Python script, import as shown here:

    from csvlogger import CsvLogger

Then initialize object with the name of ur desired csv log as its only argument

    logger = CsvLogger(ur_desired_file_name_here.csv)

Finally, call the methods to start logging!

    logger.info("Enjoy the logs!")

## Changelog
* V1.0 - 230804,    created basic csv log functionalities, added docstrings