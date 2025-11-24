import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import os
import re
import seaborn as sns
import numpy as np

# Cargar archivo Excel
archivo_excel = "./data/Literature_Review_DR.xlsx"
df = pd.read_excel(archivo_excel)

# Limpiar datos: eliminar filas vacías
df = df.dropna(subset=['Keywords', 'Year'])

# Función para limpiar y normalizar keywords
def limpiar_keyword(kw):
    kw = kw.strip().lower()
    kw = re.sub(r'\s*\(.*?\)', '', kw)  # eliminar paréntesis y su contenido
    kw = kw.replace('-', ' ')  # unificar palabras separadas por guiones

    # Normalizaciones manuales de sinónimos comunes
    normalizaciones = {
        'knowledge distillation': 'knowledge distillation',
        'kd': 'knowledge distillation',
        'deep learning': 'deep learning',
        'dl': 'deep learning',
        'machine learning': 'machine learning',
        'ml': 'machine learning',
        'cnn': 'convolutional neural network',
        'convolutional neural networks': 'convolutional neural network',
        'convolutional neural network': 'convolutional neural network',
        'dnn': 'neural network',
        'deep neural networks': 'neural network',
        'deep neural network': 'neural network',
        'neural networks': 'neural network',
        'neural network': 'neural network',
        'pruning': 'model pruning',
        'model pruning': 'model pruning',
    }

    # Aplicar reemplazos exactos
    if kw in normalizaciones:
        kw = normalizaciones[kw]

    # Eliminar plurales simples
    if kw.endswith('s') and kw[:-1] in normalizaciones:
        kw = kw[:-1]

    return kw if kw else None


# Contador global
all_keywords = []

for keywords in df['Keywords']:
    kws = [limpiar_keyword(kw) for kw in str(keywords).split(',')]
    kws = [kw for kw in kws if kw]  # eliminar None
    all_keywords.extend(kws)

conteo_global = Counter(all_keywords)

# Mostrar top 10 globales
print("Top 10 keywords más frecuentes:")
print(conteo_global.most_common(10))

# Crear DataFrame para guardar los resultados
resultados = []

# Análisis por año
años = sorted(df['Year'].unique())

print("\nTop 10 keywords por año:")
for año in años:
    df_año = df[df['Year'] == año]
    keywords_año = []

    for keywords in df_año['Keywords']:
        kws = [limpiar_keyword(kw) for kw in str(keywords).split(',')]
        kws = [kw for kw in kws if kw]
        keywords_año.extend(kws)

    conteo_año = Counter(keywords_año)
    top_5 = conteo_año.most_common(10)
    
    for kw, count in top_5:
        resultados.append({'Year': año, 'Keyword': kw, 'Count': count})

    print(f"{año}: {top_5}")

    # Gráfico por año
    if top_5:
        keywords, counts = zip(*top_5)
        plt.figure(figsize=(8, 4))
        plt.bar(keywords, counts)
        plt.title(f'Top 10 Keywords in {año}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'top10_keywords_{año}.png')
        plt.close()

# Guardar resultados en un CSV
df_resultados = pd.DataFrame(resultados)
df_resultados.to_csv('top_keywords_per_year.csv', index=False)

# Gráfico global (top 10)
top_keywords, counts = zip(*conteo_global.most_common(10))
plt.figure(figsize=(10,5))
plt.bar(top_keywords, counts)
plt.title('Top 10 Keywords Globales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top10_keywords_global.png')
plt.close()

print("\nResultados guardados en 'top_keywords_per_year.csv' y gráficos en archivos PNG.")
