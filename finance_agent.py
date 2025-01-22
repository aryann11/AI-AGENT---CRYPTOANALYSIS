from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools import Tool
from typing import Dict, Optional
from datetime import datetime
import ccxt

def get_crypto_symbol(crypto: str) -> str:
    """Get the trading symbol for a cryptocurrency."""
    symbols = {
        "Bitcoin": "BTC/USDT",
        "Ethereum": "ETH/USDT",
        "Cardano": "ADA/USDT",
        "Solana": "SOL/USDT",
        "Ripple": "XRP/USDT",
        "Polkadot": "DOT/USDT",
    }
    return symbols.get(crypto, "Unknown")

class CryptoTools:
    """Tools for cryptocurrency analysis."""
    
    def _init_(self):
        self.exchange = ccxt.binance()
    
    def get_crypto_price(self, symbol: str) -> Dict:
        """Get current price and 24h statistics for a cryptocurrency."""
        ticker = self.exchange.fetch_ticker(symbol)
        return {
            'price': ticker['last'],
            'change_24h': ticker['percentage'],
            'high_24h': ticker['high'],
            'low_24h': ticker['low'],
            'volume_24h': ticker['quoteVolume']
        }
    
    def get_market_data(self, symbol: str) -> Dict:
        """Get market data for a cryptocurrency."""
        market = self.exchange.market(symbol)
        return {
            'market_cap': market.get('info', {}).get('marketCap'),
            'total_supply': market.get('info', {}).get('totalSupply'),
            'circulating_supply': market.get('info', {}).get('circulatingSupply')
        }

# Create instances of tools
crypto_tools = CryptoTools()

# Wrap the tools properly for the Agent with function specifications
tools = [
    Tool(
        type="function",
        function={
            "name": "get_crypto_symbol",
            "description": "Get the trading symbol for a cryptocurrency",
            "parameters": {
                "type": "object",
                "properties": {
                    "crypto": {
                        "type": "string",
                        "description": "The name of the cryptocurrency"
                    }
                },
                "required": ["crypto"]
            }
        },
        fn=get_crypto_symbol
    ),
    Tool(
        type="function",
        function={
            "name": "get_crypto_price",
            "description": "Get current price and 24h statistics for a cryptocurrency",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Trading symbol (e.g., 'BTC/USDT')"
                    }
                },
                "required": ["symbol"]
            }
        },
        fn=crypto_tools.get_crypto_price
    ),
    Tool(
        type="function",
        function={
            "name": "get_market_data",
            "description": "Get market data for a cryptocurrency",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Trading symbol (e.g., 'BTC/USDT')"
                    }
                },
                "required": ["symbol"]
            }
        },
        fn=crypto_tools.get_market_data
    )
]

# Initialize the agent with properly wrapped tools
crypto_agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=tools,
    instructions=[
        "Use tables to display cryptocurrency data.",
        "If you need to find the symbol for a cryptocurrency, use the get_crypto_symbol tool.",
        "Present price changes as percentages.",
        "Show market cap in billions of USD.",
        "Format large numbers with appropriate suffixes (K, M, B, T)."
    ],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# Example usage
crypto_agent.print_response(
    "Compare Bitcoin and Ethereum's current prices, 24h changes, and market data. Show in tables.",
    stream=True
)