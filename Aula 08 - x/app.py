import streamlit as st
import pandas as pd
import pickle

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO DA PÁGINA
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Preditor · Diabetes Gestacional",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTES — limites extraídos da base de dados de treinamento
# ─────────────────────────────────────────────────────────────────────────────

MINIMO_NUMERO_GESTACOES     = 0
MAXIMO_NUMERO_GESTACOES     = 14

MINIMO_GLICOSE              = 44
MAXIMO_GLICOSE              = 192
VALOR_PADRAO_GLICOSE        = 108

MINIMO_PRESSAO_ARTERIAL     = 24
MAXIMO_PRESSAO_ARTERIAL     = 117
VALOR_PADRAO_PRESSAO        = 71

MINIMO_ESPESSURA_TRICEPS    = 7
MAXIMO_ESPESSURA_TRICEPS    = 92
VALOR_PADRAO_TRICEPS        = 29

MINIMO_INSULINA             = 14
MAXIMO_INSULINA             = 796
VALOR_PADRAO_INSULINA       = 139

MINIMO_INDICE_MASSA_CORPORAL = 18.2
MAXIMO_INDICE_MASSA_CORPORAL = 56.0
VALOR_PADRAO_IMC            = 31.6

MINIMO_PEDIGREE             = 0.08
MAXIMO_PEDIGREE             = 2.30
VALOR_PADRAO_PEDIGREE       = 0.40

MINIMO_IDADE                = 21
MAXIMO_IDADE                = 77
VALOR_PADRAO_IDADE          = 30

OPCOES_NUMERO_GESTACOES = {
    "Nenhuma gestação anterior": 0,
    "1 gestação anterior":       1,
    "2 gestações anteriores":    2,
    "3 gestações anteriores":    3,
    "4 gestações anteriores":    4,
    "5 gestações anteriores":    5,
    "6 gestações anteriores":    6,
    "7 gestações anteriores":    7,
    "8 gestações anteriores":    8,
    "9 gestações anteriores":    9,
    "10 gestações anteriores":   10,
    "11 gestações anteriores":   11,
    "12 gestações anteriores":   12,
    "13 gestações anteriores":   13,
    "14 gestações anteriores":   14,
}

# ─────────────────────────────────────────────────────────────────────────────
# CSS PERSONALIZADO
# ─────────────────────────────────────────────────────────────────────────────

ESTILOS_CSS = """
<style>

/* ── Fonte do Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=DM+Serif+Display&display=swap');

/* ── Container principal: 75% no desktop, 100% no mobile ── */
.block-container {
    max-width: 75% !important;
    margin-left: auto  !important;
    margin-right: auto !important;
    padding-top: 2.5rem !important;
    padding-bottom: 3rem !important;
    font-family: 'Inter', sans-serif !important;
}

@media (max-width: 768px) {
    .block-container {
        max-width: 100% !important;
        padding-left: 1.25rem !important;
        padding-right: 1.25rem !important;
    }
}

/* ── Tipografia global ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

/* ── Cabeçalho da aplicação ── */
.cabecalho-app {
    display: flex;
    align-items: flex-start;
    gap: 1.25rem;
    margin-bottom: 0.25rem;
}

.icone-cabecalho {
    font-size: 2.75rem;
    line-height: 1;
    margin-top: 0.15rem;
}

.titulo-principal {
    font-family: 'DM Serif Display', serif !important;
    font-size: 2.4rem !important;
    font-weight: 400 !important;
    color: #0f172a !important;
    letter-spacing: -0.5px;
    line-height: 1.15;
    margin: 0 !important;
}

.subtitulo-principal {
    font-size: 1rem;
    color: #64748b;
    margin-top: 0.35rem;
    line-height: 1.55;
}

/* ── Divisor temático ── */
.divisor-sutil {
    border: none;
    border-top: 1.5px solid #e2e8f0;
    margin: 1.75rem 0 2rem;
}

/* ── Instruções ── */
.bloco-instrucao {
    background: #f0f9ff;
    border-left: 4px solid #38bdf8;
    border-radius: 0 8px 8px 0;
    padding: 0.85rem 1.1rem;
    margin-bottom: 2rem;
    font-size: 0.9rem;
    color: #0c4a6e;
    line-height: 1.6;
}

/* ── Cartões de seção ── */
.cartao-secao {
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 14px;
    padding: 1.6rem 1.75rem 1.35rem;
    margin-bottom: 1.25rem;
}

.cabecalho-secao {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 1.25rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid #f1f5f9;
}

.icone-secao { font-size: 1.2rem; }

.titulo-secao {
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #94a3b8;
    margin: 0;
}

/* ── Resultado — Baixo Risco ── */
.resultado-baixo-risco {
    background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    border: 2px solid #86efac;
    border-radius: 18px;
    padding: 2.25rem 2rem;
    text-align: center;
    margin-top: 2rem;
}

/* ── Resultado — Alto Risco ── */
.resultado-alto-risco {
    background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
    border: 2px solid #fdba74;
    border-radius: 18px;
    padding: 2.25rem 2rem;
    text-align: center;
    margin-top: 2rem;
}

/* ── Elementos internos do resultado ── */
.etiqueta-resultado {
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.icone-resultado { font-size: 2.5rem; margin-bottom: 0.4rem; }

.percentual-risco {
    font-family: 'DM Serif Display', serif;
    font-size: 4.5rem;
    line-height: 1;
    margin: 0.25rem 0;
}

.legenda-percentual {
    font-size: 0.85rem;
    color: #64748b;
    margin-bottom: 1rem;
}

.veredicto {
    font-size: 1.05rem;
    font-weight: 600;
    margin-bottom: 0.35rem;
}

.orientacao {
    font-size: 0.875rem;
    color: #475569;
    line-height: 1.6;
    max-width: 480px;
    margin: 0 auto;
}

/* ── Aviso legal ── */
.aviso-legal {
    font-size: 0.78rem;
    color: #94a3b8;
    text-align: center;
    margin-top: 1.75rem;
    padding: 0 1rem;
    line-height: 1.6;
}

/* ── Botão de calcular ── */
.stButton > button[kind="primary"] {
    background: #0f172a !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    padding: 0.75rem 1.5rem !important;
    letter-spacing: 0.02em !important;
    transition: background 0.2s ease !important;
}

.stButton > button[kind="primary"]:hover {
    background: #1e293b !important;
}

/* ── Selectbox e sliders: refinamento visual ── */
label[data-testid="stWidgetLabel"] > div > p {
    font-size: 0.88rem !important;
    font-weight: 500 !important;
    color: #334155 !important;
}

</style>
"""

