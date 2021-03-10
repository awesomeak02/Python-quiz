import requests 
import pprint
import json
import html
import random

url="https://opentdb.com/api.php?amount=1&category=18&type=multiple"
end_game=""
score_correct=0
score_incorrect=0
while end_game !="quit":
    answer_no=1
    r=requests.get(url)
    if r.status_code != 200:
        end_game=input("Sorry there was some error retrieviewing the qts. Press enter for next question or just type quit to leave the session")
    else:
        valid_answer=False
        dict1=json.loads(r.text)
        question=dict1["results"][0]["question"]
        answers=dict1["results"][0]["incorrect_answers"]
        correct_answer=dict1["results"][0]["correct_answer"]
        answers.append(correct_answer)
        random.shuffle(answers)
        print(html.unescape(question) + " \n")
        for answer in answers:
            print(str(answer_no) + ". " +answer)
            answer_no+=1
        user_ans=int(input("Enter the answer no"+"\n"))
        if str(answers[user_ans-1])== correct_answer:
            print("Correct Answer!!")
            score_correct+=1
        else:
            print("Sorry! Better luck next time :(")
            print(answers[user_ans-1] + " is not the the right answer :(")
            print("Correct answer is " + html.unescape(correct_answer))
            score_incorrect+=1
       
        end_game=input("Press enter to continue or type quit to end the session" + "\n").lower()

total_score=score_correct+score_incorrect
print("\nYou Scored "+ str(score_correct) + " out of " + str(total_score))
print("\nThanks For Playing ! It was nice havin you here !!!")



