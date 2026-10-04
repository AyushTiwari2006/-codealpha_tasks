# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 175,
    "AMZN": 190
}

# Display available stocks
print("Available Stocks:")
for stock in stock_prices:
    print(f"{stock}: ${stock_prices[stock]}")

portfolio = {}
total_investment = 0

# Get number of stocks
n = int(input("\nHow many different stocks do you want to buy? "))

# Get stock names and quantities
for i in range(n):
    stock = input("Enter stock name: ").upper()

    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))

        investment = stock_prices[stock] * quantity
        portfolio[stock] = quantity
        total_investment += investment

        print(f"Investment in {stock}: ${investment}")
    else:
        print("Stock not found in the available stock list.")

# Display portfolio
print("\n----- Stock Portfolio -----")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock}: {quantity} shares = ${value}")

print(f"\nTotal Investment: ${total_investment}")

# Save result to a text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio\n")
        file.write("----------------------\n")

        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} shares = ${value}\n")

        file.write(f"\nTotal Investment: ${total_investment}")

    print("Portfolio saved successfully to portfolio.txt")
