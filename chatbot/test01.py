from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import JaccardSimilarity
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.conversation import Statement

#Descomentar estas lineas sólo la primera vez que se ejecute el algoritmo para instalar los componentes que falten.
#Luego se pueden volver a comentar

#import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')

#Creo una instancia de la clase ChatBot
chatbot = ChatBot(
    'Xpikuos',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./database.sqlite5', #fichero de la base de datos (si no existe se creará automáticamente)
    
    input_adapter='chatterbot.input.TerminalAdapter', #indica que la pregunta se toma del terminal
    output_adapter='chatterbot.output.TerminalAdapter', #indeica que la respuesta se saca por el terminal
    
    trainer='chatterbot.trainers.ListTrainer',
    
    #Un Logic_adapter es una clase que devuelve una respuesta ante una pregunta dada. 
    #Se pueden usar tantos logic_adapters como se quiera
    logic_adapters=[ 
        
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
            "response_selection_method": "chatterbot.response_selection.get_most_frequent_response"
        }
       
    ],
    
        preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    
    #read_only=True,
)

DEFAULT_SESSION_ID = chatbot.default_session
chatbot.train('chatterbot.corpus.spanish')
chatbot.train("./PreguntasYRespuestas.yml")


#Elegir la forma de medir la similitud entre dos frases
levenshtein_distance = LevenshteinDistance()


disparate=Statement('se te ha ido la pinza')#convertimos una frase en un tipo statement
entradaDelUsuario="" #variable que contendrá lo que haya escrito el usuario
entradaDelUsuarioAnterior=""

while entradaDelUsuario!="adios":
    entradaDelUsuario = chatbot.input.process_input_statement() #leemos la entrada del usuario
    statement, respuesta = chatbot.generate_response(entradaDelUsuario, DEFAULT_SESSION_ID)
    
    if levenshtein_distance.compare(entradaDelUsuario,disparate)>0.51:
        print('¿Qué debería haber dicho?')
        entradaDelUsuarioCorreccion = chatbot.input.process_input_statement()
        chatbot.train([entradaDelUsuarioAnterior.text,entradaDelUsuarioCorreccion.text])
        print("He aprendiendo que cuando digas {} debo responder {}".format(entradaDelUsuarioAnterior.text,entradaDelUsuarioCorreccion.text))
    
    entradaDelUsuarioAnterior=entradaDelUsuario
    #print(statement) #statement contiene el mismo valor que entradaDelUsuario
    print("\n%s\n\n" % respuesta)