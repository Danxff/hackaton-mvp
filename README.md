# 🛡️ ThreatLens AI - Modelagem de Ameaças STRIDE com IA Generativa

Este projeto é um MVP desenvolvido para a **Fase 5 da FIAP Postech IA Para Devs**, com o objetivo de automatizar a análise de segurança e modelagem de ameaças em diagramas de arquitetura de software.

## 📖 Visão Geral da Solução
A ferramenta permite que arquitetos e engenheiros de segurança subam uma imagem de um diagrama de sistema e recebam, em segundos, uma identificação detalhada dos componentes e um relatório de riscos baseado na metodologia **STRIDE** (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, e Elevation of Privilege).

---

## ⚙️ Fluxo de Desenvolvimento e Arquitetura
Para atender aos requisitos de documentação, o fluxo da solução foi desenhado da seguinte forma:

### 1. Ingestão e Visão Computacional
O sistema utiliza o modelo **Gemini 2.5 Flash** como motor de visão multimodal. Ao contrário de modelos de detecção de objetos tradicionais (como YOLO), esta abordagem utiliza *Zero-Shot Learning*, permitindo que a IA reconheça ícones de cloud (AWS, Azure, Google Cloud) e suas interconexões sem a necessidade de um treinamento prévio exaustivo de cada novo serviço lançado pelos provedores.

### 2. Processamento e Lógica de Segurança
O fluxo de dados segue estas etapas:
- **Input:** Upload da imagem via interface Streamlit.
- **Análise:** O prompt estruturado isola os componentes e avalia o contexto (ex: se um banco de dados está em uma sub-rede pública ou privada).
- **Classificação:** Aplicação da matriz STRIDE para cada ponto crítico identificado.
- **Output:** Geração de um buffer de bytes para criação de relatório PDF técnico e acadêmico.



### 3. Estratégia de Dataset e Treinamento (Fins Acadêmicos)
Embora o MVP utilize uma API de modelo de fundação, a arquitetura foi planejada para escalabilidade:
- **Anotação:** O sistema está pronto para alimentar ferramentas de anotação (como CVAT ou Roboflow) com as imagens processadas.
- **Evolução:** As saídas validadas por especialistas humanos podem ser convertidas em um dataset proprietário para o *fine-tuning* de modelos locais (YOLOv8/v10) focado em conformidade específica de segurança.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**
- **Google Gemini 2.5 Flash** (IA Multimodal)
- **Streamlit** (Interface Web)
- **FPDF2** (Motor de PDF)
- **Pillow** (Manipulação de Imagens)

---

## 🚀 Como Executar

### 1. Pré-requisitos
Certifique-se de ter o Python instalado e uma chave de API do [Google AI Studio](https://aistudio.google.com/).

### 2. Instalação
```bash
# Clone o repositório
git clone https://github.com/Danxff/hackaton-mvp.git
```

```bash
# Crie e ative o ambiente virtual
python -m venv .venv
```

```bash
# Windows:
.\.venv\Scripts\activate
```

```bash
# Linux/Mac:
source .venv/bin/activate
```

```bash
# Instale as dependências
pip install google-generativeai streamlit fpdf2 Pillow
```

```bash
# Execução
python -m streamlit run interface.py
```

📊 Estrutura do Relatório STRIDE Gerado
O relatório final apresenta para cada componente:
| Categoria | Descrição | Exemplo de Mitigação |
| :--- | :--- | :--- |
| Spoofing | Falsificação de identidade | Implementar MFA e IAM Roles |
| Tampering | Adulteração de dados | Criptografia em repouso (AES-256) |
| Repudiation | Negar uma ação realizada | Logging centralizado no CloudWatch |
| Information Disclosure | Vazamento de informações | Uso de Subnets Privadas e NAT Gateway |
| Denial of Service | Indisponibilidade do sistema | AWS Shield e WAF Rate Limiting |
| Elevation of Privilege | Ganho de acesso indevido | Princípio do Menor Privilégio |

### 👨‍💻 Autor
Desenvolvido por Daniel Assis Silva (daniel.assis@gmail.com) como parte do projeto Fase 5 da FIAP Postech - IA Para Devs.