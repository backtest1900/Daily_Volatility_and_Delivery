
import dash_bootstrap_components as dbc
from dash import dash, Input, Output, dcc, html,dash_table
import pandas as pd
# from dash.dependencies import Input, Output
from datetime import date

# Connect to main app.py file
from app import app


# Functions 
# https://archives.nseindia.com/products/content/sec_bhavdata_full_18112022.csv

def generate_table(date):
    df = pd.read_csv(f'https://www1.nseindia.com/archives/nsccl/volt/CMVOLT_{date}.CSV', header=None)
    df.drop(df.columns[[2, 3, 4, 5, 7]], axis=1, inplace=True)
    df.rename({6: 'DV', 0: 'Date', 1: 'Name'}, axis=1, inplace=True)
    # print(df)

    df1 = pd.read_csv(f'https://archives.nseindia.com/products/content/sec_bhavdata_full_{date}.csv', header=None)
    df1.drop(df1.columns[[3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12]], axis=1, inplace=True)
    df1.rename({0 : 'Name', 1: 'Series', 2: 'Date', 13: 'Delivery_Qty', 14: 'Delivery_%'}, axis=1, inplace=True)
    df1['Series'].str.replace(' ', '')
    df1 =  df1.loc[(df1['Series'] == ' EQ')]
    # print(df1)

    df2 = pd.read_csv(f'https://archives.nseindia.com/content/fo/fo_mktlots.csv', header=None, skipinitialspace = True)
    df2.drop(df2.columns[[0,2,3,4,5,6,7,8,9,10,11,11,12,13,14,15]], axis=1, inplace=True)
    df2.rename({1 : 'Name'}, axis=1, inplace=True)
    df2 = df2['Name'].str.strip()
    df2 = df2.drop([df2.index[0], df2.index[1], df2.index[2], df2.index[3], df2.index[4], df2.index[5]])
    df2 = df2.reset_index()
    df2.drop(df2.columns[[0]], axis=1, inplace=True)
    # print(df2)

    aa = df[df['Name'].isin(df2['Name'])]
    # print(aa)

    bb = df1[df1['Name'].isin(df2['Name'])]
    # print(bb)

    df3 = pd.merge(aa, bb, on="Name", how="left")
    df3.drop(df3.columns[[3, 4]], axis=1, inplace=True)
    df3['Volatility'] = df3['DV'].astype(float)
    df3["Volatility_%"] = round(df3['Volatility'] * 100,2)
    df3.drop(df3.columns[[2,5]], axis=1, inplace=True)
    order = [0,1,4,3,2] # setting column's order
    df3.rename({'ate_x': 'Date'}, axis=1, inplace=True)
    df3 = df3[[df3.columns[i] for i in order]]
    # print(df3)
    return dash_table.DataTable(df3.to_dict('records'),  [{"name": i, "id": i} for i in df3.columns], sort_action='native',)

# Functions

# Define the page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H4(children='NSE Stocks Daily Volatility')),
        html.Br(),
        html.Hr(),
        html.Center(html.H5(children='* Only trading days data available from (Mon - Fri) days date. Please select sny other trading date... '),style={"color": "red"}),
        # dbc.Col([
        #     html.P("This is column 1."), 
        #     dbc.Button("Test Button", color="primary")
        # ]), 
        dbc.Col([
            dcc.DatePickerSingle(
            id='my-date-picker-single',
            min_date_allowed=date(2000, 1, 1),
            max_date_allowed=date(2099, 12, 31),
            initial_visible_month=date.today(),
            date=date.today()),
            html.Div(id='output-container-date-picker-single'),  
        ])
    ])
])

@app.callback(
    Output('output-container-date-picker-single', 'children'),
    Input('my-date-picker-single', 'date'))

def update_output(date_value):
    if date_value is not None:
        date_object = date.fromisoformat(date_value)
        date_string = date_object.strftime('%d%m%Y')
        return generate_table(date_string) 
    else:
        return "Today Holiday Please Select Any Other Date.."

    
# def update_output(n_clicks):
#     if n_clicks is None:
#         raise PreventUpdate
#     else:
#         return "Elephants are the only animal that can't jump"
