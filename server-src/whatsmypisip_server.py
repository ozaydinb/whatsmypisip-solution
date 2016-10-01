import datetime
from flask import Flask, jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

app = Flask(__name__)
in_memory = {}

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///whatsmypisip.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class AddressEntity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    createdDate = db.Column(db.DateTime, unique=False)
    ipaddress = db.Column(db.String(15), unique=False)

    def __init__(self, createdDate, ipaddress):
        self.createdDate = createdDate
        self.ipaddress = ipaddress

    def __repr__(self):
        return "{} => {}".format(self.createdDate, self.ipaddress)


db.create_all()


@app.route('/api/get', methods=['GET'])
def get_last_ip():
    addresses = AddressEntity.query.order_by(desc(AddressEntity.createdDate)).limit(1).all()
    last_ip_address = "no record"
    if addresses:
        last_ip_address = addresses[0].ipaddress

    return jsonify({"last_ip_address": last_ip_address})


@app.route('/api/add', methods=['POST'])
def insert_ip():
    now = get_server_date()
    ip_address = request.json["ipaddress"]
    new = AddressEntity(createdDate=now,ipaddress=ip_address)
    db.session.add(new)
    db.session.commit()
    return jsonify({'result': "OK"})


def get_server_date():
    return datetime.datetime.now()


app.debug = True

if __name__ == '__main__':
    app.run(debug=True)
