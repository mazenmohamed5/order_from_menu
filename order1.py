menu = ["chicken burger" , "cheese burger" ,"hot dog" ,
        "sausage and cheese sandwich" , 
        "cola" , "pepsi" ,"water"]

name = input("what is your name sir? \n")
print ("hello " +name+" here is our menu , what do you want \n ")
print ("menu \n food")
print ("chicken burger 30$ \ncheese burger 20$ \nhot dog 10$ \nsausage&cheese sandwich 15$")
print ("drinks \n cola 2$ \n pepsi 2$ \n water 1.5$")

def get_order():
    current_order = []
    while True:
        print("What can I get for you?")
        order = input()
        if order in menu:
            current_order.append(order) #append for add an order
        else:
            print("I'm sorry, we don't serve that.")
            continue
        if is_order_complete():
            return current_order


def is_order_complete():
    print("Anything else? yes/no")
    choice = input()
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        raise Exception("invalid input")


def output_order(order_list):
    print(" RECIEPT \n")
    for order in order_list:
        print(order)

def main():
    order = get_order()
    output_order(order)
    

if __name__ == "__main__":
    main()        
    print ("thank you , the food will be done in 30 minutes")
