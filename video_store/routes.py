from video_store import app, db
from flask import jsonify
from .models import Customer, CustomerSchema

customer_schema = CustomerSchema(many=True)

@app.route('/')
@app.route('/index')
def index():
    return "Video Store API!"

@app.route('/zomg')
def it_works():
    return jsonify(zomg="It works!")
# ____ CUSTOMER ENDPOINTS ____

# GET all customers
# /customers
@app.route('/customers/')
def customers():
    customers = Customer.query.all()
    result = customer_schema.dump(customers)
    return jsonify(customers=result.data)

# GET subset of customers sorted by name, registered_at, or postal_code
# /customers/name/page1
@app.route('/customers/<column>/page<int:page>')
def customers_subset(column, page):
    customers = Customer.query.order_by(column).all()
    result = customer_schema.dump(customers)
    return jsonify(customers=result.data)

# ____ MOVIES ENDPOINTS ____

# GET all movies
# /movies
@app.route('/movies/')
def movies():
    return "List of movies!"

# GET subset of movies sorted by title or release_date
# /movies/name/page1
@app.route('/movies/<column>/page<int:page>')
def movies_subset(column, page):
    return "Subset of movies on page {}!".format(page)

# ____ RENTALS ENDPOINTS ____

# GET rental info on a specific movie
@app.route('/rentals/<movie_title>')
def rental_movie(movie_title):
    return "List of rental movies!"
