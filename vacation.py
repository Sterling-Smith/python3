DAYSINWEEK = 7

startDayStr = input("Please enter your start day number: ")
lengthOfStayStr = input("Please enter the number of days that you will be gone: ")

startDayInt = int(startDayStr)
lengthOfStayInt = int(lengthOfStayStr)

returnDay = startDayInt + lengthOfStayInt % DAYSINWEEK

print(returnDay)