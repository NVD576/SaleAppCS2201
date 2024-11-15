from flask import render_template, request, redirect, session
import dao
from saleapp import app
from saleapp.dao import auth_user


@app.route('/')
def index():
    q = request.args.get("q")
    cate_id = request.args.get("category_id")
    products = dao.load_products(q=q, cate_id=cate_id)
    return render_template('index.html', products=products)


@app.route('/products/<int:id>')
def details(id):
    product = dao.load_product_by_id(id)
    return render_template('product-details.html', product = product)

@app.route('/login', methods=['GET', 'POST'])
def login_my():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pwd']
        if auth_user(username, password):
            session['username'] = username
            return redirect("/")
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.context_processor
def common_attributes():
    return {
        "categories": dao.load_categories()
    }

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)