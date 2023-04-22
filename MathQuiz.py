import random

def math_quiz():
    while True:
        try:
            level = int(input("Select difficulty level: 1-Easy, 2-Medium, 3-Hard\n"))
            if level not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print("Please enter only 1, 2 or 3 !")
    
    if level == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif level == 2:
        num1 = random.randint(1, 30)
        num2 = random.randint(1, 30)
    elif level == 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    
    question1 = f"What is {num1}+{num2}?"
    answer1 = num1 + num2
    question2 = f"What is {num1}*{num2}?"
    answer2 = num1 * num2
    question3 = f"What is {num1}/5-{num2}/10?"
    answer3 = round(num1/5 - num2/10, 2)
    
    print(question1)
    while True:
        try:
            user_answer1 = float(input())
            break
        except ValueError:
            print("Please enter the number only")
    if user_answer1 != answer1:
        print("Gameover!")
        return
    print(question2)
    while True:
        try:
            user_answer2 = float(input())
            break
        except ValueError:
            print("Please enter the number only")
    if user_answer2 != answer2:
        print("Gameover!")
        return
    print(question3)
    while True:
        try:
            user_answer3 = float(input())
            break
        except ValueError:
            print("Please enter the number only")
    if user_answer3 != answer3:
        print("Gameover!")
        return
    
    print("Congratulations! You are winner!")

math_quiz()
