from random import choice

word = "champion"
words = list(word)
loop = True
lst =[]
while loop:
    random_letter = choice(words)
    words.remove(random_letter)
    lst.append(random_letter)
    if len(words) == 0:
        loop = False
print(*lst)

ans = input ("Your Guess")

if ans == word:
    print ("Hura")
else: 
    print (":(")

