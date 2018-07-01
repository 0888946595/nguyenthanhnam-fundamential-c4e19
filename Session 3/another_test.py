# food1 = "Kem"
# food2 = "Xoi"
# food3 = "Pho"
# food4 = "Thit"
# food5 = "Tao Pho"

# list / array

menu = ["Kem","Xoi", "Pho", "Thit", "Tao Pho"]

# del: xoa theo index

# del menu [1]

# pop: xoa theo index
# menu.pop(1)

# remove: xoa theo item

# menu.remove ("Tao Pho")


#sep = separator: khoang cach

# print (*menu, sep=", ")
# print(len(menu))   

# len = lenght (chieu dai ky tu)

menu.append("Che")
# append: them thong tin

print (*menu, sep=", ")
print(len(menu))

# for i in range (len(menu)):
#     print(menu[i])
# chi in ra index
# for index, item in enumerate(menu):
#     print (index, item)

for item in menu:
    print (item)


