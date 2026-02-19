# reporte.py - Generador de reportes (para practicar ramas en Git)
# Este archivo lo crearéis en la rama feature/nuevo-reporte

def generar_reporte(kpis, nombre_tienda="Tienda Central"):
    """Genera un reporte bonito con los KPIs."""
    ancho = 44
    print("\n" + "=" * ancho)
    print(f"{'REPORTE MENSUAL DE VENTAS':^{ancho}}")
    print(f"{'Tienda: ' + nombre_tienda:^{ancho}}")
    print("=" * ancho)
    
    for nombre, valor in kpis.items():
        nombre_formateado = nombre.replace("_", " ").title()
        print(f"  📌 {nombre_formateado}: {valor}")
    
    print("=" * ancho)
    print(f"  Total KPIs analizados: {len(kpis)}")
    print("=" * ancho + "\n")
    return True


def exportar_csv(kpis, ruta_salida="output/reporte.csv"):
    """Exporta los KPIs a CSV (simulado)."""
    print(f"💾 Exportando reporte a {ruta_salida}...")
    # Simulamos la exportación
    print("✅ Reporte exportado correctamente")
    return ruta_salida


if __name__ == "__main__":
    kpis_ejemplo = {
        "ticket_medio": 58.14,
        "frecuencia_compra": 2.87,
        "clientes_activos": 150,
        "tasa_devolucion": 5.35
    }
    generar_reporte(kpis_ejemplo, "DataLab Store")
    exportar_csv(kpis_ejemplo)
