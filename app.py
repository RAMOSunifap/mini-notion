import streamlit as st
import google.generativeai as genai

# 1. Configurar a IA
# Você vai colocar a sua chave gerada no Google AI Studio
genai.configure(api_key="SUA_CHAVE_API_AQUI")
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Interface do App
st.title("Meu Mini-Notion Inteligente 🧠")

# Área para você escrever (como se fossem os blocos do Notion)
st.subheader("Minhas Anotações")
nota = st.text_area("Escreva suas ideias, resumos de física, etc...", height=250)

# 3. Interação com a IA
st.subheader("Assistente de IA")
pergunta = st.text_input("O que você quer que a IA faça com esse texto? (Ex: Resuma, corrija, crie exercícios)")

if st.button("Gerar com IA"):
    if nota and pergunta:
        # Junta a sua nota com a instrução para a IA
        prompt = f"Aqui estão minhas anotações:\n{nota}\n\nTarefa: {pergunta}"
        
        with st.spinner("A IA está pensando..."):
            resposta = model.generate_content(prompt)
            st.success("Pronto!")
            st.write(resposta.text)
    else:
        st.warning("Escreva alguma anotação e uma instrução para a IA primeiro.")
