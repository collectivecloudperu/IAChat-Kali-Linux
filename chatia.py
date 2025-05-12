import google.generativeai as genai

# Configuramos la API
API_KEY = "TU_API_KEY"

# Creamos nuestro chat
genai.configure(api_key=API_KEY)

# Crea un modelo de chat (usando Gemini)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

# Conversar con la IA en la terminal
print("Escribe 'salir' para terminar.")
while True:
    mensaje = input("Tú: ")
    if mensaje.lower() in ["salir", "exit", "quit"]:
        break

    respuesta = chat.send_message(mensaje)
    print("Gemini:", respuesta.text)
