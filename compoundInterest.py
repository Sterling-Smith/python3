#principal amount (initial investment)	
P = 1000

#number of times the interest is compounded per year
N = 12

#annual nominal interest rate (as a variable)
R = .08

#number of years
t = int(input("How many years will your money compound for? "))

final = P * ((1 + (R / N)) ** (N * t))

print("The final amount after", t, "years is", final)