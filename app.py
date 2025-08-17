from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration (update username/password as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/food_ordering'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ----------- MODELS -----------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    price = db.Column(db.Float)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('menu.id'))

# ----------- ROUTES -----------

@app.route("/users", methods=["POST"])
def create_user():
    """Register a new user"""
    data = request.get_json()
    new_user = User(name=data["name"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully!"}), 201

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    """Fetch a user by ID"""
    user = User.query.get_or_404(id)
    return jsonify({"id": user.id, "name": user.name, "email": user.email})

@app.route("/menu", methods=["POST"])
def add_menu_item():
    """Add a new food item to the menu"""
    data = request.get_json()
    new_item = Menu(item_name=data["item_name"], price=data["price"])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Menu item added!"}), 201

@app.route("/menu", methods=["GET"])
def get_menu():
    """Fetch all menu items"""
    items = Menu.query.all()
    return jsonify([{"id": item.id, "name": item.item_name, "price": item.price} for item in items])

@app.route("/orders", methods=["POST"])
def place_order():
    """Place a new order"""
    data = request.get_json()
    new_order = Order(user_id=data["user_id"], item_id=data["item_id"])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order placed successfully!"}), 201

@app.route("/orders/<int:id>", methods=["GET"])
def get_order(id):
    """Fetch an order by ID"""
    order = Order.query.get_or_404(id)
    return jsonify({"order_id": order.id, "user_id": order.user_id, "item_id": order.item_id})

# ----------- MAIN -----------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
