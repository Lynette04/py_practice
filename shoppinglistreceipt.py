items_price={
    "sugar": 4000,
    "soap" : 3000,
    "salt": 1000,
    "splash": 2000,
    "soda": 1000,
    "tea leaves": 3000,
    "water": 1000,
    "flour": 10000,
    "eggs": 14000
}


cart=[]
def fill_cart():
    print("-----WELCOME TO ML Supermarket-----")
    print("Below is the list of our available items")
    print(f"{'Name':<15} | {'Price':<10}")
    print("-" * 28)
    
    for key, value in items_price.items():
        print(f"{key:<15} |  ugx{value:<10}")
    
    n= int(input("Enter the number of distinct items to add to your cart: "))
    total=0
    for i in range(n):
        cart_item= input("Enter an item to add to your cart: ")
        cart.append(cart_item)
        total+=items_price[cart_item]
        
    for item in cart:
        print(f"{item} -> ugx{items_price[item]}")
    print(f"Your total is ugx{total}. Feel free to come back and shop with us our lovely customer.")    
    



    
    
    
   
    
    
        
      

    

fill_cart()
