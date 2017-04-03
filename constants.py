#!/usr/bin/env python3


HOST = 'localhost'
PORT = '5000'

# operat help message
HELP_MSG = '''
Help:
    List all avaiable bots - "list"
    Start communicating with one of the bots - "start_session <BOT_NAME>"
    End communication with bot - "end_session"
'''
# commands
LIST = "list"
START_SESSION = "start_session"
END_SESSION = "end_session"

# operat err messages
NO_BOT = 'No bot is choosen'
SPECIFY_BOT = 'You should specify bot'
