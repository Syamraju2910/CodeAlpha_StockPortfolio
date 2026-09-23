# CodeAlpha Stock Portfolio Tracker

## Objective
Build a simple stock tracker that calculates total investment based on manually defined stock prices.

## CodeAlpha Requirements
- User enters stock names and quantities.
- Use a hardcoded dictionary for stock prices.
- Display total investment value.
- Optionally save the result to a `.txt` or `.csv` file.
- Use dictionaries, input/output, arithmetic, and optional file handling.

## Features
- Five predefined stock symbols and prices.
- Quantity validation.
- Investment value calculation.
- Portfolio summary.
- Automatic CSV export.

## Technologies
- Python 3
- `csv` standard library

## How to Run
1. Install Python 3.
2. Open a terminal in this folder.
3. Run:
   `python stock_tracker.py`

## Sample Output
```text
=== CodeAlpha Stock Portfolio Tracker ===
Available stocks: AAPL, TSLA, MSFT, GOOGL, AMZN

Enter stock symbol (or 'done' to finish): AAPL
Enter quantity: 5
AAPL: 5 × $180.00 = $900.00

Enter stock symbol (or 'done' to finish): TSLA
Enter quantity: 2
TSLA: 2 × $250.00 = $500.00

Enter stock symbol (or 'done' to finish): done

--- Portfolio Summary ---
AAPL: 5 shares × $180.00 = $900.00
TSLA: 2 shares × $250.00 = $500.00
Total Investment Value: $1400.00
Portfolio saved to portfolio.csv
```

## CSV Output
The program creates `portfolio.csv` containing the stock, quantity, predefined price, investment value, and total.

## Project Structure
```text
CodeAlpha_StockPortfolio/
├── stock_tracker.py
├── portfolio.csv       # generated after running
├── README.md
└── screenshots/
```

## Note
The prices are intentionally hardcoded to match the internship's simplified task. They are not live market prices.
