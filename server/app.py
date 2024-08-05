#!/usr/bin/env python3

from flask import request
from config import app, db
from models import Candy, Vegetable
# from sqlalchemy import IntegrityError


# ROUTES

@app.get('/')
def index():
    return { "response": "hello world" }, 200

# CANDIES ##############################################################################

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

@app.post('/candies')
def make_new_amazing_candy():
    data = request.json
    # data from client --> { "name": "Baby Ruth", "brand": "Mars", "price": 3 }

    try: # we can get a variety of errors so a try/except makes sense here

        # 1. make the instance
        new_candy = Candy(name=data['name'], brand=data['brand'], price=data['price'])
        # new_candy = Candy(**data) --> alternate using kargs to put in whole dictionary at once

        # 2. add / commit the instance
        db.session.add(new_candy)
        db.session.commit()

        # 3. return the candy
        return new_candy.to_dict(), 201
    
    except Exception as e:
        return { 'error': str(e) }, 400 # need to convert 'e' to a string to send


# DESTROY

@app.delete('/candies/<int:id>')
def delete_candy(id):
    candy_to_delete = Candy.query.where(Candy.id == id).first()

    if candy_to_delete:
        db.session.delete( candy_to_delete )
        db.session.commit()

        return {}, 204

    else:
        return {'error': 'Not found'}, 404


# UPDATE

@app.patch('/candies/<int:id>')
def update_candy(id):
    candy_to_update = Candy.query.where(Candy.id == id).first()

    if candy_to_update:

        try:

            data = request.json # --> { "name": "M&Ms", "price": 15 }

            for key in data:
                setattr(candy_to_update, key, data[key])
                # setattr(candy_to_update, "name", "M&Ms")
                # setattr(candy_to_update, "price", 15)

            db.session.add(candy_to_update)
            db.session.commit()

            return candy_to_update.to_dict(), 202
        
        except Exception as e:
            return { "error": str(e) }, 400

    else:
        return {'error': 'Does not exist'}, 404










# VEGETABLES ##############################################################################

@app.get('/vegetables')
def all_vegetables():
    return [ veg.to_dict() for veg in Vegetable.query.all() ]


@app.get('/vegetables/<int:id>')
def vegetable_by_id(id):
    found_vegetable = Vegetable.query.where(Vegetable.id == id).first()

    if found_vegetable:
        return found_vegetable.to_dict(), 200
    else:
        return { 'error': 'NOPE' }, 404


# APP RUN

if __name__ == '__main__':
    app.run(port=5555, debug=True)