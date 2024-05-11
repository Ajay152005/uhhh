subscribers = {}

Menu = """

 1.ADD
 2.VIEW
 3.MODIFY NAME
 4.DELETE
 5.EXIT

 ENTER YOUR OPTIONS: """

while True:
    input_val = eval(input(Menu))

    if input_val == 1:
        name = input("Enter the name: ")
        phone = eval(input("Enter the Phone Number: "))
        subscribers[phone] = name
    elif input_val == 2:
        subscribers_name = []
        for ph, name in subscribers.items():
            subscribers_name.append(subscribers[ph])
        print("Subscribers: ", subscribers_name)
    elif input_val == 3:
        ph = eval(input("Phone number: "))
        if ph in subscribers:
            new_name = input("enter new name: ")
            subscribers[ph] = new_name
        else:
            print("wrong number.")
    elif input_val == 4:
        ph = eval(input("Phone number: "))
        if ph in subscribers:
            del subscribers[ph]
        else:
            print("wrong number.")
    elif input_val == 5:
        break
