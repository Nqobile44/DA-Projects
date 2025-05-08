import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from millify import millify

@st.cache_data
def load_data():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTBd-eYSraldHJJaVDgVeAh1U-kKN2czInpbFwSeeFV7lhsQi2DQbXwnRk3FTaEtMF7Z1niY5R6Vkpz/pub?gid=1563795435&single=true&output=csv"
    url1 = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTBd-eYSraldHJJaVDgVeAh1U-kKN2czInpbFwSeeFV7lhsQi2DQbXwnRk3FTaEtMF7Z1niY5R6Vkpz/pub?gid=1563795435&single=true&output=csv"
    return pd.read_csv(url1, low_memory=False)
st.set_page_config(layout="wide")
with st.spinner('Loading data... hang tight! ⏳'):
    df = load_data()
df['Date'] = pd.to_datetime(df['Date'])

data = df.copy()

monthly_date = df['Date'].dt.strftime('%Y-%m').copy()



st.sidebar.header('Filters')
calculation = st.sidebar.selectbox('Select Calculation', ['Mean', 'Median', 'Sum'])
order_type = st.sidebar.selectbox('Select Order Type', ['Both', 'B2B', 'None B2B'])

if order_type == 'B2B':
    total_b2b = df['B2B'].apply(lambda x: True if x else False)
    df = df[total_b2b]
elif order_type == 'None B2B':
    total_none_b2b = df['B2B'].apply(lambda x: True if not x else False)
    df = df[total_none_b2b]
else:
    pass

st.markdown("<h1 style='text-align: center;'>Amazon Sale Report</h1>", unsafe_allow_html=True)


total_amount = df.groupby('Fulfilment')['Amount'].sum()

col1, col2, col3 = st.columns(3, border=True)

with col1:
    st.metric(label='Total Amount in Amazon', value=millify(total_amount.loc['Amazon'], precision=1))

with col2:
    st.metric(label='Total Amount in Merchant', value=millify(total_amount.loc['Merchant'], precision=1))

with col3:
    st.metric(label='Total Amount', value=millify(round(df['Amount'].sum(), 1), precision=1))

# -------------------------------------------------------Insights Section ----------------------------------------------------- 

with st.expander('Key Takeaways'):
    st.subheader('Key Takeaways')
    st.markdown(
        "<ul>" \
        "<li>Amazon dominated the high-water mark with ₹704, while Merchant peaked at ₹699.</li>" \
        "<li>Shipped orders drove the bulk of both volume (77K) and revenue lift.</li>" \
        "<li>Cancelled orders were the third-highest status by count but were a major drag on total value.</li>" \
        "<li>B2B orders consistently delivered higher per-order revenue compared to non-B2B.</li>" \
        "<li>Size preferences varied sharply by category, with M, L, and XL dominating most categories.</li>" \
        "<li>The May period marked a turning point, pushing the market into a stronger, more resilient phase with higher-value orders.</li>" \
        "</ul>",
        unsafe_allow_html=True
    )
with st.expander('Summary Insights'):
    st.subheader('Summary Insights')
    st.write(
        """
The fulfillment landscape between Amazon and Merchant over Q2 2022 reveals a story of steady growth, 
punctuated by volatility—largely tied to shipment patterns and order cancellations. 
The rise in high-cost shipped and delivered orders, particularly among B2B buyers, 
pushed average order values upward. Meanwhile, 
category and size analysis highlight the importance of inventory planning, 
especially around top sizes like M, L, and XL. The May surge was pivotal, 
marking a shift to a more robust trend above ₹640, 
setting the stage for a potentially stronger Q3.
"""
    )

