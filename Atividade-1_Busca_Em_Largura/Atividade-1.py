import networkx as nx  # Importa a biblioteca NetworkX para criação e manipulação de grafos
import matplotlib.pyplot as plt  # Importa a biblioteca Matplotlib para plotar gráficos
from collections import deque  # Importa deque da biblioteca collections para criar filas de alta performance

def bfs_mapa(estradas, inicio, destino):
    visitado = set()  # Cria um conjunto para armazenar cidades visitadas
    fila = deque([([inicio], 0)])  # Cria uma fila com o estado inicial e a distância percorrida (0)

    while fila:  # Enquanto a fila não estiver vazia, continue o loop
        caminho, distancia_percorrida = fila.popleft()  # Remove o primeiro item da fila e retorna o caminho e a distância
        cidade = caminho[-1]  # Obtém a última cidade do caminho

        if cidade == destino:  # Se a cidade atual for o destino, retorna o caminho e a distância
            print("Visitando:", cidade)
            return caminho, distancia_percorrida

        if cidade not in visitado:  # Se a cidade não foi visitada ainda, marca como visitada
            visitado.add(cidade) # Adiciona a cidade ao conjunto de visitados
            print("Visitando:", cidade)
            for vizinho, distancia in estradas.get(cidade, []):  # Itera pelos vizinhos da cidade atual
                #print(vizinho+" é vizinho de "+cidade)
                novo_caminho = list(caminho)  # Cria uma cópia do caminho atual
                novo_caminho.append(vizinho)  # Adiciona o vizinho ao novo caminho
                soma_distancia = distancia_percorrida + distancia  # Atualiza a distância percorrida
                fila.append((novo_caminho, soma_distancia))  # Adiciona o novo caminho e a nova distância à fila

    return None, 0  # Se não encontrar caminho, retorna None e distância 0


def normalizar_estado(estado_input):
    # Converte a entrada para minúsculas e remove espaços extras
    estado_normalizado = estado_input.strip().lower()

    # Verifica se é uma abreviação ou nome de estado em minúsculas
    if estado_normalizado in abreviacoes_estados:
        return abreviacoes_estados[estado_normalizado]

    # Se não for abreviação, tenta capitalizar o nome corretamente
    for estado in estradas:
        if estado_normalizado == estado.lower():
            return estado

    # Se não encontrar, retorna o original para indicar erro
    return estado_input


def encontrar_rota(estradas):
    while True:  # Loop para receber o estado de início
        inicio_input = input("\nDigite o estado onde você está agora: ").strip()
        inicio = normalizar_estado(inicio_input)
        if inicio not in estradas:
            print(f"Estado de início '{inicio_input}' inválido. Por favor, tente novamente.")
        else:
            break

    while True:  # Loop para receber o estado de destino
        destino_input = input("Digite o estado para onde você quer ir: ").strip()
        destino = normalizar_estado(destino_input)
        if destino not in estradas:
            print(f"Estado de destino '{destino_input}' inválido. Por favor, tente novamente.\n")
        else:
            break

    rota, distancia_rota = bfs_mapa(estradas, inicio, destino)  # Chama a função de busca em largura (BFS)

    if rota:
        print("\nRota encontrada:", " -> ".join(rota))  # Imprime a rota encontrada
        print("Distância da rota:", distancia_rota, "km")  # Imprime a distância da rota
        desenhar_arvore(estradas, rota)  # Desenha o grafo representando o mapa e a rota encontrada
    else:
        print("\nNenhuma rota encontrada entre", inicio, "e", destino)

    while True:  # Loop para continuar ou encerrar o programa
        resposta = input("\nDigite 1 para fazer outra consulta ou 2 para encerrar o programa: ")
        if resposta == '1':
            encontrar_rota(estradas)  # Reinicia o processo de busca
            break
        elif resposta == '2':
            print("Programa encerrado.")
            print("Obrigado por usar nosso sistema de busca de rotas!")
            break
        else:
            print("Entrada inválida. Por favor, digite 1 ou 2.")


def desenhar_arvore(estradas, rota):
    G = nx.Graph()  # Cria um grafo vazio usando a biblioteca NetworkX

    # Adiciona arestas ao grafo, ignorando distâncias
    for estado, vizinhos in estradas.items():
        for vizinho, _ in vizinhos:
            G.add_edge(estado, vizinho)

    pos = nx.spring_layout(G, seed=42, k=2.5, iterations=1000)  # Define a posição dos nós no gráfico

    plt.figure(figsize=(14, 10))  # Configura o tamanho da figura do gráfico
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold',
            edge_color='gray')  # Desenha o grafo com nós e arestas

    path_edges = list(zip(rota, rota[1:]))  # Destaca as arestas que fazem parte da rota encontrada
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=4)
    nx.draw_networkx_nodes(G, pos, nodelist=rota, node_color='green', node_size=3000)

    plt.title("Árvore de Busca em Largura")  # Define o título do gráfico
    plt.show()  # Exibe o gráfico


