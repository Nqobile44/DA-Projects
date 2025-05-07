import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
from millify import millify
import pdfkit

insights_text = """
Key Takeaways:
- China leads global vaccination efforts by a massive margin, driving the global totals far higher than any other country.
- While partial vaccination rates are rising worldwide, full vaccination rates consistently lag behind especially in most countries.
- A small group of countries (like the Philippines and Ethiopia) stand out for having more fully vaccinated people than partially vaccinated, bucking the global trend.
- The top vaccines (Oxford/AstraZeneca, Moderna, Pfizer/BioNTech, Johnson & Johnson) dominate worldwide because of wide international distribution, particularly in high-volume countries like France, Spain, and Canada.
- Global vaccination campaigns heavily rely on a few major sources, with the World Health Organization playing the largest role across 74 countries.


Detailed Insights:
1. Total Vaccinations Growth
    - From February 2, 2021, to March 29, 2022, total global vaccinations rose sharply, reaching 150 million doses. China leads this surge with 1.8 billion doses administered, followed by India (755 million) and the United States (329 million). The large gap between China and India highlights China’s significant contribution. The median peak for total vaccinations over time was 17 million, recorded on March 19, 2022. Daily vaccinations fluctuated considerably: from December 14, 2020, to June 27, 2020, daily doses peaked at 201,000, then dropped to 79,000 by March 13, 2022, before surging again to 281,000 over a nine-day period.

2. Fully vs. Partially Vaccinated Populations
    - While both fully and partially vaccinated numbers have increased, partially vaccinated individuals consistently outnumber fully vaccinated ones. Even when measured per hundred people, partially vaccinated rates surpass fully vaccinated rates.

3. Lowest and Highest Vaccination Rates
    - Countries with the lowest total vaccinations (below 5,000 doses) include Burundi, Falkland Islands, Saint Helena, Montserrat, Niue, Tokelau, and Pitcairn, with Pitcairn recording the lowest at just 69.6 doses. However, the highest daily vaccinations per million are seen in Falkland Islands, Saint Helena, Tokelau, Pitcairn, and Cuba.

4. Correlation Patterns
    - There is generally a strong correlation between partially and fully vaccinated rates across countries, with few exceptions. Luxembourg notably stands out, showing no clear correlation, with 49.4 partially vaccinated per hundred but only 2.9 fully vaccinated per hundred.

5. Daily Vaccination Surges
    - March 2021 marked a significant surge, with daily vaccinations per million surpassing 100,000. Four days that month saw over 100 million doses administered in a single day, peaking at 117 million. A similar surge occurred in April, reaching up to 92 million.

6. Most Widely Used Vaccines
    - The top vaccines globally are Johnson & Johnson, Moderna, Oxford/AstraZeneca, and Pfizer/BioNTech. Johnson & Johnson leads, being distributed across 17 countries; Moderna, AstraZeneca, and Pfizer/BioNTech follow with 15 countries; AstraZeneca alone reaches 20 countries, making it the most widely distributed. These vaccines dominate due to broad international distribution, particularly to Canada, France, and Spain — with France exceeding 70 million total vaccinations.

7. Countries with More Fully Vaccinated Than Partially Vaccinated
    - In most countries, partially vaccinated numbers are higher. However, exceptions include the Philippines (21 million fully vaccinated vs. 8.1 million partially vaccinated) and Ethiopia (19 million fully vaccinated vs. 5.3 million partially vaccinated). Altogether, 12 countries show a higher number of fully vaccinated individuals compared to those partially vaccinated.

8. Leading Vaccine Sources
    - The World Health Organization (WHO) leads vaccine distribution, supporting 74 countries. The Ministry of Health follows with 37 countries, and the SPC Public Health Division comes third with 14 countries. In terms of vaccine variety, WHO distributes 44 types, followed by the Ministry of Health with 26, while SPC ranks fifth with five types.
"""
st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Country Vaccinations</h1>", unsafe_allow_html=True)
url_data = "https://raw.githubusercontent.com/Nqobile44/DA-Projects/refs/heads/main/country_vaccinations/country_vaccinations_dashboard/data/country_vaccination/country_vaccinations.csv"
df = pd.read_csv(url_data)
df['date'] = pd.to_datetime(df['date'])
month_to_month = df['date'].dt.strftime('%Y-%m').copy()
total_vaccin = df['total_vaccinations'].sum()
total_peo_vaccin = df['people_fully_vaccinated'].sum()
total_peo_fully_vaccin = df['people_fully_vaccinated'].sum()

