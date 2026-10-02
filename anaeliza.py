import streamlit as st
import pandas as pd
import matplotlib.pyplot as pit

st.title("Painel de Operações - Expresso Mobilidade")
nome = st. text_input ("Digite seu nome:") 
if nome: 
    st.write("Ola,", nome)
# 2. Seleção de linha individual
linha = st.selectbox("Escolha uma linha:", ["510", "520", "550"])
st.write(" Linha selecionada:",linha)
# 3. Seleção de múltiplas linhas
linhas = st.multiselect("Escolha as linhas:", ["510", "520", "550", "620"])
st.write("Linhas selecionadas para relatório:", linhas)
# 4. Disparo do cálculo de frota if
if st.button("Calcular"):
    st.write("Calculando demanda e alocação de frota...")

#st.write("Olá, mundo")

# df = pd.DataFrame({
# 'first column': ["Português" , "Matemática" , "Python","Frame"],
# 'second column': [5, 9, 7, 10]
# })

# df

# st.title("Meu primeiro dash")
# st.subheader("Anna Eliza - 12402710")