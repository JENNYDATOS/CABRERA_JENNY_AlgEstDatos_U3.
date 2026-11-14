
import heapq
from collections import deque


def crear_grafo():
    """Crea un grafo de ciudades con distancias en kilómetros."""
    grafo = {
        "Cuenca": {
            "Quito": 450,
            "Guayaquil": 200,
            "Loja": 210
        },
        "Quito": {
            "Cuenca": 450,
            "Ambato": 150,
            "Riobamba": 190
        },
        "Guayaquil": {
            "Cuenca": 200,
            "Machala": 180
        },
        "Loja": {
            "Cuenca": 210,
            "Machala": 230
        },
        "Ambato": {
            "Quito": 150,
            "Riobamba": 60
        },
        "Riobamba": {
            "Quito": 190,
            "Ambato": 60
        },
        "Machala": {
            "Guayaquil": 180,
            "Loja": 230
        }
    }
    return grafo


def calcular_grados(grafo):
    """Calcula el número de conexiones de cada ciudad."""
    grados = {}

    for ciudad in grafo:
        grados[ciudad] = len(grafo[ciudad])

    return grados


def bfs(grafo, inicio):
    """Realiza un recorrido BFS y calcula el número de escalas."""
    visitados = set()
    cola = deque([(inicio, 0)])
    resultados = {}

    while cola:
        ciudad, escalas = cola.popleft()

        if ciudad not in visitados:
            visitados.add(ciudad)
            resultados[ciudad] = escalas

            for vecino in grafo[ciudad]:
                if vecino not in visitados:
                    cola.append((vecino, escalas + 1))

    return resultados


def dijkstra(grafo, inicio):
    """Calcula las distancias mínimas desde una ciudad inicial."""
    distancias = {ciudad: float("inf") for ciudad in grafo}
    anteriores = {ciudad: None for ciudad in grafo}

    distancias[inicio] = 0
    cola = [(0, inicio)]

    while cola:
        distancia_actual, ciudad = heapq.heappop(cola)

        if distancia_actual > distancias[ciudad]:
            continue

        for vecino, peso in grafo[ciudad].items():
            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = ciudad

                heapq.heappush(
                    cola,
                    (nueva_distancia, vecino)
                )

    return distancias, anteriores


def reconstruir_ruta(anteriores, destino):
    """Reconstruye la ruta mínima hasta una ciudad."""
    ruta = []
    actual = destino

    while actual is not None:
        ruta.append(actual)
        actual = anteriores[actual]

    ruta.reverse()
    return ruta
