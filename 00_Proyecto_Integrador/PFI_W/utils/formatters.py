

# Función para formatear como moneda ARS
def formato_moneda(valor):
    return f"${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")