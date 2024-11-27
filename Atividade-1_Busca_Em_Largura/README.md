# **Atividade 1 - Busca em Largura (BFS)**

Este repositório contém a implementação do algoritmo de **Busca em Largura (BFS)**, aplicado à resolução de problemas de busca em grafos. A atividade faz parte 
da disciplina de **Inteligência Artificial** no curso de **Bacharelado em Sistemas de Informação (BSI)** da **Universidade Federal de Uberlândia (UFU)**, 
ministrada pelo Prof. **Jefferson Rodrigo de Souza**.

---

## **Descrição da Atividade**

A Busca em Largura (Breadth-First Search - BFS) é uma estratégia de busca cega ou não informada. Ela expande os nós de um grafo de forma sistemática, garantindo 
encontrar a solução mais próxima da raiz quando todos os custos das arestas são iguais. Essa implementação foi aplicada a um problema de busca de rotas entre 
os 26 estados brasileiros, considerando distâncias reais.

---

## **Destaques do Algoritmo**

- **Completude:** Garante encontrar uma solução, caso ela exista.
- **Ótima:** Retorna o menor caminho em termos de número de passos ou custo uniforme.
- **Complexidade:** Tempo \(O(b^{d+1})\), onde \(b\) é o fator de ramificação e \(d\) a profundidade da solução.

---

## **Detalhes do Projeto**

### **Funcionalidades**
- Permite encontrar rotas entre estados brasileiros, exibindo:
  - O caminho percorrido.
  - A distância total.
- Gera uma visualização gráfica do grafo, destacando a rota encontrada.

### **Bibliotecas Utilizadas**
- `networkx`: Manipulação de grafos.
- `matplotlib`: Visualização gráfica do grafo.
- `collections (deque)`: Gerenciamento eficiente da fila de estados.

### **Como Executar**
1. Certifique-se de ter o Python 3.8+ instalado.
2. Instale as bibliotecas necessárias, que estão mencionadas no código.