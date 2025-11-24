import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from matplotlib.patches import Patch

def plot_distributions(input_file):
    
    data = pd.read_excel(input_file, sheet_name='papers')
    # Análisis de distribuciones y conteos
    plt.figure(figsize=(16, 10))

    # Distribución del año
    plt.subplot(2, 2, 1)
    sns.histplot(data['Year'], kde=False, bins=10, color='skyblue')
    plt.title('Year distribution')

    # Conteo de acceso a modelos
    plt.subplot(2, 2, 2)
    sns.countplot(data=data, x='Normalized Numeric Access to Model', palette='viridis')
    plt.title('Access to Model')
    plt.xticks(rotation=45)

    # Conteo de acceso a datos de entrenamiento
    plt.subplot(2, 2, 3)
    sns.countplot(data=data, x='Normalized Numeric Access to Training Data', palette='plasma')
    plt.title('Access to Trainig data')
    plt.xticks(rotation=45)

    # Conteo de DL o ML
    plt.subplot(2, 2, 4)
    sns.countplot(data=data, x='DL or ML?', palette='Set2')
    plt.title('DL or ML')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

    # new plot
    plt.figure(figsize=(10, 6))
    sns.countplot(
        data=data,
        y='Task',
        palette='rocket',
        order=data['Task'].value_counts().index
    )

    # Escala logarítmica en el eje x 
    plt.xscale('log')

    plt.title('Task (Logarithmic Scale)', fontsize=14)
    plt.xlabel('Number of Papers (Log Scale)')
    plt.ylabel('Task')
    plt.tight_layout()
    plt.show()

    # new plot
    plt.figure(figsize=(10, 6))
    sns.countplot(
        data=data,
        y='Main methology',
        palette='rocket',
        order=data['Main methology'].value_counts().index
    )

    # Escala logarítmica en el eje x 
    plt.xscale('log')

    plt.title('Main methodology (Logarithmic Scale)', fontsize=14)
    plt.xlabel('Number of Papers (Log Scale)')
    plt.ylabel('Main Methodology')
    plt.tight_layout()
    plt.show()