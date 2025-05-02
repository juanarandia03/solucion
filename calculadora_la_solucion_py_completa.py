import sympy as sp
import matplotlib.pyplot as plt
from datetime import datetime

def mostrar_resultado(etiqueta, valor):
    print(f"\n{etiqueta}:")
    print("-" * len(etiqueta))
    print(valor)

def exportar_resultado(nombre, funcion, operacion, resultado, pasos):
    archivo = f"{nombre}.txt"
    with open(archivo, "w") as f:
        f.write(f"Función: {funcion}\n")
        f.write(f"Operación: {operacion}\n")
        f.write(f"Resultado: {resultado}\n\n")
        f.write("Pasos:\n")
        for p in pasos:
            f.write(f"- {p}\n")
    print(f"\n✅ Resultado guardado como: {archivo}")

def graficar(funcion, variable):
    sp.plot(funcion, (variable, -10, 10), title=f"Gráfica de {funcion}", xlabel=str(variable), ylabel="f(x)")

def main():
    x = sp.symbols('x')
    historial = []

    print("🔷 Calculadora La Solución - Consola Avanzada")
    print("Resuelve funciones, derivadas, integrales, límites y más.\n")

    while True:
        expresion = input("✏️ Ingresa una función matemática (ej: x**2 + 3*x): ")
        operacion = input("🔧 ¿Qué deseas calcular? (Evaluar / Derivada / Integral / Límite): ").strip().capitalize()

        funcion = sp.sympify(expresion)
        resultado = ""
        pasos = []

        if operacion == "Evaluar":
            valor = float(input("🔢 Ingresa el valor de x: "))
            resultado = funcion.evalf(subs={x: valor})
            pasos = [f"Se sustituyó x = {valor}", f"Resultado: {resultado}"]
        elif operacion == "Derivada":
            derivada = sp.diff(funcion, x)
            resultado = derivada
            pasos = [f"Se derivó la expresión.", f"Resultado: {resultado}"]
        elif operacion == "Integral":
            integral = sp.integrate(funcion, x)
            resultado = integral
            pasos = [f"Se integró la función.", f"Resultado: {resultado} + C"]
        elif operacion == "Límite":
            punto = float(input("📍 ¿Hacia qué valor tiende x?: "))
            limite = sp.limit(funcion, x, punto)
            resultado = limite
            pasos = [f"Se evaluó el límite cuando x → {punto}", f"Resultado: {limite}"]
        else:
            print("❌ Operación no reconocida.")
            continue

        mostrar_resultado("📊 Resultado", resultado)
        mostrar_resultado("🧾 Pasos", "\n".join(pasos))

        # Guardar en historial
        historial.append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), expresion, operacion, resultado))

        if input("\n📈 ¿Deseas ver la gráfica? (s/n): ").lower() == "s":
            graficar(funcion, x)

        if input("📄 ¿Deseas guardar los resultados? (s/n): ").lower() == "s":
            nombre_archivo = input("📁 Nombre del archivo (sin extensión): ")
            exportar_resultado(nombre_archivo, expresion, operacion, resultado, pasos)

        if input("🔁 ¿Deseas realizar otra operación? (s/n): ").lower() != "s":
            break

    print("\n🕘 Últimas operaciones realizadas:")
    for h in historial[-5:]:
        print(f"- [{h[0]}] {h[1]} → {h[2]} = {h[3]}")
    print("\nGracias por usar Calculadora La Solución ✨")

if __name__ == "__main__":
    main()