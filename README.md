## Interactive Trading Simulator  

A multi-page Streamlit app designed to help beginners learn trading in a safe, risk-free environment using historical stock data. 

### 🎯 Project Purpose

The Interactive Trading Simulator is built to help beginners learn stock trading safely using historical data. It provides practice trading, portfolio tracking, and educational resources — all in a risk-free environment.

### 🔎 Quick Start

Follow these steps to get started:
1. Clone the repository.
```
git clone https://github.com/ejiang444/interactive-trading-simulator.git
cd interactive-trading-simulator
```
2. Install dependencies.
```
pip install -r requirements.txt
```
3. Run the application.
```
streamlit run dashboard.py
```
4. Explore the dashboard pages:
    - Start Here
    - Beginner's Guide
    - Trading Simulator
    - Support Center

### ⭐ Features
- Beginner-friendly onboarding and guidance
- Trading simulator with market & limit orders, portfolio tracking, and charts
- Support Center to contact the developer directly
- Educational resources on stocks, charts, and trading strategies

### 🗃️ Multi-Page Application
The app is organized into four main pages:
1. Start Here
    - Onboarding and navigation tips
    - Guides users through the app structure and basic usage
2. Beginner’s Guide 
    - Introduces trading basics, strategies, and risk management
    - Provides step-by-step guidance for creating a trading plan
3. Trading Simulator 
    - Practice trading using historical stock data
    - Explore market trends, place buy/sell orders, and track portfolio performance
4. Support Center 
    - Contact form to send messages directly to the developer
    - Provides help and support for any questions or issues

### 👨‍💻 Trading Simulator Highlights
- Load default or custom CSV stock datasets
- Navigate day-by-day through historical trading data
- Execute market and limit orders
- Real-time portfolio tracking: cash, positions, P/L, and total portfolio value
- Interactive price chart with buy/sell markers using Plotly
- Full trade history table with detailed transaction logs 

### 📖 Educational Features
- Understand stock basics, candlestick charts, and order types
- Learn about risk, fees, and slippage in trading
- Identify common mistakes and tips to avoid them
- Access helpful external resources, including YouTube tutorials and articles

### 💬 Support Center
- Send messages directly to the developer’s email
- Simple and intuitive form with fields for name, email, and message
- Friendly success and error notifications to confirm message delivery

### 🔐 Secrets Setup
The Support Center uses email for message sending. Do not commit this file to GitHub. Add it to `.gitignore`.

Create a `.streamlit/secrets.toml` file in the root directory with:
```
[email]
address = "your_email@gmail.com"
password = "your_app_password"
```

### 📂 File Structure
```
project/
│
├── dashboard.py                 # Main multi-page router
├── start_here.py                # Start Here page
├── beginners_guide.py           # Beginner’s Guide page
├── trading_simulator.py         # Trading Simulator page
├── support_center.py            # Support Center page
├── report.pdf                   # Detailed project report
├── requirement.txt              # Dependencies
├── README.md                    # This README
└── data/                        # Default stock CSV files
    ├── AAPL.csv
    ├── MSFT.csv
    └── ...
```

### 📊 Data Requirements
Dates are automatically parsed and sorted by the application.
- Default stock datasets are stored in the data folder
- Users can upload their own CSV stock data
- CSV files should include at minimum: 
    - Date
    - Open
    - High
    - Low
    - Close

### ⬇️ Dependencies
Install all required packages:
```
pip install -r requirements.txt
```

### ⚙️ System Requirements
- Python 3.10+ recommended
- Compatible with Windows, macOS, and Linux

### 📄 Project Report
A detailed project report for the Interactive Trading Simulator is included as `report.pdf`. The report (~1,200 words) provides an in-depth overview of the project and includes the following sections:

- Project Description and Methodology:
    - Explains the purpose of the simulator, its target audience, and the design approach used
- Steps Taken and Challenges Encountered:
    - Details the development process, tools and libraries used, and any obstacles faced along the way
- Results and Analysis:
    - Highlights the outcomes of the project, including simulator functionality, user experience, and educational value
- Effort Justification:
    - Explains how the project meets a 1.5× effort level per contributor, including:
        - What makes this project more substantial than a typical assignment
        - New skills or techniques learned during development
- Rubric Checklist:
    - Demonstrates how the project fulfills proposed rubric criteria, ensuring all requirements are met

### 📎 Acknowledgement
- Special thanks to Dr. Ingrid Eva Maria Hybinette for providing the data, and to CSCI 4170/6170 Introduction to Computational Investing for the course guidance and inspiration.

### 👥 Contributor(s)
Emily Jiang
