def stock_portfolio_tracker():
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOG": 2800, "AMZN": 3500}
    total_value = 0
    stocks = {}

    print("📈 Welcome to Stock Portfolio Tracker!")
    while True:
        name = input("Enter stock symbol (or 'done' to finish): ").upper()
        if name == 'DONE':
            break
        if name not in stock_prices:
            print("❗ Stock not in price list.")
            print("Available slocks  = AAPL,TSLA,GOOG,AMZN")
            continue
        quantity = int(input(f"Enter quantity for {name}: "))
        stocks[name] = quantity
        total_value += stock_prices[name] * quantity

    print("\n📊 Portfolio Summary:")
    for name, qty in stocks.items():
        print(f"{name} - Quantity: {qty}, Price: ₹{stock_prices[name]}, Value: ₹{stock_prices[name] * qty}")
    print(f"\n💰 Total Investment: ₹{total_value}")

    # Save to file (optional)
    with open("portfolio.txt", "w") as file:
        for name, qty in stocks.items():                                           
            file.write(f"{name},{qty},{stock_prices[name]},{stock_prices[name] * qty}\n")                              
        file.write(f"Total,{total_value}\n")
    print("📁 Portfolio saved to 'portfolio.txt'")
                                                                                                                                                                                                             
stock_portfolio_tracker()
