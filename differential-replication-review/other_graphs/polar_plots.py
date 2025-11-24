import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib as mpl
import matplotlib.font_manager as fm

def plot_cluster_distribution(clusters, cluster_count, percentage, total_papers=75, ring_colours=None, save_path=None):
    df = pd.DataFrame({'LITH': clusters, 'COUNT': cluster_count})
    num_classes = len(clusters)

    # Paletas por defecto
    default_colours = {
        5: ["#F1595C", "#000B3D", "#224BA0", "#00AE88", "#F9B937"],
        7: ['#f1595c', '#78324c', '#112b6e', '#224ba0', '#117d94', '#7cb360', '#f9b937'],
        8: ['#f1595c', '#78324c', '#000b3d', '#112b6e', '#224ba0', '#117d94', '#00ae88', '#f9b937'],
        9: ['#f1595c', '#78324c', '#000b3d', '#112b6e', '#224ba0', '#117d94', '#00ae88', '#7cb360', '#f9b937']
    }
    if ring_colours is None:
        ring_colours = default_colours.get(num_classes, default_colours[5] * (num_classes // 5 + 1))

    ring_labels = [f'   {x}: {v} ({z}%) ' for x, v, z in zip(df['LITH'], df['COUNT'], percentage)]

    fig = plt.figure(figsize=(10, 6), linewidth=10)

    font_path = './src_fonts/mabrypro_regular.ttf'
    custom_font = fm.FontProperties(fname=font_path)
    mpl.rcParams['font.family'] = custom_font.get_name()
    font_path = './src_fonts/mabrypro_regular.ttf'
    fm.fontManager.addfont(font_path)
    rect = [0.1, 0.1, 0.8, 0.8]

    # Background
    ax_polar_bg = fig.add_axes(rect, polar=True, frameon=False)
    ax_polar_bg.set_theta_zero_location('N')
    ax_polar_bg.set_theta_direction(1)
    for i in range(len(df)):
        ax_polar_bg.barh(i, total_papers * 1.5 * np.pi / total_papers, color='grey', alpha=0.1)
    ax_polar_bg.axis('off')

    # Foreground
    ax_polar = fig.add_axes(rect, polar=True, frameon=False)
    ax_polar.set_theta_zero_location('N')
    ax_polar.set_theta_direction(1)
    ax_polar.set_rgrids(range(len(df)), labels=ring_labels, angle=0,
                        fontsize=14, fontweight='bold', color='black', verticalalignment='center')
    for i in range(len(df)):
        ax_polar.barh(i, df['COUNT'].iloc[i] * 1.5 * np.pi / total_papers,
                      color=ring_colours[i % len(ring_colours)])
    ax_polar.grid(False)
    ax_polar.tick_params(axis='both', left=False, bottom=False,
                         labelbottom=False, labelleft=True)

    if save_path:
        plt.savefig(save_path, transparent=True, bbox_inches='tight', pad_inches=0)

    plt.show()


def run_case(values, percentages=None, total_papers=75, save_path=None):
    if percentages is None:
        freq = Counter(values)
        values, counts = zip(*sorted(freq.items()))
        percentages = [round(v * 100 / total_papers, 1) for v in counts]
    else:
        counts = [round(p * total_papers / 100) for p in percentages]

    plot_cluster_distribution(values, counts, percentages, total_papers=total_papers, save_path=save_path)


def main():
    total_papers = 75

    cases = {
        "tasks": {
            "values": ['Image classification', 'Multi-modal classification', 'Tabular data prediction', 'Text classification', 'Others'],
            "percentages": [68.8, 10.4, 9.1, 7.8, 3.9],
            "save_path": "./figures/version 6/tasks_polar.png"
        },
        "use_cases": {
            "values": ['Adversarial Learning', 'Explainability', 'Privacy', 'Model Compression'],
            "percentages": [52.4, 33.3, 9.5, 4.8],
            "save_path": "./figures/version 6/use_cases_polar.png"
        },
        "techniques": {
            "values": [
                "Knowledge Distillation", "Model Compression", "Active Learning", "Surrogate Models",
                "Others (Jacobian, DCGAN, etc.)", "Federated Learning", "Data Editing", "Label Refinery", "Model Ensemble"
            ],
            "percentages": [28.0, 14.7, 8.0, 8.0, 8.0, 6.7, 6.7, 6.7, 5.3],
            "save_path": "./figures/version 6/techniques_polar.png"
        },
        "model_cluster": {
            "values": [
                0.2, 0.2, 0.5, 0.2, 0.5, 0.8, 0.65, 0.8, 0.5, 0.8,
                0.8, 0.3, 0.3, 0.8, 0.8, 0.8, 0.65, 0.8, 1.0, 0.8,
                0.8, 0.8, 0.65, 0.2, 0.2, 0.5, 0.3, 1.0, 0.8, 0.8,
                0.5, 0.2, 0.5, 0.2, 1.0, 0.8, 0.65, 0.3, 0.65, 0.2,
                0.2, 0.8, 0.2, 0.8, 0.2, 0.2, 0.8, 0.2, 0.8, 1.0,
                0.8, 0.8, 0.2, 0.1, 0.1, 0.2, 0.1, 0.1, 0.2, 0.1,
                0.1, 0.1, 0.5, 0.1, 0.1, 1.0, 0.2, 0.1, 0.1, 0.1,
                0.1, 0.1, 0.5, 0.1, 0.1
            ],
            "save_path": "./figures/model_acc_polar.png"
        },
        "data_cluster": {
            "values": [
                1, 1, 0, 1, 1, 0.7, 1, 0.6, 0.7, 1,
                0.7, 1, 1, 1, 0.7, 0.7, 1, 0.7, 0.7, 0,
                1, 1, 0.7, 0.7, 0.7, 0.7, 1, 1, 0.6, 1,
                0.6, 0.7, 1, 0.2, 1, 1, 1, 1, 0.7, 1,
                0.7, 1, 1, 1, 0.7, 0, 1, 1, 1, 0.7,
                0.6, 0.7, 1, 1, 1, 1, 0, 0, 0, 0.1,
                0.1, 1, 0.1, 0.2, 0.2, 1, 0.3, 0.3,
                0.1, 0.3, 0.2, 0.3, 0.2, 0.4, 0.4
            ],
            "save_path": "./figures/data_acc_polar.png"
        }
    }

    # Activar/desactivar casos
    active_cases = ["tasks", "use_cases", "techniques", "model_cluster", "data_cluster"]
    #active_cases = ["data_cluster"]

    for case in active_cases:
        run_case(**cases[case], total_papers=total_papers)


if __name__ == "__main__":
    main()
