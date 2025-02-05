import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
import os
from config import DB_CONFIG

app = Flask(__name__)

# Configure file upload folder
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Connect to MySQL
db = mysql.connector.connect(
    host=DB_CONFIG['host'],
    user=DB_CONFIG['user'],
    password=DB_CONFIG['password'],
    database=DB_CONFIG['database']
)
cursor = db.cursor()

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def student_form():
    if request.method == "POST":
        name = request.form["name"]
        student_id = request.form["student_id"]
        course = request.form["course"]
        address = request.form["address"]
        image = request.files["image"]

        # Save the uploaded image
        if image:
            image_filename = student_id + "_" + image.filename  # Rename file
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
            image.save(image_path)
        else:
            image_filename = None

        # Save data to MySQL
        sql = "INSERT INTO students (name, student_id, course, address, image_path) VALUES (%s, %s, %s, %s, %s)"
        values = (name, student_id, course, address, image_filename)
        cursor.execute(sql, values)
        db.commit()

        return redirect(url_for("student_form"))

    # Fetch all students
    cursor.execute("SELECT id, name, student_id, course, address, image_path FROM students")
    students = cursor.fetchall()

    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)
