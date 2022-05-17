from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from helper import get_current_time_object
from helper import IAMBOT, DESC, QUES1, SKILL_DESC

MORNING_GREETING = "Buenos dias!"
AFTERNOON_GREETING = "Buenas tardes!"
NIGHT_GREETING = "Buenas noches!"

class ActionGreetDependsHour(Action):

    def name(self) -> Text:
        return "action_greet_depends_hour"

    def run(self, 
                dispatcher: CollectingDispatcher, 
                tracker: Tracker,         
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        now = get_current_time_object()
        greet_time = ''
        if now.hour < 12 :
            greet_time = MORNING_GREETING
        elif now.hour < 19:
            greet_time = AFTERNOON_GREETING
        else:
            greet_time = NIGHT_GREETING
        dispatcher.utter_message(text=f'{greet_time}. {IAMBOT} y {DESC}, {SKILL_DESC} {QUES1}')
        return []  # edit to return json response