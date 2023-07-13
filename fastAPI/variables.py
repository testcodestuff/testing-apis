from types import User

users_db = {
    "username1": {
        "username": "username1",
        "full_name": "full_name1",
        "email": "email1@email.com",
        "disabled": False,
        "password": "user1password",
    },
    "username2": {
        "username": "username2",
        "full_name": "full_name2",
        "email": "email2@email.com",
        "disabled": True,
        "password": "user2password",
    },
    "username3": {
        "username": "username3",
        "full_name": "full_name3",
        "email": "email3@email.com",
        "disabled": False,
        "password": "user3password",
    }
}

list_of_products = ["Product 1",
                    "Product 2",
                    "Product 3",
                    "Product 4",
                    "Product 5"]

list_of_users = [User(name="Name1", surname="surname1", id=1),
                 User(name="Name2", surname="surname2", id=2),
                 User(name="Name3", surname="surname3", id=3)]
