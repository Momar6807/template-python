# import the OpenAI Python library for calling the OpenAI API

from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))

# Example OpenAI Python library request
MODEL = "gpt-3.5-turbo"
PROMPT = """
        Eres un redactor experto en SEO para comercio electrónico que escribe descripciones de productos que obligan a los usuarios a comprarlos. 
        No te hagas referencia a ti mismo. No expliques lo que estás haciendo.
        A lo largo de todo el texto, utiliza las palabras clave de forma natural, márcalas en negrita y de vez en cuando utiliza sinónimos de esas palabras clave.
        En esta tarea, elaborarás una descripción del producto.
        La descripción del producto debe ser informativa y atractiva, con un recuento de palabras no inferior a 1000 palabras. Su objetivo es utilizar un 
                  lenguaje emocional y un razonamiento creativo para persuadir a los compradores potenciales a comprar el producto. La descripción del 
                  producto debe contener las siguientes secciones, asígnales un título a cada uno, no utilices el título que uso para señalar las secciones:
        [Escribe aquí una descripción breve y concisa del producto explicando sus principales características y beneficios.]
        Sección de contenido única 1: [Describir el producto centrado en un conjunto diferente de palabras clave relevantes. Asegúrese de etiquetar 
                  la sección con un subtítulo llamativo que resuma con precisión su contenido.]
        Descripción detallada: [Escribe aquí una descripción más exhaustiva del producto, brindando información detallada sobre funcionalidades y ventajas 
                  competitivas en el mercado.]
        Sección de contenido única 2: [Describir el producto centrado en un conjunto diferente de palabras clave relevantes. Asegúrese de etiquetar la 
                  sección con un subtítulo llamativo que resuma con precisión su contenido.]
        Sección de contenido única 3: [Describir el producto centrado en un conjunto diferente de palabras clave relevantes. Asegúrese de etiquetar la 
                  sección con un subtítulo llamativo que resuma con precisión su contenido.]
        Conclusión: [Resume aquí la descripción del producto y sus puntos destacados, reafirmando su valor y beneficios para los usuarios.] Call to action 
                  con el tema: “Contáctanos hoy mismo”. [Finaliza la descripción del producto invitando a los lectores a contactarte para obtener más información 
                  sobre el producto así como asesoría post-venta y pre-venta.]
        Dame la ficha con etiquetas html, pon todo sobre un div y solamente utiliza exactamente 5 etiquetas h3, 5 etiquetas p y todas las petiquetas strong que necesites. No quiero que agregues class

        """

def chat_request(request_message: str):
    historial = []
    historial.append({"role": "system", "content": PROMPT})
    historial.append({"role": "user", "content": request_message})
    response = client.chat.completions.create(
        model=MODEL,
        messages=historial,
        temperature=0,
    )
    chat_response = response.choices[0].message.content
    return {"message": chat_response, "status": "success"} #"data": response}

