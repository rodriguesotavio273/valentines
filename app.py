import streamlit as st
from datetime import datetime
import random

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Nossa História ❤️",
    page_icon="❤️",
    layout="centered"
)

# Estilo CSS leve para deixar a aparência mais romântica e centralizada
st.markdown("""
    <style>
    .main {
        background-color: #fff5f7;
    }
    h1, h2, h3 {
        text-align: center;
        color: #b81d48;
    }
    .stButton>button {
        width: 100%;
        background-color: #e63946;
        color: white;
        font-size: 18px;
        border-radius: 12px;
        padding: 10px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #d62828;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. CABEÇALHO E TRILHA SONORA
# ==========================================
st.title("Para o amor da minha vida ❤️")
st.markdown("<p style='text-align: center; font-size: 18px;'>Um pedacinho da nossa história guardado para sempre.</p>", unsafe_allow_html=True)

st.subheader("🎵 Nossa Música")
# ALTERE AQUI: Cole o link do YouTube da música de vocês
st.video("https://youtu.be/kI6ywewtYkc?si=Q-7xSYB7MhZnlQvh")

st.divider()

# ==========================================
# 3. CONTADOR DE TEMPO JUNTOS
# ==========================================
st.subheader("⏳ Estamos juntos há...")

# ALTERE AQUI: Ano, Mês, Dia, Hora, Minuto do início do relacionamento
data_inicio = datetime(2026, 10, 9, 22, 23, 0) 
agora = datetime.now()
diferenca = agora - data_inicio

dias = diferenca.days
segundos_totais = diferenca.seconds
horas = segundos_totais // 3600
minutos = (segundos_totais % 3600) // 60

col1, col2, col3 = st.columns(3)
col1.metric("Dias", f"{dias} dias")
col2.metric("Horas", f"{horas} horas")
col3.metric("Minutos", f"{minutos} min")

if st.button("🔄 Atualizar cronômetro"):
    st.rerun()

st.divider()

# ==========================================
# 4. LINHA DO TEMPO E FOTOS
# ==========================================
st.subheader("📸 Nossos Momentos")

# Momento 1
col_img1, col_txt1 = st.columns([1, 1])
with col_img1:
    # ALTERE AQUI: Certifique-se de que o nome e extensão batem com a pasta fotos
    st.image("fotos/foto1.jpg", use_container_width=True)
with col_txt1:
    st.markdown("### Eu indo ver você no IFTO pela primeira vez")
    st.caption("Novembro de 2026") # ALTERE AQUI
    st.write("Foi muito bom te ver nesse dia pois você é minha presença favorita!.") # ALTERE AQUI

st.write("") # Espaçamento

# Momento 2 (Invertido para dar dinamismo visual)
col_txt2, col_img2 = st.columns([1, 1])
with col_txt2:
    st.markdown("### Você na Afya me mandando um linda foto sua! ")
    st.caption("Novembro de 2026") # ALTERE AQUI
    st.write("Amo quando você me manda fotos suas!") # ALTERE AQUI
with col_img2:
    st.image("fotos/foto2.jpg", use_container_width=True)

st.write("")

# Momento 3
col_img3, col_txt3 = st.columns([1, 1])
with col_img3:
    st.image("fotos/foto3.jpeg", use_container_width=True)
with col_txt3:
    st.markdown("### Aquele dia incrível que passamos juntos na sua casa!")
    st.caption("Novembro de 2026") # ALTERE AQUI
    st.write("Estavamos tão fofinhos!.") # ALTERE AQUI

st.divider()

# ==========================================
# 5. BOTÃO INTERATIVO DE MOTIVOS
# ==========================================
st.subheader("💌 Por que eu te amo?")
st.markdown("<p style='text-align: center;'>Clique no botão abaixo sempre que quiser lembrar de um motivo:</p>", unsafe_allow_html=True)

# ALTERE AQUI: Adicione quantos motivos quiser dentro da lista
motivos = [
    "Pelo seu sorriso que ilumina qualquer dia ruim meu.",
    "Pelo jeito que só você tem!.",
    "Porque qualquer programa simples vira o melhor rolê quando estou com você.",
    "Pelo seu abraço, que é o meu lugar favorito no mundo.",
    "Pela sua inteligência, dedicação e pelo jeito incrível que você cuida de quem ama.",
    "Porque você é especial no meu coração."
]

if st.button("✨ Sortear um motivo"):
    motivo_escolhido = random.choice(motivos)
    st.success(f"❤️ **{motivo_escolhido}**")
    st.balloons() # Solta balões na tela (ou use st.snow() para flocos)

st.divider()

# ==========================================
# 6. CARTA ABERTA
# ==========================================
st.subheader("✍️ Para Você")

# ALTERE AQUI: Escreva sua carta aberta entre as três aspas
carta = """
Meu amor,

Resolvi juntar um pouco do que eu sei fazer com o que eu sinto por você para criar esse cantinho só nosso. 

Cada foto aqui em cima representa um pedaço da felicidade que você trouxe para a minha vida. Obrigado por ser minha parceira, minha melhor amiga e por dividir seus dias comigo.

Que esse contador de dias continue crescendo por toda a nossa vida. TE AMO MUITO! ❤️

Você é a minha princesa, minha inspiração e a razão do meu sorriso todos os dias. Que possamos continuar construindo nossa história juntos, com muito amor, respeito e cumplicidade.

Com todo o meu amor,
José Otávio ❤️
"""

st.info(carta)