# 🚀 **Crypto Insights with AI-Powered Agent**  

This repository demonstrates how to leverage AI and external tools to analyze cryptocurrency data, providing real-time insights in an organized and user-friendly manner. With features like real-time pricing, 24-hour market statistics, and market capitalization, this project is ideal for traders, enthusiasts, and developers looking to integrate AI into their crypto analysis workflow.  

---

## 🔍 **Features**  

### 🌐 **Real-Time Crypto Analysis**  
- Fetch current prices, 24-hour percentage changes, highs, lows, and volume.  
- Support for popular cryptocurrencies like Bitcoin, Ethereum, Cardano, and more.

### 📊 **Market Data Insights**  
- Market capitalization, total supply, and circulating supply for cryptocurrencies.  
- Data sourced from Binance via the `ccxt` library.  

### 🛠️ **AI-Powered Interaction**  
- Uses the `phi` and `groq` frameworks for natural language understanding and tool integrations.  
- Dynamic responses presented in structured tables for clarity.  

### ⚙️ **Flexible Tooling**  
- Custom tools for symbol resolution, price retrieval, and market data.  
- Easy-to-extend architecture for adding more functionality.  

---

## 💻 **How It Works**  

1. **Crypto Symbol Resolution**  
   Converts user-friendly cryptocurrency names (e.g., Bitcoin) into tradable symbols (e.g., BTC/USDT).  

2. **Real-Time Data Fetching**  
   Accesses Binance's live data for prices and market trends using the `ccxt` library.  

3. **Interactive AI Agent**  
   An AI assistant built using `phi.Agent` and powered by `Groq` to interpret queries and deliver insightful responses in markdown tables.  

---

## 📦 **Getting Started**  

### 🔑 **Prerequisites**  
- Python 3.8+  
- Install the required libraries:  
  ```bash
  pip install -r requirements.txt
  ```  

### 🛠️ **Setup**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```  
2. Run the script:  
   ```bash
   python finance_agent.py
   ```  

---

## 🌟 **Example Usage**  
Ask the agent:  
> "Compare Bitcoin and Ethereum's current prices, 24h changes, and market data. Show in tables."

And get responses like:  
| **Crypto**  | **Price (USD)** | **24h Change (%)** | **Market Cap (B)** |  
|-------------|-----------------|--------------------|--------------------|  
| Bitcoin     | $30,500         | +3.5%              | $550B              |  
| Ethereum    | $2,200          | +2.1%              | $260B              |  

---

## 🤝 **Contributing**  

Contributions are welcome! Feel free to open issues or submit pull requests to improve functionality or add new features.  

---