with st.expander('Full Insights'):
    st.subheader('Full Insights')
    st.markdown(
        """
<h4>Fulfillment: Amazon vs. Merchant Trends (March 31 - June 29, 2022)</h4>
<p>Between March 31 and June 29, 2022, Amazon and Merchant fulfillment amounts showed a dynamic tug-of-war.</p>

<p>From March 31 to April 3, both fluctuated below ₹660. But come early May, the momentum shifted:</p>

<ul>
    <li>Between May 1-6, both <strong>broke above ₹660</strong>, riding on the back of a surge in shipped and shipped-delivered orders.</li>
    <li>Amazon peaked at an all-time high of <strong>₹704 on May 5</strong>, while Merchant topped at <strong>₹679.</strong></li>
</ul>

<p>Afterward, both hovered between <strong>₹628-₹700</strong>, a pattern driven largely by daily cancelled orders, totaling a significant <strong>18.3K</strong> ranking third by status volume.</p>

<p><strong>Notably:</strong></p>
<ul>
    <li>Amazon's lowest point was <strong>₹579 on April 16.</strong></li>
    <li>Merchant's highest peak was <strong>₹699 on May 19.</strong></li>
    <li>The general amount trend showed slow growth with fluctuations—starting below ₹650 in early April, breaking the ₹650 ceiling by April 11, and reaching ₹687 on May 6. From May 4 onward, neither fell below ₹640, supported by higher-cost shipped orders.</li>

</ul>
<br>
<h4>Order Status Breakdown</h4>
<ul>
    <li><strong>Top 3 Statuses By volume:</strong>
        <ul>
            <li>Shipped → 77K orders</li>
            <li>Shipped - Delivered to Buyer → 28K orders</li>
            <li>Cancelled → 18K orders</li>
        </ul><li>
</ul>
<p>Other statuses (all under 2K) include: shipped-returned to seller, shipped-picked up, pending, shipped-out for delivery, shipped-rejected by buyer, and a handful of damaged or lost in transit cases.

</p>
<p>The <strong>boost in amount trends after May</strong> can be traced to the surge in high-value shipped orders, compared to pre-May when amounts often sat below ₹660.</p>
<br>

<h4>Order Amount Details</h4>
<ul>
    <li><strong>Cancelled Orders:</strong> Most ranged between ₹550-₹727, with only two below ₹550.</li>
    <li><strong>Pending Orders (June 17-29):</strong> Mainly under ₹800, except one outlier at ₹913.</li>
    <li><strong>Shipped - Picked Up (June 1-27):</strong> Mostly between ₹600-₹755.</li>
    <li><strong>Shipped - Out for Delivery:</strong> Also increased notably in June.</li>
    <li><strong>Shipped - Damaged:</strong> Only one recorded at a whopping ₹1136.</li>
    <li><strong>Pending - Waiting for Pick Up:</strong> Two only—₹526 (June 27) and ₹701 (June 28).</li>
</ul>
<br>

<h4>B2B vs. Non-B2B Orders</h4>
<p>B2B orders consistently outpaced non-B2B in value:</p>
<ul>
    <li>B2B Average Amount → ₹701</li>
    <li>Non-B2B Average Amount → ₹648</li>
</ul>
<p>By status, B2B leaders were:</p>
<ol>
    <li>Shipped - Picked Up → ₹898</li>
    <li>Pending → ₹821</li>
    <li>Shipped - Delivered to Buyer → ₹731</li>
    <li>Cancelled → ₹691</li>
    <li>Shipped → ₹685</li>
    <li>Shipped - Returned to Seller → ₹665</li>
</ol>
<p>For non-B2B, top order values were:</p>
<ol>
    <li>Shipped - Damaged → ₹1136 (single order)</li>
    <li>Shipped - Out for Delivery → ₹770</li>
    <li>Shipped - Returning to Seller</li>
</ol>
<br>
<h4>Size and Category Insights</h4>
<p><strong>Top 3 sizes per category:</strong></p>
<ul>
    <li><strong>Set:</strong> M (9.3K), L (8.1K), XL (7.5K)</li>
    <li><strong>Kurta:</strong> L (8.9K), XL (8.6K), M (8.5K)</li>
    <li><strong>Western Dress:</strong> L (2.8K), M (2.5K), XL (2.3K)</li>
    <li><strong>Top:</strong> XL (1.8K), M (1.8K), XXL (1.7K)</li>
    <li><strong>Ethnic Dress:</strong> XL (194), L (192), M (180)</li>
    <li><strong>Saree:</strong> Free size (164)</li>
    <li><strong>Blouse:</strong> Free size (211), M (154), S (140)</li>
    <li><strong>Dupatta:</strong> Free size (no size breakdown)</li>    
</ul>






""",
unsafe_allow_html=True
    )

