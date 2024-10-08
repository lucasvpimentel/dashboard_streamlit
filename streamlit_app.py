import streamlit as st
import pandas as pd 
import plotly.express as px

st.title('DASHBOARD RECLAMAÇÕES')

# streamlit run streamlit_app.py


empresa = st.selectbox('SELECIONE A EMPRESA',
                        ['Hapvida','Ibyte', 'Nagem'])


df_hapvida_silver = pd.read_csv('csv_treated/hapvida/silver_hapvida.csv')
df_ibyte_silver = pd.read_csv('csv_treated/ibyte/silver_ibyte.csv')
df_nagem_silver = pd.read_csv('csv_treated/nagem/silver_nagem.csv')

status = st.selectbox('SELECIONE O STATUS',
                    ['Não respondida', 'Respondida',
                    'Resolvido', 'Em réplica','Não resolvido'],
                    index = 0)

col1 , col2 = st.columns(2)
with col1:
    total = df_hapvida_silver['STATUS'].value_counts().sum() + df_ibyte_silver['STATUS'].value_counts().sum() + df_nagem_silver.value_counts().sum()
    st.metric(label='TOTAL RECLAMAÇÕES',
            value=total)
with col2:
    temp = df_hapvida_silver['STATUS'].value_counts().loc[status] + df_ibyte_silver['STATUS'].value_counts().loc[status] + df_nagem_silver['STATUS'].value_counts().loc[status]
    st.metric(label= status.upper(),
              value=temp)


    


st.markdown('---')

#### Series temporais Número de Reclamações

if empresa == 'Hapvida':  
    df_hapvida = pd.read_csv('csv_treated/hapvida/time_series.csv')
    df_estado = pd.read_csv('csv_treated/hapvida/by_state.csv')


    lista_estados = ['TODOS'] + list(df_hapvida_silver['ESTADO'].unique())

    
    estado = st.selectbox('SELECIONE O ESTADO',
                            lista_estados,
                              index= 0)


    if estado == 'TODOS':
        
        # Série Temporal
        
        st.header(f'Reclamações ao longo do tempo - {empresa}')

        fig = px.line(df_hapvida, x = 'MES_ANO', y = 'TOTAL_RECLAMACOES')

        fig.update_layout(
            xaxis_title='DATA',
            yaxis_title='RECLAMAÇÕES'
        )

        st.plotly_chart(fig)
        ################################

        # Reclamações por Estado
        st.header(f'Reclamações por Estado - {empresa}')

        fig2 = px.bar(df_estado, x= 'ESTADO', y='TOTAL_RECLAMACOES')

        fig2.update_layout(
            xaxis_title='ESTADO',
            yaxis_title='RECLAMAÇÕES'
        )

        st.plotly_chart(fig2)
        ##############################################

        # Status    
        df_status = pd.read_csv('csv_treated/hapvida/status.csv')
        st.header(f'Status Reclamações  - {empresa}')

        df_status = pd.read_csv('csv_treated/hapvida/status.csv')

        fig3 = px.bar(df_status, x= 'STATUS', y='STATUS_RECLAMACOES')

        fig3.update_layout(
            xaxis_title='STATUS',
            yaxis_title='QUANTIDADE'
        )

        st.plotly_chart(fig3)

        # Quantatidade de Caracteres

        st.header(f'Quantidade de Caracteres por Reclamação  - {empresa}')

        df_char = pd.read_csv('csv_treated/hapvida/size_compl.csv')

        fig4 = px.histogram(df_char, x='TAMANHO_TEXTO', nbins=100)

        fig4.update_layout(
            xaxis_title='TAMANHO TEXTO',
            yaxis_title='QUANTIDADE DE CARACTERES'
        )

        st.plotly_chart(fig4)
    else:
        df_hapvida_gold = df_hapvida_silver[df_hapvida_silver['ESTADO'] == estado]

        # Série Temporal
        
        st.header(f'Reclamações ao longo do tempo - {empresa} - {estado}')


        fig1 = px.line(df_hapvida_gold.groupby('MES_ANO').size().reset_index(name='TOTAL_RECLAMACOES'),
                        x = 'MES_ANO',
                          y = 'TOTAL_RECLAMACOES')

        fig1.update_layout(
            xaxis_title='DATA',
            yaxis_title='RECLAMAÇÕES'
        )

        st.plotly_chart(fig1)


        # Reclamações por Estado
        st.header(f'Reclamações por Estado - {empresa} - {estado}')

        st.metric(label='RECLAMAÇÕES', value= df_hapvida_gold.groupby('ESTADO').size().values[0])

        # Status    
        st.header(f'Status Reclamações  - {empresa} - {estado}')
    

        fig3 = px.bar(df_hapvida_gold.groupby('STATUS').size().reset_index(name='STATUS_RECLAMACOES')
                      , x= 'STATUS',
                        y='STATUS_RECLAMACOES')

        fig3.update_layout(
            xaxis_title='STATUS',
            yaxis_title='QUANTIDADE'
        )

        st.plotly_chart(fig3)


        # Quantatidade de Caracteres

        st.header(f'Quantidade de Caracteres por Reclamação  - {empresa} - {estado}')


        fig4 = px.histogram(df_hapvida_gold, x='TAMANHO_TEXTO', nbins=100)

        fig4.update_layout(
            xaxis_title='TAMANHO TEXTO',
            yaxis_title='QUANTIDADE DE CARACTERES'
        )

        st.plotly_chart(fig4)

