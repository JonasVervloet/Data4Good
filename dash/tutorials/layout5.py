import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

options_list = [
    {
        'label': 'New York City',
        'value': 'NYC'
    },
    {
        'label': 'Montreal',
        'value': 'MTL'
    },
    {
        'label': 'San Francisco',
        'value': 'SF'
    }
]

app.layout = html.Div(
    children=[
        html.Label(
            children='Drop down'
        ),
        dcc.Dropdown(
            options=options_list,
            value='MTL'
        ),

        html.Label(
            children='Radio Items'
        ),
        dcc.RadioItems(
            options=options_list,
            value='MTL'
        ),

        html.Label(
            children='Checkboxes'
        ),
        dcc.Checklist(
            options=options_list,
            value=['MTL', 'SF']
        ),

        html.Label(
            children='Text Input'
        ),
        dcc.Input(
            value='MTL',
            type='text'
        ),

        html.Label(
            children='Slider'
        ),
        dcc.Slider(
            min=0,
            max=9,
            marks={
                i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)
            },
            value=5
        )
    ],
    style={
        'columnCount': 2
    }
)

if __name__ == '__main__':
    app.run_server(
        debug=True
    )
