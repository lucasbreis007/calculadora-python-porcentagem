import io
import sys
from calculadora import main

# Simula as seguintes entradas do usuário:
# 1) Opção 5 (Porcentagem) -> Base: 250 -> Percentual: 20 -> Repetir: 's'
# 2) Opção 4 (Divisão)     -> Primeiro: 10 -> Segundo: 0 (Divisão por zero) -> Repetir: 's'
# 3) Opção 1 (Soma)        -> Primeiro: 'abc' (inválido) -> 15 -> Segundo: 25 -> Repetir: 'n'
entradas_simuladas = [
    # Teste 1: Porcentagem
    "5", "250", "20", "s",
    # Teste 2: Divisão por zero
    "4", "10", "0", "s",
    # Teste 3: Tratamento de erro de digitação + Soma
    "1", "abc", "15", "25", "n"
]

sys.stdin = io.StringIO("\n".join(entradas_simuladas) + "\n")

print("--- INÍCIO DA SIMULAÇÃO INTERATIVA ---")
main()
print("--- FIM DA SIMULAÇÃO INTERATIVA ---")
