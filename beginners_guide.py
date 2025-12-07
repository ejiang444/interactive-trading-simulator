import streamlit as st

def run():

# BEGINNER'S GUIDE
    st.title("📚 Beginner's Guide")
    st.markdown("""
    Everyone starts somewhere, and you’re in the right place. Here are some tips and resources to get you started with trading.
    """)

    st.markdown("----")

    # BASIC CONCEPTS
    st.markdown("""
    ### **💭 Basic Concepts**
    """)

    with st.expander("Stock Definition"):
        st.markdown("""
            A stock represents ownership in a company. When you buy a stock, you become a partial owner of that company.

            Key Points:
            - Each share equals a small piece of the company.
            - Stock prices change based on supply, demand, and company performance.
            - You can profit through price appreciation or dividends.
            - Prices can go up or down – you can lose money.
            """)
        st.text("Example: If Apple stock rises from $150 to $160, and you own 100 shares, you gain $1,000.")

    
    with st.expander("Candlestick Charts"):
        st.markdown("""
        Candlestick charts show price movements over time. Each candle represents trading activity during a specific period.
        """)
        with st.expander("How to Read Candles"):
            st.markdown("""
            - Green/White Candle: 
                - Price went UP (close > open)
            - Red/Black Candle: 
                - Price went DOWN (close < open)
            - Body: 
                - Range between open and close prices
            - Wicks: 
                - Highest and lowest prices reached
            """)
        with st.expander("What to Look For"):
            st.markdown("""
            - Trends: 
                - Series of higher highs means uptrend, series of lower lows means downtrend
            - Support: 
                - Price level where stock tends to stop falling
            - Resistance: 
                - Price level where stock tends to stop rising
            - Volume: 
                - More trading activity means more reliable movements
            """)

    with st.expander("Order Types"):
        st.markdown("""
        Market Order:
        - Executes immediately at current market price
        - Guaranteed execution, but price not guaranteed
        - Best for quick trades, liquid stocks, small orders
        
        Limit Order:
        - Only executes at your specified price or better
        - Price control, but may not execute
        - Best for volatile stocks, large orders, when you can wait
        """)
        st.text("Example: Stock at $50. Market order might fill at $50.05. Limit order at $49.50 only fills if price drops to $49.50 or lower.")

    with st.expander("Risk, Fees, and Slippage"):
        st.markdown("""
        Types of Risk:
        - Market risk, company risk, liquidity risk, volatility risk
        - Never invest money you can't afford to lose
        - Diversify and use stop-loss orders
        
        Trading Fees:
        - Commission: 
            - Fee per trade (many brokers now free)
        - Other fees: 
            - SEC fees, exchange fees, account fees
        
        Slippage:
        - Difference between expected price and actual execution price
        - Occurs due to market movement, low liquidity, large orders, volatility
        - Minimize with:
            - Limit orders, liquid stocks, smaller order sizes
        """)
    
    st.markdown("----")

    # AVOID COMMON MISTAKES
    st.markdown("""
    ### **‼️ Avoid Common Mistakes**
    - Emotional trading can lead to fear of missing out, panic selling, or revenge trading. 
    - Poor risk management, such as not using stop-loss orders or risking too much, can result in significant losses.
    - Lack of planning, including trading without a strategy or making random entries and exits, often causes unnecessary mistakes.
    - Overtrading by making too many trades too frequently can also harm your results.
    """)

    st.markdown("----")

    # CREATE TRADING PLAN
    st.markdown("""
    ### **✍️ Create Trading Plan**
    1. Goals: 
        - What do you want to achieve?
    2. Strategy: 
        - What signals will you trade?
    3. Risk Rules: 
        - How much per trade?
    4. Entry/Exit Rules: 
        - When do you buy/sell?
    5. Review: 
        - How will you learn from trades?
    """)

    st.markdown("----")
    
    # HELPFUL RESOURCES
    st.markdown("""
    ### **🔗 Helpful Resources**

    YouTube Channels
    - [How Does The Stock Market Work](https://www.youtube.com/watch?v=p7HKvqRI_Bo)
    - [Trading 212](https://www.youtube.com/c/Trading212)
    - [The Plain Bagel](https://www.youtube.com/c/ThePlainBagel)
    - [Rayner Teo](https://www.youtube.com/channel/UCFSn-h8wTnhpKJMteN76Abg)

    Websites
    - [Introduction to Stock Trading](https://www.investopedia.com/stock-trading-4689660)
    - [Investing: An Introduction](https://www.investopedia.com/articles/basics/11/3-s-simple-investing.asp)
    - [Stock Market Basics: A Beginner's Guide](https://www.fool.com/investing/stock-market/basics/)
    - [Robinhood Learn](https://robinhood.com/us/en/learn/)
    - [Trading Strategies](https://www.investopedia.com/trading-strategies-4689646)
    """)

    st.markdown("----")

    # TIP
    st.markdown("""
    ### 💡 **Tip** 
    Start small, focus on learning strategies, and use the Trading Simulator to practice without risk.
    """)
