import random

def poser_question(question, reponses_correctes, reponse_utilisateur):
    print(question)
    for i, reponse in enumerate(reponses_correctes, start=1):
        print(f"{i}. {reponse}")

    try:
        reponse_utilisateur = int(input("Votre réponse (entrez le numéro correspondant) : "))
        if 1 <= reponse_utilisateur <= len(reponses_correctes):
            return reponses_correctes[reponse_utilisateur - 1]
        else:
            print("Veuillez entrer un numéro valide.")
            return poser_question(question, reponses_correctes, reponse_utilisateur)
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        return poser_question(question, reponses_correctes, reponse_utilisateur)

def jouer_quiz():
    questions = [
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
       
    ]

    

    score = 0

    for q in questions:
        reponse_utilisateur = None
        reponse_correcte = poser_question(q["question"], q["reponses"], reponse_utilisateur)
        
        if reponse_correcte == q["reponse_correcte"]:
            print("Bonne réponse!\n")
            score += 1
        else:
            print(f"Mauvaise réponse. La réponse correcte est {q['reponse_correcte']}.\n")

    print(f"Votre score final est de {score}/{len(questions)}.")

if __name__ == "__main__":
    jouer_quiz()
