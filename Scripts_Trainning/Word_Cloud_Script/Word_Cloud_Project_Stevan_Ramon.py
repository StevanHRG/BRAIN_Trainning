# Word Cloud Project - Stevan Ramon
# Importando bibliotecas que serão utilizadas;
import re
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import wordcloud

# 1) Receber Texto como INPUT;
texto = "The indefinite article takes two forms. It’s the word a when it precedes a word that begins with a consonant. It’s the word an when it precedes a word that begins with a vowel. The indefinite article indicates that a noun refers to a general idea rather than a particular thing. For example, you might ask your friend, “Should I bring a gift to the party?” Your friend will understand that you are not asking about a specific type of gift or a specific item. “I am going to bring an apple pie,” your friend tells you. Again, the indefinite article indicates that she is not talking about a specific apple pie. Your friend probably doesn’t even have any pie yet"
# 2) Tratando o Texto: Tirando caracteres especiais, deixando todas as palavras com a inicial maiuscula e separando as palavras em uma lista;
texto = re.sub("[^a-zA-Z0-9 \\\]", "", texto).title().split()

# 3) Retirando palavras como The, if, for, a, it, That etc...
for word in texto:
    if len(word) < 4:
        texto.remove(word)
    elif word == "That":
        texto.remove(word)
    else:
        continue

print(texto)

# 4) Gerando um token para cada palavra do texto e um número de repetição da mesma palavra;
freq = FreqDist(texto)
data = dict(freq)
print(data)

cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(data)
cloud.to_file("myfile.jpg")