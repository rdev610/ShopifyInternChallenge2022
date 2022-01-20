from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Product
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

#login page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

#logout page
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

#sign-up page
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than three characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than one character.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than six characters.', category='error')
        #creates new user and adds the user to the user databse
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", user=current_user)

#goes to the add product page
@auth.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        count = request.form.get('count')
        description = request.form.get('description')
        #paramters and restrictions to the inputs
        if int(count) < 1:
            flash('Minimum stock of the product has to be at least one. Please enter a valid number', category='error')
        elif len(name) < 2:
            flash('Name of product must be greater than one character. Please enter a valid name', category='error')
        elif len(description) < 1:
            flash('There must be a description of the product. Please enter a descrption', category='error')
        elif len(category) < 1:
            flash('The category name must be greater than once character. Please enter a valid category', category='error')
        #creeates a new product with the specifications given by the user
        else:
            new_product = Product(name = name, category=category,  count = count,description = description, user_id = current_user.id)
            db.session.add(new_product)
            db.session.commit()
            flash('Product added!', category='success')
            return redirect(url_for('views.home'))

    return render_template("add-product.html", user=current_user)

#goes to the specfic page of the product that needs to be updates
@auth.route('/<variable>/update-product', methods=['GET', 'POST'])
def update_product(variable):
    part_to_update = Product.query.get(variable)
    if request.method == 'POST':
        part_to_update.name = request.form.get('name')
        part_to_update.category = request.form.get('category')
        part_to_update.count = request.form.get('count')
        part_to_update.description = request.form.get('description')
        #same paramters and restrictions as the add-product page
        if int(part_to_update.count) < 1:
            flash('Minimum stock of the product has to be at least one. Please enter a valid number', category='error')
        elif len(part_to_update.name) < 2:
            flash('Name of product must be greater than one character. Please enter a valid name', category='error')
        elif len(part_to_update.description) < 1:
            flash('There must be a description of the product. Please enter a descrption', category='error')
        elif len(part_to_update.category) < 1:
            flash('The category name must be greater than once character. Please enter a valid category', category='error')
        #updates the product's information
        else:
            db.session.commit()
            flash('Product updated!', category='success')
            return redirect(url_for('views.home'))

    return render_template("update-product.html", user=current_user, products = Product.query.get(variable))

