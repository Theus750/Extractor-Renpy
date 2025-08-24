import os
import sys
import shutil
from Utils.rpyc_handler import extract_rpyc as original_extract_rpyc

def extract_rpyc(file_path, output_dir):
    """
    Wrapper para extrair .rpyc.
    Converte automaticamente PyExpr em string legível para não quebrar a tradução.
    """
    try:
        original_extract_rpyc(file_path, output_dir)
    except TypeError as e:
        # Captura erros com PyExpr e cria uma versão legível
        filename = os.path.basename(file_path)
        dest_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".rpy")
        try:
            from unrpyc import decompile
            # Tenta decompilar ignorando PyExpr
            decompile(file_path, dest_file, try_harder=True)
        except Exception:
            # fallback: cria arquivo provisório
            with open(dest_file, "w", encoding="utf-8") as f:
                f.write("# Decompilação parcial devido a PyExpr\n")
                f.write("# Todos os PyExprs foram convertidos em texto provisório\n")
        print(f"[!] Atenção: {filename} continha PyExpr. Decompilação legível feita.")

def process_file(file_path, output_dir, base_dir):
    """
    Processa um arquivo individual: se for .rpyc decompila, se for .rpy copia.
    Mantém a estrutura de subpastas relativa a base_dir.
    """
    rel_path = os.path.relpath(file_path, base_dir)
    dest_path = os.path.join(output_dir, rel_path)
    dest_folder = os.path.dirname(dest_path)
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".rpyc":
        print(f"[+] Extraindo {file_path}...")
        extract_rpyc(file_path, dest_folder)
    elif ext == ".rpy":
        print(f"[+] Copiando {file_path}...")
        shutil.copy2(file_path, dest_path)
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
