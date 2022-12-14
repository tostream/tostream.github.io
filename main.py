import dash_bootstrap_components as dbc
from dash import Dash

from src.components.layout import create_layout


def main() -> None:
    """single page personal project"""
    app:Dash = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,dbc.icons.BOOTSTRAP])
    app.title = "Frontend Bootcamp"
    app.layout = create_layout(app)
    app.run()
    
if __name__ == "__main__":
    main()
