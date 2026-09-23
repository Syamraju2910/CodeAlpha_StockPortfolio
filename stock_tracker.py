import csv

STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 160.00,
    "AMZN": 190.00
}


def save_portfolio(records, filename="portfolio.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Price", "Investment Value"])
        writer.writerows(records)
        writer.writerow(["TOTAL", "", "", sum(row[3] for row in records)])


def run_tracker():
    print("\n=== CodeAlpha Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(STOCK_PRICES))

    records = []

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not available in the predefined price list.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a positive whole-number quantity.")
            continue

        price = STOCK_PRICES[stock]
        value = price * quantity
        records.append([stock, quantity, price, value])
        print(f"{stock}: {quantity} × ${price:.2f} = ${value:.2f}")

    if not records:
        print("No stocks entered.")
        return

    total = sum(row[3] for row in records)

    print("\n--- Portfolio Summary ---")
    for stock, quantity, price, value in records:
        print(f"{stock}: {quantity} shares × ${price:.2f} = ${value:.2f}")
    print(f"Total Investment Value: ${total:.2f}")

    save_portfolio(records)
    print("Portfolio saved to portfolio.csv")


if __name__ == "__main__":
    run_tracker()
