import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = [
    "https://codepen.io/chriddyp/pen/bWLwgP.css"
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

app.layout = html.Div(
    children=[
        dcc.Input(
            id='input-1-state',
            type='text',
            value='Montréal'
        ),
        dcc.Input(
            id='input-2-state',
            type='text',
            value='Canada'
        ),
        html.Button(
            id='submit-button-state',
            n_clicks=0,
            children='Submit'
        ),
        html.Div(
            id='output-state'
        )
    ]
)


@app.callback(
    Output(
        component_id='output-state',
        component_property='children'
    ),
    [
        Input(
            component_id='submit-button-state',
            component_property='n_clicks'
        )
    ],
    [
        State(
            component_id='input-1-state',
            component_property='value'
        ),
        State(
            component_id='input-2-state',
            component_property='value'
        )
    ]
)
def update_output(nb_clicks, input1, input2):
    return '''
    The button has been pressed {} times,
    Input 1 is {},
    and Input 2 is {}
    '''.format(
        nb_clicks,
        input1,
        input2
    )


if __name__ == '__main__':
    app.run_server(
        debug=True
    )