import streamlit as st
import pandas as pd
import os
from datetime import datetime
import plotly.graph_objects as go

# HELPER FUNCTIONS
def get_current_price(data, current_day):
    return data.loc[current_day, 'Close']

def get_portfolio_value(cash, position, current_price):
    return cash + position * current_price

def execute_buy(shares, current_price):
    slippage = 0.001
    execution_price = current_price * (1 + slippage)
    total_cost = shares * execution_price + 1 
    if total_cost > st.session_state.cash:
        st.error(f"❌ Not enough cash to buy {shares} shares!")
        return
    st.session_state.cash -= total_cost
    st.session_state.position += shares
    st.session_state.trades.append({
        "date": st.session_state.data.loc[st.session_state.current_day, "Date"],
        "action": "BUY",
        "shares": shares,
        "price": execution_price,
        "commission": 1,
        "total": total_cost
    })
    st.success(f"Bought {shares} shares at ${execution_price:.2f} (market: ${current_price:.2f})")

def execute_sell(shares, current_price):
    slippage = 0.001
    execution_price = current_price * (1 - slippage)
    if shares > st.session_state.position:
        st.error(f"❌ You only have {st.session_state.position} shares!")
        return
    total_revenue = shares * execution_price - 1 
    st.session_state.cash += total_revenue
    st.session_state.position -= shares
    st.session_state.trades.append({
        "date": st.session_state.data.loc[st.session_state.current_day, "Date"],
        "action": "SELL",
        "shares": shares,
        "price": execution_price,
        "commission": 1,
        "total": total_revenue
    })
    st.success(f"Sold {shares} shares at ${execution_price:.2f} (market: ${current_price:.2f})")

def plot_price_chart(data, trades):
    fig = go.Figure()

    # PRICE LINE
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], mode='lines', name='Close Price', line=dict(color='blue')))

    # TRADE MARKERS
    for trade in trades:
        if trade['date'] in data['Date'].values:
            color = "green" if trade['action']=="BUY" else "red"
            symbol = "triangle-up" if trade['action']=="BUY" else "triangle-down"
            fig.add_trace(go.Scatter(
                x=[trade['date']], y=[trade['price']],
                mode='markers+text',
                marker=dict(size=12, color=color, symbol=symbol),
                text=[trade['action']],
                textposition='top center',
                name=f"{trade['action']} ({trade['shares']})"
            ))
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price ($)",
        hovermode="x unified",
        height=600,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

def render_trade_table(trades):
    st.subheader("📝 Trade History")
    if trades:
        df = pd.DataFrame(trades)
        df['date'] = df['date'].dt.strftime("%m-%d-%Y")
        st.dataframe(df[['date','action','shares','price','commission','total']], use_container_width=True)
    else:
        st.info("No trades yet.")

