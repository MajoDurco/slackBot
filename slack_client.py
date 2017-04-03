#!/usr/bin/env python3

import os
import time

from slackclient import SlackClient
from operat import Operator


AT_BOT = '@tellme'
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
operator = Operator()


def giveReponse(question, channel):
    '''
    Give a response from bot or operator

    question - question to the bot
    channel - channel where message was received
    '''
    botAnswer = operator.getAnswer(question)
    slack_client.api_call("chat.postMessage",
                          channel=channel,
                          text=botAnswer,
                          as_user=True)


def parseSlackOutput(slack_rtm_output):
    '''
    Parsing function for all messages

    slackt_rtm_output - all received messages from slack API
    return - None unless a message is to bot, based on its ID.
    '''
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'content' in output and AT_BOT in output['content']:
                # return text after the @ mention, whitespace removed
                return (output['content'].split(AT_BOT)[1].strip(),
                        output['channel'])
    return (None, None)

if __name__ == "__main__":
    websocket_delay = 1
    if slack_client.rtm_connect():
        while True:
            question, channel = parseSlackOutput(slack_client.rtm_read())
            if question and channel:
                giveReponse(question, channel)
            time.sleep(websocket_delay)
    else:
        print("Connection err")
