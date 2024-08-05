#!/usr/bin/env python3

from config import app, db
from models import Candy
from faker import Faker
import random

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        Candy.query.delete()

        # MANUAL WAY

        c1 = Candy(name="Reese's", brand="Hersheys", price=2)
        c2 = Candy(name="Skittles", brand="Mars", price=3)
        c3 = Candy(name="Snickers", brand="Mars", price=3)

        db.session.add_all( [c1, c2, c3] )
        db.session.commit()

        print("CANDIES ADDED THE MANUAL WAY...")

        # END MANUAL WAY

        # THE LOOP WAY

        for _ in range(1000):
            new_candy = Candy( name=faker.name(), brand=faker.address(), price=random.choice( range( 1, 7 ) ) )
            db.session.add( new_candy )

        db.session.commit()

        print("CANDIES ADDED THE LOOPING WAY...")

        # END LOOP WAY

        print("Seeding complete!")
