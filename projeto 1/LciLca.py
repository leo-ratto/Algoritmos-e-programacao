
def lci_lca(capital_inicial: float, aportes_mensais: float, prazo_investimento: int, cdiAplicadoA_lciLca: float, cdi_mensal: float) -> str:
    taxa_juros_mensal = (cdiAplicadoA_lciLca * cdi_mensal)/100
    montante = capital_inicial * (1 + taxa_juros_mensal) ** prazo_investimento + aportes_mensais * (((1 + taxa_juros_mensal) ** prazo_investimento - 1) / taxa_juros_mensal)
    return f'{montante:.2f}'