# ─────────────────────────────────────────────────────────────────────────────
# CARREGAMENTO DO MODELO — executado uma única vez, mantido em cache
# ─────────────────────────────────────────────────────────────────────────────

@st.cache_resource
def carregar_modelo_preditivo():
    """Carrega o modelo treinado do disco e mantém em memória entre interações."""
    with open("preditor-diabetes.pkl", "rb") as arquivo_modelo:
        modelo_carregado = pickle.load(arquivo_modelo)
    return modelo_carregado

# ─────────────────────────────────────────────────────────────────────────────
# FUNÇÕES DE INTERFACE
# ─────────────────────────────────────────────────────────────────────────────

def exibir_cabecalho():
    """Exibe o título, subtítulo e instrução de uso."""
    st.markdown("""
    <div class="cabecalho-app">
        <div class="icone-cabecalho">🩺</div>
        <div>
            <div class="titulo-principal">Preditor de Diabetes Gestacional</div>
            <div class="subtitulo-principal">
                Avaliação do risco individual com base em indicadores clínicos e histórico da paciente
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divisor-sutil">', unsafe_allow_html=True)

    st.markdown("""
    <div class="bloco-instrucao">
        <strong>Como usar:</strong> preencha os campos abaixo com os dados da paciente usando
        as listas e controles deslizantes — não é necessário digitar nada.
        Ao terminar, clique em <strong>Calcular Risco</strong>.
    </div>
    """, unsafe_allow_html=True)


def coletar_dados_gestacionais():
    """Exibe os campos de dados gestacionais e pessoais e retorna os valores."""
    st.markdown("""
    <div class="cartao-secao">
        <div class="cabecalho-secao">
            <span class="icone-secao">👶</span>
            <span class="titulo-secao">Histórico Gestacional e Dados Pessoais</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    coluna_esquerda, coluna_direita = st.columns(2, gap="large")

    with coluna_esquerda:
        rotulo_selecionado = st.selectbox(
            "Número de gestações anteriores",
            options=list(OPCOES_NUMERO_GESTACOES.keys()),
            index=2,
            help="Contagem de gestações que a paciente já teve, incluindo abortos e natimortos.",
        )
        numero_gestacoes = OPCOES_NUMERO_GESTACOES[rotulo_selecionado]

    with coluna_direita:
        idade = st.slider(
            "Idade da paciente (anos)",
            min_value=MINIMO_IDADE,
            max_value=MAXIMO_IDADE,
            value=VALOR_PADRAO_IDADE,
            step=1,
            help=f"Faixa registrada na base de dados: {MINIMO_IDADE} a {MAXIMO_IDADE} anos.",
        )

    return numero_gestacoes, idade


def coletar_medicoes_clinicas():
    """Exibe os campos de medições clínicas e retorna os valores."""
    st.markdown("""
    <div class="cartao-secao">
        <div class="cabecalho-secao">
            <span class="icone-secao">🩸</span>
            <span class="titulo-secao">Medições Clínicas</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    coluna_esquerda, coluna_central, coluna_direita = st.columns(3, gap="large")

    with coluna_esquerda:
        nivel_glicose = st.slider(
            "Glicose plasmática em jejum (mg/dL)",
            min_value=MINIMO_GLICOSE,
            max_value=MAXIMO_GLICOSE,
            value=VALOR_PADRAO_GLICOSE,
            step=1,
            help=f"Concentração de glicose no plasma após jejum. Referência na base: {MINIMO_GLICOSE}–{MAXIMO_GLICOSE} mg/dL.",
        )

    with coluna_central:
        pressao_arterial_diastolica = st.slider(
            "Pressão arterial diastólica (mmHg)",
            min_value=MINIMO_PRESSAO_ARTERIAL,
            max_value=MAXIMO_PRESSAO_ARTERIAL,
            value=VALOR_PADRAO_PRESSAO,
            step=1,
            help=f"Pressão no momento em que o coração relaxa. Referência na base: {MINIMO_PRESSAO_ARTERIAL}–{MAXIMO_PRESSAO_ARTERIAL} mmHg.",
        )

    with coluna_direita:
        nivel_insulina = st.slider(
            "Insulina sérica 2 h após teste (μU/mL)",
            min_value=MINIMO_INSULINA,
            max_value=MAXIMO_INSULINA,
            value=VALOR_PADRAO_INSULINA,
            step=1,
            help=f"Insulina medida 2 horas após ingestão de glicose. Referência na base: {MINIMO_INSULINA}–{MAXIMO_INSULINA} μU/mL.",
        )

    return nivel_glicose, pressao_arterial_diastolica, nivel_insulina


def coletar_medidas_corporais():
    """Exibe os campos de medidas corporais e retorna os valores."""
    st.markdown("""
    <div class="cartao-secao">
        <div class="cabecalho-secao">
            <span class="icone-secao">📏</span>
            <span class="titulo-secao">Medidas Corporais</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    coluna_esquerda, coluna_direita = st.columns(2, gap="large")

    with coluna_esquerda:
        espessura_dobra_cutanea_triceps = st.slider(
            "Espessura da dobra cutânea do tríceps (mm)",
            min_value=MINIMO_ESPESSURA_TRICEPS,
            max_value=MAXIMO_ESPESSURA_TRICEPS,
            value=VALOR_PADRAO_TRICEPS,
            step=1,
            help=f"Medida da dobra de gordura na parte posterior do braço. Referência na base: {MINIMO_ESPESSURA_TRICEPS}–{MAXIMO_ESPESSURA_TRICEPS} mm.",
        )

    with coluna_direita:
        indice_massa_corporal = st.slider(
            "Índice de Massa Corporal — IMC (kg/m²)",
            min_value=MINIMO_INDICE_MASSA_CORPORAL,
            max_value=MAXIMO_INDICE_MASSA_CORPORAL,
            value=VALOR_PADRAO_IMC,
            step=0.1,
            format="%.1f",
            help=f"Peso dividido pelo quadrado da altura. Referência na base: {MINIMO_INDICE_MASSA_CORPORAL}–{MAXIMO_INDICE_MASSA_CORPORAL} kg/m².",
        )

    return espessura_dobra_cutanea_triceps, indice_massa_corporal


def coletar_historico_familiar():
    """Exibe o campo de índice de pedigree e retorna o valor."""
    st.markdown("""
    <div class="cartao-secao">
        <div class="cabecalho-secao">
            <span class="icone-secao">🧬</span>
            <span class="titulo-secao">Histórico Familiar</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    indice_pedigree_diabetes = st.slider(
        "Índice de pedigree de diabetes familiar",
        min_value=MINIMO_PEDIGREE,
        max_value=MAXIMO_PEDIGREE,
        value=VALOR_PADRAO_PEDIGREE,
        step=0.01,
        format="%.2f",
        help=(
            "Pontuação que quantifica a predisposição genética com base no histórico "
            f"de diabetes na família da paciente. Quanto maior, mais intenso o histórico. "
            f"Referência na base: {MINIMO_PEDIGREE}–{MAXIMO_PEDIGREE}."
        ),
    )

    return indice_pedigree_diabetes


def montar_dataframe_para_predicao(
    numero_gestacoes,
    nivel_glicose,
    pressao_arterial_diastolica,
    espessura_dobra_cutanea_triceps,
    nivel_insulina,
    indice_massa_corporal,
    indice_pedigree_diabetes,
    idade,
):
    """Organiza os dados coletados no formato de colunas que o modelo espera."""
    dicionario_dados_paciente = {
        "gravidez":               [numero_gestacoes],
        "glicose":                [nivel_glicose],
        "pressao-arterial":       [pressao_arterial_diastolica],
        "espessura-triceps":      [espessura_dobra_cutanea_triceps],
        "insulina":               [nivel_insulina],
        "indice-massa-corporal":  [indice_massa_corporal],
        "diabetes-pedigree":      [indice_pedigree_diabetes],
        "idade":                  [idade],
    }
    dataframe_paciente = pd.DataFrame(dicionario_dados_paciente)
    return dataframe_paciente


def calcular_risco_diabetes(modelo_preditivo, dataframe_paciente):
    """Executa a predição e retorna a probabilidade de risco e a classificação."""
    vetor_probabilidades = modelo_preditivo.predict_proba(dataframe_paciente)[0]
    percentual_risco = vetor_probabilidades[1] * 100
    classificacao_binaria = modelo_preditivo.predict(dataframe_paciente)[0]
    return percentual_risco, classificacao_binaria


def exibir_resultado_predicao(percentual_risco, classificacao_binaria):
    """Renderiza o bloco de resultado com destaque visual conforme o nível de risco."""
    if classificacao_binaria == 1:
        classe_cartao   = "resultado-alto-risco"
        icone           = "⚠️"
        cor_percentual  = "#c2410c"
        etiqueta        = "ALTO RISCO DE DIABETES GESTACIONAL"
        veredicto       = "Risco elevado identificado"
        orientacao      = (
            "O modelo indica probabilidade elevada de diabetes gestacional. "
            "Recomenda-se encaminhar a paciente para avaliação médica especializada "
            "e acompanhamento pré-natal reforçado."
        )
    else:
        classe_cartao   = "resultado-baixo-risco"
        icone           = "✅"
        cor_percentual  = "#15803d"
        etiqueta        = "BAIXO RISCO DE DIABETES GESTACIONAL"
        veredicto       = "Risco baixo identificado"
        orientacao      = (
            "O modelo indica baixa probabilidade de diabetes gestacional. "
            "Mantenha o acompanhamento pré-natal regular e repita os exames "
            "conforme orientação do médico responsável."
        )

    st.markdown(f"""
    <div class="{classe_cartao}">
        <div class="etiqueta-resultado">{etiqueta}</div>
        <div class="icone-resultado">{icone}</div>
        <div class="percentual-risco" style="color:{cor_percentual};">
            {percentual_risco:.1f}%
        </div>
        <div class="legenda-percentual">de probabilidade estimada de diabetes gestacional</div>
        <div class="veredicto">{veredicto}</div>
        <div class="orientacao">{orientacao}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="aviso-legal">
        ⚕️ Esta ferramenta é um <strong>instrumento de apoio à decisão clínica</strong> e
        não substitui a avaliação de um profissional de saúde habilitado.
        Os resultados devem ser interpretados em conjunto com o quadro clínico completo da paciente.
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# FUNÇÃO PRINCIPAL — orquestra a interface e o fluxo de predição
# ─────────────────────────────────────────────────────────────────────────────

def main():
    """Ponto de entrada da aplicação: monta a tela e coordena as interações."""

    # Aplica o CSS personalizado
    st.markdown(ESTILOS_CSS, unsafe_allow_html=True)

    # Carrega o modelo uma única vez (resultado mantido em cache pelo Streamlit)
    modelo_preditivo = carregar_modelo_preditivo()

    # Renderiza o cabeçalho da página
    exibir_cabecalho()

    # Formulário: agrupa todos os controles e só dispara o resultado ao clicar
    with st.form(key="formulario_de_predicao"):

        numero_gestacoes, idade = coletar_dados_gestacionais()

        nivel_glicose, pressao_arterial_diastolica, nivel_insulina = coletar_medicoes_clinicas()

        espessura_dobra_cutanea_triceps, indice_massa_corporal = coletar_medidas_corporais()

        indice_pedigree_diabetes = coletar_historico_familiar()

        botao_calcular_pressionado = st.form_submit_button(
            "🔍 Calcular Risco",
            use_container_width=True,
            type="primary",
        )

    # Executa a predição somente após o clique no botão
    if botao_calcular_pressionado:

        dataframe_paciente = montar_dataframe_para_predicao(
            numero_gestacoes,
            nivel_glicose,
            pressao_arterial_diastolica,
            espessura_dobra_cutanea_triceps,
            nivel_insulina,
            indice_massa_corporal,
            indice_pedigree_diabetes,
            idade,
        )

        percentual_risco, classificacao_binaria = calcular_risco_diabetes(
            modelo_preditivo,
            dataframe_paciente,
        )

        exibir_resultado_predicao(percentual_risco, classificacao_binaria)


# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
