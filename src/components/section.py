
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, html


def create_section(app) -> html.Div:
    return html.Div(
        dbc.Container(
        create_firstSect(app))
    )

def create_firstSect(app) -> html.Div:
    return html.Div(
        create_webdev(app),
        className="d-sm-flex align-items-center justify-content-between",
    )

def create_webdev(app:Dash) -> html.Div:
    
    @app.callback(
        Output("enroll", "hidden"),
        [Input("enroll-button", "n_clicks")],
        [State("enroll", "hidden")],
    )
    def toggle_enroll(n, hidden):
        if n:
            return not hidden
        return hidden  

    return html.Div(
        [
            create_enrollment_form(),
            html.H1(["Become a ",html.Span("Web Developer",className='text-warning')] ),
            html.P(" We focus on teaching our students the fundamentals of the latest \
              and greatest technologies to prepare them for their first dev role",
              className="lead my-4"),
            html.Button(
                "Start The Enrollment",
                className="btn btn-primary btn-lg",
                id="enroll-button",
                n_clicks=0)
        ]
    )

def create_enrollment_form() -> html.Div:
    return html.Div(
        [''],
        className="model Fade",
        id="enroll",
        tabIndex="-1",
        hidden=True,
    )

