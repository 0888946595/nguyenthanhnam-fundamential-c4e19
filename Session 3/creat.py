# print ("Hi there, here your favorites thing so far ")

# menu = ["death note", "netlix", "teaching"]

# print (*menu, sep=", ")

# add = input ("Name one thing you want to add? ")

# menu.append(add)

# print (*menu, sep=", ")


print ("Hi there, here your favorite things so far")

new_fav = ["death note", "netflix", "teaching"]

for index, item in enumerate (new_fav):
    print(index, item, sep=". ")

print (*new_fav, sep=", ")

update = int(input("Position you want to update? "))
print (update)
update_fav = input("Your replacing fav: ")
new_fav [update -1] = update_fav

for index, item in enumerate (new_fav):
    print(index, item, sep=". ")


