import plotly.express as px
import numpy as np

# Plot Function
def interactive_plot(df):
    fig = px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x=df['Date'], y=df[i], name=i)
    fig.update_layout(width=450, margin=dict(l=20, r=20, t=50, b=50), legend=dict(orientation='h',yanchor='bottom', y=1.02, xanchor='right',x=1))
    return fig

#Normalising Function based on initial Price
def normalize(df_2):
    df = df_2.copy()
    #Skip First column
    for i in df.columns[1:]:
        #take first price and based on that normalize the prices
        df[i] = df[i]/df[i][0]
    return df

#Calculate Daily returns and stock performance
def daily_return(df):
    df_daily_return = df.copy()
    for i in df.columns[1:]:
        for j in range(1,len(df)):
            #calculating daily returns
            df_daily_return[i][j] = ((df[i][j]-df[i][j-1])/df[i][j-1])*100
        df_daily_return[i][0] = 0
    return df_daily_return

#fucntion to calculae
def calculate_beta(stocks_daily_return, stocks):
    rm = stocks_daily_return['sp500'].mean()*252
    b, a = np.polyfit(stocks_daily_return['sp500'], stocks_daily_return[stocks],1)
    return b,a