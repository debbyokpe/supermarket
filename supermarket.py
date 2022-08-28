import os

products = {"Milo" : 4,
                "Cowbell": 5,
                "Bournvita":5,
                "Peak":5 ,
                "Loya":6,
                "Lux":7,
                "Premier":6,
                "CloseUp":2,
                "Oats":5,
                "Golden Morn":4,
                "Golden Spaghetti":3}

 
while True:
    customer = {}

    print("Welcome To Debby SuperStore")
    
    print("\n")
    
    print("Here are the products available in the supermarket ")

    print("\n")

    print("Product   Value")
    for x in products:
        print(str(x) + "   "+ str(products[x]))
        
    print("\n")

    numberOfItems = int(input("How many Items do you which to buy "))

    print("\n")

    for x in range(numberOfItems):
        product = input("Which Product do you want to buy ")
        print("\n")
        number = int(input("How many of the product do you want "))
        print("\n")

        if product in products.keys():
            if (number > products[product]):
                print("There not enough products please reduce the number of products you want ")
                print("\n")
                number = int(input("How many of the product do you want "))
                print("\n")
        else:
            print("The product does not exist")
            break
    else:
        break

        customer[product] = number
        print(customer)

    print("\n")

    print("Here is your reciept")

    print("\n")

    print("Product   Value")

    print("\n")

    for x in customer:
        print(str(x) + "   "+ str(customer[x]))
    print("\n")
        

    for x in customer:
        remainingStock = products[x] - customer[x]
        products[x] = remainingStock


    print("Here is the remaining Stock")

    print("\n")

    print("Product   Value")
    for x in products:
        print(str(x) + "   "+ str(products[x]))

    print("\n")

    os.system('clear')


    

    

    
        
