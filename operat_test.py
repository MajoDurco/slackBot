#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import random
from operat import Operator
from constants import (NO_BOT, SPECIFY_BOT, HELP_MSG, LIST,
                       START_SESSION, END_SESSION)


class OperatorTest(unittest.TestCase):

    def setUp(self):
        self.operator = Operator()

    def test_init_vals(self):
        self.assertIsNone(self.operator.active_bot)
        self.assertIs(type(self.operator.bots), dict)

    def test_set_bot_activity(self):
        bot = self.getRandomBotName()
        self.assertIn('active', self.operator.setBotActivity(bot, True))
        self.assertIn('deactivated', self.operator.setBotActivity(bot, False))
        self.assertIn('active', self.operator.setBotActivity(bot, True))

    def test_set_wrong_bot_activity(self):
        bot = 'foo'
        self.assertIn('unknown', self.operator.setBotActivity(bot, True))
        self.assertIn('unknown', self.operator.setBotActivity(bot, False))

    def test_get_answer(self):
        # no bot selected
        self.assertEqual(self.operator.getAnswer(''), HELP_MSG)
        self.assertIn(NO_BOT, self.operator.getAnswer('Hi'))
        # select a bot
        self.test_set_bot_activity()
        self.assertNotIn(NO_BOT, self.operator.getAnswer('Hi'))
        # deactivate
        self.assertIn('deactivated', self.deactivate_bot())
        self.assertIn(NO_BOT, self.operator.getAnswer('Hi'))

    def test_commands(self):
        bots = self.operator.bots
        # list
        for bot in bots:
            self.assertIn(bot, self.operator.getAnswer(LIST))
        # deactivate without active bot
        self.assertIn(NO_BOT, self.operator.getAnswer(END_SESSION))
        # start_session without bot
        self.assertIn(SPECIFY_BOT, self.operator.getAnswer(START_SESSION))
        # choose correct bot
        message = ' '.join((START_SESSION, self.getRandomBotName()))
        self.assertIn('active', self.operator.getAnswer(message))
        self.assertEqual(type(self.operator.getAnswer('Hi')), str)
        self.assertIn('deactivated', self.operator.getAnswer(END_SESSION))

    def test_get_command(self):
        # LIST
        self.assertEqual(LIST, self.operator.getCommand(LIST))
        # START_SESSION
        self.assertEqual(START_SESSION,
                         self.operator.getCommand(START_SESSION))
        # END_SESSION
        self.assertEqual(END_SESSION, self.operator.getCommand(END_SESSION))
        # OTHER
        self.assertEqual(False, self.operator.getCommand('foo'))

    # util functions
    def deactivate_bot(self):
        return self.operator.setBotActivity(self.operator.active_bot.name,
                                            False)

    def getRandomBotName(self):
        bot_names = list(self.operator.bots.keys())
        return random.choice(bot_names)


if __name__ == '__main__':
    unittest.main(verbosity=2)
