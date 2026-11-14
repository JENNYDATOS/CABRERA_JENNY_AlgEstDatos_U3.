
from utilidades import (
    crear_grafo,
    calcular_grados,
    bfs,
    dijkstra,
    reconstruir_ruta
)


def main():
    grafo = crear_grafo()
    inicio = "Cuenca"

    print("===================================")
    print(" SISTEMA DE ANALISIS DE GRAFOS")
    print("===================================")

    # R1. Mostrar el grafo y sus grados
    print("\nR1. CONEXIONES DE LAS CIUDADES")

    for ciudad, conexiones in grafo.items():
        print(f"{ciudad}: {conexiones}")

    print("\nGrado de cada ciudad:")

    grados = calcular_grados(grafo)

    for ciudad, grado in grados.items():
        print(f"{ciudad}: {grado} conexiones")

    # R2. Recorrido BFS
    print("\nR2. RECORRIDO BFS")
    print(f"Ciudad inicial: {inicio}")

    resultados_bfs = bfs(grafo, inicio)

    for ciudad, escalas in resultados_bfs.items():
        print(f"{ciudad}: {escalas} escalas")

    # R3. Algoritmo Dijkstra
    print("\nR3. DISTANCIAS MINIMAS CON DIJKSTRA")

    distancias, anteriores = dijkstra(grafo, inicio)

    for ciudad in grafo:
        ruta = reconstruir_ruta(anteriores, ciudad)

        print(f"\nDestino: {ciudad}")
        print(f"Distancia minima: {distancias[ciudad]} km")
        print("Ruta:", " -> ".join(ruta))

    # R4. Comparación BFS y Dijkstra
    print("\nR4. COMPARACION DE RESULTADOS")

    for ciudad in grafo:
        escalas = resultados_bfs[ciudad]
        distancia = distancias[ciudad]

        print(
            f"{ciudad}: {escalas} escalas, "
            f"{distancia} km de distancia minima"
        )

    print("\nCONCLUSION:")
    print(
        "El algoritmo BFS encuentra rutas con el menor "
        "numero de conexiones, mientras que Dijkstra "
        "encuentra las rutas con menor distancia."
    )


if __name__ == "__main__":
    main()
