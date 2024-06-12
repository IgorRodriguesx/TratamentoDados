# Transformação de arquivo CSV

import csv
import chardet
import pandas as pd

# Nome do arquivo CSV no formato Unix
file_name = '/root/tratamentoDados/env-trat/relatorio_sessoes.csv'

try:
    with open(file_name, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']
    
    df = pd.read_csv(file_name, encoding=encoding)
    output_file_name = '/root/tratamentoDados/env-trat/relatorio_sessoes_corrigido.csv'
    df.to_csv(output_file_name, index=False, encoding='utf-8')
    print(f'Arquivo corrigido salvo como {output_file_name}')
except FileNotFoundError:
    print(f'Erro: O arquivo {file_name} não foi encontrado. Verifique o caminho e o nome do arquivo.')

