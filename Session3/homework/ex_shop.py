print ("Have A Nice Day!!! ")

our_item = ["T-Shirt","Sweater"]
count = 0
loop = True


while loop:
    action = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if action == "r" or action == "R":
        print (*our_item, sep=", ")
    elif action == "c" or action == "C":
        creat_shop = input("New items? ")
        our_item.append (creat_shop)
        print (*our_item, sep=", ")
    elif action == "u" or action == "U":
        u_shop = int(input("Update Position: "))
        update_shop = input ("New items: ")
        our_item [u_shop -1] = update_shop
        print (*our_item, sep=", ")
    elif action == "d" or action == "D":
        del_pos = int(input("Delete Position: "))
        our_item.pop (del_pos)
        print(*our_item, sep=", ")
    else:
        print ("Access Denied")
    
    count +=1
    if count == 4:
        print ("See You Again ")
        loop = False




   