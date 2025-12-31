# Import required libraries
from flask import Flask, render_template
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle
import sqlite3
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Create a Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for the data page
@app.route('/data')
def data():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Query the data
    cursor.execute('SELECT * FROM data')
    data = cursor.fetchall()
    
    # Close the connection
    conn.close()
    
    # Create a Plotly figure
    fig = px.line(x=[1, 2, 3], y=[1, 2, 3])
    
    # Create a Dash application
    dash_app = dash.Dash(__name__)
    
    # Define the layout
    dash_app.layout = html.Div(children=[
        html.H1(children='Data Page'),
        dcc.Graph(id='example-graph', figure=fig)
    ])
    
    # Run the Dash application
    if __name__ == '__main__':
        dash_app.run_server(debug=True)
