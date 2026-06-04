import random

from intents import intent_actions
from responses import intent_responses


def get_actions_by_intent(intent_name):
    """
    Searches through all domains to find the matching intent.
    Args:
        intent_name (str): The name of the intent to search for.
    Returns:
        list: A list of actions associated with the intent, or an empty list if not found.
    """
    for domain, intents in intent_actions.items():
        if intent_name in intents:
            return intents[intent_name]
        
    return [] # Return an empty list if not found (or if it's Out of Scope)



def get_chat_response(intent_name):
    """
    Searches across domains to find the intent responses list.
    Defaults to the Out of Scope responses if not found.
    Args:
        intent_name (str): The name of the intent to search for.
    Returns:
        str: A randomly selected response from the list of responses for the intent, or a random Out-of-Scope response if not found.
    """
    for domain, intents in intent_responses.items():
        if intent_name in intents:
            # pick a random phrasing from the list of variations
            return random.choice(intents[intent_name])
            
    # fallback to a random Out-of-Scope response if the intent doesn't exist
    return random.choice(intent_responses["out_of_scope"]["oos"])