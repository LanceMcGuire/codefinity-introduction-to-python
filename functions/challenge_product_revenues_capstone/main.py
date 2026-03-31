# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

#Calculate the revenue for each product by multiplying the price by the quantity sold, and store all results in a new list called revenue;
products_list = [products, prices, quantities_sold]
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i]*quantities_sold[i])
    return revenue
    
def formatted_output(revenues):
    for name, rev in sorted(revenues):
        print(f"{name} has total revenue of ${rev}")

revenue = calculate_revenue(prices,quantities_sold)
revenue_per_product = list(zip(products, revenue))

formatted_output(revenue_per_product)