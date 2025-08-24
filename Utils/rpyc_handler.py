import os
from rpycdec import decompile

def extract_rpyc(file_path, output_dir):
    """
    Decompila um arquivo .rpyc e salva na pasta de saída.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = os.path.basename(file_path)
    dest_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".rpy")

    decompile(file_path, dest_file)

