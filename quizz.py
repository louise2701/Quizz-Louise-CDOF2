import random

def poser_question(question, reponses_correctes, reponse_utilisateur, langage):
    print(question)
    for i, reponse in enumerate(reponses_correctes, start=1):
        print(f"{i}. {reponse}")

    try:
        if langage == "fr":
            reponse_utilisateur = int(input("Votre réponse (entrez le numéro correspondant) : "))
            if 1 <= reponse_utilisateur <= len(reponses_correctes):
                return reponses_correctes[reponse_utilisateur - 1]
            else:
                print("Veuillez entrer un numéro valide.")
                return poser_question(question, reponses_correctes, reponse_utilisateur, langage)
        elif langage == "en":
            reponse_utilisateur = int(input("Your answer (enter the corresponding number): "))
            if 1 <= reponse_utilisateur <= len(reponses_correctes):
                return reponses_correctes[reponse_utilisateur - 1]
            else:
                print("Please enter a valid number.")
                return poser_question(question, reponses_correctes, reponse_utilisateur, langage)
        elif langage == "es":
            reponse_utilisateur = int(input("Su respuesta (ingrese el número correspondiente): "))
            if 1 <= reponse_utilisateur <= len(reponses_correctes):
                return reponses_correctes[reponse_utilisateur - 1]
            else:
                print("Por favor ingrese un número válido.")
                return poser_question(question, reponses_correctes, reponse_utilisateur, langage)
    except ValueError:
        if langage == "fr":
            print("Veuillez entrer un numéro valide.")
        elif langage == "en":
            print("Please enter a valid number.")
        elif langage == "es":
            print("Por favor ingrese un número válido.")
        return poser_question(question, reponses_correctes, reponse_utilisateur, langage)

def choisir_langue():
    print("Choisissez votre langue :")
    print("1. Français")
    print("2. English")
    print("3. Español")

    try:
        langue = int(input("Votre choix (entrez le numéro correspondant) : "))
        if langue == 1:
            return "fr"
        elif langue == 2:
            return "en"
        elif langue == 3:
            return "es"
        else:
            print("Veuillez entrer un numéro valide.")
            return choisir_langue()
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        return choisir_langue()

def jouer_quiz():
    langage = choisir_langue()

    questions = {
        "fr": [
            {
                "question": "Quelle est la capitale de la France?",
                "reponses": ["Paris", "Londres", "Berlin", "Madrid"],
                "reponse_correcte": "Paris"
            },
            {
                "question": "Quel est le plus grand océan du monde?",
                "reponses": ["Atlantique", "Indien", "Pacifique", "Arctique"],
                "reponse_correcte": "Pacifique"
            },
            {
                "question": "Combien de continents y a-t-il sur Terre?",
                "reponses": ["5", "6", "7", "8"],
                "reponse_correcte": "7"
            }
        ],
        "en": [
            {
                "question": "What is the capital of France?",
                "reponses": ["Paris", "London", "Berlin", "Madrid"],
                "reponse_correcte": "Paris"
            },
            {
                "question": "What is the largest ocean in the world?",
                "reponses": ["Atlantic", "Indian", "Pacific", "Arctic"],
                "reponse_correcte": "Pacific"
            },
            {
                "question": "How many continents are there on Earth?",
                "reponses": ["5", "6", "7", "8"],
                "reponse_correcte": "7"
            }
        ],
        "es": [
            {
                "question": "¿Cuál es la capital de Francia?",
                "reponses": ["París", "Londres", "Berlín", "Madrid"],
                "reponse_correcte": "París"
            },
            {
                "question": "¿Cuál es el océano más grande del mundo?",
                "reponses": ["Atlántico", "Indio", "Pacífico", "Ártico"],
                "reponse_correcte": "Pacífico"
            },
            {
                "question": "¿Cuántos continentes hay en la Tierra?",
                "reponses": ["5", "6", "7", "8"],
                "reponse_correcte": "7"
            }
        ],
    }

    # convert the dictionary to a list of tuples
    questions_list = list(questions[langage])
    random.shuffle(questions_list)

    score = 0

    for q in questions_list:
        reponse_utilisateur = None
        reponse_correcte = poser_question(q["question"], q["reponses"], reponse_utilisateur, langage)
        
        if reponse_correcte == q["reponse_correcte"]:
            if langage == "fr":
                print("Bonne réponse!\n")
            elif langage == "en":
                print("Correct answer!\n")
            elif langage == "es":
                print("¡Respuesta correcta!\n")
            score += 1
        else:
            if langage == "fr":
                print(f"Mauvaise réponse. La réponse correcte est {q['reponse_correcte']}.\n")
            elif langage == "en":
                print(f"Wrong answer. The correct answer is {q['reponse_correcte']}.\n")
            elif langage == "es":
                print(f"Respuesta incorrecta. La respuesta correcta es {q['reponse_correcte']}.\n")

    if langage == "fr":
        print(f"Votre score final est de {score}/{len(questions)}.\n")
    elif langage == "en":
        print(f"Your final score is {score}/{len(questions)}.\n")
    elif langage == "es":
        print(f"Su puntaje final es de {score}/{len(questions)}.\n")

if __name__ == "__main__":
    jouer_quiz()