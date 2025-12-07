# pip install Streamlit
# python -m .venv
# python -m streamlit run final.py 


# Importamos todas las librerías necesarias
import streamlit as st # para crear la pagina web
import pandas as pd # para manejar el database de excel
import random # para el programa que elegirá películas al azar
import folium # para crear mapas interactivos
from streamlit.components.v1 import html # para insertar el mapa en el streamlit

# definimos las páginas de la barra lateral
paginas = ['Presentación', 'Recomendación', 'Juego: Ahorcado', 'Mensajito']

# st.sidebar.selectbox() devuelve texto de la opción seleccionada
pagina_seleccionada = st.sidebar.selectbox('Escoge la sección que deseas ver!', paginas)

# PÁGINA DE PRESENTACIÓN
if pagina_seleccionada == 'Presentación':

    # título principal de la página
    st.markdown("<h1 style='text-align: center; '>🎬₊⊹ DATA FILM ₊⊹🎬</h1>", unsafe_allow_html=True)

    # subtitulo de bienvenida, presentando el programa y la integrante
    st.markdown("<h3 style='text-align: center; '>¡Hola!🤗 Esto es Data Film, un proyecto desarrollado por Maria Pia Enriquez Jimenez🦕</h3>", unsafe_allow_html=True)

    # texto de bienvenida
    texto_bienvenida = """
    Bienvenid@ a mi página web, un espacio diseñado para ayudarte a descrubrir ✨nuevas películas✨ -o quizás redescubrir algunas que ya conocías👀- de manera sencilla, rápida y personalizada. ( ദ്ദി ˙ᗜ˙ )
    """
    # se usa HTML para justificar el texto y cambiar tamaño de fuente
    st.markdown(f"<div style='text-align: justify; font-size: 18px'>{texto_bienvenida}</div>", unsafe_allow_html=True)

    # párrafo explicando idea general del proyecto
    texto_1 = """
    Data Film es una plataforma interactiva creada para facilitar la elección de qué película ver. Conozco muy bien la situación de querer ver algo, pero no saber qué exactamente. Por eso se me ocurrió en un primer lugar este proyecto, el usar filtros claros y una interfaz amigable para recomendar a otros películas de un repertorio amplio según sus preferencias.
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px'>{texto_1}</div>", unsafe_allow_html=True)
    
    # creamos columnas para dividir una en texto y la otra imagen
    col1, col2 = st.columns(2)

    # texto largo que irá en la col1, explicando que diferencia a mi programa de otros
    texto_2 = """
    A diferencia de un buscador tradicional, Data Film no solo te sugiere un título, sino que:
    """
    col1.markdown(f"<div style='text-align: justify; font-size: 18px; '{texto_2}</div>", unsafe_allow_html=True)
    
    # textos más pequeños, también en la col1, que sirven como en formato de lista
    col1.markdown(f"<p style='font-size:18px;'>🌟Es una recomendación totalmente personalizada</p>", unsafe_allow_html=True)
    col1.markdown(f"<p style='font-size:18px;'>🌟Analiza lo que estás buscando</p>", unsafe_allow_html=True)
    col1.markdown(f"<p style='font-size:18px;'>🌟Te muestra una ficha descriptiva con información del título</p>", unsafe_allow_html=True)
    col1.markdown(f"<p style='font-size:18px;'>El objetivo es crear una experiencia que no solo te ayude a elegir🙂, pero que te invite a hacer nuevos descrubrimientos cinematográficos🫵🏻</p>", unsafe_allow_html=True)

    # imagen decorativa
    col2.image("pelicula.JPG", use_container_width=True)

    # frase en h3 
    st.markdown("<h3 style='text-align: center; '>≽ ^⎚ ˕ ⎚^ ≼ Data Film es, en esencia, un espacio para explorar, aprender y disfrutar del cine🍵</h3>", unsafe_allow_html=True)

    # imagen final de la sección de presnetación
    st.image("es_cine.png", width=500)

# PÁGINA DE PROGRAMA DE RECOMENDACIÓN RANDOM
elif pagina_seleccionada == 'Recomendación':

    # cargamos, definimos y leemos la base de datos excel, devolviendolo como un dataframe definido
    def cargar_peliculas():
        df_pelis = pd.read_excel('peliculas.xlsx')
        return df_pelis
    
    # cargamos la base de datos
    df_pelis = cargar_peliculas()
    
    # titulo de la sección de recomendación
    st.markdown("<h2 style='text-align: center; '>ᓚ₍ ^. .^₎ Recomendación de pelis ᓚ₍ ^. .^₎</h2>", unsafe_allow_html=True)

    # presentamos la primera pregunta, sobre la década
    # st.radio() muestra un widget de selección única, con botones circulares
    st.markdown("<h6 style='text-align: left; '>1. ¿De qué época prefieres ver hoy?</h6>", unsafe_allow_html=True)
    decada = st.radio(
        "Elige una opción",
        ("Antes del 2000", "Después del 2000")
    )

    # presentamos la segunda pregunta, sobre la plataforma de elección
    # st.selectbox es un menú desplegable
    st.markdown("<h6 style='text-align: left; '>2. ¿En qué plataforma quieres verla?</h6>", unsafe_allow_html=True)
    plataforma = st.selectbox(
        "Elige una opción",
        ("Netflix", "HBO Max", "Disney+", "Apple TV", "Prime Video")
    )
    
    # tercera pregunta, sobre el género de la película
    st.markdown("<h6 style='text-align: left; '>3. ¿Qué género te provoca ver?</h6>", unsafe_allow_html=True)
    genero = st.selectbox(
        "Elige una opción",
        ("Drama", "Comedia", "Romance", "Animación", "Terror", "Acción", "Ciencia-ficción")
    )

    # cuarta pregunta, sobre la duración de la película
    st.markdown("<h6 style='text-align: left; '>4. ¿De cuántas horas quieres que sea la peli?</h6>", unsafe_allow_html=True)
    tiempo = st.radio(
        "Elige una opción",
        ("Menos de dos horas", "Más de dos horas")
    )

    # ultima pregunta, sobre el nivel de rating
    st.markdown("<h6 style='text-align: left; '>5. ¿Qué nivel de rating prefieres?</h6>", unsafe_allow_html=True)
    rating = st.radio(
        "Elige una opción",
        ("Media", "Alta")
    )

    # copiamos el dataframe original para no modificarlo directamente
    df_filtrado = df_pelis.copy()

    # primer filtrado, por década
    if decada == "Antes del 2000":
        df_filtrado = df_filtrado[df_filtrado["Año"] < 2000]
    else:
        df_filtrado = df_filtrado[df_filtrado["Año"] >= 2000]
    
    # filtrado por plataforma
    df_filtrado = df_filtrado[df_filtrado["Plataforma"].str.lower() == plataforma.lower()]

    # filtrado por género
    df_filtrado = df_filtrado[df_filtrado["Genero_clasi"].str.lower() == genero.lower()]

    # filtrado por duración
    if tiempo == "Menos de dos horas":
        df_filtrado = df_filtrado[df_filtrado["Tiempo_clasi"] == "Menos"]
    else:
        df_filtrado = df_filtrado[df_filtrado["Tiempo_clasi"] == "Más"]

    # filtrado por nivel de rating segun IMDb
    if rating == "Media":
        df_filtrado = df_filtrado[df_filtrado["IMDb_clasi"] == "Media"]
    else:
        df_filtrado = df_filtrado[df_filtrado["IMDb_clasi"] == "Alta"]

    # función para elegir una película al azar de las que quedan después del filtrado
    def elegir_pelicula():
        # sample(1) elige una fila aleatoria y .iloc[0] la convierte en un registro
        return df_filtrado.sample(1).iloc[0]

    # creamos el botón que dispara la recomendación
    if st.button("✨Tu película es✨:"):
        if df_filtrado.empty:
            # opción por si después de todos los filtros no hay una película recomendada
            st.markdown(f"<div style='text-align: center; font-size: 20px; '>No hay películas en este repositorio que cumplan con tus filtros😢, ¡intenta con otos!</div>", unsafe_allow_html=True)
        else:
            # elegimos una película aleatoria
            peli = elegir_pelicula()

            # titulo con el nombre de la película recomendada
            st.markdown(f"<h3 style='text-align: center; '>🎬Te recomiendo: {peli['Titulo']}🎬</h3>", unsafe_allow_html=True)

            # creamos columnas para la información (col1) y la imagen de portada (col2)
            col1, col2 = st.columns (2)

            # información principal de la película, que está en el db
            col1.markdown(f"<p style='font-size:17px;'>🗓️ <b>Año 🗓️:</b> {peli['Año']}</p>", unsafe_allow_html=True)
            col1.markdown(f"<p style='font-size:17px;'>🎭 <b>Género 🎭:</b> {peli['Genero_show']}</p>", unsafe_allow_html=True)
            col1.markdown(f"<p style='font-size:17px;'>⏳ <b>Duración ⏳:</b> {peli['Tiempo_show']}</p>", unsafe_allow_html=True)
            col1.markdown(f"<p style='font-size:17px;'>⭐ <b>Rating IMDb ⭐:</b> {peli['IMDb_rating']}</p>", unsafe_allow_html=True)
            col1.markdown(f"<p style='font-size:17px;'>💻 <b>Plataforma 💻:</b> {peli['Plataforma']}</p>", unsafe_allow_html=True)
            col1.markdown(f"<p style='text-align: justify; 'font-size:18px;'>🦖<b>Sinopsis🦖:</b> {peli['Sinopsis']}</p>", unsafe_allow_html=True)
            
            # imagen de portada, usando el link que esta en el db
            col2.image(peli['Link'], use_container_width=True)

            # coordenadas de filmación, para el mapa interactivo, que están en el db
            lat = peli['Latitud']
            lon = peli['Longitud']

            # verificamos que hayan datos útiles
            if pd.notna(lat) and pd.notna(lon):
                st.markdown("<h6 style='text-align: center; '>🌍 ¿Dónde se grabó? 🌍</h6>", unsafe_allow_html=True)
                
                # creamos el mapa centrado en las coordenadas de cada película
                mapa = folium.Map(location=[lat, lon], zoom_start=4)

                # contenido del popup que aparecerá al hacer clic en el marcador
                contenido = f"""
                <b>{peli['Titulo']}</b><br>
                Plataforma: {peli['Genero_show']}<br>
                Año: {peli['Año']}
                """

                # creamos el marcador a las coordenadas y lo agregamos al mapa
                folium.Marker(
                    location=[lat,lon],
                    popup=folium.Popup(contenido, max_width=250),
                    icon=folium.Icon(color='lightgreen', icon='info-sign')
                ).add_to(mapa)

                # convertimos el mapa a HTML e integramos al streamlit
                mapa_html = mapa._repr_html_()
                html(mapa_html, height=400)
            else:
                # mensaje que bota si es que no hay información o si las coordenadas no son válidas
                st.info("No se pude encontrar la ubicación de esta peli🥺")

# PÁGINA DE JUEGO DEL AHORCADO
elif pagina_seleccionada == 'Juego: Ahorcado':

    # titulo de juego
    st.markdown("<h1 style='text-align: center; '>🐈¡Juego del Ahorcado!🐈‍⬛</h1>", unsafe_allow_html=True)

    # cargamos de nuevo la base de datos
    df_pelis = pd.read_excel('peliculas.xlsx')
    # lo filtramos solo para obtener los nombres (sin valores nulos)
    lista_peliculas = df_pelis['Titulo'].dropna().astype(str).tolist()

    # iniciamos variables del juego en st.session_state (solo la primera vez)
    if 'palabra_secreta' not in st.session_state:
        # compuatdora elige una película al azar y convertimos a minúsculas
        palabra = random.choice(lista_peliculas).lower()
        st.session_state.palabra_secreta = palabra # titulo que debe adivinar
        st.session_state.letras_adivinadas = [] # lista de letras que el usuario ya intentó
        st.session_state.intentos_maximos = 7 # número máximo de intentos fallidos
        st.session_state.intentos = 0 # contador de intentos usados
        st.session_state.juego_terminado = False # estado del juego (si se ha perdido o ganado)

    # recuperamos valores del estado actual del juego
    palabra_secreta = st.session_state.palabra_secreta
    letras_adivinadas = st.session_state.letras_adivinadas
    intentos = st.session_state.intentos
    intentos_maximos = st.session_state.intentos_maximos

    # mensaje de introducción
    st.markdown(f"<div style='text-align: center; font-size: 20px; '>🦕ྀི¡Juguemos un pequeño juego del Ahorcado con los títulos de las películas en el repositorio!🦕ྀི</div>", unsafe_allow_html=True)

    # mostramos cuantas letras tiene la palabra y cuantos intentos qudan
    st.markdown(f"<div style='text-align: justify; font-size: 18px; '>La palabra tiene {len(palabra_secreta)} letras.🫢</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: justify; font-size: 18px; '>Intentos restantes: {intentos_maximos - intentos}</div>", unsafe_allow_html=True)

    # el progreso actual de letras adivinadas y guiones bajos
    progreso = ""
    for letra in palabra_secreta:
        if letra == " ":
            # usamos una barra para indicar espacio entre palabras del titulo a adivinar
            progreso += "/ "
        elif letra in letras_adivinadas:
            # si la letra ya fue adivinada, la mostramos
            progreso += letra + " "
        else:
            # si no, ponemos guion bajo
            progreso += "_" + " "
    # mostramos progreso como subhead
    st.subheader(progreso)

    # caja de texto para ingresar letra
    intento = st.text_input("Adivina una letra: ", max_chars=1)

    # boton para ingresar palabra
    if st.button("Probar letra") and not st.session_state.juego_terminado:

        # validamos que el usuario haya puesto una letra
        if len(intento) != 1:
            st.warning("Ingresa solo 1 letra.😠")
        # validamos que no se repita la letra
        elif intento in letras_adivinadas:
            st.info("Ya intentaste esa letra.🧐")
        else:
            # agregamos la letra a la lista de letras usadas
            letras_adivinadas.append(intento)
            st.session_state.letras_adivinadas = letras_adivinadas

            # si la letra está en la palabra secreta
            if intento in palabra_secreta:
                st.success("¡Buena elección!")
            else:
                # sumamos un intento fallido
                st.session_state.intentos += 1
                intentos =  st.session_state.intentos
                st.error(f"Letra incorrecta. Te quedan {intentos_maximos - intentos} intentos.")

        # revisamos si se adivinó la palabra
        palabra_completa = True
        for letra in palabra_secreta:
            # ignoramos los espacios, pero verificamos que todas las letras estén adivinadas
            if letra != " " and letra not in letras_adivinadas:
                palabra_completa = False
                break
        
        # si todas las letras fueron adivinadas, mostramos mensaje de felicitaciones
        if palabra_completa:
            st.markdown(f"<h4 style='text-align: center; '>🤩¡Felicidades! Adivinaste la película🤩: {palabra_secreta}</h4>", unsafe_allow_html=True)
            st.session_state.juego_terminado = True

        # si se acaban los intentos, muestra mensjae de derrota
        if intentos >= intentos_maximos:
            st.markdown("<h4 style='text-align: center; '>😭¡Perdiste!😭</h4>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='text-align: center; '>Tu película era: {palabra_secreta}</h4>", unsafe_allow_html=True)
            st.session_state.juego_terminado = True
    
    # botón para volver a jugar
    if st.button("Jugar otra vez"):
        st.session_state.clear() # borramos todas las variables
        st.rerun() # recargamos a cero

# PAGINA DE MENSAJE FINAL
else:
     #titulo
    st.markdown("<h1 style='text-align: center; '>❄️Un poquito de reflexión❄️</h1>", unsafe_allow_html=True)
    
    # dos columnas principaless
    col1, col2 = st.columns(2)

    # mensaje de reflexión
    texto_final = """
    Ahora un mensajito final que quise poner para ponerme un poco sentimental (pueden saltarlo sin roche ^._.^ฅ). Bueno, termina aqui una de las experiencias que más me diviertieron de todo este semestre🐢. Cuando empezó el curso, programar me parecía tan intimidante🦈, pero poco a poco descubrí lo interesante que es decubrir todos estos comandos y soluciones, que le agarre un gran cariño^••^•. En construir esta página, el armar los filtros, etc., aunque fueron un gran dolor de cabeza, al final me hace sentir orgullosa de lo que he podido lograr😎. La verdad que espero poder seguir practicando después del semestre y quería agradecer tanto al profesor como a mi JP Luisa, que todo el semestre nos guío en esta medio complicada ruta de la programación. ᓚ₍^..^₎♡
    """
    col1.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_final}</div>", unsafe_allow_html=True)

    # imagen divertida
    col2.image("rigby.JPG", use_container_width=True)

    # mensajito de feliz navidad a quien me revise el trabajo:)
    st.markdown(f"<h3 style='text-align: center; '>*‧ ☃️‧*❆ ₊⋆¡FELIZ NAVIDAD Y AÑO NUEVO!•❅*‧🎄‧*❆ ₊⋆</h3>", unsafe_allow_html=True)

    # columnas para poder centrar la imagen
    col3, col4, col5= st.columns(3)
    col4.image("navidad.JPG", use_container_width=True)
    
    # muchas gracias por todo, fue muy divertido<3