elif empresa == 'Ibyte':
    df_ibyte = pd.read_csv('csv_treated/ibyte/time_series.csv')
    df_estado = pd.read_csv('csv_treated/ibyte/by_state.csv')
    

    lista_estados = ['TODOS'] + list(df_ibyte_silver['ESTADO'].unique())

    
    estado = st.selectbox('SELECIONE O ESTADO',
                            lista_estados,
                              index= 0)


    if estado == 'TODOS':
        
        # Série Temporal
        
        st.header(f'Reclamações ao longo do tempo - {empresa}')

        fig = px.line(df_ibyte, x = 'MES_ANO', y = 'TOTAL_RECLAMACOES')

        fig.update_layout(
            xaxis_title='DATA',
            yaxis_title='RECLAMAÇÕES'
        )

        st.plotly_chart(fig)
        ################################

        # Reclamações por Estado
        st.header(f'Reclamações por Estado - {empresa}')

        fig2 = px.bar(df_estado, x= 'ESTADO', y='TOTAL_RECLAMACOES')

        fig2.update_layout(
            xaxis_title='ESTADO',
            yaxis_title='RECLAMAÇÕES'
        )

        st.plotly_chart(fig2)
        ##############################################

        # Status    
        df_status = pd.read_csv('csv_treated/ibyte/status.csv')
        st.header(f'Status Reclamações  - {empresa}')

        df_status = pd.read_csv('csv_treated/ibyte/status.csv')

        fig3 = px.bar(df_status,
                       x='STATUS',
                       y='QUANTIDADE')

        fig3.update_layout(
            xaxis_title='STATUS',
            yaxis_title='QUANTIDADE'
        )

        st.plotly_chart(fig3)

        # Quantatidade de Caracteres

        st.header(f'Quantidade de Caracteres por Reclamação  - {empresa}')

        df_char = pd.read_csv('csv_treated/ibyte/size_compl.csv')

        fig4 = px.histogram(df_char, x='TAMANHO_TEXTO', nbins=100)

        fig4.update_layout(
            xaxis_title='TAMANHO TEXTO',
            yaxis_title='QUANTIDADE DE CARACTERES'
        )

        st.plotly_chart(fig4)
    else:
        df_ibyte_gold = df_ibyte_silver[df_ibyte_silver['ESTADO'] == estado]

        # Série Temporal

        st.header(f'Reclamações ao longo do tempo - {empresa} - {estado}')


        fig1 = px.line(df_ibyte_gold.groupby('MES_ANO').size().reset_index(name='TOTAL_RECLAMACOES'),
                        x = 'MES_ANO',
                        y = 'TOTAL_RECLAMACOES')

        fig1.update_layout(
            xaxis_title='DATA',
            yaxis_title='RECLAMAÇÕES'
        )

        st.plotly_chart(fig1)


        # Reclamações por Estado
        st.header(f'Reclamações por Estado - {empresa} - {estado}')

        st.metric(label='RECLAMAÇÕES', value= df_ibyte_gold.groupby('ESTADO').size().values[0])

        # Status    
        st.header(f'Status Reclamações  - {empresa} - {estado}')


        fig3 = px.bar(df_ibyte_gold.groupby('STATUS').size().reset_index(name='STATUS_RECLAMACOES')
                    , x= 'STATUS',
                        y='STATUS_RECLAMACOES')

        fig3.update_layout(
            xaxis_title='STATUS',
            yaxis_title='QUANTIDADE'
        )

        st.plotly_chart(fig3)


        # Quantatidade de Caracteres

        st.header(f'Quantidade de Caracteres por Reclamação  - {empresa} - {estado}')


        fig4 = px.histogram(df_ibyte_gold, x='TAMANHO_TEXTO', nbins=100)

        fig4.update_layout(
            xaxis_title='TAMANHO TEXTO',
            yaxis_title='QUANTIDADE DE CARACTERES'
        )

        st.plotly_chart(fig4)

