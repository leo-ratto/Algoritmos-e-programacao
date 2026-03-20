
import locale

def formatar_valor(valor: float) -> str:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor, grouping=True)

