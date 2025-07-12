from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/estado_actual")
def estado_actual():
    # Zona horaria de Tucumán
    tz = pytz.timezone("America/Argentina/Tucuman")
    ahora = datetime.now(tz)
    hora_actual = ahora.strftime("%H:%M:%S")

    # Datos del clima (actuales al momento de tu consulta)
    temperatura = "11°C"
    sensacion = "10°C"
    cielo = "Nublado ☁️"
    humedad = "96%"
    viento = "8 km/h 💨"

    return {
        "mensaje": f"""
🕒 Hora actual en San Miguel de Tucumán: {hora_actual}

🌡️ Temperatura: {temperatura} (Sensación: {sensacion})  
🌥️ Estado del cielo: {cielo}  
💧 Humedad: {humedad}  
🌬️ Viento: {viento}

🎉 ¡Tu API está más despierta que un mate a las 7 AM!  
        """
    }