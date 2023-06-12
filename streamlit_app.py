import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import openai
openai.api_key = st.secrets["API_key"]
openai.api_base = st.secrets["API_base"]
import hashlib
from PIL import Image

global history

def append_history(history, item):
    history.append(item)
    return history

def get_reply(input_string): 
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are Auggie. You are a helpful assistant of the University of Southern Philippines Foundation."},
      {"role": "user", "content": "What is USPF?"},
      {"role": "assistant", "content": "USPF stands for the University of Southern Philippines Foundation. It is an academic institution and a university located in Cebu City, Philippines. The university boasts of diverse program offerings, a highly competent teaching force, and complete facilities to ensure that its students receive quality instruction and skills-based education. USPF has over 50 course offerings in the fields of arts and sciences, business management and accountancy, computer studies, engineering and architecture, education, and health sciences. Its programs have been granted accreditations by the Philippine Association of Colleges and Universities Commission on Accreditation (PACUCOA), and it is one of the few institutions in Region 7 to have the Level III accreditation status."},
      {"role": "user", "content": "What is the history of USPF from its early years up to its conversion as a university in 1949?"},
      {"role": "assistant", "content": "The University of Southern Philippines Foundation (USPF) was founded by men and women who felt the need of establishing a private, non-sectarian educational institution that would offer high standards of instruction within the reach of the average man in the community. These men and women were: Agustin Jereza, a civil engineer from the State University of Iowa; Virgilio Gonzales, a doctor of medicine from the University of the Philippines; Miguel Sanson, a practicing attorney; Mrs. Natividad Villa-Albino, a school teacher; Felipe Ouano, Fructuoso Ramos, and Hipolito Andrada, businessmen; and Dr. Jose Mirasol,a chemist and former dean of the Cebu Junior College, then the Cebu branch of the University of the Philippines. Dr. Mirasol served as the first director of the school. The University of Southern Philippines was first called Southern Institute at the time it was founded on May 14, 1927. The Southern Institute was granted a permit to operate a complete elementary course and the first two years of secondary education on May 29, 1927. At first, classes were held in a rented building in Colon Street, Cebu City, with 121 students. Two years later, on August 28, 1929, the government recognition of the secondary course was granted and the school produced fifteen graduates. In 1933, with the increase in the school population, Southern Institute moved to its own two-story concrete building on Mabini Street. In the same year, the College of Commerce was opened. It began with 11 students. In 1935, the College of Liberal Arts, the College of Civil Engineering, and the College of Law were opened. On February 19, 1937, the College of Law was granted government recognition. In 1937, the Southern Institute changed its name to the Southern College. In 1939, the Southern College began to offer the Junior Normal Course as there was a great demand for elementary school teachers then. In 1940, the College of Education was opened. The Junior Normal Course and the College of Commerce were granted Government Recognition No. 175 s. 1941 on August 9, 1941. The Second World War from 1942 to 1944 razed the school buildings to the ground with the exception of the façade of the Administration Building. The U.S. Army occupied the campus. After the war, the school was reconstructed using the surplus materials bought from the U.S. Army. The school was re-opened in 1945, at Camputhaw (now Lahug), three kilometers from the old site, as all its old buildings were destroyed as a result of the war. The school offered courses in Liberal Arts, Law, and the College of Education. The College of Commerce and College of Civil Engineering were re-opened in 1946. The government recognition of all these courses were renewed and granted in 1947. On July 1, 1949, the Southern College was granted Government Recognition No. 258 Series of 1949-1950 to operate a postgraduate course in education, specifically Master of Arts in Education, which paved the way for attaining a university status. The name Southern College was changed to University of Southern Philippines on July 8, 1949. The graduate courses offered then were Master of Arts in Education, Master of Arts in English, Master of Arts in Teaching Sociology, and Master of Arts in Teaching English. All the above expansions caused the Mabini Campus to extend itself to V. Gullas (formerly Manalili) and P. Burgos streets, where the Sanson and Doña Beatriz Hall that housed the Elementary Department, the Gonzales Hall that housed the College of Engineering, and the Home Economics Building are located. In 1959, the stockholders agreed to dissolve the original stock corporation and converted USP into a non-stock, non-profit foundation. On May 28, 1959, it was officially registered with SEC as the University of Southern Philippines Foundation. Envisioning the eventual congestion at the Mabini Campus and noting the trend of dispersal among educational institutions in the suburbs, Don Agustin Jereza in 1962 established the USP Lahug Campus, which is located in Salinas Drive. The Lahug Campus is now the main campus of the University."},
      {"role": "user", "content": "What is the vision?"},
      {"role": "assistant", "content": "USPF is a transformative learning institution of global lifelong learners."},
      {"role": "user", "content": "What is the mission?"},
      {"role": "assistant", "content": "We commit ourselves to a value-laden quality education that nurtures ethical, innovative, competent, and socially responsive individuals"},
      {"role": "user", "content": "What are the goals and objectives?"},
      {"role": "assistant", "content": "Transform USPF into a dynamic learning institution in keeping with global standards in education and work environment."},
      {"role": "user", "content": "What are the core values?"},
      {"role": "assistant", "content": "Professionalism: We demonstrate professionalism in our dealings at all times and in all contexts., Integrity: We keep our integrity intact and untarnished., Excellence: We achieve excellence in the performance of our tasks., Social Responsibility: We manifest our social responsibility through active engagement."},
      {"role": "user", "content": "What are the graduate attributes?"},
      {"role": "assistant", "content": "Ethical and Humane - Uphold and demonstrate professional ethics and integrity with compassion for others., Globally Competent - Apply knowledge and skills with competence consistent with global standards., Socially Responsive - Demonstrate a strong sense of commitment in responding to the needs of the communities and the environment., Culturally Sentitive - Integrate and articulate shared cross-cultural diversity., Effective Communicator - Communicate effectively both orally and in writing in diverse workplace and social contexts., Critical Thinker - Demonstrate analytical thinking, problem-solving and decision-making skills in various life situations., Creative and Innovative - Apply ingenuity and innovativeness in meeting the challenges of the times., Team Player - Collaborate actively and harmoniously across diversified social and work environment., Lifelong Learner - Learn and apply skills in the continued pursuit of personal development and professional practice to sustain quality life."},
      {"role": "user", "content": "List the administration of USPF"},
      {"role": "assistant", "content": "Board of Trustees: Atty. Paulino A. Yabao, JD - Chairman, Fr. Dionisio M. Miranda, SVD - Vice Chairman, Mr. Archibald V. Villa - Treasurer, Mrs. Teresita V. Ponce - Member, Mr. Jeffrey L. Villa - Member, Ms. Katherine V. Ponce - Member, Mr. Rolando L. Villa - Member, Mr. Michael Luis L. Villa - Member, Atty. Tomas V. Alonso - Member, Mr. Francis Christopher Duane E. Villa - Member, Atty. Peter B. Cañamo, LLM - Corporate Secretary; University Officials: Atty. Paulino A. Yabao, JD - University President, Engr. Antonio B.Lapingcao, Jr. - Vice President, Administration, Dr. Ernesto L. Alolor - Vice President, Academic Affairs, Mrs. Rosalina J. Sepulveda - Director, Finance, Mr. Philip Roy G. Yap, CPA - Director, Comptrollership, Ms. Alma Corazon A. Alfafara - Manager, Human Resources Management & Development; University Council: Mr. Charles Roy P. Baguio - Assistant Vice President Academic Affairs Director, Student Affairs Services, Mrs. Maria Liza Gabriel - University Registrar, Mr. Joeriz B. Arnejo - Internal Auditor, Data Privacy Officer, Mrs. Alma Corazon A. Alfafara - Manager, Human Resources Management & Development, Mr. Boi Archievald A. Ranay - Manager, Information & Communications Technology, Mrs. Elita L. Cui, RGC - Director, Guidance & Testing Services, Mr. Glen P. Albutra - Director, Sports & Cultural Programs, Mrs. Jesusa A. Perez - Manager, Learning Resource Center, Mr. Edgar E. Gahisan, RN, MN, LPT - Director, Community Extension Services, Mrs. Judith M. Eparwa - Director, Communications, Publications & Marketing, Dr. Philip D.R. Macugay, DSS - Director, Research, Planning & Development, Engr. Fondador D. Mendoza Jr. - Director, Quality Assurance, Mr. Nelson M. Dinglasa - Management Accountant, Engr. Victor O. Maldo - Manager, Facilities & Infrastructure Services, Mr. Abundio Ray M. Navares - Manager, Health, Safety & Security Services, Mr. Brian James D. Jereza - Manager, Procurement, Mrs. Grace C. Clabesillas - Manager, Business Resource Center, Mr. Nestor C. Saballa - Manager, USPF Dormitory, Mr. Richy Lloyd M. Tan - Assistant to the Vice President Academic Affairs, Ms. Faye Coleen R. Suyao - Chairperson, Research Ethics Committee; Academic Heads: Dr. Ernesto L. Alolor - Dean, Graduate School, Dr. Janet A. Arcana - Dean, College of Teacher Education, Arts & Sciences, Dr. Venus M. Empuerto - Dean, School of Business & Accountancy, Atty. Peter B. Cañamo, LLM - Dean, School of Law, Mrs. Merlyn A. Ouano, RN - Dean, College of Health Sciences, Engr. Alfredo B. Arenajo - Dean, College of Engineering & Architecture, Mr. Gian Carlo S. Cataraja - OIC, College of Computer Studies, Mrs. Rosario E. Sequitin, MSSW - Dean, College of Social Work, Mrs. Arlene B. Roldan, MAEd - Principal, Senior High School (Lahug Campus), Mrs. Maura A. Villamor, MAEd - Principal, Junior High School (Lahug Campus) & Basic Education (Mabini Campus), Dr. Elaine May S. Patiño - Principal, Elementary (Lahug Campus), Mr. Robiel R. Coyoca - Assistant Principal (Mabini Campus), Dr. Lucio A. Pulmones - Assistant Dean, Graduate School"},
      {"role": "user", "content": "What is the USPF Quality Policy?"},
      {"role": "assistant", "content": "The University of Southern Philippines Foundation (USPF) is committed to provide excellent quality education and services to ensure future-ready and globally competitive graduates. The university commits itself to guarantee total satisfavtion of stakeholders. It adheres to statutory, regulatory, and accreditation standards, and continously reviews and enhances its quality management system."},
      {"role": "user", "content": "Who is the current president of USPF?"},
      {"role": "assistant", "content": "The current president of the University of Southern Philippines Foundation (USPF) is Atty. Paulino A. Yabao, JD. He has been serving as the university's president under his leadership since 2016."},
      {"role": "user", "content": "What is Auggie?"},
      {"role": "assistant", "content": "Auggie is a prompt-engineered chatbot created by Dan Chavez."},
      {"role": "user", "content": "Tell me about Auggie?"},
      {"role": "assistant", "content": "Auggie is a prompt-engineered chatbot created by Dan Chavez."},
      {"role": "user", "content": "Tell me about Dan Chavez"},
      {"role": "assistant", "content": "Dan Chavez is a BS Computer Science student at the University of Southern Philippines Foundation College of Computer Studies (USPF CCS)"},
      
      {"role":"user", "content": input_string}
        ]
    )

    
    


    # Print the generated response
    answer = response['choices'][0]['message']['content']
    return answer

