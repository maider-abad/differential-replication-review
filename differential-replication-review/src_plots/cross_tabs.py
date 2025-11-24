import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from matplotlib.patches import Patch

def plot_crosstabs(input_file):# Tablas cruzadas y visualización de relaciones
    data = pd.read_excel(input_file, sheet_name='papers')
    
    # Crear la tabla cruzada
    cross_tab = pd.crosstab(data['Normalized Numeric Access to Model'], data['DL or ML?'])
    print("\nCross tab (Access to Models vs DL or ML):\n", cross_tab)

    # Ordenar el eje y para que el 0 esté en la parte inferior
    cross_tab = cross_tab.sort_index(ascending=False)

    # Crear el heatmap
    plt.figure(figsize=(10, 6))  
    sns.heatmap(cross_tab, annot=True, cmap='viridis', fmt='d')

    plt.title('Access to Models vs DL or ML')
    plt.show()

    #access training data vs DL/ML
    cross_tab = pd.crosstab(data['Normalized Numeric Access to Training Data'], data['DL or ML?'])
    print("\nCross Tab (Access a Training Data vs DL o ML):\n", cross_tab)
    # Ordenar el eje y para que el 0 esté en la parte inferior
    cross_tab = cross_tab.sort_index(ascending=False)

    # Crear el heatmap
    plt.figure(figsize=(10, 6)) 
    sns.heatmap(cross_tab, annot=True, cmap='viridis', fmt='d')
    plt.title('Access to Training data vs DL or ML')
    plt.show()


    # Crear la tabla cruzada
    cross_tab_model_meth = pd.crosstab(data['Normalized Numeric Access to Model'], data['Main methology'])

    # Ordenar el eje y al revés
    cross_tab_model_meth = cross_tab_model_meth.sort_index(ascending=False)

    # Ordenar las columnas (etiquetas del eje x) según la frecuencia total
    column_order = cross_tab_model_meth.sum(axis=0).sort_values(ascending=False).index
    cross_tab_model_meth = cross_tab_model_meth[column_order]

    # Crear el heatmap
    plt.figure(figsize=(12, 8))  
    sns.heatmap(cross_tab_model_meth, annot=True, cmap='coolwarm', fmt='d', cbar=True)

    
    plt.title('Access to Model vs Main Methodology')
    plt.xticks(rotation=45, ha='right')  # Rotar etiquetas del eje x para mejor visibilidad
    plt.tight_layout()
    plt.show()

    # Crear la tabla cruzada
    cross_tab_model_meth = pd.crosstab(data['Normalized Numeric Access to Training Data'], data['Main methology'])

    # Ordenar el eje y al revés
    cross_tab_model_meth = cross_tab_model_meth.sort_index(ascending=False)

    # Ordenar las columnas (etiquetas del eje x) según la frecuencia total
    column_order = cross_tab_model_meth.sum(axis=0).sort_values(ascending=False).index
    cross_tab_model_meth = cross_tab_model_meth[column_order]

    # Crear el heatmap
    plt.figure(figsize=(12, 8))  
    sns.heatmap(cross_tab_model_meth, annot=True, cmap='coolwarm', fmt='d', cbar=True)

   
    plt.title('Access to Training Data vs Main Methodology')
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()
    plt.show()