graph1, graph2 = st.columns(2)

with graph1:
    choices = st.multiselect('Choose Fulfillment', ['Both', 'Merchant', 'Amazon'], default='Both')

    new_data = df[['index', 'Date', 'Amount', 'Fulfilment', 'B2B']].copy()
    new_data['Date'] = new_data['Date'].dt.strftime('%y-%m-%d')

    total_merchant = new_data['Fulfilment'].apply(lambda x: True if x == 'Merchant' else False)
    total_merchant = new_data[total_merchant]

    total_amazon = new_data['Fulfilment'].apply(lambda x: True if x == 'Amazon' else False)
    total_amazon = new_data[total_amazon]

    total_b2b = new_data['B2B'].apply(lambda x: True if x else False)
    total_b2b = new_data[total_b2b]

    total_none_b2b = new_data['B2B'].apply(lambda x: True if not x else False)
    total_none_b2b = new_data[total_none_b2b]
    
    if calculation == 'Mean':
        total_amazon = total_amazon.groupby('Date')['Amount'].mean()
        total_merchant = total_merchant.groupby('Date')['Amount'].mean()
        total_amount1 = new_data.groupby('Date')['Amount'].mean()
        total_b2b = total_b2b.groupby('Date')['Amount'].mean()
        total_none_b2b = total_none_b2b.groupby('Date')['Amount'].mean()
    elif calculation == 'Median':
        total_amazon = total_amazon.groupby('Date')['Amount'].median()
        total_merchant = total_merchant.groupby('Date')['Amount'].median()
        total_amount1 = new_data.groupby('Date')['Amount'].median()
        total_b2b = total_b2b.groupby('Date')['Amount'].median()
        total_none_b2b = total_none_b2b.groupby('Date')['Amount'].median()
    else:
        total_amazon = total_amazon.groupby('Date')['Amount'].sum()
        total_merchant = total_merchant.groupby('Date')['Amount'].sum()
        total_amount1 = new_data.groupby('Date')['Amount'].sum()
        total_b2b = total_b2b.groupby('Date')['Amount'].sum()
        total_none_b2b = total_none_b2b.groupby('Date')['Amount'].sum()

    fig = go.Figure()

    for item in choices:
        if item == 'Both':
            fig.add_trace(go.Line(x=total_amount1.index, y=total_amount1, name=item))
            # st.plotly_chart(fig)
        if item == 'Merchant':
            fig.add_trace(go.Line(x=total_merchant.index, y=total_merchant, name=item))
            # st.plotly_chart(fig)
        if item == 'Amazon':
            fig.add_trace(go.Line(x=total_amazon.index, y=total_amazon, name=item))
        if item == 'B2B':
            fig.add_trace(go.Line(x=total_b2b.index, y=total_b2b, name=item))
        if item == 'None B2B':
            fig.add_trace(go.Line(x=total_none_b2b.index, y=total_none_b2b, name=item))
        fig.update_layout(
            title='Amount Trend Over Time',
            xaxis_title='Date',
            yaxis_title='Amount',
            yaxis_tickprefix='₹'
            )
    st.plotly_chart(fig)