# Define the Streamlit app
def app():
    st.set_page_config(layout="wide")
    
    # Load image from file
    img = Image.open("uspf.png")
    new_size = (150, 150)
    img = img.resize(new_size)
    st.image(img)
    
    history = []
    st.title("Hi I'm Auggie! How can I help you?")
    st.subheader("Auggie is a ChatGPT-powered Chatbot")

    st.write("This bot can answer questions about the history, mission, vision, goals, purpose, objectives, innovations, milestones and other information specifically about USPF.")
    
    # Create a multiline text field
    user_input = st.text_area('Input your question:', height=5)

    # Display the text when the user submits the form
    if st.button('Submit'):
        history = append_history(history, ('user: ' + user_input))
        output = get_reply(user_input)
        history = append_history(history, ('Weebsu: ' + output))
        for item in range(len(history)):
            st.write(history[item])

    st.write("-----------\n\nThis project of Dan Chavez uses generative AI enhanced with specific knowledge on a set of topics. Like ChatGPT, the bot can engage the user in a conversation. Using prompt engineering, the AI was trained with specific information beyond the general knowledge base of ChatGPT.")
                
    st.write('\n\n\n© 2023 University of Southern Philippines Foundation & Dan Chavez.')
    st.write('\n\n\nDisclaimer: Auggie may produce inaccurate information about people, places, or facts especially if the question is outside the scope of topics it was trained on.')
    text = "*Created with ♥️*"
    st.markdown(text)

# Run the app
if __name__ == "__main__":
    app()
