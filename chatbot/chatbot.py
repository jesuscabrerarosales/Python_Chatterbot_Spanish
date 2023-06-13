from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__,template_folder='template')

#banco de palabras para que aprenda el chatbot
conversation = ['hola','Hola, espero tu consulta','Que buscas?','dime el tramite',"¡Hola!",
"¿Cómo estás?",
"Muy bien gracias",
"Es bueno oír eso",
"Gracias.",
"De nada.",
'¿Cómo te llamas?', 'Me llamo Trovador',
'¿Quien te creó?',
'Jesús',"¿En que parte del menu principal solicito mi carpte de grado bachiller?",
"En carpeta de grado bachiller",
"¿Como sé de que escuela soy?",
"Dirigete al menu principal de Trilce",
"¿En que afecta agregar el recibo?",
"Podemos hacer un seguimiento",
"¿Que tipos de pagas puedo realizar?",
"Pagos desde banca movil",
"¿Es necesario completar todos los campos de Dirección?",
"Si es necesario para una mejor atencion",
"¿Que pasa si designo un dni equivocado?",
"El tramite no se hara correctamente","¿Cómo puedo obtener mi código ORCI?","Necesitas crear tu código ORCI en la pagina de orcid",
"¿Cómo puedo saber si mi documento ha sido aceptado?","Una vez que hayas subido tus archivos, en la columna de observaciones te aparecerá si el documento es el correcto o si falta validar por escuela",
"¿Qué debo hacer si no me aparece automáticamente mi código ORCI al completar la opción de estudiante?","Necesitas crear tu codigo ORCI",
"¿Qué tipo de archivos puedo subir en la segunda pestaña al subir un trabajo?","Formato PDF",
"¿Es obligatorio completar todos los campos que se indican al subir un trabajo?","Sí, es obligatorio completar todos los datos que se indican al subir un trabajo",
"¿En que tramites puedes ayudarme?","Actualmente he aprendido preguntas basicas sobre los tramites de "]

trovador = ChatBot("Trovador")
trainer = ListTrainer(trovador)
trainer.train(conversation)
trainer.train("chatterbot.corpus.spanish")

#FLASK

@app.route("/")
def home():
    return render_template("index.html")

#@app.route("/get_bot_response")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(trovador.get_response(userText))


if __name__ == "__main__":
    app.run()


