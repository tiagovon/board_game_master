import pandas as pd
import streamlit as st

# Caminho do arquivo Excel (ajuste conforme necessário)
caminho_arquivo = 'boar_game_exel.xlsx'

# Carregando o DataFrame principal
df = pd.read_excel(caminho_arquivo)

# Título do site
st.title('Board Game Master - Resultados dos Jogos')

# Mostrando a tabela atual
st.subheader('Tabela Atual')
st.dataframe(df)

# Entrada para o número de jogos do dia
num = st.number_input("Quantos jogos teve no dia?", min_value=1, step=1)

# Dicionários para controle de linhas e pontos dos jogadores
jogadores_linhas_tabela = {"caio": 0, "tiago": 1, "vijo": 2, "judice": 3}
jogadores_pontos = {"caio": 0, "tiago": 0, "vijo": 0, "judice": 0}
posicao_para_pontos = {"1": 5, "2": 3, "3": 2, "4": 1}

# Loop para capturar os resultados de cada jogo
for _ in range(num):
    st.subheader("Adicionar Resultados de um Novo Jogo")
    novo_jogo = st.text_input("Qual é o nome do jogo?", key=f"jogo_{_}")
    
    if novo_jogo:
        if novo_jogo not in df.columns:
            df[novo_jogo] = [0, 0, 0, 0]  # Inicializa a coluna do novo jogo

        for name, linha in jogadores_linhas_tabela.items():
            posicao = st.selectbox(
                f"Qual foi a posição de {name} no jogo {novo_jogo}?",
                ["1", "2", "3", "4"],
                key=f"{name}_{_}"
            )
            pontos = posicao_para_pontos[posicao]
            df.at[linha, novo_jogo] = pontos  # Usando .at para garantir a atribuição
            df.at[linha, 'total'] += pontos
            jogadores_pontos[name] += pontos

# Botão para determinar o campeão do dia
if st.button("Determinar Campeão do Dia"):
    campeao, valor_maximo = max(jogadores_pontos.items(), key=lambda item: item[1])
    st.success(f"Campeão do dia: {campeao}")
    
    # Atualizando a coluna 'dias' no DataFrame com .at para garantir a modificação
    df.at[jogadores_linhas_tabela[campeao], 'dias'] += 1
    st.write(f"A coluna 'dias' foi atualizada para o jogador {campeao}.")

# Exibindo a tabela atualizada antes do salvamento
st.subheader("Tabela Atualizada (Antes de Salvar)")
st.dataframe(df)

# Salvando as mudanças no arquivo Excel
if st.button("Salvar Alterações"):
    try:
        # Salvando o DataFrame atualizado no arquivo Excel
        df.to_excel(caminho_arquivo, index=False)
        st.success("Alterações salvas com sucesso!")
        
        # Verificando se as alterações foram refletidas no arquivo
        df_recarregado = pd.read_excel(caminho_arquivo)
        st.subheader("Tabela Recarregada do Arquivo")
        st.dataframe(df_recarregado)
    except Exception as e:
        st.error(f"Ocorreu um erro ao salvar as alterações: {e}")