st.sidebar.header('Filters')
calculations = st.sidebar.selectbox('Select A Calculation', ['Mean', 'Median', "Sum"])
legend_value = st.sidebar.toggle('Show Legend', value=True)

full_names = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion']
col1, col2, col3 = st.columns(3)
with col1:
    st.metric('Total Vaccinations', millify(total_vaccin))
with col2:
    st.metric('Total People Vaccinated', millify(total_peo_vaccin))
with col3:
    st.metric('Total People Fully Vaccinated', millify(total_peo_fully_vaccin))

st.divider()

with st.expander("Key Takeaways"):
    st.subheader('Key Takeaways')
    st.markdown("<ul><li>China leads global vaccination efforts by a massive margin, " \
    "driving the global totals far higher than any other country.</li></ul>", unsafe_allow_html=True)
    st.markdown("<ul><li>While partial vaccination rates are rising worldwide, " \
    "full vaccination rates consistently lag behind, especially in most countries.</li></ul>", unsafe_allow_html=True)
    st.markdown("<ul><li>A small group of countries (like the Philippines and Ethiopia) " \
    "stand out for having more fully vaccinated people than partially vaccinated, bucking the global trend.</li></ul>", unsafe_allow_html=True)
    st.markdown("<ul><li>The top vaccines (Oxford/AstraZeneca, Moderna, Pfizer/BioNTech, Johnson & Johnson) " \
    "dominate worldwide because of wide international distribution, particularly in high-volume countries like France, Spain, and Canada.</li></ul>", unsafe_allow_html=True)
    st.markdown("<ul><li>Global vaccination campaigns heavily rely on a few major sources, with the World Health Organization playing the largest role across 74 countries.</li></ul>", unsafe_allow_html=True)

