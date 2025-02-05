# Student-Hub-Registration-Management-System
🌟 Project Overview Student Hub is a simple yet efficient student registration and management system built with Flask and MySQL. It provides a user-friendly interface where students can register, upload their details, and view a list of all registered students in a structured manner.


🎯 Features
✅ Student Registration Form – Enter name, student ID, course, address, and upload an image.
✅ Automatic Student List Display – Newly registered students appear below the form.
✅ Image Upload & Display – Profile pictures are stored and displayed with student details.
✅ Database Integration – All data is securely stored in a MySQL database.
✅ Dynamic Webpage – The form and student list are updated in real time.


🔧 Technologies Used
Frontend: HTML, CSS (Internal Styling)
Backend: Flask (Python)
Database: MySQL
Server: Flask Development Server
File Handling: Image Uploads



CREATE DATABASE flask_students;
USE flask_students;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    student_id VARCHAR(50) UNIQUE,
    course VARCHAR(100),
    address TEXT,
    image_path VARCHAR(255)
);
