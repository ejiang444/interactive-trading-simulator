import streamlit as st

def run():

    # START HERE
    st.title("👋 Start Here")
    st.markdown(""" 
    Welcome! 
    This is your starting point for learning the platform and getting comfortable with trading in a safe environment.
    """)

    st.markdown("----")

    # NAVIGATION
    st.markdown("""
    ### **📍 How To Navigate**
    Located in the sidebar, you’ll find several key pages to explore:
    
    **Start Here**
    > This introduction and guide to get you started.

    **Beginner’s Guide**
    > Learn trading basics, simple strategies, and key concepts.
    
    **Trading Simulator**
    > Practice buying and selling using real historical data.
    > Track your portfolio, P&L, performance metrics, and trade history.
    
    **Support Center**
    > Get answers and help whenever you need it.
    """)

    st.markdown("----")

    # GETTING STARTED CHECKLIST
    st.markdown("""
    ### **✅ Getting Started Checklist**
    1. **Navigate to the Trading Simulator**
        - This is where you'll view charts, load stock data, and make trades.
        - Familiarize yourself with the layout and tools available.
    2. **Load Stock**
        - Use the dropdown bar to select a CSV file from the given databases.
        - Feel free to upload your own CSV files with historical stock data.
    3. **Explore Market History**
        - Use the day navigation tool to move through past market days and watch price changes.
        - Analyze charts and indicators to inform your trading decisions.
    4. **Place Your First Trades**
        - Buy or sell shares and see how it affects your cash, position, and profit/loss.
        - Try different order types and see how they behave.
    5. **Track Your Portfolio**
        - The simulator displays your cash, positions, portfolio value, and profit/loss in real time.
        - Review your trade history to learn from your actions.
    """)

    st.markdown("----")

    # REMINDER
    st.markdown("""
    ### 🔔 **Reminder** 
    There’s no risk because it’s all virtual. Have fun and go crazy!
    """)
