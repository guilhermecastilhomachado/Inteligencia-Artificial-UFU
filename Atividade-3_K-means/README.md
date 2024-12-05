# **Atividade 3 - Algoritmo K-means**

Este repositório contém a implementação do algoritmo de **K-means**, aplicado à análise e agrupamento de dados. Esta atividade faz parte da disciplina de **Inteligência Artificial** no curso de **Bacharelado em Sistemas de Informação (BSI)** da **Universidade Federal de Uberlândia (UFU)**, ministrada pelo Prof. **Jefferson Rodrigo de Souza**.

---

## **Descrição da Atividade**

O algoritmo **K-means** é uma técnica de aprendizado não supervisionado utilizada para agrupar objetos semelhantes em **k** clusters distintos, minimizando a variabilidade intra-cluster e maximizando a variabilidade inter-cluster. Nesta atividade, utilizamos dados reais para:

- Normalizar e processar os dados.
- Dividir os objetos em clusters com base na distância euclidiana.
- Visualizar os agrupamentos e avaliar os resultados.

---

## **Por que usar Jupyter Notebook (.ipynb)?**

O formato **`.ipynb`** foi escolhido por ser:
- **Interativo:** Permite executar células de código individualmente, facilitando o teste e a análise de cada etapa.
- **Visualmente Rico:** Combina explicações textuais, gráficos e tabelas no mesmo documento.
- **Ideal para aprendizado:** Oferece um ambiente amigável e didático, ideal para apresentar os resultados de agrupamentos.

Para executar este notebook, é necessário ter o **Jupyter Notebook** instalado e configurado.

---

## **Destaques do Algoritmo K-means**

- **Baseado em centróides:** Cada cluster é representado por um centróide, que é recalculado iterativamente.
- **Simplicidade:** Fácil de entender e implementar.
- **Aplicações práticas:** Segmentação de clientes, agrupamento de imagens, análise de padrões, entre outros.

### **Funcionamento**
1. Seleciona-se aleatoriamente **k** centróides iniciais.
2. Cada ponto é associado ao centróide mais próximo.
3. Recalculam-se os centróides com base nos pontos atribuídos.
4. Repete-se até que os centróides não mudem significativamente.

---

## **Colaboradores Da Criação do Código**
Nesta atividade, a codificação foi feito em equipe de forma colaborativa, com um grupo formado por 8 colegas da turma, juntos, trabalhamos para 
desenvolver e implementar o algoritmo de **Busca em Largura (BFS)**. Os integrantes do grupo são:

- **Davi Mota Campos**  
- **Felipe Roza Bonetti**  
- **Guilherme Castilho Machado**  
- **Gustavo Melo do Carmo**  
- **Marcelo Prado Ribeiro**  
- **Miguel Borges de Rezende Costa**  
- **Tarick Tavares Prado Cruz**  
- **Tiago de Paula Alves**  

---

## **Detalhes do Projeto**

### **Bibliotecas Utilizadas**
- `pandas`: Manipulação de dados tabulares.
- `numpy`: Operações matemáticas eficientes.
- `matplotlib` e `seaborn`: Visualização de dados e gráficos.
- `scikit-learn`: Implementação do K-means e ferramentas de pré-processamento.

### **Como Executar**
1. Certifique-se de ter o Python 3.8+ e o Jupyter Notebook instalados.
2. Instale as bibliotecas necessárias, que estão mencionadas no código.