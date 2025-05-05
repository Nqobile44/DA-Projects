import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title('Practicing Time')
st.header('heading')
st.subheader('sub heading')
st.markdown('hello **my goal** _is_..')
st.caption('small text')

code_example = """
def test(life):
    return "{life} successfully tested"
"""
st.code(code_example, language='python')

st.divider()
st.title("Data Cleaning")
st.image(os.path.join(os.getcwd(), 'static', 'data cleaning.png'))

df = pd.read_csv('country_vaccination/country_vaccinations.csv')

st.title('DataFrame')
st.dataframe(df)

st.title('Data Editor')
st.data_editor(df)

st.title('Simple Table')
st.table(df.head()[['country', 'date', 'source_name']])

st.divider()
st.metric(label='Total Rows', value=len(df))
st.metric(label='Daily Vaccinations Average', value=round(df['daily_vaccinations'].mean(), 1))

country_count = df['country'].value_counts().head()

country_count
st.bar_chart(country_count, x_label='Countries', y_label='Number of Vaccines', color='#ffaa0088')

date = pd.to_datetime(df['date']).dt.strftime('%Y').value_counts()
date

st.divider()
fig, ax = plt.subplots()
ax = sns.barplot(date, palette='viridis')
for index in range(len(date.index)):
    ax.bar_label(ax.containers[index], )
plt.title('hello', fontweight='bold', fontsize=50)
plt.xlabel('Date', fontweight='bold')
plt.ylabel('Vaccines Numbers', fontweight='bold')
plt.grid(axis='y')
st.pyplot(fig)
st.plotly_chart

st.divider()

df = px.data.gapminder().query("year == 2021")
fig = px.line(df, x="gdpPercap", y="lifeExp", size="pop", color="continent")
st.plotly_chart(fig)