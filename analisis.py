# analisis.py - Script de análisis de ventas (DataLab)
# Este archivo es para practicar Git, no hace análisis real 😄

def cargar_datos(ruta_archivo):
    """Carga los datos desde un CSV (simulado)."""
    print(f"Cargando datos desde {ruta_archivo}...")
    # Datos fake para la práctica
    datos = {
        "clientes": 150,
        "pedidos": 430,
        "revenue": 15000,
        "productos_vendidos": 890,
        "devoluciones": 23
    }
    print(f"✅ Datos cargados: {len(datos)} métricas")
    return datos


def calcular_kpis(datos):
    """Calcula los KPIs principales del negocio."""
    ticket_medio = datos["revenue"] / datos["pedidos"]
    frecuencia = datos["pedidos"] / datos["clientes"]
    tasa_devolucion = datos["devoluciones"] / datos["pedidos"] * 100
    
    kpis = {
        "ticket_medio": round(ticket_medio, 2),
        "frecuencia_compra": round(frecuencia, 2),
        "tasa_devolucion": round(tasa_devolucion, 2)
    }
    return kpis


def mostrar_resumen(kpis):
    """Muestra un resumen de los KPIs."""
    print("\n📊 RESUMEN DE KPIs")
    print("-" * 30)
    for nombre, valor in kpis.items():
        print(f"  {nombre}: {valor}")
    print("-" * 30)


if __name__ == "__main__":
    datos = cargar_datos("datos/ventas_2024.csv")
    kpis = calcular_kpis(datos)
    mostrar_resumen(kpis)
