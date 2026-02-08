import random,time

def generate_question():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    choice = random.choice(['-','+','*','/'])
    
    if choice == '+':
        answer = num1 + num2
    elif choice == '-':
        answer = num1 - num2
    elif choice == '*':
        answer = num1 * num2
    elif choice == '/':
        answer = num1 / num2
    else:
        print("wrong operator")
    
    return f"{num1} {choice} {num2} = ", answer

def math_quiz():
    score = 0
    rounds = int(input("how much question do you want to answer: "))

    
    for i in range(rounds):
        timer = 5
        question,correct_answer = generate_question()
        print(f"\nQuestion {i + 1}. {question}")
        
        user_answer = float(input("Your answer: "))
        if user_answer == correct_answer:
            print("correct answer")
            score += 2
        else:
            print(f"wrong answer this is the correct answer {correct_answer}")
        
        while timer > -1:
            print(f"⏳ Next question in {timer} seconds...", end="\r")
            timer -= 1
            time.sleep(1)
        
            
    print("\nGame Over")
    print(f"Your final score is {score}")
    
    if score == 10:
        print("congratulations, you got all questions correct!!")
    elif score >= 6:
        print('good job!, you did well')
    else:
        print("keep practicing!!")
        
math_quiz()       