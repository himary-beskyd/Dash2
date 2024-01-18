import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_auth
from dash_bootstrap_templates import load_figure_template

VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world'
}

load_figure_template(["materia", "minty"])
external_stylesheets = [dbc.themes.MATERIA]

app = dash.Dash(__name__, use_pages=True, suppress_callback_exceptions=True, external_stylesheets=external_stylesheets, meta_tags=[{'name': 'viewport',
'content': 'width=device-width, initial-scale=1.0'}])

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
server=app.server

sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
                if page["module"] != "pages.not_found_404"
            ],
            vertical=True,
            navbar_scroll=True,
            pills=True,
            className="bg-light",
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div("Python Multipage App with Dash",
                         style={'fontSize':50, 'textAlign':'center'}))
    ]),

    html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
], fluid=True)


if __name__ == "__main__":
    app.run(debug=True, port=8070)