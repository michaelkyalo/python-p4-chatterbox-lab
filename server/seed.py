from app import app, db
from models import Message

with app.app_context():
    db.drop_all()
    db.create_all()

    m1 = Message(body="Hello, World!", username="Ian")
    m2 = Message(body="First Post!", username="Sarah")

    db.session.add_all([m1, m2])
    db.session.commit()

    print("✅ Database seeded!")
