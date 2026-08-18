
def cdb (capitalInicial: float, aportesMensais: float, meses: int, cdiMensal: float, cdiAplicadoAoCdb: float) -> float:
    cdbMensal = cdiMensal * cdiAplicadoAoCdb/100
    totalInvestido = capitalInicial + (aportesMensais * meses)
    montante = capitalInicial * (1 + cdbMensal)**meses + aportesMensais * (((1 + cdbMensal)**meses - 1) / cdbMensal)
    lucro = montante - totalInvestido

    if meses * 30 <= 180:
        imposto = lucro * 0.225
    elif meses * 30 <= 360:
        imposto = lucro * 0.20
    elif meses * 30 <= 720:
        imposto = lucro * 0.175
    else:
        imposto = lucro * 0.15

    valorFinalCdb = montante - imposto
    return f'{valorFinalCdb:.2f}'
