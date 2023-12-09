import streamlit as st
import streamlit as st
from streamlit_lottie 
import st_lottie
import time


# Find more emojis here: https://www.webfx.com/tools/emojis-cheat-sheet/
st.set_page_config(page_title="College Students", page_icon=":mortar_board:", layout="wide")

# ---- LOAD ASSETS ----
with st.echo():
    st_lottie("https://lottie.host/830ba297-eb73-4c04-b34d-c439f6013e91/iKOAFldNRi.json")
    
# ---- HEADER SECTION ----
st.subheader("🎓 This is Clifford M. Epis 📚")
st.title("A student of BSCPE 1B")
st.write("In today's challenging economic landscape, a significant number of students find themselves grappling with the formidable burden of financial constraints. The pursuit of education, once considered a pathway to personal and professional advancement, has become increasingly intertwined with the harsh reality of economic instability. As tuition fees soar, living costs rise, and the job market remains fiercely competitive, a growing population of students is thrust into the precarious realm of financial hardship.For these students, the pursuit of knowledge is accompanied by a constant juggling act – a delicate balance between academic aspirations and the pressing demands of financial survival. The weight of student loans, coupled with the rising cost of textbooks, housing, and other essential expenses, often casts a looming shadow over the educational journey. As dreams of intellectual growth and academic achievement take root, the specter of financial strain can cast a stifling pallor, obstructing the path to success.The repercussions of this financial struggle extend beyond the immediate challenges of making ends meet. Mental health can bear the brunt of the financial stress, as students grapple with the emotional toll of balancing academic responsibilities with the relentless pressure of financial instability. The strain of living on a tight budget can manifest in anxiety, stress, and a sense of isolation, creating an added layer of complexity to an already demanding academic environment.Moreover, the impact of financial constraints is not confined to the individual student; it reverberates through the broader educational landscape. The potential loss of diverse perspectives and talents is a societal cost that cannot be overlooked, as brilliant minds are forced to navigate a labyrinth of financial hurdles, often deterring them from realizing their full potential.In confronting the multifaceted issue of student financial struggles, it becomes imperative for institutions, policymakers, and society at large to engage in a collective dialogue aimed at fostering a more inclusive and supportive educational environment. By acknowledging and addressing the root causes of financial hardship, we can strive towards creating a future where students can pursue their academic endeavors unencumbered by the burden of financial uncertainty.💸")

# ---- ADDITIONAL INFORMATION SECTION ----
st.header("College Life Challenges")
st.write("Navigating through college life presents a myriad of challenges, and one significant hurdle is the financial strain that students often face. The following insights shed light on how students can overcome these obstacles:")
   
# ---- ANIMATION SECTION ----
st.header("Overcoming Obstacles 🌟")
with st.spinner("Exploring ways to overcome financial challenges..."):
    time.sleep(3)  # Simulating some processing time
    st.success("Here are some detailed insights into how college students can overcome these obstacles:")


# ---- LIST OF INSIGHTS WITH DESCRIPTIONS ----
insights_with_descriptions = [
    ("Apply for scholarships and grants.", "Seek out and apply for various scholarships and grants available based on your academic achievements, talents, and interests."),
    ("Create a budget and stick to it.", "Develop a realistic budget that covers your expenses, including tuition, housing, food, and other essentials. Stick to this budget to manage your finances effectively."),
    ("Explore part-time job opportunities.", "Consider taking on part-time employment to supplement your income. Look for opportunities on or near campus that align with your schedule."),
    ("Utilize campus resources like financial aid offices.", "Visit your college's financial aid office to explore available resources, such as counseling, emergency funds, or advice on managing student loans."),
    ("Consider alternative housing options.", "Explore cost-effective housing options, such as sharing accommodation with roommates or considering off-campus housing that may be more affordable."),
]

st.write("### Insights:")
for insight, description in insights_with_descriptions:
    st.write(f"- *{insight}*: {description}")

# ---- CONCLUSION SECTION ----
st.header("Conclusion 🎓")
st.write("In conclusion, overcoming financial challenges during college requires a combination of proactive strategies and resource utilization. By applying for scholarships, creating and sticking to a budget, exploring part-time employment, utilizing campus resources, and considering alternative housing options, students can navigate financial hardships successfully. Remember, each step taken brings you closer to a brighter academic future.")

# ---- FOOTER SECTION ----
st.markdown("---")
st.info("Connect with me on: https://github.com/porddiee")
