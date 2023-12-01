import streamlit as st
import time

# Find more emojis here: https://www.webfx.com/tools/emojis-cheat-sheet/
st.set_page_config(page_title="College Students", page_icon=":mortar_board:", layout="wide")

# ---- HEADER SECTION ----
st.subheader("🎓 This is Clifford M. Epis 📚")
st.title("A student of BSCPE 1B")
st.write("Let us talk about college students struggling with financial difficulties. 💸")

# ---- ADDITIONAL INFORMATION SECTION ----
st.header("College Life Challenges")
st.write("College life is often associated with exciting experiences, personal growth, and academic achievements. However, behind the scenes, many college students face a silent battle with financial hardships.")

# ---- ANIMATION SECTION ----
st.header("Overcoming Obstacles 🌟")
with st.spinner("Exploring ways to overcome financial challenges..."):
    time.sleep(3)  # Simulating some processing time
    st.success("Here are some insights into how college students can overcome these obstacles:")

# ---- LIST OF INSIGHTS ----
insights = [
    "Apply for scholarships and grants.",
    "Create a budget and stick to it.",
    "Explore part-time job opportunities.",
    "Utilize campus resources like financial aid offices.",
    "Consider alternative housing options.",
]

st.write("### Insights:")
for insight in insights:
    st.write(f"- {insight}")

# ---- CONCLUSION SECTION ----
st.header("Conclusion 🎓")
st.write("By being aware of available resources and implementing practical strategies, college students can navigate financial challenges and focus on their education.")

# ---- FOOTER SECTION ----
st.markdown("---")
st.info("Connect with Clifford M. Epis on LinkedIn: [Clifford's LinkedIn Profile](#)")
