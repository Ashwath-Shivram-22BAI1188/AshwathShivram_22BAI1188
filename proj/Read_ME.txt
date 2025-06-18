# Book ISBN CRUD App using Flask and MongoDB

This is a basic web application built using Python (Flask framework) and MongoDB Atlas. It allows users to register, log in, and manage a list of books using their ISBN numbers and titles. All data is stored in a MongoDB database in the cloud.

---

## Features

- User registration and login
- Add, view, update, and delete book records (ISBN and title)
- User-specific data storage (each user sees only their own books)
- Uses MongoDB Atlas as the database
- Minimal HTML interface

---

## Folder Structure

crud-app/
│
├── app.py # Main Python application
│
├── templates/ # HTML files used by Flask
│ ├── login.html # Login page
│ ├── register.html # Registration page
│ └── dashboard.html # Main page to manage books


how to run:

open cmd:-
cd Desktop\crud-app

python app.py

Open your browser and go to:
 http://127.0.0.1:5000/register