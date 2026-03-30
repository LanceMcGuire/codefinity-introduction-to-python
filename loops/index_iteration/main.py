prices = [29.99, 45.50, 12.75, 38.20]
discount_factor = [.10,.20,.15,.05]
for cost in range(len(prices)):
    prices[cost] = prices[cost]-prices[cost]*discount_factor[cost]
    print(f"Updated price for item {cost}: ${prices[cost]:.2f}")
    