with st.expander("Master Dataset Summary (Big Picture)"):
    st.subheader("Summary of Global COVID-19 Vaccination Insights")
    st.markdown('<br><h4>Total Vaccinations Growth</h4>', unsafe_allow_html=True)
    st.markdown("<ul><li>From February 2, 2021, to March 29, 2022, total global vaccinations rose sharply, " \
    "reaching 150 million doses. China leads this surge with 1.8 billion doses administered, " \
    "followed by India (755 million) and the United States (329 million). " \
    "The large gap between China and India highlights China's significant contribution. " \
    "The median peak for total vaccinations over time was 17 million, recorded on March 19, 2022. " \
    "Daily vaccinations fluctuated considerably: from December 14, 2020, to June 27, 2020, daily doses peaked at 201,000, " \
    "then dropped to 79,000 by March 13, 2022, before surging again to 281,000 over a nine-day period.</li></ul>", unsafe_allow_html=True)
    st.markdown('<br><h4>Fully vs. Partially Vaccinated Populations</h4>', unsafe_allow_html=True)
    st.markdown('<ul><li>While both fully and partially vaccinated numbers have increased, ' \
    'partially vaccinated individuals consistently outnumber fully vaccinated ones. ' \
    'Even when measured per hundred people, partially vaccinated rates surpass fully vaccinated rates.</li></ul>', unsafe_allow_html=True)
    st.markdown('<br><h4>Lowest and Highest Vaccination Rates</h4>', unsafe_allow_html=True)
    st.markdown('<ul><li>Countries with the lowest total vaccinations (below 5,000 doses) include Burundi, ' \
    'Falkland Islands, Saint Helena, Montserrat, Niue, Tokelau, and Pitcairn, with Pitcairn recording the lowest at just 69.6 doses. ' \
    'However, the highest daily vaccinations per million are seen in Falkland Islands, Saint Helena, Tokelau, Pitcairn, and Cuba.</li></ul>', unsafe_allow_html=True)
    st.markdown('<br><h4>Correlation Patterns</h4>', unsafe_allow_html=True)
    st.markdown('<ul><li>There is generally a strong correlation between partially and fully vaccinated rates across countries, ' \
    'with few exceptions. Luxembourg notably stands out, showing no clear correlation, ' \
    'with 49.4 partially vaccinated per hundred but only 2.9 fully vaccinated per hundred.</li></ul>', unsafe_allow_html=True)
    st.markdown('<br><h4>Daily Vaccination Surges</h4>', unsafe_allow_html=True)
    st.markdown('<ul><li>March 2021 marked a significant surge, with daily vaccinations per million surpassing 100,000. ' \
    'Four days that month saw over 100 million doses administered in a single day, peaking at 117 million. ' \
    'A similar surge occurred in April, reaching up to 92 million.</li></ul>', unsafe_allow_html=True)
    st.markdown('<br><h4>Most Widely Used Vaccines</h4>', unsafe_allow_html=True)
    st.markdown('<ul><li>The top vaccines globally are Johnson & Johnson, Moderna, Oxford/AstraZeneca, '
    'and Pfizer/BioNTech. Johnson & Johnson leads, being distributed across 17 countries; Moderna, AstraZeneca, and Pfizer/BioNTech follow with 15 countries; ' \
    'AstraZeneca alone reaches 20 countries, making it the most widely distributed. ' \
    'These vaccines dominate due to broad international distribution, particularly to Canada, France, and ' \
    'Spain with France exceeding 70 million total vaccinations.</li></ul>', unsafe_allow_html=True)
    st.markdown('<br><h4>Countries with More Fully Vaccinated Than Partially Vaccinated</h4>', unsafe_allow_html=True)
    st.markdown('<ul><li>In most countries, partially vaccinated numbers are higher. However, exceptions include the Philippines '
    '(21 million fully vaccinated vs. 8.1 million partially vaccinated) and ' \
    'Ethiopia (19 million fully vaccinated vs. 5.3 million partially vaccinated). ' \
    'Altogether, 12 countries show a higher number of fully vaccinated individuals compared to those partially vaccinated.</li></ul>', unsafe_allow_html=True)
    st.markdown('<br><h4>Leading Vaccine Source</h4>', unsafe_allow_html=True)
    st.markdown('<ul><li>The World Health Organization (WHO) leads vaccine distribution, supporting 74 countries. ' \
    'The Ministry of Health follows with 37 countries, and the SPC Public Health Division comes third with 14 countries. ' \
    'In terms of vaccine variety, WHO distributes 44 types, followed by the Ministry of Health with 26, ' \
    'while SPC ranks fifth with five types.</li></ul>', unsafe_allow_html=True)

st.download_button(
    label="Download Summary as Text",
    data=insights_text,
    file_name="vaccination_summary.txt"
)

st.divider()

graph1, graph2, graph3 = st.columns(3)

