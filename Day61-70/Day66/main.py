from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import randint

app = Flask(__name__, template_folder="templates")

# Default placeholder image when none provided
DEFAULT_IMG_URL = "https://via.placeholder.com/400x300.png?text=No+Image"


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Error Handling > Boolean form values:
def str_to_bool(string):
    """
    It receives a string, check if the string is a valid positive answer and return the result. This function goal is
    to make the dev life easier, basically during form tests.
    :param string: the text.
    :return: bool
    """
    if string in ["1", "YES", "Yes", "yes", "Y", "y", "TRUE", "True", "true", "T", "t"]:
        return True
    return False


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {
            self.name: {
                "id": self.id,
                "map": self.map_url,
                "image": self.img_url,
                "location": self.location,
                "seats": self.seats,
                "toilet": self.has_toilet,
                "wifi": self.has_wifi,
                "sockets": self.has_sockets,
                "calls": self.can_take_calls,
                "price": self.coffee_price
            }
        }

    def __repr__(self):
        return f"<Cafe id-{self.id}: {self.name}>"


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")  # by default, all routes are method GET when "methods" are not declared.
def get_random():
    shop_id = randint(1, Cafe.query.count())  # checking the length of coffee shop in database.
    shop_selected = db.get_or_404(Cafe, shop_id)
    return render_template("random.html", shop=shop_selected)


@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    # List Comprehension to convert each object (coffee shop) in a dictionary:
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


# HTTP POST - Create Record
@app.route("/add", methods=["GET", "POST"])
def post_new_cafe():
    if request.method == "POST":
        # Validate required fields to prevent NOT NULL DB errors
        # img_url, location and seats are optional now and will receive defaults when not provided
        required = ["name", "map_url"]
        missing = []
        for field in required:
            val = request.form.get(field)
            if val is None or str(val).strip() == "":
                missing.append(field)

        if missing:
            return jsonify(error="Missing required form fields.", missing=missing), 400

        # Build the new object from the form inputs (safe now that required fields exist)
        img = request.form.get("img_url") or DEFAULT_IMG_URL
        location = request.form.get("location") or "Unknown"
        seats = request.form.get("seats") or "Not specified"

        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=img,
            location=location,
            seats=seats,
            has_toilet=str_to_bool(request.form.get("has_toilet")),
            has_wifi=str_to_bool(request.form.get("has_wifi")),
            has_sockets=str_to_bool(request.form.get("has_sockets")),
            can_take_calls=str_to_bool(request.form.get("can_take_calls")),
            coffee_price=request.form.get("coffee_price"),
        )

        # Try to save and handle DB errors cleanly
        try:
            db.session.add(new_cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully added the new cafe."}), 201
        except Exception as e:
            # Rollback to keep the session usable and return an informative error
            db.session.rollback()
            return jsonify(error="Database error during insert.", details=str(e)), 500

    # If the method is "GET", show the page (if you have a form template)
    return render_template("add.html")


# HTTP PUT & PATCH
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    if not new_price:
        return jsonify(error="Missing required parameter: new_price"), 400
    
    try:
        cafe = db.session.get(Cafe, cafe_id)
        if cafe:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(success="Successfully updated the price.")
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify(error="Database error during update.", details=str(e)), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)