# TRADING SIMULATOR
def run():
    st.title("📈 Trading Simulator")
    st.markdown("Use this tool to practice trading with historical stock data in a risk-free environment.")

    # GUIDE
    with st.expander("Guide", expanded=True):
        st.markdown("""
        ### 👉 How To Use
        1. Select a stock from the sidebar and load its historical data.
        2. Use the day slider to navigate through historical market days.
        3. Place buy/sell orders using market or limit orders.
        4. Track your cash, position, portfolio value, and profit/loss in real-time.
        5. Review your trade history and analyze your performance.
        """)
        
        st.markdown("----")
        
        st.markdown("""
        ### 🌱 Have Fun
        Money don't grow on trees, but your portfolio can branch out!
        """)
    
    st.markdown("----")

    # INITIALIZE SESSION STATE
    if 'trades' not in st.session_state:
        st.session_state.trades = []
        st.session_state.current_day = 50
        st.session_state.cash = 100_000
        st.session_state.position = 0
        st.session_state.data = None
        st.session_state.stock_name = None

    # LOAD DATA
    data_folder = "data" 
    csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]
    
    st.sidebar.subheader("📂 Stock Dataset")
    selected_file = st.sidebar.selectbox("Select Default Stock", csv_files)
    
    if st.sidebar.button("Load Stock", use_container_width=True, key="load_default_btn"):
        new_stock_name = selected_file.replace(".csv","").upper()
        default_path = os.path.join(data_folder, selected_file)
        try:
            df = pd.read_csv(default_path)
            df['Date'] = pd.to_datetime(df['Date'])
            df = df.sort_values("Date").reset_index(drop=True)
            
            # RESET PORTFOLIO FOR NEW STOCK
            st.session_state.data = df
            st.session_state.stock_name = new_stock_name
            st.session_state.trades = []
            st.session_state.cash = 100_000
            st.session_state.position = 0
            st.session_state.current_day = min(50, len(df)-1)
            st.success(f"Loaded {new_stock_name}")
            st.rerun()
        except Exception as e:
            st.error(f"Failed to load: {e}")
        
    uploaded_file = st.sidebar.file_uploader("Upload Your Own CSV", type=["csv"])
    
    if uploaded_file is not None:
        if st.sidebar.button("Load Stock", use_container_width=True, key="load_uploaded_btn"):
            new_stock_name = uploaded_file.name.replace(".csv","").upper()
            try:
                df = pd.read_csv(uploaded_file)
                df['Date'] = pd.to_datetime(df['Date'])
                df = df.sort_values("Date").reset_index(drop=True)
                
                # RESET PORTFOLIO FOR NEW UPLOADED STOCK
                st.session_state.data = df
                st.session_state.stock_name = new_stock_name
                st.session_state.trades = []
                st.session_state.cash = 100_000
                st.session_state.position = 0
                st.session_state.current_day = min(50, len(df)-1)
                st.success(f"Loaded {new_stock_name}")
                st.rerun()
            except Exception as e:
                st.error(f"Failed to load: {e}")
    
    # LOAD DEFAULT STOCK ON FIRST RUN
    if st.session_state.data is None:
        default_path = os.path.join(data_folder, csv_files[0])
        df = pd.read_csv(default_path)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values("Date").reset_index(drop=True)
        st.session_state.data = df
        st.session_state.stock_name = csv_files[0].replace(".csv","").upper()
        st.session_state.current_day = min(50, len(df)-1)

    # METRICS
    data = st.session_state.data
    min_day = 0
    max_day = len(data) - 1
    if st.session_state.current_day > max_day:
        st.session_state.current_day = max_day
    if st.session_state.current_day < min_day:
        st.session_state.current_day = min_day
    current_price = get_current_price(data, st.session_state.current_day)
    portfolio_value = get_portfolio_value(st.session_state.cash, st.session_state.position, current_price)
    total_pnl = portfolio_value - 100_000
    total_pnl_pct = total_pnl / 100_000 * 100

    # DAY NAVIGATION
    st.subheader("📅 Navigate Trading Days")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("⏮️ 10 Days", use_container_width=True):
            st.session_state.current_day = max(min_day, st.session_state.current_day - 10)
            st.rerun()
    with col2:
        if st.button("◀️ Previous", use_container_width=True):
            st.session_state.current_day = max(min_day, st.session_state.current_day - 1)
            st.rerun()
    with col3:
        if st.button("🔄 RESET", use_container_width=True):
            st.session_state.confirm_reset = True
            st.rerun()
    with col4:
        if st.button("Next ▶️", use_container_width=True):
            st.session_state.current_day = min(max_day, st.session_state.current_day + 1)
            st.rerun()
    with col5:
        if st.button("10 Days ⏭️", use_container_width=True):
            st.session_state.current_day = min(max_day, st.session_state.current_day + 10)
            st.rerun()

    # CONFIRMATION DIALOG FOR RESET
    if st.session_state.get('confirm_reset', False):
        st.warning("⚠️ Are you sure you want to reset? This will clear all trades and reset your portfolio.")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🙂‍↕️ YES", use_container_width=True):
                st.session_state.trades = []
                st.session_state.cash = 100_000
                st.session_state.position = 0
                st.session_state.current_day = 50
                st.session_state.confirm_reset = False
                st.rerun()
        with col2:
            if st.button("🙂‍↔️ NO", use_container_width=True):
                st.session_state.confirm_reset = False
                st.rerun()
    
    # TRADING PANEL
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("**Day:**")
        st.write(f"{st.session_state.current_day} / {len(data)-1}")
    with col2:
        st.write("**Date:**")
        st.write(f"{data.loc[st.session_state.current_day,'Date'].strftime('%m-%d-%Y')}")
    with col3:
        st.write("**Price:**")
        st.write(f"${current_price:.2f}")
    with col4:
        order_type = st.radio(
            "**Order Type**", 
            ["Market", "Limit"], 
            horizontal=True, 
            key="order_type_radio"
        )
    
    st.markdown("----")

    # PLACE ORDER
    st.subheader("🛒 Place Order")
    col1, col2 = st.columns(2)
    with col1:
        if order_type == "Market":
            st.text_input(
                "Limit Price", 
                value="--", 
                disabled=True, 
                key="limit_price_disabled"
            )
            limit_price = None
        else:
            limit_price = st.number_input(
                "Limit Price", 
                min_value=0.01, 
                value=float(current_price),
                step=0.01, 
                key="limit_price"
            )
    with col2: 
        shares = st.number_input("Shares", min_value=1, value=10, step=1)

    # BUY/SELL
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🟢 BUY", use_container_width=True):
            if order_type == "Market" or (limit_price and current_price <= limit_price):
                execute_buy(shares, current_price)
                st.rerun()
            else:
                st.error(f"Price ${current_price:.2f} above limit ${limit_price:.2f}")
    with col2:
        if st.button("🔴 SELL", use_container_width=True):
            if order_type == "Market" or (limit_price and current_price >= limit_price):
                execute_sell(shares, current_price)
                st.rerun()
            else:
                st.error(f"Price ${current_price:.2f} below limit ${limit_price:.2f}")
    
    st.markdown("----")

    # PRICE CHART
    st.subheader("🪙 Price Chart")
    max_days = st.session_state.get("chart_days", min(50, len(data)))
    st.write("ℹ️ There is a $1 commission per trade and a slippage of 0.1%.")
    col1, col2 = st.columns([4, 1])
    with col1:
        start_idx = max(0, st.session_state.current_day - max_days)
        visible_data = data.iloc[start_idx : st.session_state.current_day + 1]
        plot_price_chart(visible_data, st.session_state.trades)
    with col2:
        st.write("\n")
        st.write("\n")
        max_days = st.number_input(
            "Days to Display", 
            min_value=10, 
            max_value=len(data), 
            value=max_days,
            step=10,
            key="chart_days"
        )
        st.metric("Current Price", f"${current_price:,.2f}")
        st.metric("Position (Shares)", f"{st.session_state.position}")
        st.metric("Total Profit/Loss", f"${total_pnl:,.2f}", f"{total_pnl_pct:+.2f}%")
        st.metric("Cash", f"${st.session_state.cash:,.2f}")
        st.metric("Portfolio Value", f"${portfolio_value:,.2f}")

    st.markdown("----")

    # TRADE HISTORY
    render_trade_table(st.session_state.trades)
