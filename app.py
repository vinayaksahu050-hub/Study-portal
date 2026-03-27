import streamlit as st
import pandas as pd

st.set_page_config(page_title="Study Portal", layout="wide")

# 🏠 HOME SECTION
st.title("🎓 Study Portal")
st.write("Your one-stop destination for all your career guidance and study needs.")
st.write("Explore our resources, get personalized advice, and take the next step towards your dream career!")

st.header("Notes for all stream and subjects")
st.subheader("Choose a notes of subject you want")

st.markdown("<br>", unsafe_allow_html=True)

# 🎨 STREAM CARDS
col1, col2, col3 = st.columns(3)

with col1:
    st.image("artifacts/images/SCI.jpg")
    st.markdown("### 🔬 Science")
    st.write("PCM, PCB, Engineering, Medical")

with col2:
    st.image("artifacts/images/COM.webp")
    st.markdown("### 💼 Commerce")
    st.write("CA, Business, Finance")

with col3:
    st.image("artifacts/images/Arts.webp")
    st.markdown("### 🎨 Arts")
    st.write("UPSC, Law, Humanities")


# 📚 NOTES SECTION
st.markdown("---")
st.header("📚 Notes Section")

stream = st.radio("Select Your Stream", ["Science","Commerce","Arts"])

if stream == "Science":
    subject = st.selectbox("Select Subject", ["Physics", "Chemistry", "Maths"])

    if subject == "Physics":
        
        with open("notes/physics.pdf", "rb") as file:
            st.download_button(
            label="📥 Download Physics Notes",
            data=file,
            file_name="physics.pdf",
            mime="application/pdf"
        )

    elif subject == "Chemistry":
        with open("notes/chemistry.pdf", "rb") as file:
            st.download_button(
            label="📥 Download Chemistry Notes",
            data=file,
            file_name="chemistry.pdf",
            mime="application/pdf"
        )

    elif subject == "Maths":
        with open("notes/maths.pdf", "rb") as file:
            st.download_button(
            label="📥 Download Maths Notes",
            data=file,
            file_name="maths.pdf",
            mime="application/pdf"
        )

elif stream == "Commerce":
    subject = st.selectbox("Select Subject", ["Accounts", "Economics", "Business Studies"])
    if subject == "Accounts":
        with open("notes/accounts.pdf", "rb") as file:
            st.download_button(
                label="📥 Download Accounts Notes",
                data=file,
                file_name="accounts.pdf",
                mime="application/pdf"
            )
    else:
        st.write(f"📘 {subject} Notes coming soon...")

elif stream == "Arts":
    subject = st.selectbox("Select Subject", ["History", "Political Science", "Physical Education"])
    if subject == "Physical Education":
        with open("notes/physical_education.pdf","rb") as file:
            st.download_button(
                label="📥 Download Physical Education Notes",
                data=file,
                file_name="physical_education.pdf",
                mime="application/pdf"
            )
    else:
        st.write(f"📘 {subject} Notes coming soon...")

selected_class = st.selectbox("Select Your Class", ["11th", "12th"])


# 📩 CONTACT SECTION
st.markdown("---")
st.header("📩 Contact Us")

with st.form("contact_form"):
    name = st.text_input("Enter Your Name")
    phone = st.text_input("Enter Your Contact No")
    email = st.text_input("Enter Your Email Id")
    address = st.text_area("Enter Your Full Address", placeholder="Mumbai")

    submit = st.form_submit_button("Submit")

    if submit:
        st.success("✅ Form submitted successfully!")
        st.write(f"Welcome {name} 🎉")
        st.switch_page('pages/form_feedback.py')