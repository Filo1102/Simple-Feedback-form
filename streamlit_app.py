import streamlit as st

st.title(":blue[USER SATISFACTION FORM]")
st.write(":green[**Let us know your opinion. Your feedback is important for us**]")

# Creating a form
with st.form("user_form"):
    # Text input (name)
    name = st.text_input("Full Name:", placeholder="Enter your name...")

    # Number input (age)
    age = st.number_input("Age:", min_value=1, max_value=120, value=25, step=1)

    # Select box (dropdown) for gender
    gender = st.selectbox("Gender:", ["Select an option", "Male", "Female", "Other"])

    # Slider for rating
    Rating = st.slider("App's rating", 1, 5, 3)

    Feedback = st.text_area("Any additional feedback or thoughts?", placeholder="Write your comment here...")
    # Submit button
    submitted = st.form_submit_button("Submit")

# Display output after submission
if submitted:
    
    if name and gender != "Select an option":
        st.success(f"✅ Form submitted!\n\n**Name:** {name}\n**Age:** {age}\n**Gender:** {gender}")
        
        st.write("⭐ **App rating:**", Rating)
        st.write("💬 **Additional Feedback:**", Feedback)

        if Rating <= 2:
            st.warning("Thank you for your feedback. We'll work to improve.")
        elif Rating >= 4:
            st.success("Thank you, we're happy you enjoyed the app!")

    else:
        st.warning("⚠️ Please fill out all fields correctly.")