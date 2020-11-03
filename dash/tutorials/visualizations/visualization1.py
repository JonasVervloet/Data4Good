import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import json


external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

df = pd.DataFrame({
    'x': [1, 2, 1, 2],
    'y': [1, 2, 3, 4],
    'customdata': [1, 2, 3, 4],
    'fruit': ['apple', 'apple', 'orange', 'orange']
})

fig = px.scatter(
    df,
    x='x',
    y='y',
    color='fruit',
    custom_data=['customdata']
)

fig.update_layout(
    clickmode='event+select'
)

fig.update_traces(
    marker_size=20
)

app.layout = html.Div(
    children=[
        dcc.Graph(
            id='basic-interactions',
            figure=fig
        ),
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='three columns',
                    children=[
                        dcc.Markdown("""
                        **Hover Data**
                        Mouse over values in the graph.
                        """),
                        html.Pre(
                            id='hover-data',
                            style=styles['pre']
                        )
                    ]
                ),

                html.Div(
                    className='three-columns',
                    children=[
                        dcc.Markdown("""
                        **Click Data**
                        Click on points in the graph.
                        """),
                        html.Pre(
                            id='click-data',
                            style=styles['pre']
                        )
                    ]
                ),

                html.Div(
                    className='three-columns',
                    children=[
                        dcc.Markdown("""
                        **Selection Data**
                        
                        Choose the lasso or rectangle tool in the graph's menu
                        bar and then select points in the graph.
                        
                        Note that if `layout.clickmode = 'event+select'`, selection data also
                        accumulates (or un-accumulates) selected data if you hold down the shift
                        button while clicking.
                        """),
                        html.Pre(
                            id='selected-data',
                            style=styles['pre']
                        )
                    ]
                ),

                html.Div(
                    className='three-columns',
                    children=[
                        dcc.Markdown("""
                        **Zoom and Relayout Data**
                        
                        Click and drag on the graph to zoom or click on the zoom
                        buttons in the graph's menu bar.
                        
                        Clicking on legend items also fires this event.
                        """),
                        html.Pre(
                            id='relayout-data',
                            style=styles['pre']
                        )
                    ]
                )
            ]
        )
    ]
)


@app.callback(
    Output(
        component_id='hover-data',
        component_property='children'
    ),
    [
        Input(
            'basic-interactions',
            'hoverData'
        )
    ]
)
def display_hover_data(hover_data):
    return json.dumps(
        hover_data,
        indent=2
    )


@app.callback(
    Output(
        component_id='click-data',
        component_property='children'
    ),
    [
        Input(
            component_id='basic-interactions',
            component_property='clickData'
        )
    ]
)
def display_click_data(click_data):
    return json.dumps(click_data, indent=2)


@app.callback(
    Output(
        component_id='selected-data',
        component_property='children'
    ),
    [
        Input(
            component_id='basic-interactions',
            component_property='selectedData'
        )
    ]
)
def display_selected_data(selected_data):
    return json.dumps(selected_data, indent=2)


@app.callback(
    Output(
        component_id='relayout-data',
        component_property='children'
    ),
    [
        Input(
            component_id='basic-interactions',
            component_property='relayoutData'
        )
    ]
)
def display_relayout_data(relayout_data):
    return json.dumps(relayout_data, indent=2)


if __name__ == '__main__':
    app.run_server(
        debug=True
    )