from Data import data

text1 = ""

def v1() :
    count = 0
    text1 = ""
    while (count < len(data)) :
        text1 = text1 + data[count] + " : "
        count = count + 1
        # change the sign for + or - depending on the number.
        if (data[count] >= 0) :
            text1 = text1 + "GMT+" + str(data[count]) + "\n"
        else :
            text1 = text1 + "GMT" + str(data[count]) + "\n"
        count = count + 1

def v2() :
    count = 0
    list = []
    text2 = ""
    while (count < len(data)):
        text2 = text2 + data[count] + " : "
        count = count + 1
        # change the sign for + or - depending on the number.
        if (data[count] >= 0):
            text2 = text2 + "GMT+" + str(data[count])
        else:
            text2 = text2 + "GMT" + str(data[count])
        list.append(text2)
        text2 = ""
        count = count + 1
    list.sort()
    text = ""
    count = 0
    while (count < len(list)) :
        text = text + list[count] + "\n"
        count = count + 1

    print("there are " + str(len(list)) + " registered members")
    print(text)

def v3() :
    count = 0
    list = []
    text2 = ""
    while (count < len(data)):
        text2 = text2 + data[count]
        list.append(text2)
        text2 = ""
        count = count + 2
    list.sort()
    text = ""
    count = 0
    while (count < len(list)) :
        text = text + list[count] + "\n"
        count = count + 1

    print("there are " + str(len(list)) + " registered members")
    print(text)

def v4() :
    count = 1
    list = []

    while (count < len(data)):
        list.append(data[count])
        count = count + 2

    list.sort(reverse=False)
    text = ""
    count = 0

    while (count < len(list)):
        text = text + str(list[count]) + "\n"
        count = count + 1

    print("there are " + str(len(list)) + " registered members")
    print(text)

def v5() :
    question = input("Enter a player's IGN : ")
    count = 0
    found = False
    while (count < len(data) and found == False):
        if (data[count] != question) :
            count = count + 2
        else :
            # change the sign for + or - depending on the number.
            if (data[count + 1] >= 0):
                print(f"The timezone of the player named " + data[count] + " is GMT+" + str(data[count + 1]))
            else:
                print(f"The timezone of the player named " + data[count] + " is GMT" + str(data[count + 1]))
            found = True

    if (found == False) :
        print("The IGN was not found, check if you spelled '" + question + "' correctly")


# Change to v1() for the list of players with their timezones in the list's order.
# Change to v2() for the list of players with their timezones in alphabetical order.
# Change to v3() for the list of players in alphabetical order.
# Change to v4() for the list of timezones in lowest to highest value order.
# Change to V4() for a Search menu by IGN.

v4()