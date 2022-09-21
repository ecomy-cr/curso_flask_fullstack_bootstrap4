from app import app
from aplicaciones.contacts import contacts
from aplicaciones.oficiales import oficiales

app.register_blueprint(contacts)
app.register_blueprint(oficiales)


# starting the app
if __name__ == "__main__":
    app.run(port=8777, debug=True)
