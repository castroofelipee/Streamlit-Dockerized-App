import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'Lucro (R$)': [1800000, 2200000, 1500000, 1700000, 1900000, 1400000, 1600000, 2100000, 1500000, 1300000, 2200000, 1700000]
}

df = pd.DataFrame(data)

st.title("Lucro Mensal da Empresa")
st.write("Dados fictícios de lucro mensal (em milhões de reais)")

st.write("Dados Mensais:")
st.write(df)

fig, ax = plt.subplots()
bars = ax.bar(df['Mês'], df['Lucro (R$)'])


for i, bar in enumerate(bars):
    if data['Lucro (R$)'][i] < 1500000:
        bar.set_color('red')

ax.set_xlabel("Mês")
ax.set_ylabel("Lucro (R$)")
ax.set_title("Lucro Mensal da Empresa")


st.pyplot(fig)
