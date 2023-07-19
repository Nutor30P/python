import requests
from bs4 import BeautifulSoup
import smtplib

# URL del sitio web de búsqueda de vuelos
url = "https://www.turkishairlines.com/es-int/flights/booking/availability-international/?cId=41ce889c-0ad1-4689-9a45-9f8d9536da03"

# Headers para evitar el bloqueo por parte del sitio web
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

def check_flight_price():
    # Realizar la solicitud HTTP al sitio web
    response = requests.get(url, headers=headers)
    
    # Parsear el contenido HTML de la página web
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extraer los elementos relevantes de la página web
    # Puedes inspeccionar la estructura HTML del sitio web para obtener los selectores adecuados
    flight_price = soup.select(".flight-price")[0].get_text()
    
    # Convertir el precio a un número flotante (asumiendo que el precio está en formato numérico)
    flight_price = float(flight_price.replace("$", "").replace(",", ""))
    
    return flight_price

def send_notification(price):
    # Configurar el servidor SMTP para enviar correos electrónicos
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("pabueno2002@gmail.com", "Pablo3006")
    
    # Crear el mensaje del correo electrónico
    subject = "¡El precio del vuelo ha bajado!"
    body = f"El nuevo precio del vuelo es: {price}"
    message = f"Subject: {subject}\n\n{body}"
    
    # Enviar el correo electrónico
    server.sendmail("pabueno2002@gmail.com", "pabueno2002@gmail.com", message)
    
    # Cerrar la conexión con el servidor SMTP
    server.quit()

# Precio objetivo al que deseas recibir una notificación
target_price = 3500000

# Realizar un seguimiento continuo del precio del vuelo
while True:
    current_price = check_flight_price()
    
    if current_price <= target_price:
        send_notification(current_price)
        break