with graph1:
    col1, col2 = st.columns(2)
    bar = False
    with col1:
        column_select = st.multiselect(
            'Select Columns', 
            [
                'Total Vaccinations', 
                'People Fully Vaccinated', 
                'People Partially Vaccinated', 
                'Daily Vaccinations', 
                'Total Vaccinations Per Hundred', 
                'People Partially Vaccinated Per Hundred', 
                'People Fully Vaccinated Per Hundred', 
                'Daily Vaccinations Per Million',
                'Daily Vaccinations Raw' 
            ]
        )
    with col2:
        monthly = st.checkbox('Monthly')
        if monthly:
            bar = st.checkbox('Bar Chart', value=False)


    column = list()
    if 'Total Vaccinations' in column_select:
        column.append('total_vaccinations')
    if 'People Fully Vaccinated' in column_select:
        column.append('people_fully_vaccinated')
    if 'People Partially Vaccinated' in column_select:
        column.append('people_vaccinated')
    if 'Daily Vaccinations' in column_select:
        column.append('daily_vaccinations')
    if 'Total Vaccinations Per Hundred' in column_select:
        column.append('total_vaccinations_per_hundred')
    if 'People Partially Vaccinated Per Hundred' in column_select:
        column.append('people_vaccinated_per_hundred')
    if 'People Fully Vaccinated Per Hundred' in column_select:
        column.append('people_fully_vaccinated_per_hundred')
    if 'Daily Vaccinations Raw' in column_select:
        column.append('daily_vaccinations_raw')
    if 'Daily Vaccinations Per Million' in column_select: # Daily Vaccinations Per Million
        column.append('daily_vaccinations_per_million')

    if monthly:
        if calculations == "Mean":
            total_vaccinations = df.groupby(month_to_month)[column].mean()
        elif calculations == "Median":
            total_vaccinations = df.groupby(month_to_month)[column].median()
        else:
            total_vaccinations = df.groupby(month_to_month)[column].sum()
    else:
        if calculations == "Mean":
            total_vaccinations = df.groupby('date')[column].mean()
        elif calculations == "Median":
            total_vaccinations = df.groupby('date')[column].median()
        else:
            total_vaccinations = df.groupby('date')[column].sum()

    if bar:
        if monthly:
            fig = px.bar(total_vaccinations, x=total_vaccinations.index, y=column, title='Vaccination Progress Over Time')
        else:
            fig = px.bar(total_vaccinations, x=total_vaccinations.index, y=column, title='Vaccination Progress Over Time')
    else:
        if monthly:
            fig = px.line(total_vaccinations, x=total_vaccinations.index, y=column, title='Vaccination Progress Over Time')
        else:
            fig = px.line(total_vaccinations, x=total_vaccinations.index, y=column, title='Vaccination Progress Over Time')
    
    fig.update_layout(xaxis_title='Date', yaxis_title='Population Number', showlegend=legend_value)
    st.plotly_chart(fig)


with graph2:
    search = st.toggle("Search Countries")
    col1, col2 = st.columns(2)

    with col2:
        vaccinated_category = st.selectbox('Select A Column',
                                            ['People Fully Vaccinated', 
                                            'People Partially Vaccinated', 
                                            'Daily Vaccinations', 
                                            'Total Vaccinations',
                                            'Total Vaccinations Per Hundred',
                                            'People Vaccinated Per Hundred',
                                            'People Fully Vaccinated Per Hundred',
                                            'Daily Vaccinations Per Million'])



    y_title_value1 = ""
    column_name = ''
    title_value = ''
    if vaccinated_category == 'People Fully Vaccinated':
        column_name = 'people_fully_vaccinated'
        title_value = 'Total People Fully Vaccinated In Countries'
        y_title_value1 = 'People Fully Vaccinated'
    elif vaccinated_category == 'People Partially Vaccinated':
        column_name = 'people_vaccinated'
        title_value = 'Total People Partially Vaccinated In Countries'
        y_title_value1 = 'People Partially Vaccinated'
    elif vaccinated_category == 'Total Vaccinations':
        column_name = 'total_vaccinations'
        title_value = 'Total Vaccinations In Countries'
        y_title_value1 = 'Total Vaccinations'
    elif vaccinated_category == 'Total Vaccinations Per Hundred':
        column_name = 'total_vaccinations_per_hundred'
        title_value = 'Total of Total Vaccinations Per Hundred In Countries'
        y_title_value1 = 'Total Vaccinations Per Hundred'
    elif vaccinated_category == 'People Vaccinated Per Hundred':
        column_name = 'people_vaccinated_per_hundred'
        title_value = 'Total Vaccinated Vaccinated Per Hundred'
        y_title_value1 = 'People Vaccinated Per Hundred'
    elif vaccinated_category == 'People Fully Vaccinated Per Hundred':
        column_name = 'people_fully_vaccinated_per_hundred'
        title_value = 'Total People Fully Vaccinated Per Hundred In Countries'
        y_title_value1 = 'People Fully Vaccinated Per Hundred'
    elif vaccinated_category == 'Daily Vaccinations Per Million':
        column_name = 'daily_vaccinations_per_million'
        title_value = 'Total Daily Vaccinations Per Million'
        y_title_value1 = 'Daily Vaccinations Per Million'
    else: # Daily Vaccinations
        column_name = 'daily_vaccinations'
        title_value = 'Total Daily Vaccinations In Each Country'
        y_title_value1 = 'Daily Vaccinations'

    if search:
        with col1:
            countries_selected = st.multiselect('Select Countries', df['country'].unique())
            country_vac = df.groupby('country')[column_name].mean().sort_values(ascending=False)
            if countries_selected:
                country_vac = country_vac[countries_selected]
            
    else:
        with col1:
            start_country = st.slider('Slider Across Countries', 0, 210, 0, 30)
            if calculations == 'Mean':
                country_vac = df.groupby('country')[column_name].mean().sort_values(ascending=False)[start_country:start_country+30]
            elif calculations == 'Median':
                country_vac = df.groupby('country')[column_name].median().sort_values(ascending=False)[start_country:start_country+30]
            else:
                country_vac = df.groupby('country')[column_name].sum().sort_values(ascending=False)[start_country:start_country+30]

    st.write('I can add textbar for searching a country to view')
    fig = px.bar(country_vac, x=country_vac.index, y=country_vac)
    fig.update_layout(title=title_value, xaxis_title='Countries', yaxis_title=y_title_value1)
    st.plotly_chart(fig)

