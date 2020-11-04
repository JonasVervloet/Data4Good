import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


compas_df = pd.read_csv('./docs/compas.csv')
doj_df = pd.read_csv('./docs/DOJ_summary_statistics.csv')

race_value_count = compas_df['race'].value_counts()
race_value_count_df = pd.DataFrame({
    'race': race_value_count.keys(),
    'count': race_value_count.values
})

race_count_fig = px.bar(race_value_count_df, x="race", y="count", color="race")

race_list = []
count_list = []
rate_list = []

for race in race_value_count.keys():
    race_selec = compas_df[compas_df['race'] == race]
    race_count = len(race_selec)

    true_samples = race_selec[
        race_selec['is_recidivist'] == 1
    ]
    true_pos_smpls = true_samples[
        true_samples['prediction'] == 1
        ]
    false_neg_smpls = true_samples[
        true_samples['prediction'] == 0
        ]

    false_samples = race_selec[
        race_selec['is_recidivist'] == 0
    ]
    false_pos_smpls = false_samples[
        false_samples['prediction'] == 1
        ]
    true_neg_smpls = false_samples[
        false_samples['prediction'] == 0
        ]

    race_list += [race, race, race, race]
    count_list += [
        len(true_pos_smpls)/race_count,
        len(false_neg_smpls)/race_count,
        len(false_pos_smpls)/race_count,
        len(true_neg_smpls)/race_count
    ]
    rate_list += ['tp', 'fn', 'fp', 'tn']

race_df = pd.DataFrame({
    'race': race_list,
    'count': count_list,
    'rate': rate_list
})

race_fig = px.bar(
    race_df,
    x="race",
    y="count",
    color="rate",
    barmode='group'
)
race_fig2 = px.bar(
    race_df,
    x="rate",
    y="count",
    color="race",
    barmode='group'
)

afro_df = compas_df[
    compas_df['race'] == 'African-American'
]
afro_count = len(afro_df)
positives_afro = len(
    afro_df[
        afro_df['prediction'] == 1
        ]
)
demograhpic_parity_afro = positives_afro / afro_count

caucasian_df = compas_df[
    compas_df['race'] == 'Caucasian'
]
cauc_count = len(caucasian_df)
positives_cauc = len(
    caucasian_df[
        caucasian_df['prediction'] == 1
        ]
)
demographic_parity_cauc = positives_cauc / cauc_count

demographic_parity_df = pd.DataFrame({
    'race': ['African-American', 'Caucasian'],
    'ratio': [demograhpic_parity_afro, demographic_parity_cauc]
})

demographic_parity_fig = px.bar(
    demographic_parity_df,
    x="race",
    y="ratio",
    color="race"
)

true_samples_afro = afro_df[
    afro_df['is_recidivist'] == 1
]
true_afro_count = len(true_samples_afro)
true_positives_afro = len(
    true_samples_afro[
        true_samples_afro['prediction'] == 1
        ]
)
equal_opportunity_afro = true_positives_afro / true_afro_count
true_samples_cauc = caucasian_df[
    caucasian_df['is_recidivist'] == 1
]
true_cauc_count = len(true_samples_cauc)
true_positives_cauc = len(
    true_samples_cauc[
        true_samples_cauc['prediction'] == 1
        ]
)
equal_opportunity_cauc = true_positives_cauc / true_cauc_count
equal_opportunity_df = pd.DataFrame({
    'race': ['African-American', 'Caucasian'],
    'ratio': [equal_opportunity_afro, equal_opportunity_cauc]
})
equal_opportunity_fig = px.bar(
    equal_opportunity_df,
    x="race",
    y="ratio",
    color="race"
)

false_samples_afro = afro_df[
    afro_df['is_recidivist'] == 0
]
false_afro_count = len(false_samples_afro)
false_positives_afro = len(
    false_samples_afro[
        false_samples_afro['prediction'] == 1
        ]
)
equalized_odds_afro = false_positives_afro / false_afro_count

false_samples_cauc = caucasian_df[
    caucasian_df['is_recidivist'] == 0
]
false_cauc_count = len(false_samples_cauc)
false_positives_cauc = len(
    false_samples_cauc[
        false_samples_cauc['prediction'] == 1
        ]
)
equalized_odds_cauc = false_positives_cauc / false_cauc_count

equalized_odds_df = pd.DataFrame({
    'race': ['African-American', 'Caucasian', 'African-American', 'Caucasian'],
    'ratio': [equal_opportunity_afro, equal_opportunity_cauc,
              equalized_odds_afro, equalized_odds_cauc],
    'category': ['equal opportunity', 'equal opportunity',
                    'false positive rate', 'false positive rate']
})

equalized_odds_fig = px.bar(
    equalized_odds_df,
    x="category",
    y="ratio",
    color="race",
    barmode='group'
)



# gender_value_count = compas_df['sex'].value_counts()
# gender_value_count_df = pd.DataFrame({
#     'sex': gender_value_count.keys(),
#     'count': gender_value_count.values
# })
# gender_fig = px.bar(gender_value_count_df, x="sex", y="count", color="sex")


def generate_table(data_frame, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in data_frame.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(data_frame.iloc[i][col]) for col in data_frame.columns
            ]) for i in range(min(len(data_frame), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(compas_df),
    generate_table(doj_df, 50),

    dcc.Graph(
        id='example-graph-1',
        figure=race_count_fig
    ),
    dcc.Graph(
        id='example-graph-2',
        figure=demographic_parity_fig
    ),
    dcc.Graph(
        id='example-graph-3',
        figure=equal_opportunity_fig
    ),
    dcc.Graph(
        id='example-graph-4',
        figure=equalized_odds_fig
    ),
    dcc.Graph(
        id='example-graph-5',
        figure=race_fig
    ),
    dcc.Graph(
        id='example-graph-6',
        figure=race_fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)