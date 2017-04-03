#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bots.chatty import bot_chatty as chatty
from bots.herbie import bot_herbie as herbie
from bots.clever import bot_clever as clever
from constants import (NO_BOT, SPECIFY_BOT, HELP_MSG, LIST,
                       START_SESSION, END_SESSION)


class Operator(object):
    '''
    Presents connection layer between each bot and server
    all communication goes through here
    changing session, listing bot,.... is done within this class
    '''
    def __init__(self):
        self.bots = {'chatty': chatty,
                     'herbie': herbie,
                     'clever': clever}
        self.active_bot = None

    def getAnswer(self, question):
        '''
        Main switch which take care of choosing if bot or an operator will give
        response to the user

        question - user input
        return - return message which will be printed out(action info/
        bot response/err message with help)
        '''
        if question:
            if self.active_bot is None:  # non active bot mode
                command = self.getCommand(question)
                if command:
                    if command is LIST:
                        return self.showBots()
                    if command is START_SESSION:
                        return self.manageSession(question, START_SESSION)
                    if command is END_SESSION:
                        return self.operatorAnswer(NO_BOT)
                else:
                    return self.operatorAnswer(NO_BOT)
            else:  # active bot mode
                command = self.getCommand(question)
                if command is END_SESSION:
                    return self.manageSession(question, END_SESSION)
                else:  # message is for bot
                    return self.askBot(question)
        else:  # no question
            return self.operatorAnswer()  # show just help

    def manageSession(self, question, session):
        '''
        Changes communication between bot or server

        question - user input
        session - to start or to end communication with bot
        return - String, which is response to user, error one or successful
            info about changing the session
        '''
        if session is START_SESSION:
            bot = self.getBot(question)
            if bot:
                return self.setBotActivity(name=bot, activity=True)
            else:
                return self.operatorAnswer(SPECIFY_BOT)
        else:  # END_SESSION
            return self.setBotActivity(self.active_bot.name, activity=False)

    def setBotActivity(self, name, activity):
        '''
        Set activity of a bot

        name - name of bot
        activity - Boolean, true if activity wants to be set
        return - info message about result of this operation
        '''
        if name.lower() in self.bots and name is not None:
            if activity:
                self.active_bot = self.bots[name]
                return 'Bot {} is active now'.format(
                    self.active_bot.name)
            else:
                self.active_bot = None
                return 'Bot {} is deactivated'.format(name)
        else:
            return 'Bot {} is unknown!'.format(name)


    def getCommand(self, question):
        '''
        Get command from user input if used

        question - user input
        return - return a command or False if no command have been founded
        '''
        if question.startswith(LIST):
            return LIST
        if question.startswith(START_SESSION):
            return START_SESSION
        if question.startswith(END_SESSION):
            return END_SESSION
        return False

    def askBot(self, question):
        return str(self.active_bot.get_response(question))

    def operatorAnswer(self, msg=''):
        '''
        Prints optional message with help

        msg - additonal message inserted before help
        return - String, mesg parmeter with help
        '''
        return '{}{}'.format(msg, HELP_MSG)

    def showBots(self):
        return '\n'.join(self.bots)

    def getBot(self, question):
        '''
        Parse user input in order to get bot while starting new session

        question - user input
        return - False,  if bot is not inserted
                 String,  the second word after start session keyword from
                 user input
            ! checking correctness of bot is not done here !
        '''
        try:
            return question.lstrip(START_SESSION).strip().split()[0]
        except IndexError:
            return False
