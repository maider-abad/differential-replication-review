import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Cargar y limpiar datos (igual que antes)
file_path = './keywords/top_keywords_per_year.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

df_clean = df.iloc[1:]
df_clean.columns = ['Year', 'Keyword', 'Count']
df_clean['Year'] = pd.to_numeric(df_clean['Year'], errors='coerce')
df_clean['Count'] = pd.to_numeric(df_clean['Count'], errors='coerce')

df_filtered = df_clean[df_clean.groupby('Keyword')['Count'].transform('sum') > 1]
df_grouped = df_filtered.groupby(['Year', 'Keyword'])['Count'].sum().reset_index()
keywords_unique = df_grouped['Keyword'].unique()

# Colores y estilos
my_colors = ['#f1595c', '#78324c', "#1c8cd1", "#0a1d51", '#117d94', '#224ba0', '#00ae88', '#7cb360', '#f9b937']
colors = my_colors[:len(keywords_unique)]
keyword_colors_automatic = {keyword: color for keyword, color in zip(keywords_unique, colors)}
line_styles = ['-', '--']                      # alternamos sólido / dashed
keyword_linestyles = {k: line_styles[i % 2] for i, k in enumerate(keywords_unique)}

if "knowledge distillation" in keyword_linestyles:
    keyword_linestyles["knowledge distillation"] = '--'

width = 0.2

# Figura y ejes
fig, ax = plt.subplots(figsize=(14, 8))

# Scatter
for i, (year, group) in enumerate(df_grouped.groupby('Year')):
    for j, (keyword, keyword_group) in enumerate(group.groupby('Keyword')):
        ax.scatter(
            np.full_like(keyword_group['Year'], year),
            keyword_group['Count'] + j * width,
            color=keyword_colors_automatic.get(keyword, 'gray'),
            marker='o',
            s=100
        )

# Líneas conectando puntos
for keyword in keywords_unique:
    keyword_rows = df_grouped[df_grouped['Keyword'] == keyword].sort_values('Year')
    x_vals, y_vals = [], []
    for idx, row in keyword_rows.iterrows():
        year = row['Year']; count = row['Count']
        group_year = df_grouped[df_grouped['Year'] == year]
        keywords_in_year = sorted(group_year['Keyword'].unique())
        j = keywords_in_year.index(keyword)
        x_vals.append(year)
        y_vals.append(count + j * width)

    ax.plot(
        x_vals,
        y_vals,
        color=keyword_colors_automatic.get(keyword, 'gray'),
        linestyle=keyword_linestyles[keyword],
        linewidth=2,
        alpha=0.7
    )

# Etiquetas y estilo de ejes (fontsize SIN CAMBIAR)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Count', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.set_title('Keywords per Year', fontsize=16)

# Handles personalizados para la leyenda (color + estilo + marcador)
legend_handles = [
    Line2D([0], [0],
           color=keyword_colors_automatic[keyword],
           linestyle=keyword_linestyles[keyword],
           linewidth=2,
           marker='o',
           markersize=8,
           label=keyword)
    for keyword in keywords_unique
]

# ======= LEYENDA: anclada con un bbox de 4 elementos para ocupar TODO el ancho del eje =======
# bbox_to_anchor = (x0, y0, width, height) en COORDENADAS DEL AXES -> width=1 ocupa ancho completo
ax.legend(
    handles=legend_handles,
    title='Keywords',
    loc='lower left',                 # 'lower left' dentro del bbox definido
    bbox_to_anchor=(0, 1.08, 1, 0.15),# x0=0, y0=1.02 (un poco encima del eje), width=1 (ancho completo), height=0.15
    ncol=4,                           # ajustar columnas según número de keywords
    mode='expand',                    # expande las entradas a lo largo del ancho del bbox
    handlelength=4,                   # línea más larga en la leyenda para que se note el '--'
    fontsize=12,                      # NO cambiamos
    title_fontsize=13,
    borderaxespad=0.3,
    frameon=True
)

# Dejar espacio arriba para la leyenda (evitar usar tight_layout() porque puede re-ajustar y comprimir)
fig.subplots_adjust(top=0.78)

plt.show()
