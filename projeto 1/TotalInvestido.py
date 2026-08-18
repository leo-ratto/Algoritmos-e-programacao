
def total_investido (capitalInicial: float, aportesMensais: float, meses: int) -> float:
    totalInvestido = capitalInicial + (aportesMensais * meses)
    return f'{totalInvestido:.2f}'