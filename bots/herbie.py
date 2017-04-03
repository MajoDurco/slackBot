#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from chatterbot import ChatBot

bot_herbie = ChatBot("Herbie",
                     output_adapter="chatterbot.output.OutputAdapter",
                     input_adapter="chatterbot.input.VariableInputTypeAdapter",
                     logic_adapters=[{
                         "import_path": "chatterbot.logic.BestMatch"
                     }, {
                         "import_path": "chatterbot.logic.LowConfidenceAdapter",
                         "treshold": 0.5,
                         "default_response": "Vrooom!!!"
                     }]
                     )
