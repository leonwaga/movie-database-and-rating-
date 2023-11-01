#!/usr/bin/env python3

from app import app
from models import db, Movie, Genre, MovieGenreAssociation, User, Rating
from datetime import datetime


with app.app_context():

   # Delete existing data from all tables
    db.session.query(Movie).delete()
    db.session.query(Rating).delete()
    db.session.query(User).delete()
    db.session.query(Genre).delete()
    db.session.query(MovieGenreAssociation).delete()


    #add movie records
    hocus = Movie(
        id=1,
        name="hocus",
        image="./images/hocus.jpeg",
        release_date=datetime(2023, 1, 1),
        description= "This is the description of Movie 1."
    )

    animal = Movie(
        id=2,
        name="animal",
        image="./images/animal.jpeg",
        release_date= datetime(2023, 2, 15),
        description= "This is the description of Movie 2."
    )

    db.session.add_all([hocus, animal])

    # Add rating records
    user1 = User(
        id=1,
        username="user1",
        email="shallon@gmail.com",
        password="password1"
    )

    user2 = User(
        id=2,
        username="user2",
        email="joedoe@gmail.com",
        password="password2"
    )

    db.session.add_all([user1, user2])

    rating1 = Rating(
        id=1,
        user_id=1,
        movie_id=1,
        rating=4,
        review="Good movie."
    )

    rating2 = Rating(
        id=2,
        user_id=2,
        movie_id=1,
        rating=5,
        review="Excellent movie."
    )

    db.session.add_all([rating1, rating2])

    # Add genre records
    action = Genre(
        id=1,
        name="Action"
    )

    comedy = Genre(
        id=2,
        name="Comedy"
    )

    db.session.add_all([action, comedy])

   # Create associations
    ##association1 = MovieGenreAssociation(movie=hocus, genre=action)
    #association2 = MovieGenreAssociation(movie=hocus, genre=comedy)
    #association3 = MovieGenreAssociation(movie=animal, genre=comedy)

    #db.session.add_all([association1, association2, association3])


    db.session.commit()
