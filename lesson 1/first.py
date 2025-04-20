def calulate(price,quantity):
    discount=0.2
    all=price*quantity*(1-discount)
    return all


price=float(input("price is:"))
quantity=float(input("quantity is:"))

print("price after discount is: "+str(calulate(price,quantity)))