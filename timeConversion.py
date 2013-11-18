#CurrentTime

currentTimeStr = input("What time is it? ")
alarmSetTimeStr = input("How long do you need to wait? ")

currentTimeInt = int(currentTimeStr)
alarmSetTimeInt = int(currentTimeStr)

hours = currentTimeInt + alarmSetTimeInt

timeOfDay = hours % 24

print(timeOfDay)