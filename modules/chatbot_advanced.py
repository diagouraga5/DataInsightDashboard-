import os
from dotenv import load_dotenv
from openai import OpenAI

# -----------------------------
# CHARGEMENT DE LA CLE API
# -----------------------------
load_dotenv()  # charge le fichier .env à la racine
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Erreur : OPENAI_API_KEY non trouvé dans .env")

# Création du client OpenAI
client = OpenAI(api_key=api_key)


# -----------------------------
# FONCTION CHATBOT IA AVANCÉE
# -----------------------------
def chatbot_advanced(question, df):
    """
    question : str, question de l'utilisateur
    df : pandas.DataFrame, dataset pour l'analyse
    """
    # Limite d'affichage pour ne pas envoyer tout le dataset
    data_sample = df.head(5).to_string()

    prompt = f"""
    Tu es un expert en data science et statistiques.

    Voici un extrait du dataset :
    {data_sample}

    Question utilisateur :
    {question}

    Réponds de façon claire, structurée et professionnelle.
    Fournis des analyses, insights ou recommandations si possible.
    """

    # Requête à l'IA
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # modèle rapide et puissant
        messages=[
            {"role": "system", "content": "Tu es un expert en analyse de données."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3  # plus bas = réponses plus précises, moins créatives
    )

    return response.choices[0].message.content