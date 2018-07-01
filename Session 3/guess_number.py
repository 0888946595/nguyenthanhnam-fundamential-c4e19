# # from random import randint


# # guess = 49
# # loop = True
# # guess = int(input("Guess my number (1-100): "))
# # while loop:
# #     if guess >50:
# #         # loop = False
# #         print("A Little too large ")
# #     elif guess <48:
# #         # loop = False
# #         print("Wrongggg")
# #     else:
# #         print ("bingo ")
# #         loop = False

# # print ()

from random import randint

numb = 49

playing = True
count = 0
while playing:
    guess = int(input("Guess my number (0-100): "))

    if guess > numb:
        print ("Too large ")
    elif guess < numb:
        print ("too Small ")
    else:
        print ("Bingo ")
        playing = False
        

    count += 1
    if count == 7:
        print ("You lose ")
        playing = False


