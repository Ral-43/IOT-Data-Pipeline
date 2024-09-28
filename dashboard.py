import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import streamlit as st

# Conexão com o banco de dados
engine = create_engine('postgresql://postgres:123456@localhost:5432/postgres')

# Função para carregar dados de uma view
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# Função para criar gráficos
def create_plot(df, x, y, title, kind='line'):
    fig = px.line(df, x=x, y=y, title=title)
    fig.update_layout(xaxis_title=x.capitalize(), yaxis_title=y.capitalize())
    return fig

# Título do dashboard
st.title('Dashboard de Temperaturas IoT')

# Seleção da view
view_options = [
    'correlation_between_temp_and_location',
    'temp_trends_by_location',
    'average_temp_by_hour'
]
selected_view = st.selectbox('Selecione a view:', view_options)

# Carregar os dados da view selecionada
df = load_data(selected_view)

# Gráfico
if selected_view == 'correlation_between_temp_and_location':
    
    fig = px.bar(df, x='location', y=['average_temp', 'stddev_temp'], title='Correlação entre Temperatura e Local')
elif selected_view == 'temp_trends_by_location':
   
    fig = px.line(df, x='noted_date', y='moving_average', color='location', title='Tendência de Temperatura por Local')
elif selected_view == 'average_temp_by_hour':
    fig = px.line(df, x='hour', y='average_temp', title='Média de Temperatura por Hora do Dia')

st.plotly_chart(fig)