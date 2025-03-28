import streamlit as st # type: ignore
import datetime

# st.date_input("Enter your date of birth", datetime.date(1990, 1, 1))

# gender = ["Male", "Female", "Other"]
# st.radio("Select your gender", gender)

#two head slider
# min_value = st.slider("Select a arnge", 100, 300, (25, 75))

st.title("🎉 Happy Birthday Jalees! 🎉")
st.balloons()
st.markdown("""
<style>
@keyframes birthday {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}
h1 {
    color: #FF69B4;
    animation: birthday 1s infinite;
}
</style>
<h1>🎂 Wishing you a day filled with love and joy! 🎂</h1>
""", unsafe_allow_html=True)



# st.write("My name is shoaib")
# st.sidebar.header("This is sidebar")

# number = st.slider("Pick a number", 100, 300)
# st.write(number)

# file = st.file_uploader("Pick a file")
# color = st.color_picker("Pick a color")
# date = st.date_input("Pick a date")

# sidebar bnaya or usme slider lgaya or uski value set ki.
# st.sidebar.header("User input")
# userData = st.sidebar.slider("Select the number of years", min_value=1, max_value=100, value=20)


# st.write(userData * 2)
# st.title("Mai nikla ho gaddi ley ke")
# st.header("this is header")
# st.markdown("# this is markdown")
# st.markdown("## this is markdown")
# st.markdown("### this is markdown")
# st.markdown("#### this is markdown")


# jitna bhi code hoga uska select jesa box bana kar rakhega
# st.code("""
#  st.write("My name is shoaib")
#  st.sidebar.header("This is sidebar")

#  number = st.slider("Pick a number", 100, 300)
#  st.write(number)

#  file = st.file_uploader("Pick a file")
#  color = st.color_picker("Pick a color")
#  date = st.date_input("Pick a date")

# """)


# st.date_input("Enter your name")
# st.text_input("Enter your name")
# st.time_input("Enter your name")
# st.camera_input("Enter your name")
# st.number_input("Enter your name")



# Calculater bnaya STreamlit mein

# st.title("Simple Calculator")

# # Create input fields for the two numbers
# num1 = st.number_input("Enter the first number", value=0.0)
# num2 = st.number_input("Enter the second number", value=0.0)

# # Create a dropdown for selecting the operation
# operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

# # Perform the calculation based on the selected operation
# if st.button("Calculate"):
#     if operation == "Add":
#         result = num1 + num2
#     elif operation == "Subtract":
#         result = num1 - num2
#     elif operation == "Multiply":
#         result = num1 * num2
#     elif operation == "Divide":
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             result = "Error! Division by zero."
    
#     st.write(f"The result is: {result}")
