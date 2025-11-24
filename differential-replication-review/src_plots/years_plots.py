import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from matplotlib.patches import Patch
import matplotlib as mpl
import matplotlib.font_manager as fm
from matplotlib.ticker import MaxNLocator

def inv_plot_year_access(input_file, field):

    # --- CONFIGURACIÓN GLOBAL ---
    #MY_COLORS = ["#F1595C", "#78324c","#000B3D","#3A66C0", "#224BA0", "#00AE88", "#F9B937"]
    #MY_COLORS = ["#F1595C", "#000B3D", "#224BA0", "#00AE88", "#F9B937"]
    # 8 colors:
    #MY_COLORS = ['#f1595c', '#78324c', '#000b3d', '#224ba0', '#117d94', '#00ae88', '#7cb360', '#f9b937']
    # 7 colors:
    MY_COLORS = ['#f1595c', '#78324c', '#000b3d', '#224ba0', '#117d94', '#00ae88', '#f9b937']

    # Cargar fuente personalizada
    font_path = './src_fonts/mabrypro_regular.ttf'
    custom_font = fm.FontProperties(fname=font_path)
    mpl.rcParams['font.family'] = custom_font.get_name()

    sns.set_palette(MY_COLORS)
    mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=MY_COLORS)

    # Cargar datos
    data = pd.read_excel(input_file, sheet_name='papers')
    data['Speciality'] = data['Speciality'].replace('-', pd.NA)
    data['Frequency'] = data.groupby([field, 'Year'])['Year'].transform('count')

    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)

    # Ordenar las categorías de mayor a menor
    sorted_categories = sorted(data[field].round(2).astype(str).unique(), reverse=True)
    data[field] = pd.Categorical(data[field].astype(str), categories=sorted_categories, ordered=True)

    # Asegurar que el campo sea categórico para que se agrupe bien
    #data[field] = data[field].astype(str)

    palette = sns.color_palette(MY_COLORS, n_colors=len(sorted_categories))
    color_mapping = {cat: palette[i] for i, cat in enumerate(sorted_categories)}

    # Obtener los valores únicos y crear mapping de color
    """unique_values = sorted(data[field].unique(), reverse=True)
    palette = sns.color_palette(MY_COLORS, n_colors=len(unique_values))
    color_mapping = {cat: palette[i] for i, cat in enumerate(unique_values)}"""

    # Boxplot con colores por categoría
    sns.boxplot(
        data=data,
        y=field,
        x='Year',
        palette=color_mapping,
        showfliers=False,
        zorder=1
    )

    # Scatter por grupo con el mismo color pero alpha más bajo
    for cat in sorted_categories:
        subset = data[data[field] == cat]
        sns.scatterplot(
            data=subset,
            x='Year',
            y=field,
            size='Frequency',
            sizes=(80, 200),
            color=color_mapping[cat],
            alpha=0.6,
            legend=False,
            zorder=2
        )

    # Estética
    plt.title('')
    plt.xlabel('Year', fontsize=18)
    #plt.ylabel(' '.join(field.split()[2:]), fontsize=18)
    plt.ylabel('Access to the Original Model', fontsize=18)
    plt.xticks(fontsize=16, rotation=45)
    plt.yticks(fontsize=16)

   # Obtener todos los valores únicos de Frequency, ordenados
    unique_freqs = sorted(data['Frequency'].unique())

    # Crear un handler por cada frecuencia
    handles = [
        plt.scatter([], [], 
                    s=f * 60,              # Tamaño proporcional
                    facecolors='none',     # Sin relleno
                    edgecolors='black',    # Borde negro
                    linewidth=1.2,         # Grosor del borde
                    label=str(int(f)))     # Etiqueta
        for f in unique_freqs
    ]

    # Añadir la leyenda completa
    plt.legend(
        handles=handles,
        title='Frequency',
        loc='best',
        fontsize=12,
        title_fontsize=13,
        scatterpoints=1,
        labelspacing=1.2,
        borderpad=1
    )


    """ sns.boxplot(data=data, y=field, x='Year', palette=MY_COLORS, showfliers=False, zorder=1)
    
    sizes = data['Frequency'] * 100  

    # Puntos con tamaño proporcional a la frecuencia y leyenda automática
    sns.scatterplot(
        data=data,
        x='Year',
        y=field,
        size='Frequency',         # <- esto genera los tamaños reales
        sizes=(20, 200),          # <- rango de tamaños visibles
        color='#67728a',
        alpha=0.6,
        legend='brief',
        zorder=2            # <- activa la leyenda
    )

    # Leyendas y etiquetas
    plt.legend(title='Frequency', loc='best', fontsize=12, title_fontsize=13)

    plt.title('')
    #plt.legend(title='Frequency', loc='best', fontsize=14)
    plt.ylabel(' '.join(field.split()[2:]), fontsize=18)
    plt.xlabel('Year', fontsize=18)
    plt.xticks(fontsize=16, rotation=45)
    plt.yticks(fontsize=16)
    """


    # SUBPLOT 2: Boxplot por Year con múltiples cajas (una por acceso)
    plt.subplot(1, 2, 2)

    # Asegurar que field sea string/categórico
    #data[field] = data[field].astype(str)

    # Valores únicos y frecuencias totales
    unique_values = sorted(data[field].unique())
    freq_totals = data.groupby(field).size().reset_index(name='Frequency')

   

    # Gráfico boxplot con colores por categoría (hue innecesario si agrupamos por field)
    sns.boxplot(
        data=data,
        y=field,
        x='Year',
        palette=color_mapping,
        showfliers=False,
        dodge=False,
    )

    # Añadir texto con frecuencia total para cada categoría
    for i, (cat, freq) in enumerate(freq_totals.values):
        plt.text(
            x=int(data['Year'].max()) + 0.5,  # posición en X (a la derecha del gráfico)
            y=i,  # posición en Y
            s=f'N={round(freq)}',
            va='center',
            fontsize=14,
            color='black'
        )

    plt.title('')
    plt.xlabel('Year', fontsize=18)
    plt.ylabel('')
    plt.xticks(fontsize=16, rotation=45)
    plt.yticks(fontsize=16)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))

    plt.tight_layout()
    plt.show()

