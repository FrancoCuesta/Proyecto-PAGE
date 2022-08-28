from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


def clean_name(name):
    return "".join([c for c in name if c.isalpha()])

class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # Si el nombre es muy corto, podría estar equivocado.
        name = clean_name(slot_value)
        if len(name) == 0:
            dispatcher.utter_message(text="Eso debe haber sido un error tipográfico.")
            return {"first_name": None}
        return {"first_name": name}

    def validate_last_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # Si el nombre es muy corto, podría estar equivocado.
        name = clean_name(slot_value)
        if len(name) == 0:
            dispatcher.utter_message(text="Eso debe haber sido un error tipográfico.")
            return {"last_name": None}
        
        first_name = tracker.get_slot("first_name")
        if len(first_name) + len(name) < 3:
            dispatcher.utter_message(text="Ese es un nombre muy corto. Tememos un error tipográfico. reiniciando!")
            return {"first_name": None, "last_name": None}
        return {"last_name": name}
