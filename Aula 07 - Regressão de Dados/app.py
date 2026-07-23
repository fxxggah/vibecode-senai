import pickle
import pandas as pd
import streamlit as st


# ---------- 1. Configuração e Estilo Visual (Clean SaaS) ----------

def configurar_pagina():
    st.set_page_config(
        page_title="Previsão Salarial",
        page_icon="💼",
        layout="centered",
        initial_sidebar_state="collapsed",
    )


def aplicar_estilo_visual():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

            html, body, [class*="css"] {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            }

            /* Container principal centralizado e limpo */
            .block-container {
                max-width: 760px !important;
                padding-top: 3rem !important;
                padding-bottom: 3rem !important;
            }

            /* Estilização do Botão Principal */
            div[data-testid="stForm"] button[type="submit"] {
                background-color: #0F172A !important;
                color: #FFFFFF !important;
                border: none !important;
                border-radius: 8px !important;
                font-weight: 600 !important;
                padding: 0.6rem 1rem !important;
                transition: all 0.2s ease !important;
            }

            div[data-testid="stForm"] button[type="submit"]:hover {
                background-color: #1E293B !important;
                box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15) !important;
            }

            /* Ajustes finos nos textos do formulário */
            .stSelectbox label, .stSlider label {
                font-weight: 500 !important;
                color: #334155 !important;
                font-size: 0.9rem !important;
            }

            /* Card de Resultado com métrica em destaque */
            div[data-testid="stMetricValue"] {
                font-size: 2.2rem !important;
                font-weight: 700 !important;
                color: #0F172A !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------- 2. Carregamento do Modelo ----------

@st.cache_resource
def carregar_modelo_treinado():
    try:
        with open("preditor-salarios.pkl", "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return None


# ---------- 3. Utilitários ----------

def formatar_moeda(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def preparar_dados_e_prever(pacote_modelo, inputs):
    dados_entrada = {
        "Experiência em Anos": inputs["experiencia"],
        "Avaliação de Desempenho": inputs["desempenho"],
        "Certificações Profissionais": inputs["certificacoes"],
        f"Nível Profissional_{inputs['nivel']}": 1,
        f"Escolaridade_{inputs['escolaridade']}": 1,
    }

    tabela_entrada = pd.DataFrame([dados_entrada]).reindex(
        columns=pacote_modelo["colunas_treino"], fill_value=0
    )

    return pacote_modelo["modelo"].predict(tabela_entrada)[0]


# ---------- 4. Aplicação Principal ----------

def main():
    configurar_pagina()
    aplicar_estilo_visual()

    # Cabeçalho Limpo
    st.title("💼 Previsão Salarial")
    st.caption("Insira as métricas do perfil profissional para calcular a estimativa base de remuneração.")
    st.divider()

    pacote_modelo = carregar_modelo_treinado()

    if not pacote_modelo:
        st.error("⚠️ O arquivo `preditor-salarios.pkl` não foi localizado na raiz do projeto.")
        return

    opcoes_escolaridade = {
        "Ensino Técnico": "técnico",
        "Graduação": "graduação",
        "Pós-graduação": "pós-graduação",
        "Mestrado": "mestrado",
        "Doutorado": "doutorado",
    }

    # Form minimalista com borda suave
    with st.form("form_calculadora"):
        col_esq, col_dir = st.columns(2, gap="medium")

        with col_esq:
            nivel = st.selectbox("Nível profissional", ["Júnior", "Pleno", "Sênior"])

            escolaridade_label = st.selectbox(
                "Escolaridade", options=list(opcoes_escolaridade.keys())
            )
            escolaridade = opcoes_escolaridade[escolaridade_label]

            experiencia = st.slider(
                "Anos de experiência", min_value=0, max_value=25, value=5
            )

        with col_dir:
            desempenho = st.slider(
                "Avaliação de desempenho",
                min_value=2,
                max_value=10,
                value=6,
                help="Pontuação de 2 a 10 no ciclo de avaliação interno.",
            )

            certificacoes = st.slider(
                "Certificações profissionais", min_value=0, max_value=11, value=2
            )

        st.markdown("---")
        submetido = st.form_submit_button("Calcular Estimativa Salarial", use_container_width=True)

    # Exibição do Resultado em Card Limpo
    if submetido:
        inputs = {
            "nivel": nivel,
            "escolaridade": escolaridade,
            "experiencia": experiencia,
            "desempenho": desempenho,
            "certificacoes": certificacoes,
        }

        salario_estimado = preparar_dados_e_prever(pacote_modelo, inputs)

        st.write("")
        with st.container(border=True):
            st.metric(
                label="Salário Mensal Estimado",
                value=formatar_moeda(salario_estimado),
            )
            st.caption(" Estimativa estatística calculada com base nos parâmetros do modelo.")


if __name__ == "__main__":
    main()