def plot_year_access(input_file, field):

    # --- CONFIGURACIÓN GLOBAL ---
    #MY_COLORS = ['#f1595c', '#78324c', '#112b6e', '#224ba0', '#117d94', '#7cb360', '#f9b937'],
    MY_COLORS = ["#F1595C", "#000B3D", "#224BA0", "#00AE88", "#F9B937"] 

    # Cargar fuente personalizada
    font_path = '/Users/maider/Documents/Projects/DR/src_fonts/mabrypro_regular.ttf'
    custom_font = fm.FontProperties(fname=font_path)
    mpl.rcParams['font.family'] = custom_font.get_name()

    # Paleta
    sns.set_palette(MY_COLORS)
    mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=MY_COLORS)
   
    data = pd.read_excel(input_file, sheet_name='papers')
    # Reemplazar valores '-' en la columna 'Speciality' por NaN
    data['Speciality'] = data['Speciality'].replace('-', pd.NA)

    # Contar la frecuencia para cada combinación
    data['Frequency'] = data.groupby([field, 'Year'])['Year'].transform('count')

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    sns.boxplot(data=data, x=field, y='Year', palette=MY_COLORS, showfliers=False)

    # Agregar puntos individuales con colores según frecuencia
    scatter = sns.stripplot(
        data=data,
        x=field,
        y='Year',
        size=10, # Tamaño de los puntos
        hue='Frequency', # Colorear según frecuencia
        palette= MY_COLORS,
        dodge=True, # Separar puntos en categorías
        alpha=0.7 # Transparencia
    )

    plt.title('')
    plt.legend(title='Frequency', loc='best', fontsize=14)
    plt.xlabel(' '.join(field.split()[2:]), fontsize=18)
    plt.ylabel('Year', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)


    # Obtener valores únicos
    unique_values = sorted(data[field].unique())

    # Calcular la frecuencia total para cada categoría
    freq_totals = data.groupby(field).size().reset_index(name='Frequency')

    # Crear un diccionario de colores
    palette = sns.color_palette(MY_COLORS, n_colors=len(unique_values))
    color_mapping = {float(key): palette[i] for i, key in enumerate(unique_values)}


    # Crear el gráfico
    plt.subplot(1, 2, 2)
    sns.boxplot(
        data=data,
        x=field,
        y='Year',
        hue=field,  # Asigna hue explícitamente
        palette=color_mapping,
        showfliers=False,
        dodge=False,  # Evita separar las cajas por hue
        legend=False
    )

    # Agregar texto con frecuencia total sobre cada caja
    for i, (cat, freq) in enumerate(freq_totals.values):
        if i==-1: 
            plt.text(i, int(data['Year'].max()) + 0.1,  # Ajusta posición del texto
                f'Total: {round(freq)}', 
                ha='center', fontsize=14, color='black')

        else: 
            plt.text(i, int(data['Year'].max()) + 0.1, 
                f'{round(freq)}',
                ha='center', fontsize=14, color='black')

    plt.title('')
    plt.xlabel(' '.join(field.split()[2:]), fontsize=18)
    plt.ylabel('')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    from matplotlib.ticker import MaxNLocator
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.tight_layout()  
    plt.show()

