import pandas as pd
import streamlit as st
import plotly.express as px

# Carregando o DataFrame
df = pd.read_excel("boar_game_exel.xlsx")
df1 = df.copy()

st.header('Board Game Master')

# Barra lateral para seleção de pessoas
st.sidebar.markdown("___")
st.sidebar.markdown('## Selecione uma pessoa')

pessoas_options = st.sidebar.multiselect(
    'Quais pessoas você quer ver?',
    df['pessoas'].unique(),  # Pegando as pessoas diretamente do DataFrame
    default=df['pessoas'].unique()
)
st.sidebar.markdown("___")

# Filtrando o DataFrame com base na seleção
df = df[df['pessoas'].isin(pessoas_options)]

# Exibindo o DataFrame filtrado
st.dataframe(df)

# Definindo uma função para criar gráficos
def criar_grafico(titulo, coluna):
    st.markdown(f"### {titulo}")
    fig = px.bar(
        x=df['pessoas'], 
        y=df[coluna], 
        color=df['pessoas'], 
        labels={'x': 'Jogadores', 'y': titulo}
    )
    st.plotly_chart(fig, use_container_width=True)

# Criando abas
tap1, tap2, tap3 = st.tabs(['Pontos Totais', 'Dias Ganhos de 2024', 'Campeões Anuais'])

with tap1:
    with st.container():
        criar_grafico("Gráfico de Pontos Totais", 'total')

with tap2:
    with st.container():
        criar_grafico("Gráfico de Dias Ganhos", 'dias')

with tap3:
    with st.container():
        criar_grafico("Gráfico de Campeões Anuais", 'anual')
