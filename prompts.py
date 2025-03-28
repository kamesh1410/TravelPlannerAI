# prompts.py
def get_initial_prompt():
    return """
    You are an AI-powered travel planner. Guide the user to select:
    - Budget: Low ($0-$500), Moderate ($500-$1500), High ($1500+)
    - Trip Duration: 1-3 days, 4-7 days, 8+ days
    - Destination: Paris, New York, Tokyo, Delhi, Mumbai, Jaipur, Goa, Kerala, Agra, Bangalore, Varanasi, Udaipur, Shimla, Rishikesh, Kolkata
    - Starting Location: London, Chicago, Sydney, Delhi, Mumbai
    - Purpose: Relaxation, Adventure, Culture
    - Preferences: Food, Outdoor Activities, Museums, Luxury Stays, Budget Stays
    Process their choices directly.
    """

def refine_input_prompt(user_data):
    return f"""
    Based on selections: {user_data}, ask for additional details:
    - Dietary preferences: Vegetarian, Non-Vegetarian, Vegan
    - Mobility: High (lots of walking), Moderate, Low (accessibility needed)
    - Specific Interests: Based on purpose (e.g., Adventure → Hiking, Water Sports; Culture → Museums, History)
    Return a message confirming selections and asking for these refinements.
    """

def activity_suggestion_prompt(destination, preferences):
    return f"""
    For destination '{destination}' and preferences '{preferences}', suggest 5 unique activities:
    - Tailor suggestions to the destination and preferences.
    Return a list in a clear format.
    """

def itinerary_prompt(user_data):
    return f"""
    Using selections: {user_data}, create a day-by-day itinerary:
    - Include unique activities based on destination and preferences.
    - Group logically by day (morning, afternoon, evening).
    - Add timings and brief descriptions.
    Return a structured text block.
    """