# streamlit
import streamlit as st

# Page configuration
st.set_page_config(page_title="Growth Mindset Project", page_icon="★")

# Title
st.title("Growth Mindset Challenge: Web App with Streamlit")

# Welcome section
st.header("Welcome to your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app is here to help!")

# Quote section
st.header("🌞Today's Growth Mindset Quote")
st.write('"Success is not final, failure is not fatal: it is the courage to continue that counts." — Winston Churchill')

# Challenge input
st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

# Condition for challenge
if user_input:
    st.success(f"You're facing: {user_input}. Keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection section
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your thoughts.")

# Achievements section
st.header("Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now 🤩")

# Footer
st.markdown("---")
st.write("Keep believing in yourself. Growth is a journey, not a destination! ✨")
st.write("**Created by Bahisht Ghori**")
