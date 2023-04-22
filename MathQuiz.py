import random
import streamlit as st

def math_quiz():
    level = st.sidebar.selectbox("Select difficulty level:", ["Easy", "Medium", "Hard"])
    if level == "Easy":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif level == "Medium":
        num1 = random.randint(1, 30)
        num2 = random.randint(1, 30)
    elif level == "Hard":
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)

    question1 = f"What is {num1}+{num2}?"
    answer1 = num1 + num2
    question2 = f"What is {num1}*{num2}?"
    answer2 = num1 * num2
    question3 = f"What is {num1}/5-{num2}/10?"
    answer3 = round(num1/5 - num2/10, 2)

    st.write(question1)
    user_answer1 = st.number_input("Enter your answer:", value=0.0, step=1.0)
    if user_answer1 != answer1 and user_answer1 != 0:
        st.write("Gameover!")
        return
    st.write(question2)
    user_answer2 = st.number_input("Enter your answer:", value=0.0, step=1.0)
    if user_answer2 != answer2 and user_answer2 != 0:
        st.write("Gameover!")
        return
    st.write(question3)
    user_answer3 = st.number_input("Enter your answer:", value=0.0, step=0.01)
    if user_answer3 != answer3 and user_answer3 != 0:
        st.write("Gameover!")
        return
    
    st.write("Congratulations! You are winner!")

def app():
    st.set_page_config(page_title="Math Quiz", page_icon=":pencil:", layout="wide")
    st.title("Math Quiz")
    math_quiz()

if __name__ == "__main__":
    app()
