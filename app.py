from flask import Flask, render_template 
import requests
from dotenv import load_dotenv, dotenv_values

from sqlalchemy import create_engine, Integer, MetaData, Table, Column, String

metaData=MetaData ()


#definicion de tablas
cities = Table ('Cities',metaData,
                 Column('id', Integer(), primary_key=True, autoincrement=True),
                 Column('nombre', String (100), nullable= True, unique = True)
                 )

config = dotenv_values ('.env')
app = Flask (__name__)
engine = create_engine("sqlite:///weather.db")

def get_weather_data(city):
    API_KEY = config ['API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang&appid={API_KEY}'
    r = requests.get (url).json()
    print (r)
    return r

@app.route('/prueba')
def prueba ():
    clima=get_weather_data('Quito')
    temperatura=str (clima['main']['temp'])
    descripcion= str(clima['weather'][0]['description'])
    icono= str (clima['weather'][0]['icon'])
    r_json = {
        'ciudad': 'Quito',
        'temperatura': temperatura,
        'descripcion': descripcion,
        'icono': icono
        }
    return render_template('weather.html', clima = r_json)

@app.route('/about1')
def about1():
    return render_template()

@app.route('/Caice')
def Caice ():
    get_weather_data('Guayaquil')  
    return get_weather_data('Guayaquil')

@app.route('/about')
def about ():
    return render_template('curriculum.html')

@app.route ('/clima')
def clima ():
    return'clima'

if __name__ == '__main__':
    app.run(debug=True)



