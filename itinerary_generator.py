# itinerary_generator.py
def generate_response(prompt, user_data=None):
    if "Guide the user to select" in prompt:
        return "Please use the dropdowns and checkboxes below to plan your trip!"
    elif "ask for additional details" in prompt and user_data:
        return f"Got it! You selected: {user_data}. Now, please choose your dietary preferences, mobility level, and specific interests."
    elif "suggest 5 activities" in prompt and user_data:
        destination = user_data.get("destination", "Paris")
        preferences = user_data.get("preferences", [])
        if destination == "Paris":
            return """
            1. Louvre Museum (Art & Culture)
            2. Eiffel Tower Visit (Iconic Landmark)
            3. Seine River Cruise (Scenic Relaxation)
            4. Montmartre Walk (Hidden Gem)
            5. French Pastry Tasting (Food)
            """
        elif destination == "Delhi":
            return """
            1. Red Fort Tour (History)
            2. Qutub Minar Visit (Architecture)
            3. Street Food Tour (Food)
            4. Lotus Temple (Relaxation)
            5. Humayun’s Tomb (Culture)
            """
        elif destination == "Mumbai":
            return """
            1. Gateway of India (Landmark)
            2. Marine Drive Sunset (Relaxation)
            3. Elephanta Caves (Adventure)
            4. Bollywood Studio Tour (Culture)
            5. Local Seafood Tasting (Food)
            """
        elif destination == "Jaipur":
            return """
            1. Amber Fort (History)
            2. Hawa Mahal (Architecture)
            3. City Palace (Culture)
            4. Elephant Ride (Adventure)
            5. Rajasthani Thali (Food)
            """
        elif destination == "Goa":
            return """
            1. Baga Beach Relaxation (Beach)
            2. Water Sports at Calangute (Adventure)
            3. Old Goa Churches (Culture)
            4. Spice Plantation Tour (Food)
            5. Dudhsagar Waterfall Trek (Nature)
            """
        elif destination == "Kerala":
            return """
            1. Backwater Houseboat Ride (Relaxation)
            2. Munnar Tea Gardens (Nature)
            3. Kathakali Dance Show (Culture)
            4. Ayurvedic Spa (Wellness)
            5. Seafood Feast (Food)
            """
        elif destination == "Agra":
            return """
            1. Taj Mahal Visit (History)
            2. Agra Fort (Architecture)
            3. Mehtab Bagh Sunset (Relaxation)
            4. Local Marble Shopping (Culture)
            5. Petha Tasting (Food)
            """
        elif destination == "Bangalore":
            return """
            1. Lalbagh Botanical Garden (Nature)
            2. Bangalore Palace (Culture)
            3. Pub Crawl (Food & Drink)
            4. Nandi Hills Sunrise (Adventure)
            5. Tech Park Tour (Modern)
            """
        elif destination == "Varanasi":
            return """
            1. Ganges Aarti (Spirituality)
            2. Boat Ride on Ganga (Relaxation)
            3. Sarnath Visit (History)
            4. Street Food Walk (Food)
            5. Kashi Vishwanath Temple (Culture)
            """
        elif destination == "Udaipur":
            return """
            1. City Palace Tour (Culture)
            2. Lake Pichola Boat Ride (Relaxation)
            3. Monsoon Palace (History)
            4. Puppet Show (Tradition)
            5. Rajasthani Dinner (Food)
            """
        elif destination == "Shimla":
            return """
            1. Mall Road Stroll (Relaxation)
            2. Ridge Viewpoint (Scenery)
            3. Kufri Skiing (Adventure)
            4. Viceregal Lodge (History)
            5. Local Apple Tasting (Food)
            """
        elif destination == "Rishikesh":
            return """
            1. River Rafting (Adventure)
            2. Yoga Session (Relaxation)
            3. Triveni Ghat Aarti (Culture)
            4. Beatles Ashram (History)
            5. Chotiwala Meal (Food)
            """
        elif destination == "Kolkata":
            return """
            1. Victoria Memorial (History)
            2. Howrah Bridge View (Landmark)
            3. Tram Ride (Culture)
            4. Street Food Tour (Food)
            5. Sundarbans Day Trip (Nature)
            """
        else:
            return """
            1. Local Landmark Visit
            2. Scenic Relaxation Spot
            3. Cultural Experience
            4. Outdoor Activity
            5. Food Tasting
            """
    elif "create a day-by-day itinerary" in prompt and user_data:
        days = int(user_data["duration"].split("-")[1].split()[0]) if "-" in user_data["duration"] else 3
        destination = user_data["destination"]
        preferences = user_data["preferences"]
        itinerary = f"**Your {days}-Day Itinerary to {destination}**\n"
        
        activities = {
            "Paris": [
                "Louvre Museum Tour (9 AM - 12 PM) - Explore world-famous art",
                "Eiffel Tower Visit (2 PM - 4 PM) - Iconic views of Paris",
                "Seine River Cruise (6 PM - 7 PM) - Relaxing evening on the water"
            ],
            "Delhi": [
                "Red Fort Tour (9 AM - 11 AM) - Dive into Mughal history",
                "Street Food Tour (12 PM - 2 PM) - Taste Delhi’s chaat",
                "Qutub Minar Visit (3 PM - 5 PM) - Marvel at ancient architecture"
            ],
            "Mumbai": [
                "Gateway of India (10 AM - 12 PM) - Iconic waterfront landmark",
                "Elephanta Caves (1 PM - 3 PM) - Ferry to ancient rock-cut caves",
                "Marine Drive Sunset (4 PM - 6 PM) - Relax by the sea"
            ],
            "Jaipur": [
                "Amber Fort (9 AM - 12 PM) - Explore the majestic fort",
                "Hawa Mahal (1 PM - 3 PM) - Admire the Palace of Winds",
                "City Palace (4 PM - 6 PM) - Royal history and artifacts"
            ],
            "Goa": [
                "Baga Beach Relaxation (10 AM - 1 PM) - Sun, sand, and sea",
                "Water Sports at Calangute (2 PM - 4 PM) - Jet skiing and more",
                "Old Goa Churches (5 PM - 7 PM) - Visit historic basilicas"
            ],
            "Kerala": [
                "Backwater Houseboat Ride (10 AM - 1 PM) - Cruise through serene waters",
                "Munnar Tea Gardens (2 PM - 4 PM) - Scenic plantation walk",
                "Kathakali Dance Show (6 PM - 7 PM) - Traditional performance"
            ],
            "Agra": [
                "Taj Mahal Visit (9 AM - 12 PM) - Iconic monument of love",
                "Agra Fort (1 PM - 3 PM) - Mughal fortress exploration",
                "Mehtab Bagh Sunset (4 PM - 6 PM) - Taj view at dusk"
            ],
            "Bangalore": [
                "Lalbagh Botanical Garden (10 AM - 12 PM) - Nature and tranquility",
                "Bangalore Palace (1 PM - 3 PM) - Royal architecture",
                "Nandi Hills Sunrise (5 AM - 7 AM, Day 2) - Early morning trek"
            ],
            "Varanasi": [
                "Ganges Aarti (6 PM - 7 PM) - Evening spiritual ceremony",
                "Boat Ride on Ganga (7 AM - 9 AM) - Sunrise over the river",
                "Sarnath Visit (2 PM - 4 PM) - Buddhist heritage site"
            ],
            "Udaipur": [
                "City Palace Tour (9 AM - 12 PM) - Royal lakeside palace",
                "Lake Pichola Boat Ride (2 PM - 4 PM) - Scenic relaxation",
                "Monsoon Palace (5 PM - 7 PM) - Hilltop sunset view"
            ],
            "Shimla": [
                "Mall Road Stroll (10 AM - 12 PM) - Bust   Shimla’s famous walkway",
                "Kufri Skiing (1 PM - 3 PM) - Winter adventure",
                "Ridge Viewpoint (4 PM - 6 PM) - Panoramic views"
            ],
            "Rishikesh": [
                "River Rafting (10 AM - 12 PM) - Thrilling Ganges adventure",
                "Yoga Session (3 PM - 4 PM) - Riverside relaxation",
                "Triveni Ghat Aarti (6 PM - 7 PM) - Spiritual evening"
            ],
            "Kolkata": [
                "Victoria Memorial (10 AM - 12 PM) - Colonial-era grandeur",
                "Howrah Bridge View (2 PM - 3 PM) - Iconic city symbol",
                "Street Food Tour (5 PM - 7 PM) - Bengali culinary delights"
            ]
        }.get(destination, [
            "Local Exploration (10 AM - 1 PM) - Discover the area",
            "Relaxation Time (2 PM - 4 PM) - Unwind at a scenic spot",
            "Cultural Activity (5 PM - 7 PM) - Engage with local traditions"
        ])

        for day in range(1, days + 1):
            itinerary += f"\n**Day {day}:**\n"
            if day <= len(activities):
                itinerary += f"- {activities[day-1]}\n"
            else:
                itinerary += "- Free Day: Explore at your leisure or relax\n"
        return itinerary
    return "Processing..."