# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for day_index in range(5):
    promotion = daily_promotions[day_index]
    print(f"{weekdays[day_index]}: Promotion on {promotion}")