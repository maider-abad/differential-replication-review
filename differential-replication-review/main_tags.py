import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))  # Obtener el directorio de main.py
src_dir = os.path.join(current_dir, 'src_tags')  # Directorio 'src' en relación con main.py


if src_dir not in sys.path:
    sys.path.append(src_dir)

from src_tags.procesar_tags import procesar_tags
from src_tags.graficar_tags import graficar_tags
from src_tags.analizar_acceso import analizar_acceso

def main():
    # Rutas de los archivos
    input_file = 'data/Literature_Review_DR.xlsx'  
    output_file = 'data/resultado_tags.xlsx'  # Archivo procesado
    resultado_plot_file = 'data/resultado_tags.xlsx'  # Archivo que se usará para graficar
    output_image = 'figures/tags_plot.png'
    output_access_model = 'figures/access_model_plot.png'
    output_access_train = 'figures/access_training_plot.png'
    correlation_image = 'figures/correlation_plot.png'

    # Paso 1: Procesar los tags
    procesar_tags(input_file, output_file)

    # Paso 2: Graficar las etiquetas
    graficar_tags(resultado_plot_file, output_image)

    # Paso 3: Analizar acceso a modelo y training data
    analizar_acceso(input_file, output_access_model, output_access_train, correlation_image)

if __name__ == '__main__':
    main()
