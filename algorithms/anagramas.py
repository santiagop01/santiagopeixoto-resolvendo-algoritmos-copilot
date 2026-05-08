# Desafio: Verificar se duas palavras são anagramas
# Copilot gerou 100% do código com 1 prompt!

def sao_anagramas(palavra1, palavra2):
    """
    Verifica se duas palavras são anagramas.
    Prompt Copilot: "função python que verifica anagramas ignorando maiúsculas"
    """
    return sorted(palavra1.lower()) == sorted(palavra2.lower())

# Teste
if __name__ == "__main__":
    entrada = input().split()
    resultado = sao_anagramas(entrada[0], entrada[1])
    print("Verdadeiro" if resultado else "Falso")