with graph3:
    column_distr = st.selectbox('Select A Column', ['Countries', 'Vaccines'])
    title_value1 = ''
    xaxis_value1 = ''
    if column_distr == 'Countries':
        data2 = pd.DataFrame(df.groupby(['country', 'source_name']).size()).sort_values('source_name').reset_index()
        data2 = data2['source_name'].value_counts().iloc[:8]
        title_value1 = 'Number Of Countries Using Each Data Source'
        xaxis_value1 = 'Countries Number'
    else:
        data2 = pd.DataFrame(df.groupby(['vaccines', 'source_name']).size()).sort_values('source_name').reset_index()
        data2 = data2['source_name'].value_counts().iloc[:6]
        title_value1 = 'Number Of Vaccines Using Each Data Source'
        xaxis_value1 = 'Vaccines Number'

    fig = px.bar(data2, x='count', y=data2.index, orientation='h', color=data2.index)
    fig.update_layout(title=title_value1, 
                    xaxis_title=xaxis_value1, 
                    yaxis_title='Source Name',
                    showlegend=False)
    st.plotly_chart(fig)

graph1, graph2 = st.columns(2)

with graph1:
    if calculations == 'Mean':
        partially_vs_full = df.groupby('country')[['people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred']].mean()
    elif calculations == 'Median':
        partially_vs_full = df.groupby('country')[['people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred']].median()
    else:
        partially_vs_full = df.groupby('country')[['people_vaccinated_per_hundred', 'people_fully_vaccinated_per_hundred']].sum()

    fig = px.scatter(partially_vs_full, x='people_vaccinated_per_hundred', 
                    y='people_fully_vaccinated_per_hundred', 
                    color=partially_vs_full.index)
    fig.update_layout(title="Partially VS Fully Vaccinated People By Countries", 
                    xaxis_title='People Vaccinated Per Hundred', 
                    yaxis_title='People Fully Vaccinated Per Hundred')
    st.plotly_chart(fig)

# On the scatter graph the country has similar colors that makes it hard differentiate them.
# I Need to plot box graphs and the ones after it.

# if calculations == 'Mean':
#     country_daily_vacc = df.groupby('country')['daily_vaccinations_per_million'].mean()
# elif calculations == 'Median':
#     country_daily_vacc = df.groupby('country')['daily_vaccinations_per_million'].median()
# else:
#     country_daily_vacc = df.groupby('country')['daily_vaccinations_per_million'].sum()

with graph2:
    distribution = st.selectbox('Select Distribution', ['Daily Vaccination Per Million in Months', 'Daily Vaccination Per Million in Countries'])

    if distribution == 'Daily Vaccination Per Million in Months':
        fig = px.box(df, x=df['date'].dt.strftime('%Y-%m'), 
                    y=df['daily_vaccinations_per_million'])
        fig.update_layout(title='Distribution Of Daily Vaccinations Per Million In  Months', 
                        xaxis_title='Months', 
                        yaxis_title='Daily Vaccinations Per Million')
    else:
        start_country_count = st.slider('Slide Across Countries', 0, 80000, 0, 10000)
        new_df = df.iloc[start_country_count:start_country_count+10000]
        fig = px.box(new_df, x='country', y='daily_vaccinations_per_million', color='country')
        fig.update_layout(title='Distribution Of Daily Vaccinations Per Million In Countries', 
                        xaxis_title='Countries', 
                        yaxis_title='Daily Vaccinations Per Million', 
                        showlegend=False)
    st.plotly_chart(fig)


