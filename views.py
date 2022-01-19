from http.client import HTTPResponse
from itertools import product
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Product
from . import db
import json
import csv
from io import StringIO
from flask import make_response
from flask_http_response import success, result, error

views = Blueprint('views', __name__)


@views.route('/')
@login_required

def home():
    return render_template("home.html", user = current_user, products = Product.query.all())
    

@views.route('/delete-product', methods=['POST'])
def delete_product():
    product = json.loads(request.data)
    productId = product['productId']
    product = Product.query.get(productId)
    if product:
        if product.user_id == current_user.id:
            db.session.delete(product)
            db.session.commit()

    return jsonify({})

@views.route('/export-to-csv', methods=['GET','POST'])
def export_to_csv():
    si = StringIO()
    cw = csv.writer(si)
    records = Product.query.all()
    #cw.writerow(['name', 'category','count','description'])
    #for product in Product.objects.all().values_list('name', 'category','count','description'):   
       #cw.writerow(product)
    cw.writerow(['name', 'category','count','description'])
    cw.writerows([(r.name, r.category, r.count, r.description) for r in records])
    response = make_response(si.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    response.headers["Content-type"] = "text/csv"
    return response 
    
