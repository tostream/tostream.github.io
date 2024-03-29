
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, html


def create_section(app) -> html.Div:
    return html.Div(
        dbc.Container(
        create_firstSect(app)),
        className="bg-dark text-light p-5 p-lg-0 pt-lg-5 text-center text-sm-start"
    )

def create_firstSect(app) -> html.Div:
    return html.Div(
        [create_webdev(app),
            html.Img(
                src=app.get_asset_url('img/showcase.svg'),
                className="img-fluid w-50 d-non d-sm-block"),],
        className="d-sm-flex align-items-center justify-content-between",
    )

def create_webdev(app:Dash) -> html.Div:
    
    @app.callback(
        Output("enroll", "is_open"),
        [Input("enroll-button", "n_clicks"), Input("close", "n_clicks")],
        [State("enroll", "is_open")],
    )
    def toggle_enroll(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open

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
                n_clicks=0),
        ]
    )

def create_enrollment_form() -> html.Div:
    return html.Div([
        dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Header")),
                dbc.ModalBody("This is the enroll form"),
                dbc.ModalFooter(
                    dbc.Button(
                        "Close", id="close", className="btn-secondary", n_clicks=0
                    )
                ),
            ],
            id="enroll",
            is_open=False,
        ),
    ]
    )