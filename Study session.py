#Study focus timer
#So this is very basic logic, every 10 minutes it should ping me, "Are you studying?" by asking a yes or no question, n marks the session is broken, if y it continues, and gives me scores based on check-na

import time
count = 0
score = 0
while count<5:
    Answer = input("Are you still focused?(y/n)")
    if Answer in ('y','Y'):
        print("Great! keep up the good work")
        score += 20
        count += 1
        if count == 5:
            break
        time.sleep(600)
    elif Answer in ('n','N'):
        print("Session ended.")
        break
    else:
        print("Please choose a valid answer.")
print(f"Your final score is {score}%")
