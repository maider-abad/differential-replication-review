import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analizar_acceso(input_file: str, output_image_1: str, output_image_2: str, correlation_image: str):
    """
    Lee el archivo Excel procesado, cuenta las frecuencias de los datos en las columnas
    que comienzan con 'access to' y genera gráficos.

    input_file: str : Ruta del archivo Excel procesado con las columnas de interés
    output_image_1: str : Ruta donde se guardarán las imágenes de las frecuencias
    output_image_2: str : Ruta donde se guardará la imagen de correlación
    """
    # Leer el archivo Excel procesado
    df = pd.read_excel(input_file)

    # Filtrar las columnas que contienen los datos de acceso (aquellas cuyo nombre empieza con 'access to')
    access_columns = [col for col in df.columns if col.lower().startswith('access to')]

    if len(access_columns) != 2:
        raise ValueError("Se esperaban exactamente dos columnas que comienzan con 'access to'.")

    # Filtramos las dos columnas que nos interesan
    access_to_model = df[access_columns[0]].dropna()
    access_to_training_data = df[access_columns[1]].dropna()

    # Limpiar los valores atípicos ('x' o 'X') en ambas columnas
    access_to_model = access_to_model[~access_to_model.isin(['x', 'X'])]
    access_to_training_data = access_to_training_data[~access_to_training_data.isin(['x', 'X'])]

    # Normalizar los valores:
    # Eliminar espacios al principio y al final, y convertir todo a minúsculas
    access_to_model = access_to_model.str.strip().str.lower()
    access_to_training_data = access_to_training_data.str.strip().str.lower()

    # Unificar valores como 'High' y 'high'
    access_to_model = access_to_model.replace('high', 'high')
    access_to_training_data = access_to_training_data.replace('high', 'high')

    # Gráfico 1: Frecuencia de los valores en 'Access to Model'
    plt.figure(figsize=(10, 6))
    access_to_model.value_counts().plot(kind='bar', color='skyblue')
    plt.title(f'Frequency of {access_columns[0]} (Excluding x and X, normalized)')
    plt.xlabel(f'{access_columns[0]}')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_image_1)
    print(f"Gráfico de frecuencia guardado como {output_image_1}")

    # Gráfico 2: Frecuencia de los valores en 'Access to Training Data'
    plt.figure(figsize=(10, 6))
    access_to_training_data.value_counts().plot(kind='bar', color='lightcoral')
    plt.title(f'Frequency of {access_columns[1]} (Excluding x and X, normalized)')
    plt.xlabel(f'{access_columns[1]}')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_image_2)
    print(f"Gráfico de frecuencia guardado como {output_image_2}")

    # Ahora creamos un DataFrame con las combinaciones de los valores
    combination_counts = pd.DataFrame({
        'Access to Model': access_to_model,
        'Access to Training Data': access_to_training_data
    })

    # Contamos las combinaciones de las dos columnas
    combination_counts = combination_counts.groupby(['Access to Model', 'Access to Training Data']).size().reset_index(name='Frequency')

    # Gráfico 3: Relación entre 'Access to Model' y 'Access to Training Data' (gráfico tipo clúster con tamaños por frecuencia)
    fig, ax = plt.subplots(figsize=(10, 6))

    # Crear el gráfico de dispersión (scatter plot)
    scatter = sns.scatterplot(data=combination_counts,
                              x='Access to Model',
                              y='Access to Training Data',
                              size='Frequency',
                              sizes=(50, 1000),  # Ajusta el tamaño de los círculos
                              hue='Frequency',  # Color por frecuencia
                              palette='coolwarm',  # Paleta de colores
                              legend=False,
                              marker='o',
                              ax=ax)

    plt.title('Correlation between Access to Model and Access to Training Data (Clustered)')
    plt.xlabel(access_columns[0])
    plt.ylabel(access_columns[1])

    # Agregar leyenda de colores
    norm = plt.Normalize(vmin=combination_counts['Frequency'].min(), vmax=combination_counts['Frequency'].max())
    sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)
    sm.set_array([])  # Necesario para agregar la leyenda
    cbar = plt.colorbar(sm, ax=ax, label='Frequency')  # Asociamos la barra de colores con el eje

    plt.tight_layout()

    # Guardar el gráfico de correlación
    plt.savefig(correlation_image)
    print(f"Gráfico de correlación guardado como {correlation_image}")