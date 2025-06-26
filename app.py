import streamlit as st

st.title("💊 Calculadora de Dosis para Mascotas")

# Tipo de mascota
tipo_mascota = st.selectbox(
    "Selecciona el tipo de mascota:",
    options=["Perro", "Gato"]
)

# Base de datos de medicamentos
medicamentos = {
    "Mebermic Comprimido (antiparasitario amplio espectro)": {
        "especies": ["Perro", "Gato"],
        "calculo": lambda peso: peso / 10,
        "unidad": "comprimidos"
    },
    "Doximicin Comprimido": {
        "especies": ["Perro", "Gato"],
        "calculo": lambda peso: peso,
        "unidad": "comprimidos"
    },
    "Doximicin Oral (Doxiciclina Hiclato 11,08 mg)": {
        "especies": ["Perro", "Gato"],
        "calculo": lambda peso: peso,
        "unidad": "mL"
    },
    "Rostrum Comprimido": {
        "especies": ["Perro", "Gato"],
        "calculo": lambda peso: peso / 10,
        "unidad": "comprimidos"
    },
    "Rostrum Oral": {
        "especies": ["Perro"],
        "calculo": lambda peso: peso / 5,
        "unidad": "mL"
    },
    "Rostrum Oral (Gato)": {
        "especies": ["Gato"],
        "calculo": lambda peso: peso / 5,
        "unidad": "mL"
    },
    "Clindabone (tratamiento general)": {
        "especies": ["Perro", "Gato"],
        "calculo": lambda peso: 11 * peso,
        "unidad": "mg"
    },
    "Naxpet Oral (0,4%)": {
        "especies": ["Perro", "Gato"],
        "calculo": lambda peso: peso / 4,
        "unidad": "mL"
    },
    "Naxpet Oral Inyectable (1%)": {
        "especies": ["Perro", "Gato"],
        "calculo": lambda peso: 0.2 * peso,
        "unidad": "mL"
    },
    "Hemolitan": {
        "especies": ["Perro", "Gato"],
        "calculo": lambda peso: peso,
        "unidad": "gotas"
    },
    "Hemomic": {
        "especies": ["Perro", "Gato"],
        "calculo": lambda peso: peso,
        "unidad": "gotas"
    },
    # Meloxivet con dosis inicial y mantención
    "Meloxivet Oral (Perro)": {
        "especies": ["Perro"],
        "calculo_inicial": lambda peso: 0.2 * peso,
        "calculo_mantencion": lambda peso: 0.1 * peso,
        "unidad": "mL",
        "tratamiento": True
    },
    "Meloxivet Oral (Gato)": {
        "especies": ["Gato"],
        "calculo_inicial": lambda peso: 0.2 * peso,
        "calculo_mantencion": lambda peso: 0.1 * peso,
        "unidad": "mL",
        "tratamiento": True
    },
    # Invermic solo para gatos
    "Invermic (Gato)": {
        "especies": ["Gato"],
        "calculo": lambda peso: 6 * peso,
        "unidad": "gotas"
    }
}

# Mostrar solo medicamentos para la especie
meds_disponibles = [
    med for med, data in medicamentos.items() if tipo_mascota in data["especies"]
]

# Seleccionar medicamento
med_elegido = st.selectbox(
    f"Selecciona el medicamento para {tipo_mascota}:",
    options=meds_disponibles
)

# Entrada del peso
peso = st.number_input(
    f"Ingrese el peso del {tipo_mascota.lower()} (kg):",
    min_value=0.1,
    value=1.0,
    step=0.1
)

# Botón para calcular
if st.button("Calcular"):
    data = medicamentos[med_elegido]

    # Mostrar dosis
    if data.get("tratamiento"):
        dosis_inicial = data["calculo_inicial"](peso)
        dosis_mantencion = data["calculo_mantencion"](peso)
        st.success(
            f"Dosis inicial para {med_elegido}: {dosis_inicial:.2f} {data['unidad']}\n\n"
            f"Dosis de mantención para {med_elegido}: {dosis_mantencion:.2f} {data['unidad']} por 24 hrs."
        )
    else:
        dosis = data["calculo"](peso)
        st.success(
            f"Dosis para {med_elegido}: {dosis:.2f} {data['unidad']}"
        )