import streamlit as st

# Tabelas de categorias e variações
estilos = {
    "Estilo Rock": ["Moda Rock and Roll", "Moda Rock", "Moda Punk", "Moda Metal", "Moda Gótica"],
    "Moda Retrô": ["Moda Vintage"],
    "Casual de Negócios": [],
    "Traje para Festa": ["Festa Formal (Vestido de noite, Vestido longo)",
                         "Festa Semi-formal (Vestido de coquetel, Vestido semi-formal)",
                         "Festa Casual (Vestido de festa, Vestido preto curto)"],
    "Vestidos de Casamento": ["Casamento Formal (Vestido de noiva, Vestido de noiva formal)",
                              "Casamento Casual (Vestido de noiva casual, Vestido de noiva)"],
    "Estilo Esportivo": ["Esportivo", "Athleisure", "Roupa Ativa", "Moda de Tênis", "Moda de Rua",
                         "Casual Americano (Ameri-casual)", "Estilo ao Ar Livre", "Roupa de Yoga"],
    "Estilo ao Ar Livre": ["Roupa ao Ar Livre", "Vestuário ao Ar Livre", "Moda ao Ar Livre", "Roupa para Camping",
                           "Roupa para Caminhada", "Roupa para Pesca", "Roupa para Escalada", "Roupa para Esqui",
                           "Roupa para Snowboard"],
    "Vestuário para Casa": ["Roupa de Lazer", "Pijamas", "Roupas de Casa", "Roupa para Dormir",
                            "Roupas Confortáveis", "Roupa Relaxante"],
    "Moda de Rua": ["Moda de Rua", "Roupa de Rua", "Roupa de Rua de Alta Costura", "Moda de Skatista"],
    "Fantasias de Halloween": [],
    "Alta Costura": ["Alta Moda", "Moda", "Moda Avant-garde", "Moda Contemporânea", "Marcas de Designers"],
    "Y2K": [],
    "Kawaii": [],
    "Moda Cibernética": ["Moda Cibernética", "Techwear", "Cyberpunk", "Cybergoth", "Moda Neon"]
}

cores_cabelo = ["Loiro", "Castanho", "Preto", "Ruivo", "Colorido"]
etnias = ["Europeia", "Asiática", "Indígena", "Latina", "Negra"]
idades = ["Teen", "de 18 anos", "Adulta", "de 30 anos", "de 50 anos"]
angulos = ["Corpo inteiro", "Close", "Perfil"]

# Template do prompt em português
prompt_template = """Foto de moda de bela modelo {etnia}, {idade}, com cabelo {cor_cabelo}, usando {style}. Cena de fotografia de modelo de moda em {angulo}. Fotografado com Canon EOS R6, — ar 1:2 """

# Função para gerar prompt
def gerar_prompt(estilo, variacao, cor_cabelo, etnia, idade, angulo):
    estilo_completo = variacao if variacao else estilo
    return prompt_template.format(etnia=etnia, idade=idade, cor_cabelo=cor_cabelo, style=estilo_completo, angulo=angulo)

# Interface do Streamlit

st.image("NIDLogo.jpg")
st.write("Conheça outras aplicações do NID em www.nidlab.com.br")
st.title("Gerador de Prompts de Moda")


# Seleção de categoria de estilo
categoria = st.selectbox("Escolha a categoria de estilo", list(estilos.keys()))

# Seleção de variação (se houver)
variacoes = estilos[categoria]
variacao = st.selectbox("Escolha a variação", variacoes) if variacoes else None

# Seleção da cor do cabelo
cor_cabelo = st.selectbox("Escolha a cor do cabelo", cores_cabelo)

# Seleção da origem étnica
etnia = st.selectbox("Escolha a origem étnica da modelo", etnias)

# Seleção da idade
idade = st.selectbox("Escolha a faixa etária da modelo", idades)

# Seleção do ângulo
angulo = st.selectbox("Escolha o enquadramento", angulos)

# Geração do prompt
if st.button("Gerar Prompt"):
    prompt = gerar_prompt(categoria, variacao, cor_cabelo, etnia, idade, angulo)
    st.write("### Prompt Gerado:")
    st.code(prompt)
