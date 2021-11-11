from products import product as prd


def handleSelection(selectedId):
    selectedId=selectedItems.split(" ")
    cartItem=[]
    for id in selectedId:  
        for item in prd:
            
            if item["id"]==int(id):
                cartItem.append(item)
                
    return cartItem



def showCart(cartProducts):
    cartPrice=0
    for item in cartProducts:
        cartPrice+=item["price"]
        print("Sr No: "+  str(item["id"] ) +" "+ "Name: "+item["name"] +" "+ "Price: "+str(item["price"]) +" "+ "Quantity: "+str(item["quantity"]))
    print('\n')
    print("Your total amount is:",cartPrice)



def showShopProducts():
    for item in prd:
        print("Sr No: "+  str(item["id"] ) +" "+ "Name: "+item["name"] +" "+ "Price: "+str(item["price"]) +" "+ "Quantity: "+str(item["quantity"]))


if __name__=="__main__":
    print("Welcome In My Shop")
    showShopProducts()
    # print("Select Products")
    print('\n')
    selectedItems=input("Please Enter products Sr No To select Them: ")
    print('\n')
    cartProducts=handleSelection(selectedItems)
    print("Your cart products are:")
    print('\n')
    showCart(cartProducts)
