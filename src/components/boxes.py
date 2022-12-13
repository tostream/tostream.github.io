
import dash_bootstrap_components as dbc
from dash import  html


def create_boxes() -> html.Section:
    return html.Section(
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                            dbc.CardBody(
                                [
                                    html.Div(
                                        [html.I(className="bi bi-laptop")],
                                        className="h1 mb-3"
                                    ),
                                    html.H3("Virtual", className="card-title mb3"),
                                    html.P(
                                        "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Iure, quas quidem possimus dolorum esse eligendi?",
                                        className="card-text",
                                    ),
                                    html.A("Read More",className="btn btn-primary")
                                ],
                                class_name="text-center"
                            ),
                            ],
                            class_name="bg-dark text-light",
                        ),
                        md=True,
                    ),
                    dbc.Col(
                        dbc.Card(
                            [
                            dbc.CardBody(
                                [
                                    html.Div(
                                        [html.I(className="bi bi-person-square")],
                                        className="h1 mb-3"
                                    ),
                                    html.H3("Hybrid", className="card-title mb3"),
                                    html.P(
                                        "orem, ipsum dolor sit amet consectetur adipisicing elit. Iure, quas quidem possimus dolorum esse eligendi?",
                                        className="card-text",
                                    ),
                                    html.A("Read More",className="btn btn-primary")
                                ],
                                class_name="text-center"
                            ),
                            ],
                            class_name="bg-secondary text-light",
                        ),
                        md=True,),
                    dbc.Col(
                        dbc.Card(
                            [
                            dbc.CardBody(
                                [
                                    html.Div(
                                        [html.I(className="bi bi-people")],
                                        className="h1 mb-3"
                                    ),
                                    html.H3("In Person", className="card-title mb3"),
                                    html.P(
                                        "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Iure, quas quidem possimus dolorum esse eligendi?",
                                        className="card-text",
                                    ),
                                    html.A("Read More",className="btn btn-primary")
                                ],
                                class_name="text-center"
                            ),
                            ],
                            class_name="bg-dark text-light",
                        ),
                        md=True,),
                ],
            )
        ),
        className="p-5"

    )