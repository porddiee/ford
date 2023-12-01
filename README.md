import streamlit as st
import time

# Find more emojis here: https://www.webfx.com/tools/emojis-cheat-sheet/
st.set_page_config(page_title="College Students", page_icon=":mortar_board:", layout="wide")

# ---- HEADER SECTION ----
st.subheader("🎓 This is Clifford M. Epis 📚")
st.title("A student of BSCPE 1B")
st.write("Let's delve into the multifaceted world of college life, where exciting experiences, personal growth, and academic achievements unfold. However, beneath the surface, many students engage in a silent battle against financial hardships. 💸")

# ---- ADDITIONAL INFORMATION SECTION ----
st.header("College Life Challenges")
st.write("Navigating through college life presents a myriad of challenges, and one significant hurdle is the financial strain that students often face. The following insights shed light on how students can overcome these obstacles:")

# ---- ANIMATION SECTION ----
st.header("Overcoming Obstacles 🌟")
with st.spinner("Exploring ways to overcome financial challenges..."):
    time.sleep(3)  # Simulating some processing time
    st.success("Here are some detailed insights into how college students can overcome these obstacles:")

# ---- LIST OF INSIGHTS WITH DESCRIPTIONS ----
insights = [
    ("Apply for scholarships and grants", "Seek out and apply for various scholarships and grants available based on your academic achievements, talents, and interests."),
    ("Create a budget and stick to it", "Develop a realistic budget that covers your expenses, including tuition, housing, food, and other essentials. Stick to this budget to manage your finances effectively."),
    ("Explore part-time job opportunities", "Consider taking on part-time employment to supplement your income. Look for opportunities on or near campus that align with your schedule."),
    ("Utilize campus resources like financial aid offices", "Visit your college's financial aid office to explore available resources, such as counseling, emergency funds, or advice on managing student loans."),
    ("Consider alternative housing options", "Explore cost-effective housing options, such as sharing accommodation with roommates or considering off-campus housing that may be more affordable."),
]

st.write("### Insights:")
for insight, description in insights:
    st.write(f"- *{insight}*: {description}")

# ---- CONCLUSION SECTION ----
st.header("Conclusion 🎓")
st.write("In conclusion, overcoming financial challenges during college requires a combination of proactive strategies and resource utilization. By applying for scholarships, creating and sticking to a budget, exploring part-time employment, utilizing campus resources, and considering alternative housing options, students can navigate financial hardships successfully. Remember, each step taken brings you closer to a brighter academic future.")

# ---- FOOTER SECTION ----
st.markdown("---")
st.info("Connect with Clifford M. Epis on LinkedIn: [Clifford's LinkedIn Profile](#)")
