import matplotlib.pyplot as plt

# Data
products = ["Product A", "Product B", "Product C"]
profits = [1000, 1500, 1200]

# Create a bar chart
plt.bar(products, profits, color="skyblue")
plt.title("Product Profits")
plt.xlabel("Products")
plt.ylabel("Profit")
plt.show()
