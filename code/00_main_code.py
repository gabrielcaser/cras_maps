# Description - Main Code

# Settings
random.seed(1234)

# Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Oppening dataset
df_cras = pd.read_excel('/data/raw/Resultado ES (Completo).xlsx', sheet_name='CRAS')
# Keeping only relevant variables
df_cras = df_cras[['ID CRAS', 'NOME', 'CIDADE', 'ENDEREÇO', 'QUANTIDADE DE AVALIAÇÕES', 'NOTA']]

# Renomeando variáveis para ficarem com nomes padronizados
df_cras = df_cras.rename(columns={'ID CRAS': 'id_cras', 'NOME': 'nome_cras', 'CIDADE': 'cidade', 'ENDEREÇO': 'endereco', 'QUANTIDADE DE AVALIAÇÕES': 'n_avaliacoes', 'NOTA': 'nota_cras'})
