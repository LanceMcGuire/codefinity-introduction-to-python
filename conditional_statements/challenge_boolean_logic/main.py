seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100
overstock_risk = False
overstock_risk = seasonal and (current_stock>high_stock_threshold)
discount_eligible = False
discount_eligible = not selling_well and not on_sale
make_discount = False
make_discount = overstock_risk or discount_eligible
print("Should the item be discounted?",make_discount)