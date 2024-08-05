#!/usr/bin/env python3

from flask import request
from config import app, db
from models import Candy


# ROUTES

@app.get('/')
def index():
    return { "response": "hello world" }, 200

# READ ALL

@app.get('/candies')
def all_candies():
    # all_the_candies = Candy.query.all()
    # candy_dictionaries = []
    # for candy in all_the_candies:
    #     candy_dict = candy.to_dict()
    #     candy_dictionaries.append( candy_dict )
    # return candy_dictionaries, 200
    return [ candy.to_dict() for candy in  Candy.query.all() ], 200

# READ BY ID

@app.get('/candies/<int:id>')
def candy_by_id(id):
    found_candy = Candy.query.where(Candy.id == id).first()

    if found_candy:
        return found_candy.to_dict(), 200
    else:
        return { 'error': 'Candy not found' }, 404

# CREATE

# UPDATE

# DESTROY




# APP RUN

if __name__ == '__main__':
    app.run(port=5555, debug=True)