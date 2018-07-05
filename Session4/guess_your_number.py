from random import randint

low = 0
high = 100


com = input("Now think of a number from 0 to 100, then pess'Enter' ")
input()
# print ("All you have to do is answear t my guess")
# print ("'c' if my guess is 'C'orrect than your number")
# print ("'s' if my guess is 'S'maller than your number")
# print ("'l' if my guess is 'L'orrect than your number")

print("""
All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller
'l' if my guess is 'L'arger
""")

loop = True
# print(")

while loop:
    mid = (low + high) // 2
    ans = input("Is {0} your number? ".format(mid)).lower()
    if ans == "l":
        high = mid
        print ("Larger")       
    elif ans == "s":
        low = mid
    elif ans == "c":
        print ("I knew it ")
        loop = False
        
