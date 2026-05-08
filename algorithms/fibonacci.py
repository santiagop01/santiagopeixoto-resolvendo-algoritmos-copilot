def fibonacci_posicao(n):
    """
    Retorna o n-ésimo número de Fibonacci
    Copilot: "fibonacci python com memoization"
    """
    memo = {}
    def fib(n):
        if n in memo: return memo[n]
        if n <= 1: return n
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    return fib(n)

# Teste
print(fibonacci_posicao(int(input())))