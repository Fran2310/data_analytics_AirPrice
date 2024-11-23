# AirPrice
## ¿Qué es?
El proyecto se enfoca en proporcionar analiticas respecto a datos de reservas de vuelos en las principales seis metro ciudades de la India. Se realizaron varias pruebas de hipótesis estadísticas, identificando tendencias y patrones, para obtener información significativa del mismo y dar respuestas a preguntas beneficiosas sobre precio de los boletos de avion con respecto a las demas variables observadas.

## Datos
Se tomó un set de datos de [Kaggle](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction) extraido con la herramienta de extracción de datos Octoparse para tomar datos del sitio web “Ease My Trip”. Los datos se recopilaron en dos partes: una para los billetes de clase económica y otra para los billetes de clase ejecutiva. Se extrajeron del sitio un total de 300261 opciones de reserva de vuelos distintas. Los datos se recopilaron durante 50 días, del 11 de febrero al 31 de marzo de 2022.

### Principales Ciudades
- Chennai
- Delhi
- Hyderabad
- Kolkata
- Mumbai
- Bangalore

### Principales Aerolíneas
- Vistara
- Air India
- IndiGO
- Go First
- AirAsia
- SpiceJet

# Uso

## Web

Puede ver todas las gráficas fácilmente desde la [web del proyecto](https://fran2310.github.io/data_analytics_AirPrice/web/index.html).

##  Ejecutar las gráficas de forma local
1. Primero clone el proyecto con `git clone https://github.com/Fran2310/data_analytics_AirPrice`
1. Dentro de la carpeta del proyecto genere un entorno virtual con `python -m venv venv`
2. Luego debe activar el venv como entorno ya sea desde VS Code o desde terminal con `source ./venv/bin/activate` (Ejemplo en Linux)
3. Necesita instalar las bibliotecas con `pip install -r ./environment/requirements.txt`
4. Ahora puedes ejecutar las gráficas desde el VS Code o desde la terminal con `python main.py`
5. Puede ver las gráficas resultado de la ejecución en `./visualizations/graph_img/`

# Integrantes del proyeto
- Francisco Ramos
- Joshua Carrera
- Joel Escobar
- Jesús Cabello
- Jesús Ramírez