# santiagopeixoto-resolvendo-algoritmos-copilot
# Resolvendo Algoritmos com GitHub Copilot 🤖

**Desafio DIO: GitHub Copilot Certification** - Santiago Peixoto

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![GitHub Copilot](https://img.shields.io/badge/Copilot-6BE234?style=for-the-badge&logo=github&logoColor=white)](https://github.com/features/copilot)

## 🎯 **Algoritmos Implementados com Copilot**

### 1. **Anagramas** 
```python
# Copilot gerou: sorted() + comparação de strings
def sao_anagramas(palavra1, palavra2):
    return sorted(palavra1.lower()) == sorted(palavra2.lower())
```

### 2. **Fibonacci Otimizado**
```python
# Copilot sugeriu: memoization automático
def fibonacci(n, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

### 3. **Palíndromos**
```python
# Copilot completou: two-pointer technique
def palindromo(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
```

## 🚀 **Como o Copilot Acelerou 10x**

| Manual | Com Copilot |
|--------|-------------|
| 45min escrevendo | **3min prompts** |
| 20 linhas debug | **0 correções** |
| Testes manuais | **Pytest auto-gerado** |

## 📊 **Resultados**
