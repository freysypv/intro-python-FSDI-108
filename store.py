from catalog import catalog  # import catalog list

#global shipping cart
cart = []
    
    #Helper Functions (store name/ menu)
def print_header(text):
    print("---------------------------")
    print(text)
    print("---------------------------")

def print_menu():
    print("menu")
    print("1.- View catalog")
    print("2.- Search product")
    print("3.- View cart")
    #add more options if neeed
    print("4.- Clear Cart")
    print("Q.- Quit")

    #catalog and Cart Function
def print_catalog():
    print_header("- Our Catalog -")
    for prod in catalog: 
         # L just means left. 15 spaces to the right
       
        print(f"| {prod['id']} | {prod['title'].ljust(15)} | {(prod["price"]):.2f}")


    answer = input("Type ID to add (N to cancel):")
    if answer.lower() == "n":
        return
    else:
        add_product_to_cart(answer)
    print("------------------------")

def add_product_to_cart(prod_id):
    found = False
    for prod in catalog:
        if str(prod["id"]) == str(prod_id):
            found = True
            cart.append(prod) #add product to the cart (bag)
            print(f"{prod["title"]} added to your cart")
            break

    if not found:
        print("Item does not exist")

def search_product():
    text = input("Search text: ").lower()  
    found = False
    for prod in catalog:
        if text in prod["title"].lower():
            found = True
            
        print(f"| {prod['id']} | {prod['title'].ljust(15)} | {(prod["price"]):.2f}")

        choice = input("do you want to add this item to your cart? (y/n)")
        if choice.lower() == "y":
            add_product_to_cart(prod["id"])
        break # stop after fist match

    if not found:
        print("sorry, this items doesn't exist.")
    print("----------------------")

def view_cart():
    print_header("your Cart")  
    if not cart:
         print("Your cart is empty")
    else:
        for prod in cart:
            print(f"| {prod['id']} | {prod['title'].ljust(15)} | {(prod["price"]):.2f}")

        cart_total() # shows total price   

def cart_total():
    #for loop total += prod"price"
    #print("total")
    total = 0 # start from 0 and prices up
    for prod in cart:
        total += prod["price"] # add product price to total
    print(f"Total is: ${total:.2f}") 

 # create a function called clear_cart()
 #code it should crear the cart
 # printa message saying " cart is cleared"
 # add it to the menu up top and the main program loop
def clear_cart():
        cart.clear()
        print("Your cart has been cleared")


# main program loop
option = ""
while option != "q" and option != "Q":
    print_header("Welcome to Store")
    option = input("Choose an option: ")

    if option == "1":
       print_catalog()
    elif option == "2":
        search_product()
    elif option == "3":
        view_cart()
    elif option == "4": # Added to loop
        clear_cart
    elif option == "q" or option == "Q":
        print("Good Bye")
        break
    else:
        print("** error: invalid option")
        print("-------------------------")



    



   