with graph2:
    column_selector = st.selectbox('Select A Column', [
        'Category', 
        'Size', 
        'Status', 
        'Ship Service Level', 
        'Courier Status',
        'Qty'])

    column_value = ''

    if column_selector == 'Ship Service Level':
        column_value = 'ship-service-level'
    else:
        column_value = column_selector

    order_size = pd.DataFrame(df.groupby(['Date', column_value])['Amount'].mean()).reset_index()

    fig = px.scatter(order_size, x='Date', y='Amount', color=column_value)
    fig.update_layout(yaxis_tickprefix='₹',
                      title='Orders Performance In Amount')
    st.plotly_chart(fig)

st.divider()

graph1, graph2, graph3 = st.columns(3)

with graph1:
    bins = st.slider('Select bins', 5, 60, 25)
    fig = px.histogram(df, x='Amount', nbins=bins, title='Distribution Of Order Amounts')
    fig.update_layout(xaxis_title='Amount', yaxis_title='Number of Amounts', xaxis_tickprefix='₹')
    st.plotly_chart(fig)


with graph2:
    col1, col2 = st.columns(2)
    with col1:
        yaxis_options = st.selectbox('Select Column For yaxis', ['Order ID', 'Amount'])
    with col2:
        column_options = st.selectbox('Select A Column For xaxis', 
                                      [
                                          'Status', 
                                          'Category', 
                                          'Ship Service Level', 
                                          'Size', 
                                          'Courier Status', 
                                          'Qty', 
                                          ])
    
    if column_options == 'Size' or column_options == 'Qty':
        category_list = list(df['Category'].unique())
        category_list.insert(0, 'All')
        category = st.selectbox('Select Product Category', category_list)

        if category != 'All':
            new_df = df[df['Category'].apply(lambda x: True if x == category else False)]
        else:
            new_df = df.copy()
    else:
        new_df = df.copy()


    x_column = ''
    if column_options == 'Status':
        x_column = 'Status'
    elif column_options == 'Category':
        x_column = 'Category'
    elif column_options == 'Ship Service Level':
        x_column = 'ship-service-level'
    elif column_options == 'Size':
        x_column = 'Size'
    elif column_options == 'Courier Status':
        x_column = 'Courier Status'
    else:
        x_column = 'Qty'

    if yaxis_options == 'Order ID':
        order_status = new_df.groupby(x_column)['Order ID'].size().sort_values(ascending=False)
    else:
        if calculation == 'Mean':
            order_status = new_df.groupby(x_column)['Amount'].mean().sort_values(ascending=False)
        elif calculation == 'Median':
            order_status = new_df.groupby(x_column)['Amount'].median().sort_values(ascending=False)
        else:
            order_status = new_df.groupby(x_column)['Amount'].sum().sort_values(ascending=False)


    fig = px.bar(order_status, x=order_status.index, y=yaxis_options, color=order_status.index)
    if yaxis_options == 'Order ID':
        fig.update_layout(
            showlegend=False,
            title='Distribution Of Orders By Status',
            yaxis_title='Order Count'
            )
    else:
        fig.update_layout(
            showlegend=False, 
            title='Distribution Of Amount By Status', 
            yaxis_title='Amount', 
            yaxis_tickprefix = '₹'
            )
    st.plotly_chart(fig)


with graph3:
    current_graph = st.selectbox('Select A Graph', ['Bar Graph', 'Box Graph'])
    if calculation == 'Mean':
        b2b = data.groupby('B2B')['Amount'].mean()
    elif calculation == 'Median':
        b2b = data.groupby('B2B')['Amount'].median()
    else:
        b2b = data.groupby('B2B')['Amount'].sum()


    if current_graph == 'Box Graph':
        fig = px.box(data, x='B2B', y='Amount', title='B2B vs B2C Orders', color='B2B')
    else:
        fig = px.bar(b2b, x=b2b.index, y='Amount', title='B2B vs B2C Orders', color=b2b.index)

    fig.update_layout(
        showlegend=False, 
        yaxis_tickprefix='₹', 
        title='B2B vs. B2C Orders'
        )
    st.plotly_chart(fig)
