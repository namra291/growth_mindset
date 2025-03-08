  #streamlit 
import streamlit as st

st.set_page_config(page_title="growth mindset project",project_icon="⭐")
st.title("Growth Mindset Challenge: Web App With Streamlit")

st.header("🚀 welcom to your Growth jorney!")
st.write("Embrace challenges,learn from mistakes,and unlock your full potential.This AI-powerd app helps you build a Growth mindset with reflection,challenges,and achievements!🌟")

#quote section
st.header("💡Today's Growth Mindset Quote")
st.write(""Successnot is not final,failure is not fatal:it is the courage to continue that counts.")- Winston Churchill")
 
st.header("🔧What's your challenge Today?")
user_input = st.text_input("Describe a challenge you facing:")


#condition
if user_input:
    st.success(f"💪you re facing:{user_input}.keep pushing forward towords your goal!🚀")
else:
    st.warning("Tell us about your challege to get started!")

#reflexing
st.header("Reflect on Your Learning")
reflection = st.text_area("erite your reflections here:")

if reflection:
    st.success(f"✨Great Your reflection:{reflection}")

else:
    st.info("Reflection on past experience help your growth!Share your difficulties")

#acheivements

st.header("🏆Celebrate Your Wins!")
acheivement = st.text_input("share something you've recently accomplished:")

if acheivment:
    st.success(f"🎉Amazing you achieved:{acheivment}")
else:
    st.info("Big or small , every acheivement counts! share one now 😍")   


#footer
st.write("- - -")
st.write("🚀 Keep believing in yourself.Growth is a journey,not a destination! ✨")
st.write("** © Created by Namra Ashraf**")



