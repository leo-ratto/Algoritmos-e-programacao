from formatação import formatar_valor

def maximo(cdb: float, lci_lca: float, poupanca: float, fii: float) -> str:
    if float(cdb) > float(lci_lca) and float(cdb) > float(poupanca) and float(cdb) > float(fii):
        return f'CDB com {(formatar_valor(float(cdb)))}', (float(cdb))
    
    elif float(lci_lca) > float(cdb) and float(lci_lca) > float(poupanca) and float(lci_lca) > float(fii):
        return f'LCI/LCA com {formatar_valor(float(lci_lca))}', (float(lci_lca))
    
    elif float(poupanca) > float(cdb) and float(poupanca) > float(lci_lca) and float(poupanca) > float(fii):
        return f'Poupança com {formatar_valor(float(poupanca))}', (float(poupanca))
    
    else:
        return f'FII (Média) com {formatar_valor(float(fii))}', (float(fii))
        
