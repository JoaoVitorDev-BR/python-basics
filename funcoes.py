# Funções em Python

# Função Simples sem parêmetros

def saudacao():
    print("Olá, tudo bem?")
saudacao()

# Função com parâmetros 
def soma(x, y):
    return x + y

resultado = soma(6, 10)
print("Rsultado da soma:", resultado)


# Função com parâmetros padrão

def apresentarnome(nome="João"):
    print("Meu nome é:", nome)
apresentarnome()
apresentarnome("Vitor")
