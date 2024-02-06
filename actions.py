# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import callfunctionpyfile as cf
#
#

class ActionHelloWorld(Action):
#class ActionShowRemedy(Action):

    def name(self) -> Text:
        return "action_show_remedy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # print("Link: ", tracker.get_slot('LINK'))

        # print(tracker.latest_message['text'])
        # text = tracker.latest_message['text']
        # print(text)

        #dispatcher.utter_message("Hello World from the world of actions this time...great great great")
        dispatcher.utter_message(tracker.latest_message['text'])

        return []



class ActionHelloWorld(Action):
#class ActionShowDiagnosis(Action):

     def name(self) -> Text:
         return "action_show_diagnosis"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         #print("Link: ", tracker.get_slot('LINK'))

         #print(tracker.latest_message['text'])
         text1 = tracker.latest_message['text']
         #print(text)

         #dispatcher.utter_message(text="Hello World from the world of actions this time...great great great")
         #dispatcher.utter_message(tracker.latest_message['text'])
         text2= cf.getinput(text1)
         dispatcher.utter_message(text2)


         return []