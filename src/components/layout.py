
from dash import Dash, Input, Output, State, html

from . import footer, instructor, learn, questions
from .boxes import create_boxes
from .nav import create_toggler_nav
from .section import create_section

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

def create_layout(app: Dash) -> html.Div:
    
    return html.Div(
        className="app-div",
        children=[
            html.Nav(
                create_toggler_nav(app) ,
                className="navbar-expand-lg navbar-dark fixed-top"              
            ),
            create_section(app),
            create_boxes(),
            learn.render(app),
            learn.render2(app),
            questions.render(),
            html.Section([
                instructor.render(app),
                ],
                className="p-5 p-lg-0 pt-lg-5 text-center text-sm-start"
            ),
            footer.render()
        ]
    )

    # add callback for toggling the collapse on small screens


def create_header(title:str)-> html.Div:
    return html.Div(
        html.H1(title),style={'textAlign': 'center'})

