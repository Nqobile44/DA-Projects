import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from PIL import Image

# @st.cache_data
# def load_data():
#     return pd.read_csv('data/stock_market_data/clean_data/stock_market.csv')
df = pd.read_csv('stock_market.csv')

st.set_page_config(layout="wide")
# with st.spinner('Loading data... hang tight! ⏳'):
#     df = load_data()

data = df.copy()

stocks_list = list(df['Symbol'].unique())
stocks_list.insert(0, "None")

st.sidebar.header("Stock Selection")
stock = st.sidebar.selectbox(label="Select A Stock", options=stocks_list, key='overall', placeholder="Choose A Stock")

if stock != 'None':
    data = data[data['Symbol'].apply(lambda x: True if x == stock else False)]

st.markdown("<h2 style='text-align: center;'>Market Overview</h2>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Price Trends & Behavior", 'Distribution, Pattern & Correlation', 'Insights'])

with tab1: # Price Trends & Behavior
# ---------------------------------- Price Trend Over Time ------------------------------
    graph1, graph2 = st.columns(2)

    with graph2:
        columns_selected = st.multiselect(
            label="Select A Column", 
            options=[
                "Close", 
                "High",
                "Low", 
                "Open", 
                "Volume", 
                "Turnover", 
                "VWAP"], default="Close")

        fig = go.Figure()

        for column in columns_selected:
            close_trend = data.groupby('Date')[column].median()
            fig.add_trace(go.Line
                        (x=close_trend.index, 
                        y=close_trend, 
                        name=column))

        fig.update_layout(
            title='Price Trend Over Time',
            xaxis_title='Date',
            yaxis_title='Price',
            # line=dict(color='crimson')
        )
        st.plotly_chart(fig)


# ------------------------------ Stock Behavior -----------------------------------------

    with graph1:
        if stock == 'None':
            st.write("Select A Stock")

        stock_df = df[df['Symbol'].apply(lambda x: True if x == stock else False)]

        fig = go.Figure(data=[go.Candlestick(
            x=stock_df['Date'],
            open=stock_df['Open'],
            high=stock_df['High'],
            low=stock_df['Low'],
            close=stock_df['Close']
        )])
        fig.update_layout(
            title='Stock Behavior',
            xaxis_title='Date',
            yaxis_title='Price',
            xaxis_rangeslider_visible=False
        )

        st.plotly_chart(fig)


# --------------------------- Unusual High Price Spike -----------------------------------

    spike_high = data.groupby('Date')['High'].median().reset_index()

    fig = px.scatter(spike_high, x='Date', y='High', color='High')
    fig.update_layout(
        title="Unusual High Price Spike",
    )
    st.plotly_chart(fig)


with tab2: # Distribution, Pattern & Correlation
    graph1, graph2 = st.columns(2)
    with graph1:
# -------------------------- Price Value (Open, High, Low, Close)------------------------

        df_melted = data.melt(id_vars=['Date', 'Symbol'], 
                        value_vars=['Open', 'High', 'Low', 'Close'],
                        var_name='Price Type',
                        value_name='Price')
        fig = px.box(df_melted, x='Price Type', y='Price', color='Price Type')
        fig.update_layout(
            title="Price Value (Open, High, Low, close)"
        )
        st.plotly_chart(fig)


# ------------------------- distribution of % Deliverable ---------------------------------


    fig = go.Figure(data=[go.Histogram(
        x=data["%Deliverble"], 
        nbinsx=20,
        marker=dict(
            color='green',
            line=dict(
                color='black',
                width=2
            )
        ))])
    fig.update_layout(
        title='Distribution Of % Deliverable',
        xaxis_title='%Deliverable',
        yaxis_title='Count'
    )
    st.plotly_chart(fig)

# ----------------------- pattern between volume and turnover -----------------------------


    with graph2:
        img = Image.open('pattern_between_vol_turn.png')
        st.image(img, use_container_width=True)


