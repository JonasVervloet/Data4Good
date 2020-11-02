import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv'
)


def generate_table(data_frame, max_row=10):
    return html.Table(
        children=[
            html.Thead(
                html.Tr(
                    [html.Th(col) for col in data_frame.columns]
                )
            ),
            html.Tbody([
                html.Tr([
                    html.Td(data_frame.iloc[i][col]) for col in data_frame.columns
                ]) for i in range(min(len(data_frame), max_row))
            ])
        ]
    )


external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

app.layout = html.Div(
    children=[
        html.H4(
            children='US Agriculture Exports (2011)'
        ),
        generate_table(
            data_frame=df
        )
    ]
)

if __name__ == '__main__':
    app.run_server(
        debug=True
    )