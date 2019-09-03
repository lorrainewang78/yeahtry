import logging
'''
Logging consist in dispatching messages related to application
events to one or multiple channels (for example: stdout, files, remote log collectors etc)

Useful for 
* Debugging code
* Tracking events history for auditing purposes

The logging functions are named after the level or severity of the events they are used to track. 
The standard levels and their applicability are described below (in increasing order of severity):

DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. 'disk space low'). The software is still working as expected.
ERROR: Due to a more serious problem, the software has not been able to perform some function.
CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

'''



logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

'''
The default level is WARNING, which means that only events of this 
level and above will be tracked, unless the logging package is 
configured to do otherwise.
'''