def entradas ()-> tuple: 
    capitalInicial = float(input("Capital Inicial (R$): "))
    if capitalInicial <= 0:
        print("Valor inválido. O capital inicial deve ser um número positivo.")
        return entradas()
    aportesMensais = float(input("Aporte Mensal (R$): "))
    if aportesMensais <= 0:
        print("Valor inválido. Os aportes mensais devem ser um número positivo.")
        return entradas()
    prazoInvestimento = int(input("Prazo (meses): "))
    if prazoInvestimento <= 0:
        print("Valor inválido. O prazo do investimento deve ser um número inteiro positivo.")
        return entradas()
    cdi = float(input("CDI Anual (%): "))
    if cdi <= 0:
        print("Valor inválido. A taxa do CDI deve ser um número positivo.")
        return entradas()
    
    cdiAplicadoAoCdb = float(input("Percentual CDI no CDB (%): "))
    if cdiAplicadoAoCdb <= 0:
        print("Valor inválido. A porcentagem do CDI aplicada ao CDB deve ser um número positivo.")
        return entradas()
    
    cdiAplicadoA_lciLca = float(input("Percentual CDI na LCI/LCA (%): "))
    if cdiAplicadoA_lciLca <= 0:
        print("Valor inválido. A porcentagem do CDI aplicada à LCI/LCA deve ser um número positivo.")
        return entradas()
    
    rentabilidadeMensalFII = float(input("Rentabilidade FII (%): "))
    if rentabilidadeMensalFII <= 0:
        print("Valor inválido. A rentabilidade mensal dos FIIs deve ser um número positivo.")
        return entradas()
    
    metaDesejada = float(input("Meta Financeira (R$): "))
    if metaDesejada <= 0:
        print("Valor inválido. A meta desejada deve ser um número positivo.")
        return entradas()
    
    if metaDesejada <= capitalInicial:
        print("Valor inválido. A meta desejada deve ser maior que o capital inicial.")
        return entradas()

    return capitalInicial, aportesMensais, prazoInvestimento, cdi, cdiAplicadoAoCdb, cdiAplicadoA_lciLca, rentabilidadeMensalFII, metaDesejada