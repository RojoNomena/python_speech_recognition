"""
pip install speechrecognition pyttsx3 openai pyaudio
"""
"""
voix en texte
utilisation de reconnaissance vocale avec python
1)création d'un fonction écouter-parler-traiter requête
2) importation de speechrecognition dans la bibliothèque de python et pyttsx3
3) dans la fonction ecouter, on utilise recognizer et on le fait ecouter = .listen

"""
import speech_recognition as sr
import pyttsx3


def ecouter():
    """A)intialisation """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        """B)ecriture de ce que l'on veu écrire"""

        print("Dites quelque chose...")

        """ permet de le faire ecouter .listen"""
        audio = recognizer.listen(source)

    try:
        texte = recognizer.recognize_google(audio, language="fr-FR")
        print(f"Vous avez dit : {texte}")
        return texte
    except:
        return ""


def parler(texte):
    "pyttsx3 initialise les chose à dire"
    engine = pyttsx3.init()
    engine.say(texte)
    engine.runAndWait()


def traiter_requete(requete):
    requete = requete.lower()
    if "bonjour" in requete:
        return "Bonjour !"
    elif "ça va" in requete:
        return "Je vais bien, merci !"
    elif "stop" in requete:
        return "Au revoir !"
    else:
        return " "


if __name__ == "__main__":
    while True:
        requete = ecouter()
        if requete:
            reponse = traiter_requete(requete)
            parler(reponse)
            if "au revoir" in reponse.lower():
                break