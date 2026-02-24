#import matplotlib #si lo uso no jala
#matplotlib.use ('Agg')
import networkx as nx
import matplotlib.pyplot as plt

def crear_red_universitaria():
    G = nx.DiGraph()
    jerarquia=[
        ("Persona","Ser_Vivo"),
        ("Estudiante","Persona"),
        ("Profesor","Persona"),
        ("Ingeniero","Persona"),
        ("MAteria","Entidad_Academica"),
        ("Aula","lugar")
    ]

    instancias=[
        ("Juan", "Estudiante"),
        ("Maria", "Estudiante"),
        ("Dr.Emmanuel", "Profesor"),
        ("Dr.Emmanuel", "Ingeniero"),
        ("IA_Basica", "Materia"),
        ("Robotica", "Materia"),
        ("Lab_Computo", "Aula")
    ]

    relaciones=[
        ("Dr.Emmanuel", "IA_Basica", "imparte"),
        ("Dr.Emmanuel", "Robotica", "imparte"),
        ("Juan", "IA_Basica", "cursa"),
        ("Maria", "Robotica", "cursa"),
        ("Maria", "IA_Basica", "cursa"),
        ("IA_Basica", "Lab_Computo", "se_imparte_en"),
        ("Robotica", "Lab_Computo", "se_imparte_en"),
        ("Alumnos", "Dr.Emmanuel", "admiran")
    ]
    #Nodos y aristas
    for hijo, padre in jerarquia:
        G.add_edge(hijo, padre, relation="ES_UN")

    for individuo, clase in instancias:
        G.add_edge(individuo, clase, relation="ES_UNA_INSTANCIA")
    
    for sujeto, objeto, accion in relaciones:
        G.add_edge(sujeto, objeto, relation=accion)
    return G

if __name__ == "__main__":
    print("Creando red semantica")
    red = crear_red_universitaria()
    plt.figure(figsize=(14,10))
    pos = nx.spring_layout(red, k=0.7, iterations=42)
    nx.draw(red, pos, with_labels=True, node_size=2500, node_color="lightgreen", font_size=9, font_weight="bold", edge_color="gray", arrowsize=15)
    edge_labels = nx.get_edge_attributes(red, 'relation')
    nx.draw_networkx_edge_labels(red, pos, edge_labels=edge_labels, font_color='blue', font_size=8)
    plt.title("Red Semantica: Iteraciones Universitaria")
    plt.axis('off')
    plt.show()  