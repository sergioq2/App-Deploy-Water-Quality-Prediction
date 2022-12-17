import streamlit as st
import pandas as pd
import joblib
import datetime
from PIL import Image

model = joblib.load('modelo_entrenado_vrl.pkl')

escalar = joblib.load('estandarizacion.pkl')

image = Image.open('planta.jpg')

def main():
    st.title("Prediccion de la dosis de coagulante planta San Cristobal")
    st.title('Empresas Públicas de Medellín')
    st.image(image, caption='Planta de potabilización de agua EPM')

    st.subheader("Por favor Ingrese de datos: ")

    def user_input_parameters():
        now = datetime.datetime.now()
        Year = now.year
        Mes = now.month
        control_hora = now.hour - 5
        if control_hora < 0:
            Hora = 24+control_hora
        else:
            Hora = control_hora
        Turbiedad = st.number_input(min_value=1.,max_value=2000.,step=1.,label='Ingrese la turbiedad')
        Conductividad = st.number_input(min_value=1.,max_value=2000.,step=1.,label='Ingrese la conductividad')
        Ph = st.number_input(min_value=5.,max_value=15.,step=1.,label='Ingrese el ph')
        Color = st.number_input(min_value=1.,max_value=2000.,step=1.,label='Ingrese el color')
        Caudal = st.number_input(min_value=1.,max_value=2000.,step=1.,label='Ingrese el caudal')
        data = {'Año':Year,
        'Mes':Mes,
        'Hora':Hora,
        'Turbiedad':Turbiedad,
        'Conductividad':Conductividad,
        'Ph':Ph,
        'Color':Color,
        'Caudal':Caudal}
        features = pd.DataFrame(data, index=[0])
        return features

    df = user_input_parameters()
    input_est = escalar.transform(df)

    st.subheader('Parametros ingresados por el usuario')
    st.write(df)

    if st.button('Predecir'):
        st.subheader('La dosis de coagulante a aplicar es:')
        st.success(model.predict(input_est))

if __name__=='__main__':
    main()
        