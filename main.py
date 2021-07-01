print ("welcome to your pomodoro timer")
print("this timer is to help you stay productive")
u = str(input("would you be inputting your time in minutes or hours?"))
studyTime = int(input("How long would you like to study for?"))
print ("You want to study for", studyTime)

import time
# expected result
# return: minute value, hour value
# 1 hour = 60 minutes
if u == 'm':
  studyTimeMinutes = studyTime
  hour_val = studyTime / 60
  print(hour_val, "this is how many hours you'll be working for")
elif u == 'h':
  studyTimeMinutes = studyTime * 60
  print (studyTimeMinutes, "this is how many minutes you'll be studying for")
print ("You will be having a 5 minute break")


print ("let's begin studying")
short_break = 0
long_break = 1
study_session = 0

def countdown(t):
  while t:
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{:02d}'.format(mins,secs)
    print(timer, end="\r")
    time.sleep(1)
    t -=1
  print('worktime!')
t = input("enter the time for pomodoro countdown: ")
# countdown(int(t))

while studyTimeMinutes > 0:
    print ("study")
    studyTimeMinutes = studyTimeMinutes - 25
    print(studyTimeMinutes)
    study_session = study_session + 1
    print ("break")
    short_break = short_break + 1
    # print ("You will be having a 5 minute break")
    countdown(int(t))
    studyTimeMinutes = studyTimeMinutes - 5
    print(studyTimeMinutes)
    print("Study Session Number:", study_session)
    print("Break Number:",short_break)
    if short_break == 4:
      print("It's time for your long break")
      studyTimeMinutes = studyTimeMinutes - 30
      print(studyTimeMinutes) 
    
print("You've reached the end of your study session")
print("Here are your study results") 
print("You studied for a total of:", study_session, "sessions")
print("You took a total of:", short_break, "breaks")



    