# Mapa de estradas (estado: [(vizinho, distância)])
estradas = { # Mapa de estradas com distâncias entre estados
    'Acre': [('Amazonas', 829), ('Rondônia', 837)],
    'Alagoas': [('Bahia', 532), ('Pernambuco', 126), ('Sergipe', 233)],
    'Amapá': [('Pará', 854)],
    'Amazonas': [('Acre', 829), ('Mato Grosso', 1423), ('Pará', 1489), ('Rondônia', 933), ('Roraima', 808)],
    'Bahia': [('Alagoas', 532), ('Espírito Santo', 870), ('Goiás', 995), ('Minas Gerais', 773), ('Pernambuco', 554), ('Piauí', 401), ('Sergipe', 424), ('Tocantins', 810)],
    'Ceará': [('Paraíba', 504), ('Pernambuco', 647), ('Piauí', 528), ('Rio Grande do Norte', 418)],
    'Distrito Federal': [('Goiás', 233)],
    'Espírito Santo': [('Bahia', 870), ('Minas Gerais', 392), ('Rio de Janeiro', 694)],
    'Goiás': [('Distrito Federal', 233), ('Mato Grosso', 880), ('Mato Grosso do Sul', 1020), ('Minas Gerais', 642), ('Tocantins', 593)],
    'Maranhão': [('Pará', 794), ('Piauí', 449), ('Tocantins', 978)],
    'Mato Grosso': [('Amazonas', 1423), ('Goiás', 880), ('Mato Grosso do Sul', 927), ('Pará', 1500), ('Rondônia', 735), ('Tocantins', 902)],
    'Mato Grosso do Sul': [('Goiás', 1020), ('Minas Gerais', 1195), ('Paraná', 811), ('São Paulo', 1012), ('Mato Grosso', 927)],
    'Minas Gerais': [('Bahia', 773), ('Espírito Santo', 392), ('Goiás', 642), ('Mato Grosso do Sul', 1195), ('Rio de Janeiro', 557), ('São Paulo', 692)],
    'Pará': [('Amapá', 854), ('Amazonas', 1489), ('Maranhão', 794), ('Mato Grosso', 1500), ('Roraima', 1385), ('Tocantins', 1353)],
    'Paraíba': [('Ceará', 504), ('Pernambuco', 259), ('Rio Grande do Norte', 295)],
    'Paraná': [('Mato Grosso do Sul', 811), ('Santa Catarina', 482), ('São Paulo', 760)],
    'Pernambuco': [('Alagoas', 126), ('Bahia', 554), ('Ceará', 647), ('Paraíba', 259), ('Piauí', 686)],
    'Piauí': [('Bahia', 401), ('Ceará', 528), ('Maranhão', 449), ('Pernambuco', 686), ('Tocantins', 697)],
    'Rio de Janeiro': [('Espírito Santo', 694), ('Minas Gerais', 557), ('São Paulo', 434)],
    'Rio Grande do Norte': [('Ceará', 418), ('Paraíba', 295)],
    'Rio Grande do Sul': [('Santa Catarina', 462)],
    'Rondônia': [('Acre', 837), ('Amazonas', 933), ('Mato Grosso', 735)],
    'Roraima': [('Amazonas', 808), ('Pará', 1385)],
    'Santa Catarina': [('Paraná', 482), ('Rio Grande do Sul', 462)],
    'São Paulo': [('Mato Grosso do Sul', 1012), ('Minas Gerais', 692), ('Paraná', 760), ('Rio de Janeiro', 434)],
    'Sergipe': [('Alagoas', 233), ('Bahia', 424)],
    'Tocantins': [('Bahia', 810), ('Goiás', 593), ('Maranhão', 978), ('Mato Grosso', 902), ('Pará', 1353), ('Piauí', 697)]
}


# Mapeamento de abreviações e nomes em minúsculas para nomes completos
abreviacoes_estados = {
    'ac': 'Acre', 'al': 'Alagoas', 'ap': 'Amapá', 'am': 'Amazonas', 'ba': 'Bahia',
    'ce': 'Ceará', 'df': 'Distrito Federal', 'es': 'Espírito Santo', 'go': 'Goiás',
    'ma': 'Maranhão', 'mt': 'Mato Grosso', 'ms': 'Mato Grosso do Sul', 'mg': 'Minas Gerais',
    'pa': 'Pará', 'pb': 'Paraíba', 'pr': 'Paraná', 'pe': 'Pernambuco', 'pi': 'Piauí',
    'rj': 'Rio de Janeiro', 'rn': 'Rio Grande do Norte', 'rs': 'Rio Grande do Sul',
    'ro': 'Rondônia', 'rr': 'Roraima', 'sc': 'Santa Catarina', 'sp': 'São Paulo',
    'se': 'Sergipe', 'to': 'Tocantins'
}


print("\nBem-vindo ao sistema de busca de rotas Do Brasil!")  # Mensagem de boas-vindas
print("Aqui estão todos os 26 estados brasileiros:\n")
for estado in estradas:  # Exibe os estados disponíveis
    print(estado)


encontrar_rota(estradas)  # Executa a função principal de busca de rota