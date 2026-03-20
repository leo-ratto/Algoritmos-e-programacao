def cdi_mensal (cdiAnual: float) -> float:
    cdiMensal = (1 + cdiAnual/100)**(1/12) - 1
    return cdiMensal