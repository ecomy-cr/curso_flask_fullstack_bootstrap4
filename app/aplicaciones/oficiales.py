from flask import Blueprint, request, render_template, redirect, url_for, flash
from db import mysql

oficiales = Blueprint('oficiales', __name__, template_folder='app/templates')


@oficiales.route('/')
def Index():
    data = "Jinjai:  Esta variable es enviada al front de la siguiente manera, en el html la muestro en modo h1"
    return render_template('oficiales/index.html', data=data)