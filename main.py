# tee ratkaisu tänne
dic = {}

while True:
    answer = int(input("command(1 search, 2 add, 3 exit):"))
    if answer == 2:
        name = input("name: ")
        number = input("number: ")
        if name in dic:
            dic[name].append(number)
        else:
            dic[name] = [number]
        print("added successfully!")
    elif answer == 1:
        name = input("name: ")
        if name in dic:
            for x in dic[name]:
                print(x)
        else:
            print("no number")
    elif answer == 3:
        print("exit...")
        break