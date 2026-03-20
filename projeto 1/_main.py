
from funcoes import *


def main() -> None:
    print(f'\n{"=" * 20} PYINVEST {"=" * 20}')
    
    dados = entradas() 

    print(f'\n{"=" * 50}')
    print(f"""RELATÓRIO PYINVEST - {datas(dados[2])[0]}
Data estimada de resgate: {datas(dados[2])[1]}
Total investido: {formatar_valor(float(total_investido(dados[0], dados[1], dados[2])))}
{"-" * 50}"""
    )
    CDB = float(cdb(dados[0], dados[1], dados[2], dados[4], cdi_mensal(dados[3])))

    LCI_LCA = float(lci_lca(dados[0], dados[1], dados[2], dados[5], cdi_mensal(dados[3])))

    POUPANCA = float(poupanca(dados[0], dados[1], dados[2]))

    FII = float(fii(dados[0], dados[1], dados[2], dados[6],)[0])
    medianaFII = float(fii(dados[0], dados[1], dados[2], dados[6],)[1])
    desvioPadraoFII = float(fii(dados[0], dados[1], dados[2], dados[6],)[2])    

    graficos = grafico(float(CDB), float(LCI_LCA), float(POUPANCA), float(FII))

    print(f"""CDB         : {formatar_valor(CDB)}
Gráfico     : {graficos[0]}
LCI/LCA     : {formatar_valor(LCI_LCA)}
Gráfico     : {graficos[1]}
Poupança    : {formatar_valor(POUPANCA)}
Gráfico     : {graficos[2]}
FII (Média) : {formatar_valor(FII)}
Gráfico     : {graficos[3]}"""
    )

    print(f'{"-" * 50}')

    print(f"""Estatísticas FII (Mediana): {formatar_valor(medianaFII)}
Desvio Padrão FII: {formatar_valor(desvioPadraoFII)}
Meta atingida? {meta(float(dados[7]), maximo(CDB, LCI_LCA, POUPANCA, FII)[1])}"""
    )

    print(f"\nMelhor investimento: {maximo(CDB, LCI_LCA, POUPANCA, FII)[0]}\n")

if __name__ == "__main__":
    main()