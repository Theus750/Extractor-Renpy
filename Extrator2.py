import os
import sys
import shutil
from Utils.rpyc_handler import extract_rpyc as original_extract_rpyc

def extract_dialogs_by_character(file_path, output_dir):
    """
    Decompila .rpyc e extrai diálogos agrupados por personagem.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    filename = os.path.basename(file_path)
    dest_file = os.path.join(output_dir, os.path.splitext(filename)[0] + "_dialogs.txt")
    
    try:
        from unrpyc import decompile
        # Decompila parcialmente
        decompile(file_path, dest_file)
        
        # Processa o arquivo para organizar diálogos por personagem
        with open(dest_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        dialogs_by_character = []
        current_character = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            # Detecta possível personagem (ex: label ou personagem seguido de ":")
            if ":" in line and not line.startswith('"') and not line.startswith("'"):
                parts = line.split(":", 1)
                char, text = parts[0].strip(), parts[1].strip()
                dialogs_by_character.append(f"{char}: {text}")
            elif line.startswith('"') or line.startswith("'"):
                text = line.strip('"').strip("'")
                if current_character:
                    dialogs_by_character.append(f"{current_character}: {text}")
                else:
                    dialogs_by_character.append(f"UNKNOWN: {text}")
            else:
                # Mantém linha como comentário ou ignorada
                continue

        # Salva o resultado
        with open(dest_file, "w", encoding="utf-8") as f:
            f.write("\n".join(dialogs_by_character))
            
    except Exception as e:
        with open(dest_file, "w", encoding="utf-8") as f:
            f.write("# Não foi possível extrair diálogos corretamente\n")
        print(f"[!] Atenção: {filename} não pôde ser processado totalmente.")

def process_file(file_path, output_dir, base_dir):
    """
    Processa arquivo individual: se for .rpyc extrai diálogos, se for .rpy copia.
    Mantém a estrutura de subpastas relativa a base_dir.
    """
    rel_path = os.path.relpath(file_path, base_dir)
    dest_folder = os.path.join(output_dir, os.path.dirname(rel_path))
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".rpyc":
        print(f"[+] Extraindo diálogos de {file_path}...")
        extract_dialogs_by_character(file_path, dest_folder)
    elif ext == ".rpy":
        print(f"[+] Copiando {file_path}...")
        shutil.copy2(file_path, os.path.join(dest_folder, os.path.basename(file_path)))
    else:
        print(f"[-] Ignorando {file_path}: formato não suportado.")

def main(input_path, output_dir="output"):
    """
    Processa arquivo ou pasta inteira.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if os.path.isfile(input_path):
        process_file(input_path, output_dir, os.path.dirname(input_path))
    elif os.path.isdir(input_path):
        for root, dirs, files in os.walk(input_path):
            for file in files:
                full_path = os.path.join(root, file)
                process_file(full_path, output_dir, input_path)
    else:
        print("[-] Caminho inválido.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python extractor.py <arquivo_ou_pasta> [saida]")
    else:
        input_path = sys.argv[1]
        output_dir = sys.argv[2] if len(sys.argv) > 2 else "output"
        main(input_path, output_dir)
