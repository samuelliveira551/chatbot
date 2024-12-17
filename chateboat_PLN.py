'''
Desafio Natt or Not: Cria um chatbot simples que utiliza técnicas de PLN-Processamento de Linguagem Natural
- input: usuário faz perguntas.
- print: o sistema responde ao que foi perguntado.
'''

#Importa a biblioteca NLTK-Natural Language Toolkit.  

#Random: Para gerar respostas aleatórias quando necessário.
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import random

# Baixando recursos do NLTK (se necessário)
nltk.download('punkt')

# Definindo um dicionário de perguntas e respostas
perguntas_respostas = {
    'oi': ['Olá!', 'Tudo bem com você?', 'Hi there!'],
    'como vai?': ['Estou bem, obrigado(a). E você?', 'Indo bem, graças a Deus.'],
    'qual seu nome?': ['Meu nome é Chatbot.', 'Pode me chamar de Bot.'],
    'adeus': ['Até logo!', 'Foi bom conversar com você.']
}

# Função para processar a entrada do usuário
def processar_entrada(entrada):
    # Tokenizar a entrada
    palavras = word_tokenize(entrada.lower())

    # Stemming (reduzir palavras à sua raiz)
    stemmer = PorterStemmer()
    palavras_stemizadas = [stemmer.stem(palavra) for palavra in palavras]

    return palavras_stemizadas

# Função principal do chatbot
def chatbot():
    print("Olá! Sou seu chatbot. O que você quer conversar?")
    while True:
        entrada = input("> ")
        palavras_usuario = processar_entrada(entrada)

        # Verificar se a entrada corresponde a alguma pergunta chave
        for pergunta in perguntas_respostas:
            palavras_pergunta = processar_entrada(pergunta)
            if all(palavra in palavras_usuario for palavra in palavras_pergunta):
                respostas = perguntas_respostas[pergunta]
                print(random.choice(respostas))
                break
        else:
            print("Desculpe, não entendi.")

if __name__ == "__main__":
    chatbot()
