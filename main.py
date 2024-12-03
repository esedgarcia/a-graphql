from graphene import ObjectType, String, Schema
from flask import Flask, render_template
from flask_graphql import GraphQLView
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define the Query that we want to show
class Query(ObjectType):
    hello = String(name=String(default_value="General Kenobi!"))

    def resolve_hello(parent, info, name):
        return f"Hello there, {name}"

# Create the Schema
schema = Schema(query=Query)

# Add GraphQL endpoint 
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enables GraphiQL interface
    )
)

# Serve the frontend HTML to easily see the query
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

