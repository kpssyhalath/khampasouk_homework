
# exam1 Multiple Statements in the if block
price=50
quantity=5
if price*quantity<500:
    print("price*quantity is less than 500")
    print("price=",price)
    print("quantity=",quantity)


#exam2 Invalid Indentation in the block
price = 50
quantity = 5 
if price*quantity < 100:
    print("price is less than 500")
    print("price=",price)
    print("quantity=",quantity)

#exam3 Multiple if condition
price = 100
if price > 100: 
    print("price is greater than 100")
if price == 10:
    print("price is 100")
if price <100:
    print("price is less than 100")


#exam4 else condition 
price = 50
if price >= 100:
    print("price is greater than 100")
else:
    print("price is less than 100")


#exam5 if-elif Condition
price = 100
if price > 100:
    print("price is greater than 100")
elif price == 100:
    print("price is 100")
elif price < 100:
    print("price is lees than 100")
