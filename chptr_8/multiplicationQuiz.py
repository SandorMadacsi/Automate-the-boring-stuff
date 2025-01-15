 #! python3
 
import pyinputplus as pyip
import random, time
 
numOfQuestions = 10
correctAnswers = 0
for question in range(numOfQuestions):
 num1 = random.randint(0,9)
 num2 = random.randint(0,9)
 
 prompt = '#%s: %s X %s = ' %(question, num1, num2)
 
 try:
  pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1*num2)],
                blockRegexes=[('.*', 'incorrect')],
                timeout=8, limit=3)
 except pyip.TimeoutException:
     print('Out of time!')
 except pyip.RetryLimitException:
     print('Out of tries! Good luck next time!')
     
 else:
     print('Correct answer')
     correctAnswers +=1
 time.sleep(1)
print('Your correct answer score: %s out of %s' %(correctAnswers,numOfQuestions))