grocery_inventory = {
    "Milk":("Dairy",3.50,8),
    "Eggs":("Dairy",5.50,30),
    "Bread":("Bakery",2.99,15),
    "Apples":("Produce",1.50,50)    
}
category,old_price, stock = grocery_inventory["Eggs"]
if old_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (category, old_price -1, stock)
else:
    print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes":("Produce",1.20,30)})
print("Inventory after adding Tomatoes:",grocery_inventory)

category, price, old_stock = grocery_inventory["Milk"]
if old_stock < 10:
    print("milk needs to be restocked. increasing stock by 20 units.")
    grocery_inventory["Milk"] = (category, price, old_stock + 20)
else:
    print("Milk has sufficient stock.")

category, price, old_stock = grocery_inventory["Apples"]
if price > 2.00:
    removed_item = grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
print("Updated inventory:",grocery_inventory)
    
    