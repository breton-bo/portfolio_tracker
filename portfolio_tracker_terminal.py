import yfinance as yf

#list containing stocks for portfolio
stock_list = []

portfolio_value = 0
portfolio_cost = 0

while True:
    ticker_name = input("\nEnter the name of your stock ticker\n").upper()
    
    #Testing for valid ticker name input
    try:
        test_ticker = yf.Ticker(ticker_name)
        test_price = test_ticker.fast_info["lastPrice"]
        
        if test_price is None:
            raise ValueError
        
    except (KeyError, Exception):
        print("\nInvalid stock ticker name, Try Again!\n")
        continue
    
    #Testing for valid share input
    while True:
        try:
            user_shares = float(input("How many shares have you bought?\n"))
            if user_shares<= 0:
                print("Share value must be greater than 0!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")
    
    #Testing for valid price input
    while True:
        try:
            stock_price = float(input("At what price did you buy each share?\n"))
            if stock_price <= 0:
                print("Stock price must be greater than 0!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")
    
    stock = {"ticker": ticker_name, "shares": user_shares, "buy_price": stock_price,}
    
    #Adds stock information to stock list
    stock_list.append(stock)
    
    break_loop = input("Are you done entering your stocks?\n")
    
    if break_loop.lower() in ["yes","y"]:
        break

#Grabs live stock information and performs calculations for value and profit margins
for stock in stock_list:
    ticker = yf.Ticker(stock["ticker"])
    current_price = ticker.fast_info["lastPrice"]
    

    original_cost = stock["shares"] * stock["buy_price"]
    current_value = stock["shares"] * current_price

    stock_gain = current_value - original_cost
    profit_percentage = (stock_gain / original_cost) * 100
    
    #puts the negative sign in front of $ if stock is at a loss
    if stock_gain < 0:
        gain_string = f"-${abs(stock_gain):,.2f}"
        percentage_string = f"-{abs(profit_percentage):,.2f}%"
        
    else:
        gain_string = f"+${stock_gain:,.2f}"
        percentage_string = f"{profit_percentage:,.2f}%"
    
    #prints out stock value and profit margin
    print(f"Ticker: {stock['ticker']}   |   Stock Value: ${current_value:,.2f}  |   Profit/Loss: {gain_string}  |   Return:{percentage_string}")
    
    portfolio_value += current_value
    portfolio_cost += original_cost
    
portfolio_gain = portfolio_value - portfolio_cost

if portfolio_cost > 0:
    portfolio_percentage = (portfolio_gain/portfolio_cost) * 100
    
else:
    portfolio_percentage = 0
    
if portfolio_gain < 0:
    portfolio_gain_string = f"-${abs(portfolio_gain):,.2f}"
    portfolio_percentage_string = f"-{abs(portfolio_percentage):,.2f}%"
else:
    portfolio_gain_string = f"+${portfolio_gain:,.2f}"
    portfolio_percentage_string = f"{portfolio_percentage:,.2f}%"

#prints out total portfolio information    
print(f"\nPortfolio    |   Total Value: ${portfolio_value:,.2f}    |    Total Profit/Loss: {portfolio_gain_string}    |    Total Return: {portfolio_percentage_string}")