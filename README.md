#  Moral Cooperation Behavior Logger

Esta es una demo de una aplicación web construida con Streamlit para registrar conductas morales basadas en la Teoría de Morality as Cooperation (MAC). Los datos persisten en Supabase.

## Funcionalidades
- Registro de conductas morales con calificación en 7 dominios MAC.
- Panel de administrador (contraseña protegido) para ver/exportar registros.

## Instalación Local
1. Clona: `git clone https://github.com/tu-usuario/mac-moral-behavior-logger.git`
2. Instala: `pip install -r requirements.txt`
3. Configura `.env` con:
   
   4. Ejecuta: `streamlit run streamlit_app.py`

## Despliegue en Streamlit Community Cloud
1. Ve a [share.streamlit.io](https://share.streamlit.io).
2. Selecciona repo, branch "main", archivo "streamlit_app.py".
3. En "Secrets":

   5. Deploy.

## Configuración Supabase
1. Crea proyecto en [supabase.com](https://supabase.com).
2. Ejecuta SQL en "SQL Editor":
