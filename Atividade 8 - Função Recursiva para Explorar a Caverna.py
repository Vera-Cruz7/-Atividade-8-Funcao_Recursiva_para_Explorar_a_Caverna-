# Função recursiva para explorar a caverna
def explorar_caverna(caverna, sala_atual, visitadas=None, tesouros_encontrados=None):
    if visitadas is None:
        visitadas = set()  # Usamos um conjunto para evitar visitar a mesma sala mais de uma vez
    if tesouros_encontrados is None:
        tesouros_encontrados = []  # Lista para armazenar as salas que contêm tesouros

    # Marcar a sala atual como visitada
    visitadas.add(sala_atual)

    # Verificar se a sala atual tem um tesouro (se o valor de 'tesouro' for True)
    if caverna[sala_atual].get("tesouro", False):  # Verifica se existe a chave 'tesouro' e se o valor é True
        tesouros_encontrados.append(sala_atual)

    # Explorar as salas conectadas à sala atual
    for sala_conectada in caverna[sala_atual]["conexoes"]:
        if sala_conectada not in visitadas:
            explorar_caverna(caverna, sala_conectada, visitadas, tesouros_encontrados)

    return tesouros_encontrados

# Exemplo de uso
caverna = {
    "Entrada": {"conexoes": ["Sala 1", "Sala 2"], "tesouro": False},
    "Sala 1": {"conexoes": ["Entrada", "Sala 3"], "tesouro": True},
    "Sala 2": {"conexoes": ["Entrada", "Sala 4"], "tesouro": False},
    "Sala 3": {"conexoes": ["Sala 1"], "tesouro": True},
    "Sala 4": {"conexoes": ["Sala 2"], "tesouro": False}
}

# Iniciar a exploração pela sala "Entrada"
tesouros = explorar_caverna(caverna, "Entrada")

# Exibir as salas que contêm tesouros
print("Salas com tesouros:", tesouros)
