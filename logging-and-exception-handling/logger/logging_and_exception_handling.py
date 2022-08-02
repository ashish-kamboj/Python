from logger.variables import *
import logging
import sys


class ValueException(Exception):
    """
    This class raise the Exception
    """

    def __init__(self, error_message, output):
        """
        Constructor of the class

        Parameters
        ----------
            error_message: str
                message to be shown when an exception is raised
            output: str
                showing the ouput of unction, if any
        """
        self.error_message = error_message
        self.output = output
        super().__init__(self.error_message)


    def __str__(self):
        if(self.output is None):
            return f"{self.error_message}"
        else:
            return f"{self.error_message}\n{self.output}"


class Logger():
    """
    This class handles insertion of logs in a log file
    """

    ## Name of logger
    LOGGER_NAME = "Arithmetic-" + OPERATION_DIVISION

    def __init__(self, file_name=None):
        """
        Constructor of the class

        Parameters
        ----------
            file_name: str
                the file in which we have to save the logs
        """
        self.file_name = file_name


    def get_file_name(self,file_name):
        """
        Gets the file name on which the invoked method needs to operate on

        Parameters
        ----------
        file_name: str
            file_name provided to the invoked method

        Returns
        -------
        str
            COALESCE(file_name,self.file_name). Raises error if both are None
        """
        if file_name is not None:
            return file_name
        elif self.file_name is not None:
            return self.file_name
        else:
            raise ValueError(f"File Name not provided")


    def get_logger(self):
        """
        Create logger for modules(call inside modules)

        Parameters
        ----------
        None

        Returns
        -------
        obj
            logger object
        """
        return logging.getLogger(Logger.LOGGER_NAME)


    def setup_applevel_logger(self, file_name=None): 
        """
        Create application level logger

        Parameters
        ----------
        file_name: str
            file_name provided to the invoked method

        Returns
        -------
        obj
            logger object
            
        """
        file = self.get_file_name(file_name)

        #logger = logging.getLogger(Logger.LOGGER_NAME)
        logger = self.get_logger()

        ## Setting the logging level (Logging messages which are less severe than level will be ignored)
        logger.setLevel(logging.DEBUG)

        ## Setting the logging message format
        formatter = logging.Formatter("%(asctime)s : %(name)s : [%(pathname)s : %(funcName)s] : %(levelname)s : [LineNo %(lineno)s] : %(message)s")
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)

        logger.handlers.clear()
        logger.addHandler(stream_handler)

        ## File for storing the logs
        if file:
            file_handler = logging.FileHandler(file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger

