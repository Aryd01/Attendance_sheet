# Attendance Sheet Application

The Attendance Sheet Application is a web-based tool that allows users to manage and track attendance records for students. It provides a user-friendly interface using HTML and CSS for the frontend, Flask framework for the backend, and SQLite with SQLAlchemy for database management. This README file provides an overview of the application, installation instructions, and usage details.

## Features

- **User Registration:** New users can create an account by registering with their credentials.

- **User Login:** Registered users can log in securely using their username and password.
- **Add Attendance:** Users can add attendance records for students by specifying the student's roll number and marking their attendance for a specific date.
- **Show Daily Attendance:** Users can view the attendance records for a specific date, including details of the students who were present or absent.
- **Average Attendance:** Users can calculate the average attendance of a student for a given time period by providing the student's roll number and the start and end dates.
- **Search by Roll Number:** Users can search for a specific student's attendance records by providing their roll number.
- **Delete Attendance:** Users can delete a specific attendance record if needed.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your/repository.git
   ```

2. Navigate to the project directory: 

```bash
cd attendance_sheet
```

3. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
```
4. Activate the virtual environment:

- On macOS and Linux:
```bash 
source venv/bin/activate
```
- On Windows
```bash
venv\Scripts\activate
```
5. Install the required dependencies:

```bash
pip install -r requirements.txt
```
6. Set up the database:

- Initialize the database:
```bash
flask db init
```
- Create the necessary tables:
```bash
flask db migrate
flask db upgrade
```
7. Start the application:
```bash
flask run
```
or
```bash
python app.py
```
Access the application in your web browser at http://localhost:5000.