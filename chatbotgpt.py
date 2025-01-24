import openai
import streamlit as st

# Charger la clé API OpenAI depuis secrets.toml
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("ChatGPT Chatbot")

# Sidebar : Configuration et noms des membres
st.sidebar.header("Configuration")
st.sidebar.markdown("**Membres du groupe :**")
st.sidebar.markdown("- Seydou Soumano")
st.sidebar.markdown("- Oumaima Gaougaou")
st.sidebar.markdown("- Ilham Marzouki")

# Sélection du modèle GPT
model_options = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-instruct",
    "gpt-3.5-turbo-1106",
    "gpt-3.5-turbo-0125",
]
selected_model = st.sidebar.selectbox("Choisissez un modèle GPT", model_options)

# Slider pour définir max_tokens
max_tokens = st.sidebar.slider(
    "Nombre maximum de jetons", min_value=0, max_value=500, value=200
)

# Initialiser l'historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Bonjour ! Je suis ChatGPT. Comment puis-je vous aider aujourd'hui ?"}]

# Afficher l'historique des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Interaction utilisateur
if prompt := st.chat_input("Posez votre question :"):
    # Ajouter le message de l'utilisateur à l'historique
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Appeler l'API OpenAI pour obtenir une réponse
    with st.chat_message("assistant"):
        st.markdown("⏳ Rédaction de la réponse...")
        response = openai.ChatCompletion.create(
            model=selected_model,
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=max_tokens,
        )
        reply = response["choices"][0]["message"]["content"]
        st.markdown(reply)

    # Ajouter la réponse de l'assistant à l'historique
    st.session_state.messages.append({"role": "assistant", "content": reply})
