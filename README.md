- Projeto: Dashboard de Temperaturas IoT
Este documento descreve o projeto Dashboard de Temperaturas IoT, que consiste em dois scripts Python (pipeline.py e dashboard.py) e três views criadas no banco de dados PostgreSQL.

Objetivo
O objetivo do projeto é coletar dados de temperatura de um sensor IoT, armazená-los em um banco de dados e criar um dashboard interativo para análise visual da temperatura.

Pré-requisitos
Python 3.x
pandas
sqlalchemy
streamlit
plotly.express
PostgreSQL (servidor e cliente)
Configuração
Instalar as bibliotecas:
pip install pandas sqlalchemy streamlit plotly-express
Criar o banco de dados PostgreSQL:

Configure o servidor PostgreSQL de acordo com sua preferência.
Crie um banco de dados chamado postgres (ou outro nome de sua escolha).
Copiar os arquivos:

Copie os arquivos pipeline.py, dashboard.py, e as instruções para criar as views (incluídas neste README) para um diretório de trabalho.
Modificar credenciais do banco de dados (opcional):

Abra o arquivo pipeline.py e dashboard.py.
Edite a string de conexão ao banco de dados (engine = create_engine(...)) para refletir suas credenciais (nome do host, usuário, senha e nome do banco de dados).
Execução
Carregar dados no banco de dados (executar uma vez):

Abra um terminal ou prompt de comando e navegue até o diretório de trabalho do projeto.
Execute o comando: python pipeline.py
Este script lerá os dados do arquivo CSV (IOT-temp.csv) e os carregará na tabela temperature_readings no banco de dados PostgreSQL.
Alterar as colunas da tabela de room_id/id para room_id e out/in para location

Foram criadas 3 Views:
-- View para calcular a correlação entre temperatura e local 
CREATE VIEW correlation_between_temp_and_location AS SELECT location, AVG(temp) AS average_temp, STDDEV(temp) AS stddev_temp FROM public.temperature_readings GROUP BY location; 
-- View para identificar tendências de temperatura por local 
CREATE VIEW temp_trends_by_location AS SELECT location, noted_date, AVG(temp) OVER (PARTITION BY location ORDER BY noted_date) AS moving_average FROM public.temperature_readings; 
-- View para calcular a média de temperatura por hora do dia 
CREATE VIEW average_temp_by_hour AS SELECT EXTRACT(HOUR FROM noted_date) AS hour, AVG(temp) AS average_temp FROM public.temperature_readings GROUP BY hour;

Iniciar o dashboard:

Execute o comando: streamlit run dashboard.py
Isso abrirá o dashboard em seu navegador web padrão (http://localhost:5432).
O que o Dashboard Faz?
Conecta-se ao banco de dados PostgreSQL para recuperar os dados de temperatura.
Oferece três views selecionáveis:
Correlação entre temperatura e local: Mostra a média e o desvio padrão da temperatura para ambientes internos e externos.
Tendência de temperatura por local: Visualiza a média móvel da temperatura ao longo do tempo para cada local.
Média de temperatura por hora do dia: Exibe a variação da temperatura média ao longo de um dia (24 horas).
Utiliza gráficos interativos para facilitar a visualização e análise dos dados.

Views do Banco de Dados
As views no banco de dados foram criadas para facilitar a consulta e análise dos dados:

correlation_between_temp_and_location: Calcula a média e o desvio padrão da temperatura por local (interno ou externo).
temp_trends_by_location: Calcula a média móvel da temperatura por local ao longo do tempo.
average_temp_by_hour: Calcula a média de temperatura por hora do dia.