st.divider()

country_count = pd.DataFrame(df.groupby(['country', 'vaccines']).count())['total_vaccinations'].reset_index()


col1, col2 = st.columns(2)
with col1:
    full_view = st.toggle('Full View', True)
with col2:
    option_country_vaccines = st.toggle("Select Vaccines")
if full_view:
    pass
else:
    col1, col2 = st.columns(2)
    with col1:
        if option_country_vaccines:
            country_option = False
            vaccines_values = st.multiselect('Select Vaccines', df['vaccines'].unique())
            country_count.set_index('vaccines', inplace=True)
            country_count = country_count.loc[vaccines_values]
    with col2:
        if not option_country_vaccines:
            vaccines_option = False
            country_values = st.multiselect('Select Countries', df['country'].unique())
            country_count.set_index('country', inplace=True)
            country_count = country_count.loc[country_values]

country_count.reset_index(inplace=True)
fig = px.scatter(country_count, x='country', y='total_vaccinations', color='vaccines', color_discrete_sequence=px.colors.qualitative.Set1)
fig.update_layout(
    title='Distribution Of Vaccines By Countries',
    xaxis_title='Countries',
    yaxis_title='Vaccines Number'
)

st.plotly_chart(fig)

st.divider()

graph1, graph2 = st.columns(2)

with graph1:
    fully_partially = df.groupby('country')[['people_fully_vaccinated', 'people_vaccinated']].mean().sort_values('people_vaccinated', ascending=False)

    start_slider3 = st.slider('Slide Across Countries', 0, 210, 0, 30, key='comparison' )
    fully_partially = fully_partially.iloc[start_slider3:start_slider3+30]
    fig = go.Figure(
        data=[
            go.Bar(
                name='People Partially Vaccinated', 
                x=fully_partially.index, 
                y=fully_partially['people_vaccinated']
            ),
            go.Bar(
                name='People Fully Vaccinated',
                x=fully_partially.index,
                y=fully_partially['people_fully_vaccinated']
            )
        ]
    )
    fig.update_layout(
        title='Partially vs. Fully Vaccinated Population By Countries',
        xaxis_title='Countries',
        yaxis_title='Population Numbers'
    )

    st.plotly_chart(fig)

with graph2:
    if calculations == 'Mean':
        vacc_over_country = df.groupby('country')['total_vaccinations'].mean()
    elif calculations == 'Median':
        vacc_over_country = df.groupby('country')['total_vaccinations'].median()
    else:
        vacc_over_country = df.groupby('country')['total_vaccinations'].sum()

    vacc_over_country = pd.DataFrame(vacc_over_country).reset_index()

    fig = px.treemap(vacc_over_country, 
                    path=['country'], 
                    values='total_vaccinations')
    fig.update_layout(title='Total Vaccinations By Countries')

    st.plotly_chart(fig)

st.divider()





vaccine_count = df['vaccines'].value_counts().sort_values(ascending=False)

start_slider = st.slider('Slide Across Vaccines', 0, 80, 0, 20)
vaccine_count = vaccine_count.iloc[start_slider:start_slider+20]
fig = px.bar(vaccine_count, 
             y=vaccine_count.index, 
             x=vaccine_count, 
             orientation='h',
             color=vaccine_count.index)
fig.update_layout(showlegend=False,
                  title='Distribution of Vaccines',
                  xaxis_title='Distribution Number',
                  yaxis_title='Vaccines')
st.plotly_chart(fig)

st.divider()

new_cacl = pd.DataFrame(df.groupby(['country', 'vaccines']).size()).reset_index().set_index('country')
vaccine_country = new_cacl['vaccines'].value_counts().sort_values(ascending=False).head(37)

fig = px.bar(vaccine_country, x='count', y=vaccine_country.index, orientation='h', color=vaccine_country.index)
fig.update_layout(showlegend=False,
                  title='Vaccines Used By Multiple Countries',
                  xaxis_title='Number of Countries',
                  yaxis_title='Vaccines',
                  height=712)
st.plotly_chart(fig)
