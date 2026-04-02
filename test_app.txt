import pytest
from dash.testing.application_runners import import_app

# Fixture to load the app
@pytest.fixture
def dash_app():
    app = import_app("app")  # This imports your app.py
    return app

def test_header(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert "Soul Foods Sales Visualiser" in header.text

def test_graph_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    region_picker = dash_duo.find_element("#region-selector")
    assert region_picker is not None