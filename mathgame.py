import random
import operator

def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2)
    print(f'What is {num_1} {operation} {num_2}')
    return answer

def ask_question():
    answer = random_problem()
    guess = float(input('Enter you answer: '))
    if guess == answer:
        return True
    return answer

def game():
    score = 0
    while True:
        x = ask_question()
        if x is True:
            score += 1
            print('Correct !')
        else:
            print('Incorrect')
            break
    print(f'======== Game Over ========\nYou score is {score}\nKeep going! \nAnd last answer is {x}')

game()
