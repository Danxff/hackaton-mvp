from fpdf import FPDF
import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
from datetime import date

# Configuração da página
st.set_page_config(page_title="Analisador STRIDE - Hackathon", layout="wide")

# Cabeçalho relatório
data_hoje = date.today().strftime("%d/%m/%Y")
seu_nome = "Daniel Assis Silva"

st.title("🛡️ Análise de Arquitetura com IA")
st.subheader("Detecção de Ameaças (Metodologia STRIDE)")

# Sidebar para configuração
with st.sidebar:
    api_key = st.text_input("Insira sua Gemini API Key:", type="password")
    if api_key:
        genai.configure(api_key=api_key)

upload = st.file_uploader("Suba a imagem da sua arquitetura (PNG, JPG)", type=['png', 'jpg', 'jpeg'])

if upload and api_key:
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(upload, caption="Arquitetura Enviada", use_container_width=True)
        
    with col2:
        if st.button("🚀 Analisar Vulnerabilidades"):
            with st.spinner("A IA está analisando..."):
                # 1. Gera o conteúdo com a IA
                model = genai.GenerativeModel('gemini-2.5-flash')
                img = Image.open(upload)
                
                prompt = f"""
                    Aja como um arquiteto de segurança focado na metodologia STRIDE.
                    Gere um relatório técnico com os seguintes metadados no início:
                    **Data:** {data_hoje}
                    **Autor:** {seu_nome}

                    Instruções de conteúdo:
                    1. Identificação dos Componentes: Liste o que encontrou na imagem.
                    2. Análise STRIDE: Para cada componente, aponte a ameaça.
                    3. Mitigação: Como resolver cada problema.

                    Use um tom profissional e acadêmico.
                    """
                response = model.generate_content([prompt, img])
                texto_relatorio = response.text
                
                st.markdown("### 📄 Relatório Gerado")
                st.write(texto_relatorio)

                # 2. Lógica para criar o PDF em memória
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)

                # 2. Limpa o texto (removendo caracteres que o PDF básico não entende)
                texto_pdf = response.text.replace("**", "").replace("#", "")

                # 3. Escreve o conteúdo
                # Usamos 'latin-1' ou 'utf-8' dependendo da versão, mas 'latin-1' com ignore é mais seguro para FPDF
                pdf.multi_cell(0, 10, txt=texto_pdf.encode('latin-1', 'ignore').decode('latin-1'))

                # 4. A MÁGICA: Gerar os bytes corretamente para o Streamlit
                pdf_output = pdf.output() # No fpdf2, output() sem parâmetros retorna bytes ou bytearray

                # Converter bytearray para bytes (isso resolve o erro de Invalid binary data format)
                pdf_bytes = bytes(pdf_output)

                # 5. O Botão de Download
                st.download_button(
                    label="📥 Baixar Relatório em PDF",
                    data=pdf_bytes,
                    file_name="Relatorio_STRIDE_Hackathon.pdf",
                    mime="application/pdf"
                )
elif not api_key:
    st.info("Por favor, insira sua API Key no menu lateral para começar.")