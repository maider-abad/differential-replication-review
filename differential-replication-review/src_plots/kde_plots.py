import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import matplotlib as mpl
import matplotlib.font_manager as fm

def kdeplot(input_file, xlabel, ylabel, custom_font, maxdim_x=3, maxdim_y=3, mindim_x=0, mindim_y=0):
    data = pd.read_excel(input_file)
    # Reemplazar valores '-' en la columna 'Speciality' por NaN
    data['Speciality'] = data['Speciality'].replace('-', pd.NA)

    # Análisis de valores faltantes
    def missing_values_analysis(df):
        missing_data = df.isnull().sum()
        percent_missing = (missing_data / len(df)) * 100
        return pd.DataFrame({'Missing Values': missing_data, 'Percentage': percent_missing})

    missing_values = missing_values_analysis(data)
    print("\nValores faltantes:\n", missing_values)

    # Clustering entre Access to Model y Access to Training Data
    combination_counts = pd.DataFrame({
            'Access to Model': data[ylabel],
            'Clusters': data[xlabel] #Numeric Access to Training Data
    })

    # Contamos las combinaciones de las dos columnas
    combination_counts = combination_counts.groupby(['Access to Model', 'Clusters']).size().reset_index(name='Frequency')
    # Contamos las combinaciones de las dos columnas y calculamos el porcentaje
    total_count = len(combination_counts)

    combination_counts['Percentage'] = (combination_counts['Frequency'] / total_count) * 100

    MY_COLORS = ["#F1595C", "#000B3D", "#224BA0", "#00AE88", "#F9B937"]
    custom_cmap = LinearSegmentedColormap.from_list("my_cmap", MY_COLORS)

    # Crear el gráfico kdeplot
    fig, ax = plt.subplots(figsize=(12, 8))

    # Usar kdeplot con pesos basados en el porcentaje
    kde = sns.kdeplot(
        data=combination_counts,
        y='Access to Model',
        x='Clusters',
        weights='Percentage',
        cmap= custom_cmap, #'YlOrRd',
        shade=True,
        cbar=False,  # Desactivamos la barra de colores automática
        ax=ax
    )

    # Obtener los valores mínimo y máximo del porcentaje
    min_percentage = combination_counts['Percentage'].min()
    max_percentage = combination_counts['Percentage'].max()

    # Crear una barra de colores personalizada
    #sm = plt.cm.ScalarMappable(cmap='YlOrRd', norm=plt.Normalize(vmin=min_percentage, vmax=max_percentage))
    sm = plt.cm.ScalarMappable(cmap=custom_cmap, norm=plt.Normalize(vmin=min_percentage, vmax=max_percentage))
    sm.set_array([])

    # Añadir la barra de colores personalizada
    cbar = plt.colorbar(sm, ax=ax, pad=0.02)

    cbar.ax.tick_params(labelsize=20)

    # Personalizar la barra de colores
    cbar.set_label('', rotation=270, labelpad=20)

    # Configurar ticks personalizados
    tick_locator = plt.LinearLocator(numticks=5)  
    cbar.locator = tick_locator
    cbar.update_ticks()

    # Formatear las etiquetas de los ticks como porcentajes
    cbar.set_ticklabels([f'{x:.1f}%' for x in cbar.get_ticks()])

    mpl.rcParams['font.family'] = custom_font.get_name()
    font_path = './src_fonts/mabrypro_regular.ttf'
    fm.fontManager.addfont(font_path)

    # Configurar el gráfico
    #plt.title('Correlation between '+xlabel+' and ' + ylabel, fontsize=16)
    
    plt.xlabel(xlabel, fontsize=24)
    #plt.xlabel(' '.join(xlabel.split()[2:]), fontsize=24) # DESCOMENTAR ESTA LÍNEA PARA ACC ALL
    #plt.ylabel(' '.join(ylabel.split()[2:]), fontsize=24)
    plt.ylabel('Access to the Original Model', fontsize=24)
    plt.xlim(mindim_x, maxdim_x)
    plt.ylim(mindim_y, maxdim_y)

    """
    # Configurar el gráfico
    plt.title('Correlation between ' + xlabel + ' and ' + ylabel, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    # Ajustar los límites del eje x para que los clusters aparezcan correctamente
    plt.xlim(min(combination_counts['Clusters']), max(combination_counts['Clusters']))
    plt.ylim(mindim_y, maxdim_y)
    """

    ######## COMENTAR LAS SIGUIENTES DOS LÍNEAS PARA HACER PLOT DE DIFF ACCESOS JUNTOS
    plt.xlim(min(combination_counts['Clusters']), max(combination_counts['Clusters']))
    plt.xticks(range(int(min(combination_counts['Clusters'])), int(max(combination_counts['Clusters'])) + 1))
    
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()


