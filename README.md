# **ChatBot**
<div style="color: #2c3e50; text-align: center;">

## **Group Members:**
  
### <span style="color: #3498db;">Ilham Marzouki</span>  
### <span style="color:rgb(60, 66, 231);">Seydou Soumano</span>
### <span style="color:rgb(60, 66, 231);"> Oumaima Gaougaou </span>

</div> 

## Documentation des étapes pour créer le Chatbot avec Streamlit

### **1. Création d'un environnement virtuel :**
- **Vérifier l'installation de Python :**  
  Exécutez cette commande pour vérifier que Python est installé :
  ```bash
  python --version
  ```
  ou
  ```bash
  python3 --version
  ```

- **Vérifier l'installation de pip :**
  ```bash
  pip --version
  ```
  ou
  ```bash
  pip3 --version
  ```

- **Créer un environnement virtuel :**
  Naviguez dans votre projet et exécutez :
  ```bash
  python -m venv stenv
  ```
  ou
  ```bash
  python3 -m venv stenv
  ```

- **Activer l'environnement virtuel :**
  - Sur Windows :
    ```bash
    source stenv/Scripts/activate
    ```
  - Sur Linux/Mac :
    ```bash
    source stenv/bin/activate
    ```

- **Créer un fichier `.gitignore`** :
  Ajoutez les lignes suivantes pour ignorer l'environnement virtuel :
  ```
  # Python venv
  stenv
  ```

---

### **2. Installation des bibliothèques Python :**
1. **Créer un fichier `requirements.txt` :**
   - Ajoutez `streamlit` dans ce fichier :
     ```
     streamlit
     ```

2. **Installer les bibliothèques :**
   ```bash
   pip install -r requirements.txt
   ```

3. **Tester l'installation de Streamlit :**
   ```bash
   streamlit hello
   ```

---

### **3. Création de votre premier chatbot :**
1. **Créer une branche Git nommée `version1` :**
   ```bash
   git branch version1
   git checkout version1
   ```

2. **Créer un fichier `chatbot.py` :**
   Ajoutez le code suivant :
   ```python
   import streamlit as st

   st.title("Echo Bot")

   # Initialize chat history
   if "messages" not in st.session_state:
       st.session_state.messages = []

   # Display chat messages from history on app rerun
   for message in st.session_state.messages:
       with st.chat_message(message["role"]):
           st.markdown(message["content"])
   ```

3. **Lancer l'application :**
   ```bash
   streamlit run chatbot.py
   ```

4. **Workflow Git de base :**
   ```bash
   git add .
   git commit -m "Première version du chatbot"
   git push origin version1
   ```

5. **Fusionner avec `main` :**
   ```bash
   git checkout main
   git merge version1
   git push origin main
   ```

---

### **4. Ajout de fonctionnalités (branches Git et étapes)**

#### **Version 2 : Ajout de la réaction au message utilisateur**
1. Créer la branche `version2` :
   ```bash
   git branch version2
   git checkout version2
   ```

2. Ajouter ce code dans `chatbot.py` :
   ```python
   # React to user input
   if prompt := st.chat_input("What is up?"):
       # Display user message in chat message container
       with st.chat_message("user"):
           st.markdown(prompt)
       # Add user message to chat history
       st.session_state.messages.append({"role": "user", "content": prompt})
   ```

3. Workflow Git :
   ```bash
   git add .
   git commit -m "Ajout de la réaction au message utilisateur"
   git push origin version2
   ```

4. Fusionner avec `main` :
   ```bash
   git checkout main
   git merge version2
   git push origin main
   ```

---

#### **Version 3 : Ajout de la réponse de l'assistant**
1. Créer la branche `version3` :
   ```bash
   git branch version3
   git checkout version3
   ```

2. Ajouter ce code dans `chatbot.py` :
   ```python
   response = f"{prompt}"
   # Display assistant response in chat message container
   with st.chat_message("assistant"):
       st.markdown(response)
   # Add assistant response to chat history
   st.session_state.messages.append({"role": "assistant", "content": response})
   ```

3. Workflow Git :
   ```bash
   git add .
   git commit -m "Ajout de la réponse de l'assistant"
   git push origin version3
   ```

4. Fusionner avec `main` :
   ```bash
   git checkout main
   git merge version3
   git push origin main
   ```

---

#### **Version 4 : Construire un chatbot basé sur ChatGPT**
1. Créer la branche `version4` :
   ```bash
   git branch version4
   git checkout version4
   ```

2. Ajouter ce code dans `chatbotgpt.py` :
   ```python
   import streamlit as st
   from openai import OpenAI

   st.title("ChatGPT-like clone")

   # Set OpenAI API key from Streamlit secrets
   client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

   # Set a default model
   if "openai_model" not in st.session_state:
       st.session_state["openai_model"] = "gpt-3.5-turbo"

   # Initialize chat history
   if "messages" not in st.session_state:
       st.session_state.messages = []

   # Display chat messages from history on app rerun
   for message in st.session_state.messages:
       with st.chat_message(message["role"]):
           st.markdown(message["content"])

   # Accept user input
   if prompt := st.chat_input("What is up?"):
       # Add user message to chat history
       st.session_state.messages.append({"role": "user", "content": prompt})
       # Display user message in chat message container
       with st.chat_message("user"):
           st.markdown(prompt)
   ```

3. Workflow Git :
   ```bash
   git add .
   git commit -m "Construction du chatbot basé sur ChatGPT"
   git push origin version4
   ```

4. Fusionner avec `main` :
   ```bash
   git checkout main
   git merge version4
   git push origin main
   ```

---

#### **Version 5 : Ajout du streaming des réponses**
1. Créer la branche `version5` :
   ```bash
   git branch version5
   git checkout version5
   ```

2. Ajouter ce code dans `chatbotgpt.py` :
   ```python
   with st.chat_message("assistant"):
       stream = client.chat.completions.create(
           model=st.session_state["openai_model"],
           messages=[
               {"role": m["role"], "content": m["content"]}
               for m in st.session_state.messages
           ],
           stream=True,
           max_tokens=200,
       )
       response = st.write_stream(stream)
   st.session_state.messages.append({"role": "assistant", "content": response})
   ```

3. Workflow Git :
   ```bash
   git add .
   git commit -m "Ajout du streaming des réponses"
   git push origin version5
   ```

4. Fusionner avec `main` :
   ```bash
   git checkout main
   git merge version5
   git push origin main
   ```

---

#### **Ajout de fonctionnalités avancées :**
1. **Créer une branche pour chaque fonctionnalité :**
   - Exemple pour le `selectbox` :
     ```bash
     git branch feature-selectbox
     git checkout feature-selectbox
     ```

2. **Ajouter un `selectbox` pour choisir le modèle GPT :**
   Ajoutez ce code dans la barre latérale (sidebar) :
   ```python
   model_options = [
       "gpt-3.5-turbo",
       "gpt-3.5-turbo-instruct",
       "gpt-3.5-turbo-1106",
       "gpt-3.5-turbo-0125",
   ]
   selected_model = st.sidebar.selectbox("Choisissez un modèle GPT", model_options)
   st.session_state["openai_model"] = selected_model
   ```

3. **Ajouter un `slider` pour ajuster `max_tokens` :**
   Ajoutez ce code dans la barre latérale :
   ```python
   max_tokens = st.sidebar.slider(
       "Nombre maximum de jetons", min_value=0, max_value=500, value=200
   )
   ```






