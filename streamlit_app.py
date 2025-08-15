import streamlit as st
import pandas as pd
import datetime
import os
from supabase import create_client, Client

# Cargar credenciales de Supabase desde variables de entorno
SUPABASE_URL = os.environ.get('SUPABASE_URL')
SUPABASE_KEY = os.environ.get('SUPABASE_KEY')

# Verificar credenciales
if not SUPABASE_URL or not SUPABASE_KEY:
    st.error("Error: Credenciales de Supabase no configuradas. Contacta al administrador.")
    st.stop()

try:
    # Inicializar cliente Supabase
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
except Exception as e:
    st.error(f"Error al conectar con Supabase: {str(e)}")
    st.stop()

# Interfaz de la app
st.title('Registrador de Conductas Morales (MAC)')

st.write('Describe una conducta moral y califícala en los dominios de Morality as Cooperation (escala 1-5: bajo a alto respaldo).')

description = st.text_area('Descripción de la conducta:')

family = st.slider('Valores familiares: ¿Involucra asignación de recursos a kin?', 1, 5, 3)
group_loyalty = st.slider('Lealtad grupal: ¿Involucra coordinación para ventaja mutua?', 1, 5, 3)
reciprocity = st.slider('Reciprocidad: ¿Involucra intercambio social?', 1, 5, 3)
heroism = st.slider('Heroismo: ¿Involucra exhibiciones belicistas de dominancia?', 1, 5, 3)
deference = st.slider(': ¿Involucra exhibiciones conciliadoras de respeto?', 1, 5, 3)
fairness = st.slider('Equidad: ¿Involucra división de recursos disputados?', 1, 5, 3)
property = st.slider('Derechos de propiedad: ¿Involucra reconocimiento de posesión previa?', 1, 5, 3)

if st.button('Registrar Conducta'):
    if description:
        timestamp = datetime.datetime.now().isoformat()
        data = {
            "timestamp": timestamp,
            "description": description,
            "family": family,
            "group_loyalty": group_loyalty,
            "reciprocity": reciprocity,
            "heroism": heroism,
            "deference": deference,
            "fairness": fairness,
            "property": property
        }
        try:
            response = supabase.table('behaviors').insert(data).execute()
            if response.data:
                st.success('Conducta registrada exitosamente.')
            else:
                st.error(f'Error al registrar: {str(response.error)}')
        except Exception as e:
            st.error(f'Error al conectar con Supabase: {str(e)}')
    else:
        st.error('Por favor, ingresa una descripción.')

# Panel de Administrador
st.subheader('Panel de Administrador')
admin_password = st.text_input('Ingresa la contraseña de administrador:', type='password')
if admin_password == 'admin123':  # Cambia esta contraseña
    if st.button('Ver Registros'):
        try:
            response = supabase.table('behaviors').select('*').execute()
            if response.data:
                df = pd.DataFrame(response.data)
                st.dataframe(df)
            else:
                st.error(f'Error al cargar registros: {str(response.error)}')
        except Exception as e:
            st.error(f'Error al conectar con Supabase: {str(e)}')

    if st.button('Exportar a CSV'):
        try:
            response = supabase.table('behaviors').select('*').execute()
            if response.data:
                df = pd.DataFrame(response.data)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button('Descargar CSV', csv, file_name='moral_behaviors.csv')
            else:
                st.error(f'Error al exportar: {str(response.error)}')
        except Exception as e:
            st.error(f'Error al conectar con Supabase: {str(e)}')
