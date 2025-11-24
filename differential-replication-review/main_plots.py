import os
import sys
import seaborn as sns
import matplotlib as mpl
import matplotlib.font_manager as fm

#current_dir = os.path.dirname(os.path.abspath(__file__))  # Para obtener el directorio de main.py
#src_dir = os.path.join(current_dir, 'src_plots')  # Directorio 'src' en relación con main.py


#if src_dir not in sys.path:
 #   sys.path.append(src_dir)

from src_plots.kde_plots import kdeplot, mean_kdeplot
from src_plots.years_plots import plot_year_access, plot_year_method, inv_plot_year_access
from src_plots.distribution_plots import plot_distributions
from src_plots.cross_tabs import plot_crosstabs

# --- CONFIGURACIÓN GLOBAL ---
MY_COLORS = ["#F1595C", "#000B3D", "#224BA0", "#00AE88", "#F9B937"]  # paleta personalizada

# Cargar fuente personalizada
font_path = './src_fonts/mabrypro_regular.ttf'
custom_font = fm.FontProperties(fname=font_path)
#mpl.rcParams['font.family'] = custom_font.get_name()

# Paleta
sns.set_palette(MY_COLORS)
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=MY_COLORS)

def main():
    # Rutas de los archivos
    input_file = 'data/Literature_Review_DR.xlsx'
    xlabel = 'Complexity of the methodology'
    ylabel = 'Normalized Numeric Access to Model' #Complexity of the methodology
    maxdim_x = 1
    maxdim_y = 1
    mindim_x = 0
    mindim_y = 0

    # Kdeplot
    kdeplot(input_file, xlabel, ylabel, custom_font, maxdim_x, maxdim_y, mindim_y, mindim_y)
    mean_kdeplot(input_file, xlabel, ylabel, maxdim_x, maxdim_y, mindim_y, mindim_y)

    # Plot year
    field = 'Normalized Numeric Access to Model'
    inv_plot_year_access(input_file, field)

    field = 'Normalized Numeric Access to Training Data'
    inv_plot_year_access(input_file, field)

    field = 'Main methology'
    plot_year_method(input_file, field, filas=5, columnas=2)

    field = 'Task'
    plot_year_method(input_file, field, filas=6, columnas=3)

    plot_distributions(input_file)

    plot_crosstabs(input_file)



if __name__ == '__main__':
    main()