def mean_kdeplot(input_file, xlabel, ylabel, maxdim_x=3, maxdim_y=3, mindim_x=0, mindim_y=0):
    # Cargar los datos desde el archivo Excel
    data = pd.read_excel(input_file)

    # Clustering entre Access to Model y Access to Training Data
    combination_counts = pd.DataFrame({
        'Access to Model': data[ylabel],
        'Clusters': data[xlabel]  # Numeric Access to Training Data
    })

    # Calcular el valor medio de 'Access to Model'
    mean_value = combination_counts['Access to Model'].mean()

    # Calcular la distancia al valor medio
    combination_counts['Distance to Mean'] = abs(combination_counts['Access to Model'] - mean_value)

    # Contamos las combinaciones de las dos columnas
    combination_counts = combination_counts.groupby(['Distance to Mean', 'Clusters']).size().reset_index(name='Frequency')
    print(combination_counts)

    # Contamos las combinaciones de las dos columnas y calculamos el porcentaje
    total_count = len(combination_counts)
    combination_counts['Percentage'] = (combination_counts['Frequency'] / total_count) * 100
    print(combination_counts)
    # Crear el gráfico kdeplot
    fig, ax = plt.subplots(figsize=(12, 8))

    # Usar kdeplot con pesos basados en el porcentaje
    kde = sns.kdeplot(
        data=combination_counts,
        x='Clusters',
        y='Distance to Mean',
        weights='Percentage',
        cmap='YlOrRd',
        shade=True,
        cbar=False,  # Desactivamos la barra de colores automática
        ax=ax
    )

    # Obtener los valores mínimo y máximo del porcentaje
    min_percentage = combination_counts['Percentage'].min()
    max_percentage = combination_counts['Percentage'].max()

    # Crear una barra de colores personalizada
    sm = plt.cm.ScalarMappable(cmap='YlOrRd', norm=plt.Normalize(vmin=min_percentage, vmax=max_percentage))
    sm.set_array([])

    # Añadir la barra de colores personalizada
    cbar = plt.colorbar(sm, ax=ax, pad=0.1)

    # Personalizar la barra de colores
    cbar.set_label('Percentage', rotation=270, labelpad=15)

    # Configurar ticks personalizados
    tick_locator = plt.LinearLocator(numticks=5)  # Ajusta el número de ticks según necesites
    cbar.locator = tick_locator
    cbar.update_ticks()

    # Formatear las etiquetas de los ticks como porcentajes
    cbar.set_ticklabels([f'{x:.1f}%' for x in cbar.get_ticks()])

    # Configurar el gráfico
    plt.title('Correlation between ' + xlabel + ' and ' + ylabel, fontsize=16)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel('Distance to Mean of ' + ylabel, fontsize=12)
    # Ajustar los límites del eje x para que los clusters aparezcan correctamente
    plt.xlim(min(combination_counts['Clusters']), max(combination_counts['Clusters']))
    plt.ylim(combination_counts['Distance to Mean'].min(), combination_counts['Distance to Mean'].max())

    plt.xticks(range(int(min(combination_counts['Clusters'])), int(max(combination_counts['Clusters'])) + 1))

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()