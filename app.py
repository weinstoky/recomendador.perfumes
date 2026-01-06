import streamlit as st

# ---------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------
st.set_page_config(
    page_title="Recomendador de Perfumes",
    layout="wide"
)

# ---------------------------------
# ESTILOS
# ---------------------------------
def set_background(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ---------------------------------
# TÍTULO
# ---------------------------------
st.markdown(
    "<h1 style='text-align:center;'> Recomendador de Perfumes </h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Descubre perfumes según el pH de tu piel</p>",
    unsafe_allow_html=True
)

# ---------------------------------
# SLIDER (ESTO ES CLAVE)
# ---------------------------------
ph = st.slider(
    "Selecciona tu pH de piel",
    min_value=0.0,
    max_value=14.0,
    value=5.5,
    step=0.1
)

# ---------------------------------
# LÓGICA PRINCIPAL (5 PERFUMES)
# ---------------------------------
if ph <= 4.5:
    tipo = "Fresca y Acuática"
    color = "#E3F6FF"
    perfumes = [
        ("Acqua di Gio", "Marina y limpia", "$95"),
        ("Nautica Voyage", "Acuática ligera", "$25"),
        ("L'Eau d'Issey", "Cítrica fresca", "$75"),
        ("Versace Pour Homme", "Fresca elegante", "$85"),
        ("Cool Water", "Clásica acuática", "$60"),
    ]

elif ph <= 7.5:
    tipo = "Floral y Equilibrada"
    color = "#FFF6D9"
    perfumes = [
        ("Chanel Chance Eau Tendre", "Floral elegante", "$110"),
        ("Versace Bright Crystal", "Floral fresco", "$90"),
        ("Dolce & Gabbana Light Blue", "Cítrico moderno", "$85"),
        ("Miss Dior Blooming", "Floral juvenil", "$120"),
        ("Burberry Her", "Dulce suave", "$105"),
    ]

else:
    tipo = "Cálida y Amaderada"
    color = "#FFE1E1"
    perfumes = [
        ("Tom Ford Oud Wood", "Oud sofisticado", "$250"),
        ("Dior Sauvage Elixir", "Intenso nocturno", "$160"),
        ("YSL Y EDP", "Dulce masculino", "$140"),
        ("Spicebomb Extreme", "Especiado potente", "$120"),
        ("Bleu de Chanel Parfum", "Elegante y oscuro", "$155"),
    ]

# ---------------------------------
# APLICAR FONDO
# ---------------------------------
set_background(color)

# ---------------------------------
# INFO PRINCIPAL
# ---------------------------------
st.markdown(
    f"""
    <div style='background-color:white; padding:20px; border-radius:15px; margin-bottom:20px;'>
        <h3> Tipo de fragancia recomendada</h3>
        <p><strong>{tipo}</strong></p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------
# MOSTRAR PERFUMES (5 COLUMNAS)
# ---------------------------------
st.markdown("##  Perfumes recomendados")

cols = st.columns(5)

for i, perfume in enumerate(perfumes):
    nombre, descripcion, precio = perfume
    with cols[i]:
        st.markdown(
            f"""
            <div style='background-color:white; padding:15px; border-radius:12px; text-align:center;'>
                <h4>{nombre}</h4>
                <p>{descripcion}</p>
                <p><strong>{precio}</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------------------------
# MENSAJE FINAL
# ---------------------------------
st.markdown("---")
st.markdown(
    "<h4 style='text-align:center;'> Cada piel es única. Prueba antes de comprar </h4>",
    unsafe_allow_html=True
)
