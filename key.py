import nbformat

# Load the notebook
notebook_path = 'ImageRetrivalAndAutomated_dataset_annotation_and_evaluation_with_grounding_dino_and_sam.ipynb'
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Ensure 'state' key is present in 'metadata.widgets'
if 'widgets' in nb.metadata:
    if 'state' not in nb.metadata.widgets:
        nb.metadata.widgets['state'] = {}

# Save the modified notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print('Notebook metadata fixed.')
