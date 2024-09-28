import pandas as pd
from sqlalchemy import create_engine, text

# Conectando ao banco PostgreSQL
engine = create_engine('postgresql://postgres:123456@localhost:5432/postgres')

# Lendo o arquivo CSV
df = pd.read_csv('C:/Users/renat/Documents/Projetos Aula/Aula Disruptive/DATA_PIPELINE/IOT-temp.csv')

# Convertendo a coluna noted_date para o formato correto
df['noted_date'] = pd.to_datetime(df['noted_date'], format='%d-%m-%Y %H:%M')

# Inserindo os dados no banco de dados
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

