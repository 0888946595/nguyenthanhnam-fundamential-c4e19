tc = {
    "hc": "hoc",
    "ng": "nguoi",
    "pt": "phat trien",
    "eny": "em nguoi yeu",
    "any": "any",
    "ns": "noi",
    "ngta": "nguoi ta",
    "lm": "lam",
    "r": "roi",
    "stt": "status"
}

loop = True
while loop:
    for key in tc.keys():
        print (key, end= "\t ")
    print()
    ask = input("Your Code? ")
    if ask in tc:
        print (tc[ask])
    else:
        print ("Not Found")
        option = input ("Do you want to contribute? (Y/N) " .upper())
        if option == "y":
            trans = input ("Enter you translation: ")
            tc[ask] = trans
            print("updated")
        else:
            print("Bye")
            loop = False


    
