import json


def load_db():
    file_path = "C:/Users/asus/PycharmProjects/sushil_test_flask_v2/models/flashcard_db.json"
    with open(file_path, "r") as foo:
        return json.load(foo)


db = load_db()
