import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_excel("C:\\Users\\Tiago\\board_game\\boar_game_exel.xlsx")
df1 = df.copy()

st.header('board game master')

st.sidebar.markdown("""___""")


st.sidebar.markdown('## Selecione uma pessoa')

pessoas_options = st.sidebar.multiselect(
    'Quais pessoas vc quer ver?',
    ['caio' , 'tiago' , 'vijo' , 'judice '],
    default=['caio', 'judice ', 'vijo', 'tiago']
)
st.sidebar.markdown("""___""")

linhas_selc = df['pessoas'].isin(pessoas_options)
df = df.loc[linhas_selc,:]

st.dataframe(df)



tap1, tap2, tap3 = st.tabs(['pontos totais ','dias ganhos de 2024','Campeões anuais'])

with tap1:
    with st.container():
        st.markdown("# Garfico pontos total")

        caio = df.loc[0,'total'] 
        tiago = df.loc[1,'total']
        vijo = df.loc[2,'total']
        judice = df.loc[3,'total'] 

        fig = px.bar(x=['caio', 'tiago', 'vijo', 'judice '], y=[caio, tiago, vijo, judice], color=['caio', 'tiago', 'vijo', 'judice '])
        st.plotly_chart(fig, use_container_width=True)


with tap2:
    with st.container():
        st.markdown("# Garfico dias ganhos")

        caio = df.loc[0,'dias'] 
        tiago = df.loc[1,'dias']
        vijo = df.loc[2,'dias']
        judice = df.loc[3,'dias'] 

        fig = px.bar(x=['caio', 'tiago', 'vijo', 'judice '], y=[caio, tiago, vijo, judice], color=['caio', 'tiago', 'vijo', 'judice '])
        st.plotly_chart(fig, use_container_width=True)


with tap3:
    with st.container():
        st.markdown("# Campeao anual")

        caio = df.loc[0,'anual'] 
        tiago = df.loc[1,'anual']
        vijo = df.loc[2,'anual']
        judice = df.loc[3,'anual'] 

        fig = px.bar(x=['caio', 'tiago', 'vijo', 'judice '], y=[caio, tiago, vijo, judice], color=['caio', 'tiago', 'vijo', 'judice '])
        st.plotly_chart(fig, use_container_width=True)

#total
#dias_ganhos
#atual caempao