import streamlit as st
import webbrowser as web
import pandas as pd
from datetime import datetime
st.set_page_config(
    layout="wide",
    page_title = "Fifa data",
    page_icon = "🏠")

if "data" not in st.session_state:
    df_data = pd.read_csv("CLEAN_FIFA23_official_data.csv", index_col = 0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data



st.markdown("# FIFA23 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Desenvolvido por [Artur F. Sales](https://www.youtube.com/@turzimm9130)")

btn = st.link_button("Acesse os dados no Kaggle", "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
                     
st.markdown("""○ conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre
jogadores de futebol profissionais., conjunto de dados contém uma ampla gama de atributos, incluindo
dados demográficos do jogador, características fisicas, estatisticas de jogo, detalhes do contrato e
afliacões de clubes.


Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para analistas de
futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, pois
permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de
clubes, posicionamento de jogadores e desenvolvimento do jogador ao longa do tempo,○ conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações abrangentes sobre
jogadores de futebol profissionais., conjunto de dados contém uma ampla gama de atributos, incluindo
dados demográficos do jogador, características fisicas, estatisticas de jogo, detalhes do contrato e
afliacões de clubes.


Com mais de 17.000 registros, este conjunto de dados oferece um recurso valioso para analistas de
futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, pois
permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de
clubes, posicionamento de jogadores e desenvolvimento do jogador ao longa do tempo,""")