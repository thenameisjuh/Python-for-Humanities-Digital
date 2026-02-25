import string
from collections import Counter

# 1. Definir uma lista de Stopwords em Português
# Num cenário real, usaríamos a biblioteca 'nltk', mas para o exercício criei a minha própria lista
STOPWORDS_PT = [
    "a", "o", "as", "os", "de", "do", "da", "dos", "das", "em", "no", "na", 
    "nos", "nas", "e", "ou", "que", "com", "por", "para", "um", "uma", 
    "uns", "umas", "ser", "estar", "foi", "está", "tem", "haver"
]

def processar_texto_avancado(texto):
    # Código original: minúsculas e sem pontuação
    texto = texto.lower()
    tabela_pontuacao = str.maketrans('', '', string.punctuation)
    texto_limpo = texto.translate(tabela_pontuacao)
    
    # Tokenização
    palavras = texto_limpo.split()
    
    # NOVO: Filtragem de Stopwords
    palavras_filtradas = [p for p in palavras if p not in STOPWORDS_PT]
    
    # Cálculo de métricas
    frequencias = Counter(palavras_filtradas)
    
    return palavras_filtradas, frequencias

# Exemplo de uso
texto_exemplo = "A inteligência artificial está a transformar o mundo com rapidez."
palavras, freq = processar_texto_avancado(texto_exemplo)

print(f"Palavras Totais: {len(palavras)}")
print(f"Top 5 palavras com significado: {freq.most_common(5)}")
