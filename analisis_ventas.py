# analisis_ventas.py
import pandas as pd

def main():
    archivo = 'ventas.txt'

    try:
        # Leer archivo con separador pipe
        data = pd.read_csv(archivo, delimiter='|')

        # Calcular total de ventas por día
        ventas_por_dia = data.groupby('Fecha')['Monto'].sum().reset_index()

        # Definir umbral de ventas bajas (por ejemplo, menos de 500)
        umbral_bajo = 500

        # Filtrar días con ventas bajas
        dias_bajos = ventas_por_dia[ventas_por_dia['Monto'] < umbral_bajo]

        # Mostrar resultados
        print("Días con ventas bajas (menos de S/ 500):")
        if dias_bajos.empty:
            print("Ningún día con ventas bajas.")
        else:
            for index, row in dias_bajos.iterrows():
                print(f"- {row['Fecha']}: S/ {row['Monto']:.2f}")

    except Exception as e:
        print(f"Error leyendo archivo: {e}")

if __name__ == "__main__":
    main()