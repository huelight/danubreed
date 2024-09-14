# Random Meal Selector (10 Points)

import random
breakfast = ["bread", "pancakes", "fruits"]
lunch = ["pizza", "burger", "kfc"]
dinner = ["lobsters", "ice cream", "pounded yam"]

print(f"Your meal plan today is \n"
      f"breakfast: {random.choice(breakfast)} \n"
      f"lunch: {random.choice(lunch)} \n"
      f"dinner: {random.choice(dinner)}")