def plot_year_method(input_file, field, filas, columnas):
    
    data = pd.read_excel(input_file)
    plt.figure(figsize=(12, 6))
    sns.violinplot(
        data=data,
        y= field,
        x='Year',
        palette='muted',
        order=data[field].value_counts(ascending=True).index  # Ordenar por frecuencia ascendente
    )

    # Calcular las frecuencias de artículos para cada metodología
    method_counts = data[field].value_counts(ascending=True)
    print(method_counts)

    # Agregar el número de artículos como texto en cada violín
    for i, (method, count) in enumerate(method_counts.items()):
        plt.text(2025.2, i, f'N={count}',  
                va='center', ha='left', fontsize=18, color='black')

    # Configurar el límite máximo del eje x
    plt.xlim(data['Year'].min(), 2025)

    # Etiquetas y título
    plt.title(field+' by Year', fontsize=20)
    plt.xlabel('Year')
    plt.ylabel(field)

    plt.tight_layout()  
    plt.show()


    # Agrupar datos para el conteo por metodología y año
    counts = data.groupby(['Year', field]).size().reset_index(name='Count')


    ### Gráfico de barras apiladas
    # Pivotear los datos para un gráfico de barras apiladas
    pivot_counts = counts.pivot(index='Year', columns=field, values='Count').fillna(0)

    pivot_counts.plot(
        kind='bar',
        stacked=True,
        figsize=(10, 6),
        colormap='tab10'
    )
    plt.title('')
    plt.xlabel('Year')
    plt.ylabel('Number of Papers')
    plt.xticks(rotation=45)
    plt.legend(title=field)
    plt.tight_layout()
    plt.show()

    # Agrupar datos para el conteo por metodología y año
    counts = data.groupby(['Year', field]).size().reset_index(name='Count')
    pivot_counts = counts.pivot(index='Year', columns=field, values='Count').fillna(0)

    # Configuración de colores (uno diferente por metodología)
    colors = sns.color_palette("husl", len(pivot_counts.columns))

    # Configuración del layout del subplot
    fig, axes = plt.subplots(filas, columnas, figsize=(18, 20), sharex=True)
    axes = axes.flatten()  

    # Iterar sobre cada metodología y crear un gráfico individual
    for i, (method, color) in enumerate(zip(pivot_counts.columns, colors)):
        ax = axes[i]
        pivot_counts[method].plot(
            kind='area',
            stacked=True,
            alpha=0.8,
            ax=ax,
            color=color
        )
        ax.set_title(f'{method}', fontsize=12)  
        ax.set_ylabel('Number of Papers')
        ax.set_xlabel('Year')

    # Ocultar subplots vacíos si hay menos de 10 metodologías
    for j in range(len(pivot_counts.columns), len(axes)):
        axes[j].axis('off')

    # Ajustar diseño
    plt.tight_layout(pad=2)  # Espaciado adicional entre subplots
    plt.show()

"""
# Obtener valores únicos y frecuencias
unique_values = sorted(data['Numeric Access to Model'].unique())
freq_totals = data.groupby('Numeric Access to Model').size().reset_index(name='Frequency')

# Crear una paleta de colores
palette = sns.color_palette('Blues', n_colors=len(unique_values))
color_mapping = {float(key): palette[i] for i, key in enumerate(unique_values)}

# Crear el gráfico
plt.figure(figsize=(12, 6))
sns.boxplot(
    data=data,
    x='Numeric Access to Model',
    y='Year',
    hue='Numeric Access to Model',  # Asigna hue explícitamente
    palette=color_mapping,
    showfliers=False,
    dodge=False,
    legend=False
)


# Crear leyenda personalizada
legend_elements = [
    Patch(facecolor=color_mapping[value], edgecolor='black', label=f'{freq}')
    for value, freq in zip(freq_totals['Numeric Access to Model'], freq_totals['Frequency'])
]

plt.legend(
    handles=legend_elements,
    title='Values and Totals',
    loc='upper right',
    bbox_to_anchor=(1.25, 1),
    fontsize=10
)

# Etiquetas y título
plt.title('Access to Model by Year', fontsize=14)
plt.xlabel('Numeric Access to Model')
plt.ylabel('Year')
plt.show()
"""



"""
# Relación entre columnas categóricas y 'Year'
plt.figure(figsize=(16, 10))

# Acceso a modelos por año
plt.subplot(2, 2, 1)
sns.boxplot(data=data, x='Numeric Access to Model', y='Year', palette='Blues')
plt.title('Access to Model by Year')

# Acceso a datos de entrenamiento por año
plt.subplot(2, 2, 2)
sns.boxplot(data=data, x='Numeric Access to Training Data', y='Year', palette='Greens')
plt.title('Access to Training Data by Year')

# Metodología principal por año
plt.subplot(2, 2, 3)
sns.violinplot(data=data, y='Main methology', x='Year', palette='muted')
plt.title('Main Methodology by Year')

# Application por año
plt.subplot(2, 2, 4)
sns.boxplot(data=data, y='Main Application', x='Year', palette='coolwarm')
plt.title('Main Appliction by Year')

plt.tight_layout()
plt.show()"""