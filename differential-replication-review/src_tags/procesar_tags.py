import pandas as pd

def procesar_tags(input_file: str, output_file: str):
    """
    Procesa el archivo Excel para dividir los tags en columnas separadas y guardar el resultado.

    input_file: str : Ruta del archivo Excel de entrada
    output_file: str : Ruta donde se guardará el archivo procesado
    """
    # Leer el archivo Excel
    df = pd.read_excel(input_file)

    # Filtrar filas que tengan '-' o NaN en la columna 'Tags'
    df_filtered = df[~df['Tags'].isin(['-', None, pd.NA])]

    # Función para dividir los valores de los tags y ponerlos en columnas separadas
    def split_tags_to_columns(row):
        if isinstance(row, str):  # Si es una cadena
            return row.split('\n')
        return []  # Si no es una cadena, retornar lista vacía

    # Aplicar la función para dividir los tags en nuevas columnas
    tags_columns = df_filtered['Tags'].apply(split_tags_to_columns)

    # Convertir la lista de tags en nuevas columnas
    tags_df = pd.DataFrame(tags_columns.tolist(), index=df_filtered.index)

    # Nombrar las nuevas columnas como Tag_1, Tag_2, Tag_3, etc.
    tags_df.columns = [f"Tag_{i+1}" for i in range(tags_df.shape[1])]

    # Concatenar el DataFrame filtrado con las nuevas columnas de tags
    df_result = pd.concat([df_filtered, tags_df], axis=1)

    # Guardar el DataFrame resultante en un nuevo archivo Excel
    df_result.to_excel(output_file, index=False)

    print(f"Archivo guardado como {output_file}")
