from Purchase import Purchase
from Phone import Phone

# myPurchase = Purchase()

# print(myPurchase.internet_connection)
# print(myPurchase.phones_lines)
# print(myPurchase.cell_phones)
# print(myPurchase.price)

mySecondPurchase = Purchase()
myFirstPhone = Phone("iPhone99", 30)
mySecondPhone = Phone("Samsung99", 10)

mySecondPurchase.internet_connection = False
mySecondPurchase.phones_lines = 3
mySecondPurchase.cell_phones = [myFirstPhone, mySecondPhone]
mySecondPurchase.price = 300

print(mySecondPurchase.internet_connection)
print(mySecondPurchase.phones_lines)
print(f"{mySecondPurchase.cell_phones[0].name}-{mySecondPurchase.cell_phones[0].price}")
print(f"{mySecondPurchase.cell_phones[1].name}-{mySecondPurchase.cell_phones[1].price}")
print(mySecondPurchase.price)
