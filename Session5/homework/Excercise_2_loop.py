number = [1, 6, 8, 1, 2, 1, 5, 6]
count = 0

ask = int(input("Enter a number: "))

for item in number :
    if item == ask :
        count += 1

print("{0} appears {1} times in my list".format(ask, count))