else:
    df_nagem = pd.read_csv('csv_treated/nagem/time_series.csv')
    df_estado = pd.read_csv('csv_treated/nagem/by_state.csv')


    lista_estados = ['TODOS'] + list(df_nagem_silver['ESTADO'].unique())

    
    estado = st.selectbox('SELECIONE O ESTADO',
                            lista_estados,
                            index= 0)


    if estado == 'TODOS':
        
        # Série Temporal
        
        st.header(f'Reclamações ao longo do tempo - {empresa}')

        fig = px.line(df_nagem, x = 'MES_ANO', y = 'TOTAL_RECLAMACOES')

        fig.update_layout(
            xaxis_title='DATA',
            yaxis_title='RECLAMAÇÕES'
        )

        st.plotly_chart(fig)
        ################################

        # Reclamações por Estado
        st.header(f'Reclamações por Estado - {empresa}')

        fig2 = px.bar(df_estado, x= 'ESTADO', y='TOTAL_RECLAMACOES')

        fig2.update_layout(
            xaxis_title='ESTADO',
            yaxis_title='RECLAMAÇÕES'
        )

        st.plotly_chart(fig2)
        ##############################################

        # Status    
        df_status = pd.read_csv('csv_treated/ibyte/status.csv')
        st.header(f'Status Reclamações  - {empresa}')

        df_status = pd.read_csv('csv_treated/ibyte/status.csv')

        fig3 = px.bar(df_status,
                       x='STATUS',
                       y='QUANTIDADE')

        fig3.update_layout(
            xaxis_title='STATUS',
            yaxis_title='QUANTIDADE'
        )

        st.plotly_chart(fig3)

        # Quantatidade de Caracteres

        st.header(f'Quantidade de Caracteres por Reclamação  - {empresa}')

        df_char = pd.read_csv('csv_treated/ibyte/size_compl.csv')

        fig4 = px.histogram(df_char, x='TAMANHO_TEXTO', nbins=100)

        fig4.update_layout(
            xaxis_title='TAMANHO TEXTO',
            yaxis_title='QUANTIDADE DE CARACTERES'
        )

        st.plotly_chart(fig4)
    else:
        df_nagem_gold = df_nagem_silver[df_nagem_silver['ESTADO'] == estado]

        # Série Temporal

        st.header(f'Reclamações ao longo do tempo - {empresa} - {estado}')


        fig1 = px.line(df_nagem_gold.groupby('MES_ANO').size().reset_index(name='TOTAL_RECLAMACOES'),
                        x = 'MES_ANO',
                        y = 'TOTAL_RECLAMACOES')

        fig1.update_layout(
            xaxis_title='DATA',
            yaxis_title='RECLAMAÇÕES'
        )

        st.plotly_chart(fig1)


        # Reclamações por Estado
        st.header(f'Reclamações por Estado - {empresa} - {estado}')

        st.metric(label='RECLAMAÇÕES', value= df_nagem_gold.groupby('ESTADO').size().values[0])

        # Status    
        st.header(f'Status Reclamações  - {empresa} - {estado}')


        fig3 = px.bar(df_nagem_gold.groupby('STATUS').size().reset_index(name='STATUS_RECLAMACOES')
                    , x= 'STATUS',
                        y='STATUS_RECLAMACOES')

        fig3.update_layout(
            xaxis_title='STATUS',
            yaxis_title='QUANTIDADE'
        )

        st.plotly_chart(fig3)


        # Quantatidade de Caracteres

        st.header(f'Quantidade de Caracteres por Reclamação  - {empresa} - {estado}')


        fig4 = px.histogram(df_nagem_gold, x='TAMANHO_TEXTO', nbins=100)

        fig4.update_layout(
            xaxis_title='TAMANHO TEXTO',
            yaxis_title='QUANTIDADE DE CARACTERES'
        )

        st.plotly_chart(fig4)





    
    
    
    