import os
import pandas as pd

try:
    from openai import OpenAI
except:
    OpenAI = None


def chatbot_advanced(user_input, df):
    """
    Chatbot intelligent avec fallback si pas de clé API
    """

    # 🔑 Vérifier clé API
    api_key = os.getenv("OPENAI_API_KEY")

    # 🧠 Si pas de clé → mode offline intelligent
    if not api_key or OpenAI is None:
        return offline_response(user_input, df)

    try:
        client = OpenAI(api_key=api_key)

        # Résumé des données
        data_info = f"""
        Dataset info:
        - Rows: {df.shape[0]}
        - Columns: {df.shape[1]}
        - Columns names: {list(df.columns)}
        """

        prompt = f"""
        Tu es un expert en analyse de données.

        {data_info}

        Question utilisateur :
        {user_input}

        Réponds de manière simple, claire et utile.
        """

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Expert data analyst"},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Erreur IA : {str(e)}"


# -----------------------------
# MODE OFFLINE (SANS IA)
# -----------------------------
def offline_response(user_input, df):

    user_input = user_input.lower()

    # 📊 Moyenne
    if "moyenne" in user_input:
        return df.mean(numeric_only=True).to_string()

    # 📈 corrélation
    elif "corrélation" in user_input:
        return df.corr(numeric_only=True).to_string()

    # 📊 description
    elif "statistique" in user_input or "description" in user_input:
        return df.describe().to_string()

    # 📋 colonnes
    elif "colonnes" in user_input:
        return str(list(df.columns))

    # 🔢 taille dataset
    elif "taille" in user_input or "lignes" in user_input:
        return f"{df.shape[0]} lignes et {df.shape[1]} colonnes"

    # ❓ réponse par défaut
    else:
        return "🤖 Mode offline : pose une question comme 'moyenne', 'corrélation', ou 'statistiques'"