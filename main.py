print ("welcome to your pomodoro timer")
study_time = int(input("How long would you like to study for?"))
print ("You want to study for", study_time, "minutes")
# expected result
# return: minute value, hour value
# 1 hour = 60 minutes
min_val = study_time * 60
print (min_val, "this is how many minutes you'll be stuyding for")
hour_val = study_time / 60
print(hour_val, "this is how many hours you'll be working for")

for i in range(4):
    t = 25*60