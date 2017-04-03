#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from chatterbot import ChatBot

bot_clever = ChatBot("Clever",
                 logic_adapters=["chatterbot.logic.BestMatch",
                                 "chatterbot.logic.TimeLogicAdapter",
                                 "chatterbot.logic.MathematicalEvaluation"],
                 input_adapter="chatterbot.input.VariableInputTypeAdapter",
                 output_adapter="chatterbot.output.OutputAdapter",
                 )

