# CSV Logger
A short Python script that enables logging output into a .csv file.

### Installation
Uses Python Standard Library, so does not require any additional installation.

### Usage
To use in any Python script, import as shown here:

    from csvlogger import CsvLogger

Then initialize object with the name of ur desired csv log and whether or not to output to console (False by default)

    logger = CsvLogger(ur_desired_file_name_here.csv, output_to_console=True/False)

Finally, call the methods to start logging!

    logger.log('info', "Enjoy the logs!")

### Changelog
* V1.0 - 230803,    
    * created basic csv log functionalities
    * added docstrings
* V1.1 - 230804,    
    * added possibility to output logs to console 
    * dynamic levels support (keep amount of chars under 8 for the sake of neat logs)!
* V1.2 - 230818,
    * changed class to work asynchronously for all I/O operations
    * added error handling (and a retry mechanism) for writing to the .csv file
    * expanded docstrings

      