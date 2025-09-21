import os

def should_exclude(name, path):
    """
    Define qué carpetas y archivos deben excluirse.
    """
    exclude_patterns = [
        '__pycache__',
        '.pytest_cache',
        '.git',
        '.vscode',
        'venv',
        'Lib',
        'Scripts',
        'Include',
        'site-packages',
        '.dist-info',
        '.egg-info',
        '__init__.py',  # Opcional: puedes incluirlo si lo deseas
        '.pyc',
        '.pyo',
        '.pyd',
        '.whl',
        '.dll',
        '.lib',
        '.pdb',
        '.exp',
        '.so',
        '.dylib',
        '.cache',
        'CACHEDIR.TAG',
        'RECORD',
        'METADATA',
        'WHEEL',
        'INSTALLER',
        'LICENSE',
        'NOTICE',
        'top_level.txt',
        'entry_points.txt',
        '.gitignore',  # Puedes incluirlo si lo deseas
        '.env',        # Puedes incluirlo si lo deseas
    ]

    # Excluir por nombre exacto
    if name in exclude_patterns:
        return True

    # Excluir por extensión
    for pattern in exclude_patterns:
        if pattern.startswith('.') and name.endswith(pattern):
            return True

    # Excluir directorios de librerías comunes
    if 'site-packages' in path or 'venv' in path or 'Lib' in path:
        return True

    return False

def generate_clean_structure(startpath, output_file='estructura_limpia.txt'):
    """
    Genera un archivo de texto con la estructura de carpetas limpia.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(startpath):
            # Filtrar carpetas a excluir *antes* de recorrerlas (optimización)
            dirs[:] = [d for d in dirs if not should_exclude(d, root)]
            
            level = root.replace(startpath, '').count(os.sep)
            indent = '│   ' * level
            f.write(f'{indent}├── {os.path.basename(root)}/\n')

            # Escribir archivos (filtrados)
            subindent = '│   ' * (level + 1)
            for file in files:
                if not should_exclude(file, root):
                    f.write(f'{subindent}├── {file}\n')

    print(f"Estructura limpia guardada en: {output_file}")

# 📁 Define aquí la ruta raíz de tu proyecto
PROJECT_ROOT = r"C:\automation-framework-vita"

# 🚀 Ejecutar
generate_clean_structure(PROJECT_ROOT)