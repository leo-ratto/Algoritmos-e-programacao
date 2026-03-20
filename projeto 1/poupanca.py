
def poupanca(capital_inicial: float, aportes_mensais: float, prazo_investimento: int) -> str:
    taxa_juros_mensal = 0.005
    montante = capital_inicial * (1 + taxa_juros_mensal) ** prazo_investimento + aportes_mensais * (((1 + taxa_juros_mensal) ** prazo_investimento - 1) / taxa_juros_mensal)
    return f'{montante:.2f}'

