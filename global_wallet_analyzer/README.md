Multi-Currency Asset Portfolio Valuation Tool

A Python-based financial data analytics application that aggregates multi-currency asset portfolios from a local JSON storage, 
fetches real-time mid-market exchange rates via the National Bank of Poland (NBP) REST API, and performs total portfolio valuation along with currency allocation risk analysis.

This project showcases clean Object-Oriented Programming (OOP) principles, robust external API integrations, dynamic data transformation, and essential concepts of financial programming.

Key Technical Features

- Live REST API Integration: Dynamically establishes an HTTP connection with the official NBP API (`Table A`) using the `requests` library to fetch updated daily exchange rates,
- Data Aggregation Engine: Parses and flattens nested, multi-account structures from a local JSON dataset,
  tracking and summing identical currency balances across multiple separate institutions (e.g., combining EUR from Brokerage accounts and Cash).
- Advanced Analytics (Asset Exposure): Calculates total net worth translated into Polish Złoty (PLN) and applies statistical weighting to present a percentage breakdown of the portfolio's structural currency allocation.
- Object-Oriented Architecture (OOP): Designed around single-responsibility principles, featuring modular class design, encapsulation, and class inheritance using explicit constructor propagation (`super()`).

Architecture & Class Design

The application logic is decoupled into four highly specialized classes:

1. ExchangeRateProvider: The data acquisition layer. Initiates the API request, caches the dynamic payload, and provides structured lookups for active foreign currency mid-market exchange rates,
2. DataManager: The file I/O operations controller. Safely initializes and loads the encrypted or structured data from the local repository layout (`baskets.json`),
3. ReportGenerator: The core data manipulation machine. Sweeps through mixed asset structures to construct a dynamically aggregated key-value map (`currency_dict`) of overall positions,
4. FinalReport (Inherits from `ReportGenerator`): The front-facing business analytics and reporting module:
    - final_inventory(): Outlines absolute quantities of asset distribution,
    - final_valuation(): Translates external assets into local currency equivalents using real-time market pricing,
    - impact_analysis(): Profiles total portfolio exposure by rendering structural asset weights in percentages,
    - 
Data Schema Sample (`baskets.json`)

The analytics engine parses a nested dataset representing various financial pockets (Brokerage platforms, Cash reserves, Crypto deposits) containing diversified holdings:

```json
[
  {
    "id": 1,
    "name": "XTB_Euro",
    "currency": { "eur": 1342 }
  },
  {
    "id": 3,
    "name": "Crypto",
    "currency": { "usdt": 500, "usdc": 560 }
  }
]
