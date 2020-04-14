def fibonacci_top_down(numero):
    if numero in memoria:
        return memoria[numero]
    f=fibonacci_iterativo_v2(numero-1)+fibonacci_iterativo_v2(numero-2)
    memoria[numero]=f
    return memoria[numero]