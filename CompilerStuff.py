"""
Matt Strand
Recursive Descent Calculator Grammar
3/19/2019
"""

digit = ["0","1","2","3","4","5","6","7","8","9"]

#check if digit
def digits(num):
    if num in digit:
        return True
    else:
        return False
    
#check if real number
def realNumber(calc):
    chars = list(calc)
    count = 0

    while count < len(chars):
        if digits(chars[count]) or chars[count] == ".":
            count = count + 1
        elif chars[count] == "+" or chars[count] == "-" or chars[count] == "(" or chars[count] == ")" or chars[count] == "*" or chars[count] == "/":
            count = count + 1
        else:
            return False
    return True

#check if expression
def expression(calc):
    chars = list(calc)
    if "-" in chars or "+" in chars or "(" in chars and ")" in chars or term(calc):
        return True
    else:
        return False


#check if factor
def factor(calc):
    if realNumber(calc) or expression(calc):
        return True
    else:
        return False

#check if term
def term(calc):
    chars = list(calc)
    if factor(calc) and "*" in chars or "/" in chars:
        return True
    else:
        return False

#
#MAIN
#
#creates loop to run until exit
looper = True
while looper:
    calc = input("Type stuff for the simple calc:")

    #by checking against real number, this calls the rest of the functions within other functions
    #this also gives a base of if the user entered valid input
    if realNumber(calc) == False:
        print("Invalid Entry")
    else:
        print("Valid Input")


