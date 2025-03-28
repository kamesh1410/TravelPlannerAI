# app.py
import streamlit as st
from prompts import get_initial_prompt, refine_input_prompt, activity_suggestion_prompt, itinerary_prompt
from itinerary_generator import generate_response

st.set_page_config(page_title="Travel Planner AI", layout="wide")

# Custom CSS
st.markdown('<link rel="stylesheet" href="static/style.css">', unsafe_allow_html=True)

# State management
if "stage" not in st.session_state:
    st.session_state.stage = "initial"
if "user_data" not in st.session_state:
    st.session_state.user_data = {}

# Header
st.title("✈️ Travel Planner AI")
st.write(generate_response(get_initial_prompt()))

# Stage-based UI with optimized form handling
if st.session_state.stage == "initial":
    with st.form("initial_form", clear_on_submit=True):
        budget = st.selectbox("Budget", ["Low ($0-$500)", "Moderate ($500-$1500)", "High ($1500+)"])
        duration = st.selectbox("Trip Duration", ["1-3 days", "4-7 days", "8+ days"])
        destination = st.selectbox("Destination", ["Paris", "New York", "Tokyo", "Delhi", "Mumbai", "Jaipur", "Goa", "Kerala", "Agra", "Bangalore", "Varanasi", "Udaipur", "Shimla", "Rishikesh", "Kolkata"])
        start = st.selectbox("Starting Location", ["London", "Chicago", "Sydney", "Delhi", "Mumbai"])
        purpose = st.selectbox("Purpose", ["Relaxation", "Adventure", "Culture"])
        preferences = st.multiselect("Preferences", ["Food", "Outdoor Activities", "Museums", "Luxury Stays", "Budget Stays"])
        submit = st.form_submit_button("Next")
        if submit:
            st.session_state.user_data = {
                "budget": budget, "duration": duration, "destination": destination,
                "start": start, "purpose": purpose, "preferences": preferences
            }
            st.session_state.stage = "refine"
            st.rerun()  # Force re-render to avoid double-click

elif st.session_state.stage == "refine":
    st.write(generate_response(refine_input_prompt(st.session_state.user_data), st.session_state.user_data))
    with st.form("refine_form", clear_on_submit=True):
        diet = st.selectbox("Dietary Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"])
        mobility = st.selectbox("Mobility Level", ["High (lots of walking)", "Moderate", "Low (accessibility needed)"])
        interests = st.multiselect("Specific Interests", ["Hiking", "Museums", "Water Sports", "Fine Dining"] if "Adventure" in st.session_state.user_data["purpose"] else ["Art", "History", "Local Food"])
        submit = st.form_submit_button("Next")
        if submit:
            st.session_state.user_data.update({"diet": diet, "mobility": mobility, "interests": interests})
            st.session_state.stage = "suggest"
            st.rerun()

elif st.session_state.stage == "suggest":
    with st.spinner("Fetching suggestions..."):
        suggestions = generate_response(activity_suggestion_prompt(st.session_state.user_data["destination"], st.session_state.user_data["preferences"]), st.session_state.user_data)
    st.write("### Suggested Activities")
    st.write(suggestions)
    if st.button("Generate Itinerary"):
        st.session_state.stage = "itinerary"
        st.rerun()

elif st.session_state.stage == "itinerary":
    with st.spinner("Building your itinerary..."):
        itinerary = generate_response(itinerary_prompt(st.session_state.user_data), st.session_state.user_data)
    st.write("### Your Personalized Itinerary")
    st.markdown(itinerary)
    if st.button("Start Over"):
        st.session_state.stage = "initial"
        st.session_state.user_data = {}
        st.rerun()

# JavaScript
st.markdown('<script src="static/script.js"></script>', unsafe_allow_html=True)