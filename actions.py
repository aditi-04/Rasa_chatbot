# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# import datetime
# import pytz
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# #

# class ActionSetTime(Action):
   
#     def name(self):
#         return "action_set_time"

#     async def run(self, dispatcher, tracker, domain): 
#      #  required_slots=["clean_time "]
#         current_time = datetime.time.now()  
#         Final_time= current_time.hour+timedelta(hours=tracker.get_slot(clean_time))
#         print(Final_time)
#         # entities = tracker.latest_message.get("entities")
#         dispatcher.utter_message(template="utter_relatively", Time=current_time)
#         return [Final_time]

# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          
#         dispatcher.utter_message(text="Hello World!")

#         return []
