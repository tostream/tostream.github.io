import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, html


def create_toggler()-> dbc.NavbarToggler:
    return dbc.NavbarToggler(id="navbar-toggler", n_clicks=0)

def create_menu() -> html.Ul:
    return html.Ul([
                        dbc.NavItem(dbc.NavLink("About",
                        href="#about")),
                        dbc.NavItem(dbc.NavLink("Resume",
                        href="#resume")),
                        dbc.NavItem(dbc.NavLink("Blog",
                        href="#blog")),
                        dbc.NavItem(dbc.NavLink("Work",
                        href="#work")),
                    ],className="navbar-nav ms-auto")

def create_toggler_nav(app:Dash)-> dbc.Navbar:

    @app.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )
    def toggle_navbar_collapse(n, is_open):
        if n:
            return not is_open
        return is_open  
   
    return dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(dbc.NavbarBrand("Frontend Bootcamp", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="#",
                    style={"textDecoration": "none"},
                ),
                create_toggler(),
                dbc.Collapse(
                    create_menu(),
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ]
        ),
        color="dark",
        dark=True,
    )