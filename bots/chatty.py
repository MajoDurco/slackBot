#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from chatterbot import ChatBot

bot_chatty = ChatBot("Chatty",
                  logic_adapters=["chatterbot.logic.BestMatch"],
                  input_adapter="chatterbot.input.VariableInputTypeAdapter",
                  output_adapter="chatterbot.output.OutputAdapter"
                  )