# --------------------------------------- Insights -----------------------------------------
with tab3: # Insights
    st.markdown("<h3 style='text-align: center;'>Market Pulse: Visualizing Stock Trends (2000-2021)</h3>", unsafe_allow_html=True)
    with st.expander(label="Summary Insights"):
        st.markdown(
            "<p>Between 2000 and 2021, the stock's closing price exhibited significant fluctuations influenced by both volume and turnover. " \
            "A major rally began in 2004 and peaked in early 2021, with notable declines during 2008 and early 2020. " \
            "Volume trends followed a similar volatile pattern, with major spikes starting in 2003 and reaching up to 120 million in 2020. " \
            "Turnover exploded in the final years, especially from 2019 to 2021, indicating high trading activity. " \
            "Most orders occurred when the deliverable percentage ranged between 0.4 and 0.6.</p>",
            unsafe_allow_html=True
        )

    with st.expander(label="Full Insights"):
        st.markdown(
            "<h3>Price Trend (2000-2021)</h3>" \
            "<ul>" \
            "<li>From 2000 to early 2004, the closing price remained below 400. " \
            "A breakout occurred at the start of 2004, with the price pushing above 800 by the end of 2007.</li>" \
            "<li>In 2008, the market experienced a sharp decline, dropping to 350 by year-end.</li>" \
            "<li>A recovery took place in 2009, bringing the price back up to 800.</li>" \
            "<li>In 2020, there was a significant dip to 500 the lowest since 2012 followed " \
            "by a strong rebound later in the same year, pushing the price above 800.</li>" \
            "<li>Early 2021 marked the highest price peak, surpassing 900.</li>" \
            "</ul>" \
            "<h3>Volume Trend</h3>" \
            "<ul>" \
            "<li>From 2000 to 2003, trading volume was relatively low, below 8 million.</li>" \
            "<li>In 2003, volume spiked to 10 million, " \
            "initiating more aggressive price movements and pushing the price above 400 in the 2003-2004 period.</li>" \
            "<li>From 2008 onward, volume became increasingly volatile, " \
            "peaking at 37 million and fluctuating heavily between 2009 and 2020.</li>" \
            "<li>In 2020, volume surged dramatically to 120 million but then dropped below 20 million before year-end.</li>" \
            "<li>In 2021, volume returned to a range of 40 to 120 million. " \
            "Interestingly, while a volume increase did not always lead to a price rise, " \
            "a drop in volume often preceded a price decline.</li>" \
            "</ul>" \
            "<h3>Turnover Insights</h3>" \
            "<ul>" \
            "<li>" \
            "Major turnover years include:" \
            "<ul>" \
            "<li><strong>2019:</strong> Over 20 trillion</li>" \
            "<li><strong>2020:</strong> Over 35 trillion</li>" \
            "<li><strong>2021:</strong> Over 45 trillion (highest)</li>" \
            "</ul>" \
            "</li>" \
            "<li>This indicates a strong increase in trading value and activity during these years.</li>" \
            "</ul>" \
            "<h3>Unusual Price Activity</h3>" \
            "<ul>" \
            "<li>A pattern of unusually high price movement began around 2016 and lasted through 2021. " \
            "This period marks a clear transition to higher volatility and larger gains/losses.</li>" \
            "</ul>" \
            "<h3>Volume vs Turnover</h3>" \
            "<ul>" \
            "<li>Although volume (in millions) and turnover (in trillions) are on vastly different scales, " \
            "both metrics show a synchronized trend of increased activity from 2016 onward. " \
            "However, high volume doesn't always equate to high turnover, " \
            "suggesting that fewer trades at higher values were also contributing factors.</li>" \
            "</ul>" \
            "<h3>Deliverable & Orders</h3>" \
            "<ul>" \
            "<li>The majority of orders were placed when the deliverable percentage ranged between 0.4 and 0.6, " \
            "with those intervals having more than 20,000 orders, " \
            "indicating significant market confidence during that range.</li>" \
            "</ul>", 
            unsafe_allow_html=True
        )

    with st.expander(label="Key Takeaways"):
        st.markdown(
            "<ul>" \
            "<li><strong>Price Milesstones: </strong>Breakout in 2004, peak above 900 in 2021, major dips in 2008 and 2020.</li>" \
            "<li><strong>Volume Trends: </strong>Low until 2003, volatile after 2008, with a record high of 120M in 2020.</li>" \
            "<li><strong>Massive Turnover Growth: </strong>Peaked in 2021 with 45 trillion—indicating intense trading activity.</li>" \
            "<li><strong>Volatility Surge: </strong>Unusual highs and stronger price swings emerged from 2016 to 2021.</li>" \
            "<li><strong>Volume Price: </strong>High volume didn’t always cause price rises; however, volume drops often led to price dips.</li>" \
            "<li><strong>Deliverable Range (0.4-0.6): </strong>Attracted the highest number of orders, exceeding 20k.</li>" \
            "</ul>", unsafe_allow_html=True
        )

    