
def grafico(cdb: float, lci_lca: float, poupanca: float, fii: float) -> tuple[str, str, str, str]:
    if float(cdb) > float(lci_lca) and float(cdb) > float(poupanca) and float(cdb) > float(fii):

        graficocdb = '█' * 50
        graficolci_lca = '█' * int((float(lci_lca) / float(cdb)) * 50)
        graficopoupanca = '█' * int((float(poupanca) / float(cdb)) * 50)
        graficofii = '█' * int((float(fii) / float(cdb)) * 50)

    elif float(lci_lca) > float(cdb) and float(lci_lca) > float(poupanca) and float(lci_lca) > float(fii):

        graficocdb = '█' * int((float(cdb) / float(lci_lca)) * 50)
        graficolci_lca = '█' * 50
        graficopoupanca = '█' * int((float(poupanca) / float(lci_lca)) * 50)
        graficofii = '█' * int((float(fii) / float(lci_lca)) * 50)

    elif float(poupanca) > float(cdb) and float(poupanca) > float(lci_lca) and float(poupanca) > float(fii):

        graficocdb = '█' * int((float(cdb) / float(poupanca)) * 50)
        graficolci_lca = '█' * int((float(lci_lca) / float(poupanca)) * 50)
        graficopoupanca = '█' * 50
        graficofii = '█' * int((float(fii) / float(poupanca)) * 50)

    else:

        graficocdb = '█' * int((float(cdb) / float(fii)) * 50)
        graficolci_lca = '█' * int((float(lci_lca) / float(fii)) * 50)
        graficopoupanca = '█' * int((float(poupanca) / float(fii)) * 50)
        graficofii = '█' * 50

    
    return graficocdb, graficolci_lca, graficopoupanca, graficofii
