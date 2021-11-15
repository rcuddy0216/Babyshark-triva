quiz = {
    1 : {
        "question" : "Who is the Baby shark?",
        "answer" : "Callan"
    },
    2 : {
        "question" : "Who is the Mamma Shark?",
        "answer" : "Amy"
    },
    3 : {
        "question" : "Who is the Daddy shark?",
        "answer" : "Ryan"
    },
    4 : {
        "question" : "Who is the Doggy shark?",
        "answer" : "Finn"
    }
}

def check_ans(question, ans, attempts, score):
    """
    #Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    
    if quiz[question]['answer'].lower() == ans.lower():
        return True
    else:
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])
        else:
            print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
            return False


def intro_message():
    """
    Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
    Returns true regardless of any key pressed.
    """
    print("\n\n\n\nWelcome to this fun game about sharks! \nAre you ready to test your knowledge?")
    input()
    return True


# python project.py
intro = intro_message()
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer: ")
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1

    break



print("Thanks for playing! Your score is " + str(score) + "out of 4" )


