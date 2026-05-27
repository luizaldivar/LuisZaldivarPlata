from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os

app = Flask(__name__)

modelo_clima = None
columnas_entrada = [
    'Temperature (C)', 
    'Apparent Temperature (C)', 
    'Humidity', 
    'Wind Speed (km/h)', 
    'Wind Bearing (degrees)', 
    'Visibility (km)', 
    'Pressure (millibars)'
]

def obtener_recomendacion(prediccion_ingles):
    """
    Genera una recomendación en español basada en el texto de predicción en inglés.
    """
    pred_lower = prediccion_ingles.lower()
    if 'rain' in pred_lower:
        return 'Se esperan lluvias, se recomienda llevar paraguas e impermeable.'
    elif 'drizzle' in pred_lower:
        return 'Habrá llovizna, es buena idea llevar un paraguas ligero.'
    elif 'snow' in pred_lower:
        return 'Se esperan nevadas, abrígate muy bien y ten cuidado al conducir.'
    elif 'fog' in pred_lower:
        return 'Habrá niebla, maneja con precaución y enciende las luces antiniebla.'
    elif 'clear' in pred_lower:
        return 'El cielo estará despejado, ideal para actividades al aire libre.'
    elif 'cloudy' in pred_lower or 'overcast' in pred_lower:
        return 'Estará nublado, un clima fresco pero agradable.'
    else:
        return 'El clima puede ser variable, mantente atento a los cambios.'

def entrenar_modelo():
    """Lee el CSV y entrena el modelo."""
    global modelo_clima
    print("Cargando datos y entrenando el modelo...")
    try:
        csv_path = os.path.join(os.path.dirname(__file__), 'weatherHistory.csv')
        df = pd.read_csv(csv_path)

        df = df.dropna(subset=columnas_entrada + ['Daily Summary'])
        X = df[columnas_entrada]
        y = df['Daily Summary']

        modelo = RandomForestClassifier(
            n_estimators=50,
            max_depth=15, 
            random_state=42,
            class_weight='balanced',
            n_jobs=1
        )
        modelo.fit(X, y)
        modelo_clima = modelo
        print("¡Modelo entrenado exitosamente!")
    except Exception as e:
        print(f"Error al entrenar el modelo: {e}")

# Entrenamos el modelo al iniciar la aplicación
entrenar_modelo()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if modelo_clima is None:
        return jsonify({'error': 'El modelo no está entrenado. Revisa los logs del servidor.'}), 500

    try:
        datos = request.json
        # Convertir datos a float
        temp = float(datos['temp'])
        temp_ap = float(datos['temp_ap'])
        humedad = float(datos['humedad'])
        viento_vel = float(datos['viento_vel'])
        viento_dir = float(datos['viento_dir'])
        visibilidad = float(datos['visibilidad'])
        presion = float(datos['presion'])

        datos_usuario = pd.DataFrame(
            [[temp, temp_ap, humedad, viento_vel, viento_dir, visibilidad, presion]], 
            columns=columnas_entrada
        )

        resultado = modelo_clima.predict(datos_usuario)[0]
        recomendacion = obtener_recomendacion(resultado)

        return jsonify({
            'prediction': resultado,
            'recommendation': recomendacion
        })

    except ValueError:
        return jsonify({'error': 'Por favor, ingresa únicamente valores numéricos en todos los campos.'}), 400
    except KeyError as e:
        return jsonify({'error': f'Falta el campo: {e}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
