import networkx as nx
import matplotlib.pyplot as plt

def crear_red_semantica():
    G = nx.DiGraph()
    jerarquia=[
        ["Canario","Ave"],
        ["Avestruz","Ave"],
        ["Pinguino","Ave"],
        ["Ave","animal"],
        ["Mamifero","animal"],
        ["Gato","Mamifero"]
    ]

    propiedades=[
        ["Animal", "Vida", "tiene"],
        ["Ave", "Alas", "tiene"],
        ["Ave", "Plumas", "tiene"],
        ["Ave", "Volar", "puede"],
        ["Mamifero", "Pelo", "tiene"],
        ["Mamifero", "Leche", "tiene"],
        ["Canario", "Cantar", "puede"],
        ["Canario", "Amarillo", "es"],
        ["Avestruz", "Corre", "puede"],
        ["Pinguino", "Nadar", "puede"],
        ["Pinguino", "Volar", "No_puede"],
        ["Gato", "Maullar", "puede"],
    ]
    #Nodos y aristas
    for hijo, padre in jerarquia:
        G.add_edge(hijo, padre, relation="es_un")
    
    for sujeto, atributo, relacion in propiedades:
        G.add_edge(sujeto, atributo, relation=relacion)
    return G

def visualizar_red(G):
    plt.figure(figsize=(12,8))
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    #Dibujar Nodos
    nx.draw(G, pos, 
            with_labels=True, 
            node_size=3000, 
            node_color="lightblue", 
            font_size=10, 
            font_weight="bold", 
            edge_color="gray")
    #Dibujar Etiquetas
    edge_labels = nx.get_edge_attributes(G, 'relation')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title("Red Semantica: Jerarquia Animal")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    red = crear_red_semantica()
    visualizar_red(red)
    