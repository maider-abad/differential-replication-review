from graphviz import Digraph

# Colores finales personalizados
final_colors_latest = {
    'T1': '#9AC04E',
    'T2': '#001D5C',
    'T3': '#A33E4D',
    'T4': '#4aba77',
    'T5.1': '#1E68A8',
    'T5.2': '#1E68A8',
    'T6': '#1c8e85'
}

# Crear diagrama
dot = Digraph(comment='Differential Replication Strategy Tree', format='png', engine='dot')
dot.attr(rankdir='TB', fontname='Mabry Pro', fontsize='10', splines='ortho')

# Funciones para nodos
def add_type_node(name, label, color):
    dot.node(name, label=label, shape='box', style='filled',
             fillcolor=color, fontcolor='white', color='black',
             fontname='Mabry Pro', fontsize='10')

def add_method_node(name, label, base_color):
    dot.node(name, label=label, shape='box', style='filled',
             fillcolor=base_color + '33', fontcolor='black',
             color=base_color + '33', fontname='Mabry Pro', fontsize='10')

def add_question_node(name, label):
    dot.node(name, label=label, shape='box', style='filled',
             fillcolor='white', fontcolor='black', color='black',
             fontname='Mabry Pro', fontsize='10')

def add_label_node(name, label):
    dot.node(name, label=label, shape='box', style='filled',
             fillcolor='white', fontcolor='black', color='white',
             width='0.4', height='0.2', fontname='Mabry Pro',
             fontsize='10', fixedsize='false')

# Nodos de pregunta
add_question_node('entry', 'What is the available access context for replication?')
add_question_node('model_access', 'Access to original model?')
add_question_node('data_access_full_model', 'Access to training data?')
add_question_node('data_access_partial_model', 'Access to training data?')
add_question_node('model_access_type', 'Type of model access?')

# Etiquetas de conexión
arrow_labels = {
    'l1': 'Full',
    'l2': 'Partial/None',
    'l3': 'Full',
    'l4': 'None',
    'l5': 'None',
    'l6': 'Full',
    'l7': 'Partial',
    'l8': 'Soft',
    'l9': 'Hard',
    'l10': 'Minimal'
}
for node, text in arrow_labels.items():
    add_label_node(node, text)

# T-nodes y nodos de metodología
type_labels = {
    'T1': 'T1\nFull access to model and data',
    'T2': 'T2\nNo access to data, limited model',
    'T3': 'T3\nFull model access,\nno data access',
    'T4': 'T4\nNo model access,\nfull data access',
    'T5.1': 'T5.1\nHard labels only',
    'T5.2': 'T5.2\nSoft outputs',
    'T6': 'T6\nMinimal access to both'
}

method_labels = {
    'T1': 'Fine-tuning, pruning,\ndistillation, quantization',
    'T2': 'Output imitation,\ndata-free distillation',
    'T3': 'Model auditing,\noutput-based analysis',
    'T4': 'Data editing,\nrule extraction',
    'T5.1': 'Query-based learning,\nactive probing',
    'T5.2': 'Distillation,\nproxy models',
    'T6': 'Model copying,\nsurrogates'
}

for t in final_colors_latest:
    add_type_node(t, type_labels[t], final_colors_latest[t])
    add_method_node(f'{t}_m', method_labels[t], final_colors_latest[t])

# Conexiones principales con etiquetas como nodos
dot.edge('entry', 'model_access', arrowsize='0.4')

dot.edge('model_access', 'l1', arrowhead='none')
dot.edge('l1', 'data_access_full_model', arrowsize='0.4')
dot.edge('model_access', 'l2', arrowhead='none')
dot.edge('l2', 'data_access_partial_model', arrowsize='0.4')

dot.edge('data_access_full_model', 'l3', arrowhead='none')
dot.edge('l3', 'T1', arrowsize='0.4')
dot.edge('data_access_full_model', 'l4', arrowhead='none')
dot.edge('l4', 'T3', arrowsize='0.4')

dot.edge('data_access_partial_model', 'l5', arrowhead='none')
dot.edge('l5', 'T2', arrowsize='0.4')
dot.edge('data_access_partial_model', 'l6', arrowhead='none')
dot.edge('l6', 'T4', arrowsize='0.4')
dot.edge('data_access_partial_model', 'l7', arrowhead='none')
dot.edge('l7', 'model_access_type', arrowsize='0.4')

dot.edge('model_access_type', 'l8', arrowhead='none')
dot.edge('l8', 'T5.2', arrowsize='0.4')
dot.edge('model_access_type', 'l9', arrowhead='none')
dot.edge('l9', 'T5.1', arrowsize='0.4')
dot.edge('model_access_type', 'l10', arrowhead='none')
dot.edge('l10', 'T6', arrowsize='0.4')

# Conectar metodologías
for t in final_colors_latest:
    dot.edge(t, f'{t}_m', style='dashed', arrowhead='vee', arrowsize='0.4')

# Exportar a PNG
dot.render('replication_strategy_diagram_mabry', view=True)
