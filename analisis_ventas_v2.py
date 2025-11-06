import pandas as pd

def main(umbral_bajo=500):
    archivo = 'ventas.txt'

    try:
        data = pd.read_csv(archivo, delimiter='|')

        if 'Fecha' not in data.columns or 'Monto' not in data.columns:
            print("ERROR: El archivo debe contener las columnas 'Fecha' y 'Monto'.")

            return

        ventas_por_dia = data.groupby('Fecha')['Monto'].sum().reset_index()
        dias_bajos = ventas_por_dia[ventas_por_dia['Monto'] < umbral_bajo]

        if dias_bajos.empty:
            print(f"No hay días con ventas menores a S/ {umbral_bajo}.")
        else:
            print(f"Días con ventas bajas (menos de S/ {umbral_bajo}):")
            for index, row in dias_bajos.iterrows():
                print(f"- {row['Fecha']}: S/ {row['Monto']:.2f}")

            dias_bajos.to_csv('reporte_ventas_bajas.csv', index=False)
            print("Reporte exportado a 'reporte_ventas_bajas.csv'")

    except Exception as e:
        print(f"Error leyendo archivo: {e}")

if __name__ == "__main__":
    main()