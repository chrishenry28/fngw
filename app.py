from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/store')
def store():
    return render_template('store.html')

if __name__ == '__main__':
    app.run(debug=True)
