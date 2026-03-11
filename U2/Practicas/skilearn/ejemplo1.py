import numpy as np
from sklearn.neural_network import MLPClassifier
# --- VISUALIZACION ------
def imprimir_matriz(vector_plano, titulo):
    print(f"\n--- {titulo} ---")
    matriz = vector_plano.reshape((6, 8))
    for fila in matriz:
        print(" ".join(['■' if p == 1 else '.' for p in fila])) #219
    print("--------------------")

#--Entrenamiento--
A_ideal = np.array([
    0,0,1,1,1,1,0,0,
    0,1,0,0,0,0,1,0,
    0,1,1,1,1,1,1,0,
    0,1,0,0,0,0,1,0,
    0,1,0,0,0,0,1,0,
    0,1,0,0,0,0,1,0
])

E_ideal = np.array([
    0,1,1,1,1,1,1,0,
    0,1,0,0,0,0,0,0,
    0,1,1,1,1,1,0,0,
    0,1,0,0,0,0,0,0,
    0,1,0,0,0,0,0,0,
    0,1,1,1,1,1,1,0
])

I_ideal = np.array([
    0,0,1,1,1,1,0,0,
    0,0,0,1,1,0,0,0,
    0,0,0,1,1,0,0,0,
    0,0,0,1,1,0,0,0,
    0,0,0,1,1,0,0,0,
    0,0,1,1,1,1,0,0
])

O_ideal = np.array([
    0,0,1,1,1,1,0,0,
    0,1,0,0,0,0,1,0,
    0,1,0,0,0,0,1,0,
    0,1,0,0,0,0,1,0,
    0,1,0,0,0,0,1,0,
    0,0,1,1,1,1,0,0
])

U_ideal = np.array([
    0,1,0,0,0,0,1,0,
    0,1,0,0,0,0,1,0,
    0,1,0,0,0,0,1,0,
    0,1,0,0,0,0,1,0,
    0,1,0,0,0,0,1,0,
    0,0,1,1,1,1,0,0
])

N1_ideal = np.array([
    0,0,0,1,1,0,0,0,
    0,0,1,1,1,0,0,0,
    0,0,0,1,1,0,0,0,
    0,0,0,1,1,0,0,0,
    0,0,0,1,1,0,0,0,
    0,0,1,1,1,1,0,0
])

N2_ideal = np.array([
    0,0,1,1,1,1,0,0,
    0,1,0,0,0,0,1,0,
    0,0,0,0,0,1,0,0,
    0,0,0,1,1,0,0,0,
    0,0,1,0,0,0,0,0,
    0,1,1,1,1,1,1,0
])

N3_ideal = np.array([
    0,1,1,1,1,1,0,0,
    0,0,0,0,0,0,1,0,
    0,0,0,1,1,1,0,0,
    0,0,0,0,0,0,1,0,
    0,1,0,0,0,0,1,0,
    0,0,1,1,1,1,0,0
])

X_entrenamiento = np.array([A_ideal, E_ideal, I_ideal, O_ideal, U_ideal, N1_ideal, N2_ideal, N3_ideal])

#SKlearn
Y_entrenamiento = np.array(['A','E','I','O','U','1','2','3'])

#---Deep learning basico
print ("iniciando entrenamiento con Scikit-Learn...")


red_neuronal = MLPClassifier(
    hidden_layer_sizes=(24,),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

#Entrenamiento
red_neuronal.fit(X_entrenamiento, Y_entrenamiento)

print("entrenamiento completado en {red_neuronal.n_iter_} epocas.")
print("Errror final (Loss): {red_neuronal.loss:.4f}\n")

#prueba con ruido
matriz_ruidosa = np.array([
    0,0,1,1,1,0,0,0,
    0,1,0,0,0,0,1,0,
    0,0,0,0,0,1,0,0,
    1,0,0,1,1,0,0,0,
    0,0,1,0,0,0,0,0,
    0,1,1,1,1,0,0,0
])

imprimir_matriz(matriz_ruidosa,"Matriz de prueba")

prediccion = red_neuronal.predict([matriz_ruidosa])

probabilidades = red_neuronal.predict_proba([matriz_ruidosa])[0]
clases = red_neuronal.classes_

print("ANalisis de confianza de la red:")
for i in range (len(clases)):
    print(f"Clase'{clases[i]}': {probabilidades[i]*100:>5.2f}%")

print(f"\n RESULTADO FINAL: La red predice que es un(a)")