import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="Calculadora La Solución", layout="centered")

# Imagen de fondo directa sin interpolación
st.markdown("""
    <style>
    .stApp {
        background: url("https://i.imgur.com/J4V5Xr8.png");
        background-size: cover;
        background-attachment: fixed;
    }
    .box {
        background-color: rgba(255,255,255,0.95);
        padding: 25px;
        border-radius: 15px;
        max-width: 750px;
        margin: auto;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

x = sp.symbols('x')
st.markdown("<div class='box'>", unsafe_allow_html=True)
st.title("📘 Calculadora La Solución")
st.markdown("_Funciones, derivadas, integrales y límites con pasos, gráfica e historial_")

expresion = st.text_input("✏️ Ingresa una función matemática:", placeholder="Ej: x**2 + 3*x")
operacion = st.selectbox("🔧 Operación:", ["Evaluar", "Derivada", "Integral", "Límite"])

if expresion:
    funcion = sp.sympify(expresion)
    resultado = ""
    pasos = []

    if operacion == "Evaluar":
        valor = st.number_input("🔢 ¿Qué valor tomará x?", value=1.0)
        resultado = funcion.evalf(subs={x: valor})
        pasos = [f"1️⃣ Se sustituyó x = {valor}", f"2️⃣ Resultado: {resultado}"]
    elif operacion == "Derivada":
        derivada = sp.diff(funcion, x)
        resultado = derivada
        pasos = [f"1️⃣ Derivada de {expresion} con respecto a x", f"2️⃣ Resultado: {derivada}"]
    elif operacion == "Integral":
        integral = sp.integrate(funcion, x)
        resultado = integral
        pasos = [f"1️⃣ Integral indefinida de {expresion}", f"2️⃣ Resultado: {integral} + C"]
    elif operacion == "Límite":
        punto = st.number_input("📍 ¿Hacia qué valor tiende x?", value=0.0)
        limite = sp.limit(funcion, x, punto)
        resultado = limite
        pasos = [f"1️⃣ Límite cuando x → {punto}", f"2️⃣ Resultado: {limite}"]

    st.markdown(f"<div style='background-color:#fff9c4;padding:15px;border-radius:10px;text-align:center;'><strong>📊 Resultado:</strong><br>{resultado}</div>", unsafe_allow_html=True)

    with st.expander("🧾 Ver pasos explicativos"):
        for p in pasos:
            st.markdown(p)

    with st.expander("📈 Ver gráfica de la función"):
        fig, ax = plt.subplots()
        sp.plot(funcion, (x, -10, 10), show=False, ax=ax)
        st.pyplot(fig)

    if "historial" not in st.session_state:
        st.session_state.historial = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.historial.append((timestamp, expresion, operacion, resultado))

    if st.download_button("📄 Descargar resultado", data=f"Función: {expresion}\nOperación: {operacion}\nResultado: {resultado}\n\nPasos:\n" + "\n".join(pasos), file_name="resultado.txt"):
        st.success("Archivo generado correctamente")

st.markdown("### 🕘 Historial de operaciones")
if "historial" in st.session_state and st.session_state.historial:
    for h in reversed(st.session_state.historial[-5:]):
        st.markdown(f"- **[{h[0]}]** {h[1]} → {h[2]} = `{h[3]}`")

st.markdown("</div>", unsafe_allow_html=True)