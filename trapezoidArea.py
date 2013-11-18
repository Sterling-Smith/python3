#trapezoidArea.py

#title
print("Area of trapezoid")

#height prompt
height = float(input("Enter the height of the trapezoid:  "))

#bottom base length prompt
bottomBase = float(input("Enter the length of the bottom base:  "))

#top base length prompt
topBase = float(input("Enter the lenght of the top base:  "))

#area calculation
area = .5 * (topBase + bottomBase) * height

#area output
print("The area is: ", area)
