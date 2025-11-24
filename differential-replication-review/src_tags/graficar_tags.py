import pandas as pd
import matplotlib.pyplot as plt

def graficar_tags(input_file: str, output_image: str):
    """
    Lee un archivo procesado de Excel con columnas de etiquetas, realiza un preprocesamiento
    para unificar y eliminar algunas etiquetas, y genera un gráfico de barras con la frecuencia
    de cada etiqueta.

    input_file: str : Ruta del archivo Excel procesado con las columnas de etiquetas
    output_image: str : Ruta donde se guardará la imagen del gráfico
    """
    # Leer el archivo de entrada
    df = pd.read_excel(input_file)

    # Filtrar las columnas que comienzan con 'Tag_'
    tag_columns = [col for col in df.columns if col.startswith('Tag_')]

    if not tag_columns:
        raise ValueError("No se encontraron columnas que comiencen con 'Tag_' en el archivo.")

    # Aplanar todas las columnas de etiquetas en una sola lista
    tags = df[tag_columns].fillna('').apply(lambda row: '\n'.join(row), axis=1).str.split('\n').explode()

    # Eliminar valores vacíos generados durante el proceso
    tags = tags[tags != '']

    # Unificación de etiquetas:
    # Crear un diccionario de unificación
    unification_dict = {
        'Image classification': 'Image classification',
        'Image Classification': 'Image classification',
        'Image recognition': 'Image classification',
        'Image classification and interpretation': 'Image classification',
        'Classification': 'Image classification',
        'Knowledge distillation': 'Knowledge distillation',
        'Teacher-student': 'Knowledge distillation',
        'NLP': 'Text tasks',
        'Text tasks': 'Text tasks',
        'Text classification': 'Text tasks',
        'Tabular data': 'Text tasks',
        'NLP (machine translation)': 'Text tasks',
        'Speech recognition': 'Text tasks',
        'Federated learning': 'Federated Learning',
        'Medical Image classification': 'Medical images',
        'Medical images': 'Medical images',
        'Quantization (bit-width)': 'Quantization',
        'Differentiable Quantization': 'Quantization',
        'Quantized Distillation': 'Quantization',
        'Image explainability': 'Explainability',
        'LIME': 'Explainability',
        'Explainability': 'Explainability',
        'Attention maps (explainability but applied to training)': 'Explainability',
        'Data distillation': 'Data distillation',
        'Distillation without training': 'Data distillation',
        'Pruning':'Pruning',
        'Pruning weights':'Pruning',
        'Pruning image frames or channels':'Pruning',
        'Label refinery':'Label refinery',
        'Label smoothing':'Label refinery',
        'Data distillation':'Data distillation',
        'Data editing':'Data distillation',
    }

    # Reemplazar etiquetas usando el diccionario de unificación
    tags = tags.replace(unification_dict)

    # Etiquetas a eliminar
    tags_to_remove = [
        "SVM", "Regression",  # Ya excluidas antes
        "Model retraining",
        "Feature extraction as an input for a model",
        "Sentiment analysis",
        "Privacy",
        "Logistic regression",
        "Model simplification (editing existing model)",
        "Random forest",
    ]

    # Filtrar las etiquetas no deseadas
    tags = tags[~tags.isin(tags_to_remove)]

    # También eliminar las etiquetas que comienzan con "Mobile Speech-to-Text"
    tags = tags[~tags.str.startswith("Mobile Speech-to-Text", na=False)]

    # Contar la frecuencia de cada etiqueta
    tag_counts = tags.value_counts()

    # Crear el gráfico de barras
    plt.figure(figsize=(12, 8))
    bars = plt.bar(tag_counts.index, tag_counts.values, color='lightblue')

    # Añadir etiquetas con el número de ocurrencias sobre cada barra
    for bar, count in zip(bars, tag_counts.values):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,  # Posición del texto
                 str(count), ha='center', va='bottom', fontsize=10)

    # Añadir título y etiquetas
    plt.title('Frequency of Tags (After Unification and Filtering)', fontsize=16)
    plt.xlabel('Tag', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(rotation=45, ha='right')

    # Ajustar el diseño para que todo el texto sea legible
    plt.tight_layout()

    # Guardar el gráfico
    plt.savefig(output_image)
    print(f"Gráfico de etiquetas guardado como {output_image}")