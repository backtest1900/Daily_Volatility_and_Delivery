# Import necessary libraries 
import dash
from dash import html
import dash_bootstrap_components as dbc

### Add the page components here 
# table_header = [
#     html.Thead(html.Tr([html.Th("First Name"), html.Th("Last Name")]))
# ]

# row1 = html.Tr([html.Td("Arthur"), html.Td("Dent")])
# row2 = html.Tr([html.Td("Ford"), html.Td("Prefect")])
# row3 = html.Tr([html.Td("Zaphod"), html.Td("Beeblebrox")])
# row4 = html.Tr([html.Td("Trillian"), html.Td("Astra")])

# table_body = [html.Tbody([row1, row2, row3, row4])]

# page2_table = dbc.Table(table_header + table_body, bordered=True)

# Define the final page layout
layout = dbc.Container([
    dbc.Row([
        html.Center(html.H1("About Us")),
        html.Br(),
        html.Hr(),
        # dbc.Col([
        #     html.P("This is column 1."), 
        #     dbc.Button("Test Button", color="secondary")
        # ]), 
        dbc.Col([
            html.Center(html.H1("Badshah Algo World"),style={"color": "blue"}), 
            html.Br(),
            html.P("At Badshah Algo World, you will get to solve some extremely challenging, algo trading, trading strategy and big data problems to shape the future of this lucrative industry while working alongside other exceptional programmers, quants and traders. In a nutshell, you become part of the best in the industry to work on creating something awesome!", style={ "font-size": '24px',   "font-family": "Times New Roman"}),
            # page2_table
        ])
    ])
])