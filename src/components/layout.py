from dash import Dash, html


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.Header(html.H1(app.title),style={'textAlign': 'center'}),
            html.Nav(),
        ]
    )