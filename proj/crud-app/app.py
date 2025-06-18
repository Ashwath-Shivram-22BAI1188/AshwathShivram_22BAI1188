from flask import Flask, render_template, request, redirect, session
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "mysecretkey"

# Replace with your MongoDB connection string
client = MongoClient("mongodb+srv://cruduser:crudpass123@cluster0.z4qbj8w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["bookdb"]
users = db["users"]
books = db["books"]

@app.route('/')
def home():
    if "username" in session:
        book_list = books.find({"username": session["username"]})
        return render_template("dashboard.html", books=book_list)
    return redirect("/login")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        users.insert_one({"username": username, "password": password})
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        user = users.find_one({"username": username})
        if user and bcrypt.check_password_hash(user['password'], request.form['password']):
            session["username"] = username
            return redirect('/')
        return "Login Failed"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/add', methods=['POST'])
def add_book():
    isbn = request.form['isbn']
    title = request.form['title']
    books.insert_one({"username": session["username"], "isbn": isbn, "title": title})
    return redirect('/')

@app.route('/delete/<isbn>')
def delete_book(isbn):
    books.delete_one({"username": session["username"], "isbn": isbn})
    return redirect('/')

@app.route('/update/<isbn>', methods=['POST'])
def update_book(isbn):
    new_title = request.form['new_title']
    books.update_one({"username": session["username"], "isbn": isbn}, {"$set": {"title": new_title}})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
