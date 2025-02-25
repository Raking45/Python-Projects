#Replit to Github
#Define a dictionary of stock ticker symbols and prices. 
stock_data = {
  "AAPL": {"name": "Apple Inc", "price": 169.68},
  "AMZN": {"name": "Amazon.com Inc", "price": 105.45},
  "GOOG": {"name": "Alphabet Inc Class C", "price":108.22},
  "META": {"name": "Meta Platforms Inc", "price": 240.32},
  "NFLX": {"name": "Netflix Inc", "price": 329.93},
  "DIS": {"name": "Walt Disney Company", "price": 102.50},
  "TSLA": {"name": "Tesla Inc", "price": 164.31},
  "F": {"name": "Ford Motor Company", "price": 11.88},
  "AAPL": {"name": "Apple Inc", "price": 169.68},
  "MSFT": {"name": "Microsoft Corporation", "price": 307.26},
  "INTC": {"name": "Intel Corporation", "price": 31.06},
  "NVDA": {"name": "NVIDIA Corporation", "price": 277.49},
  "JPM": {"name": "JPMorgan Chase & Co", "price": 138.24},
  "BAC": {"name": "Bank of America Corp", "price": 29.28},
  "HBAN": {"name": "Huntington Bancshares Incorporated", "price": 11.20}, 
}

#Print instructions to the user. 
print("Enter a stocks ticker symbol to look up current value.")
print("Available ticker symbols: \n AAPL, AMZN, GOOG, META,\n NFLX, DIS, TSLA, F,\n AAPL, MSFT, INTC, NVDA,\n JPM, BAC, HBAN")
print("Enter 'q' to quit.")

#Loop until user enters 'q' to quit program. 
while True:
  
#Get user input for ticker symbol
  ticker_symbol=input("Ticker symbol: ").upper()

#Check to see if user wants to quit program. 
  if ticker_symbol=='Q':
    print("Goodbye!")
    break
  
#Look up price of given symbol
  if ticker_symbol in stock_data:
    stock_name = stock_data[ticker_symbol]["name"]
    stock_price = stock_data[ticker_symbol]["price"]
    print(f"{ticker_symbol} ({stock_name}): ${stock_price:.2f}")
  else:
    print("Invalid ticker symbol. Please try again.")