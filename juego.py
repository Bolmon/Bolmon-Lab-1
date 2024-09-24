import random

historia = [
    {"pregunta": "¿Cómo se les llamaba a los antiguos gobernantes de Egipto?", "opciones": {"A": "Faraones", "B": "Reyes", "C": "Emperadores", "D": "Condes"}, "respuesta correcta": "A"},
    {"pregunta": "¿Según las leyendas, quiénes fueron los fundadores de Roma?", "opciones": {"A": "César y Pompeyo", "B": "Rómulo y Remo", "C": "Alejandro y Aristóteles", "D": "Hércules y Perseo"}, "respuesta correcta": "B"},
    {"pregunta": "¿Cuál fue la primera civilización conocida?", "opciones": {"A": "Sumerios", "B": "Griegos", "C": "Romanos", "D": "Egipcios"}, "respuesta correcta": "A"},
    {"pregunta": "¿Qué imperio fue conocido por su red de caminos y sistema de correo?", "opciones": {"A": "Mongol", "B": "Bizantino", "C": "Persa", "D": "Romano"}, "respuesta correcta": "D"},
    {"pregunta": "¿Cuál de los siguientes fue un filósofo griego famoso?", "opciones": {"A": "Confucio", "B": "Sócrates", "C": "Platón", "D": "Buda"}, "respuesta correcta": "C"},
    {"pregunta": "¿En qué continente se desarrolló la civilización del antiguo Egipto?", "opciones": {"A": "África", "B": "Europa", "C": "Asia", "D": "América"}, "respuesta correcta": "A"},
    {"pregunta": "¿Qué dinastía unificó a China en el siglo III a.C?", "opciones": {"A": "Dinastía Tang", "B": "Dinastía Qin", "C": "Dinastía Ming", "D": "Dinastía Han"}, "respuesta correcta": "B"},
    {"pregunta": "¿Quién fue el líder de la India en su lucha por la independencia?", "opciones": {"A": "Jawaharlal Nehru", "B": "Mahatma Gandhi", "C": "Subhas Chandra Bose", "D": "Sardar Patel"}, "respuesta correcta": "B"},
    {"pregunta": "¿Qué civilización es famosa por sus ruinas en Machu Picchu?", "opciones": {"A": "Toltecas", "B": "Aztecas", "C": "Mayas", "D": "Incas"}, "respuesta correcta": "D"},
    {"pregunta": "¿Qué fue la ruta de la seda?", "opciones": {"A": "Un sistema de defensa", "B": "Un tratado de paz", "C": "Una ruta comercial", "D": "Un camino de peregrinación"}, "respuesta correcta": "C"}
]

ciencia = [
    {"pregunta": "¿Cuántos huesos hay en el cuerpo humano?", "opciones": {"A": "206", "B": "262", "C": "340", "D": "198"}, "respuesta correcta": "A"},
    {"pregunta": "¿Qué misión lunar Apolo fue la primera en llevar un vehículo lunar?", "opciones": {"A": "Misión Apolo 11", "B": "Misión Apolo 18", "C": "Misión Apolo 9", "D": "Misión Apolo 15"}, "respuesta correcta": "D"},
    {"pregunta": "¿A qué temperatura el agua se evapora?", "opciones": {"A": "87 Grados", "B": "100 Grados", "C": "115 Grados", "D": "70 Grados"}, "respuesta correcta": "B"},
    {"pregunta": "¿En qué planeta se encuentra la montaña volcánica Olympus Mons?", "opciones": {"A": "Júpiter", "B": "Saturno", "C": "Marte", "D": "Tierra"}, "respuesta correcta": "C"},
    {"pregunta": "¿Cuál es el proceso mediante el cual las plantas convierten la energía luminosa en energía química?", "opciones": {"A": "Fotorrecepción", "B": "Absorción", "C": "Hibernación", "D": "Fotosíntesis"}, "respuesta correcta": "D"},
    {"pregunta": "¿Cuál es el órgano más grande del cuerpo humano?", "opciones": {"A": "Piel", "B": "Intestino grueso", "C": "Intestino delgado", "D": "Cerebro"}, "respuesta correcta": "A"},
    {"pregunta": "¿Cuál es el símbolo químico del oro?", "opciones": {"A": "O", "B": "He", "C": "Au", "D": "Fe"}, "respuesta correcta": "C"},
    {"pregunta": "¿Cómo se llama el planeta más pequeño de nuestro sistema solar?", "opciones": {"A": "Tierra", "B": "Mercurio", "C": "Venus", "D": "Urano"}, "respuesta correcta": "B"},
    {"pregunta": "¿Cómo se llama el océano más grande del mundo?", "opciones": {"A": "Atlántico", "B": "Ártico", "C": "Antártico", "D": "Pacífico"}, "respuesta correcta": "D"},
    {"pregunta": "¿La Tierra gira sobre su eje una vez cada?", "opciones": {"A": "364 días", "B": "24 horas", "C": "12 horas", "D": "120 días"}, "respuesta correcta": "B"}
]

todas_preguntas = historia + ciencia

nombre = input("Bienvenido al juego. Ingresa tu nombre: ")
print(f"\nHola, {nombre} Iniciemos el juego.") 

puntuacion = 0

while todas_preguntas:

    pregunta = random.choice(todas_preguntas)

    categoria = "Historia" if pregunta in historia else "Ciencia"

    print(f"\nCategoría: {categoria}")
    print(pregunta["pregunta"])

    for opcion, texto in pregunta["opciones"].items():
        print(f"{opcion}: {texto}")

    while True:
        respuesta = input("Selecciona una opción (A, B, C, D) o presiona 'F' para salir del juego: ").upper()
        if respuesta in ['A', 'B', 'C', 'D', 'F']:
            break
        print("Opción no válida.")

    if respuesta == 'F':
        print("Juego terminado.")
        break  

    if respuesta == pregunta["respuesta correcta"]:
        print(f"Correcto")
        puntuacion += 1  
    else:
        print(f"Incorrecto")
        puntuacion 
    
    print(f"Puntuación actual: {puntuacion}")

    todas_preguntas.remove(pregunta)

if not todas_preguntas:
    print(f"\nHas respondido todas las preguntas.")
print(f"Puntuación final: {puntuacion}")