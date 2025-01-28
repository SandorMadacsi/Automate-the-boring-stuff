 #! python3
 
import random, time


def exit():
    print("Time is up!")
    
numOfQuestions = 10
correctAnswers = 0
answers = []

for question in range(numOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s X %s = ' %(question, num1, num2)
    numOfTries = 1
    timeUp  = False
    answer = 0
    start_time = time.time()
    while answer != num1 * num2 and numOfTries != 3:
        answer = int(input(prompt))
        current_time = time.time()
        elapsed_time = current_time - start_time
        print(elapsed_time)
        numOfTries += 1
        if elapsed_time >= 8:
            timeUp = True
            print(timeUp)
            break
        time.sleep(1)
    if timeUp == True:
        print("Your time is up!")
        answers.append({question: "Incorrect"})
    elif numOfTries == 3:
        print("You have used up your tries. Try again next time!")
        answers.append({question: "Incorrect"})
    else:
        print("Correct answer!")
        answers.append({question: "Correct"})
print(answers)
    

    