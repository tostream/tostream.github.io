
import dash_bootstrap_components as dbc
from dash import Dash, html


def render(app:Dash) -> html.Section:
    return html.Section(
        dbc.Container(
            dbc.Row(
              [
                dbc.Col(
                    html.Img(
                        src=app.get_asset_url('img/fundamentals.svg'),
                        className="img-fluid",
                        alt=''),
                    md=True,
                ),
                dbc.Col(
                    [
                        html.H2("Learn The Fundamentals"),
                        html.P(
                            "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Similique deleniti possimus magnam corporis ratione facere!",
                            className="lead"),
                        html.P(
                            "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cumque reiciendis eius autem eveniet mollitia, at asperiores suscipit quae similique laboriosam iste minus placeat odit velit quos, nulla architecto amet voluptates?",
                        ),
                        html.A(
                            [html.I(className="bi bi-chevron-right"),"Read More"],
                            href="#",
                            className="btn btn-light mt-3")
                        
                    ],
                    md=True,
                    class_name="p-5",
                ),
              ],
              class_name="lign-items-center justify-content-between"  
            )
        ),
        id="learn",
        className="p-5 p-lg-0 pt-lg-5 text-center text-sm-start"
    )

def render2(app:Dash) -> html.Section:
    return html.Section(
        dbc.Container(
            dbc.Row(
                [
                dbc.Col(
                    [
                        html.H2("Learn React"),
                        html.P(
                            "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Similique deleniti possimus magnam corporis ratione facere!",
                            className="lead"),
                        html.P(
                            "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cumque reiciendis eius autem eveniet mollitia, at asperiores suscipit quae similique laboriosam iste minus placeat odit velit quos, nulla architecto amet voluptates?",
                        ),
                        html.A(
                            [html.I(className="bi bi-chevron-right"),"Read More"],
                            href="#",
                            className="btn btn-light mt-3")
                        
                    ],
                    md=True,
                    class_name="p-5",
                ),
                dbc.Col(
                    html.Img(
                        src=app.get_asset_url('img/react.svg'),
                        className="img-fluid",
                        alt=''),
                    md=True,
                ),
              ],
                class_name="lign-items-center justify-content-between"
            )
        ),
        className="bg-dark text-light p-5 p-lg-0 pt-lg-5 text-center text-sm-start"
    )