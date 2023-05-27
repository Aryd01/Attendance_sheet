Note - If you are using Jiofiber or jio sim switch on vpn or change the isp as images doesnot load with jiofiber it is a known issue
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

## Screenshots

### Login Page

![Login](https://github.com/Aryd01/Attendance_sheet/blob/master/results/login.JPG)



### Register Page

![Register](https://github.com/Aryd01/Attendance_sheet/blob/master/results/add%20attendance%20page.JPG)


### Home Page

![Homepage](https://github.com/Aryd01/Attendance_sheet/blob/master/results/homepage.JPG)



### Daily Atendance

![Daily attendance](https://github.com/Aryd01/Attendance_sheet/blob/master/results/Daily%20Attendance.JPG)

### Average Attendance

![Avg attendance](https://github.com/Aryd01/Attendance_sheet/blob/master/results/Average%20attendance.JPG)

### Search 

![Search](https://github.com/Aryd01/Attendance_sheet/blob/master/results/search%20student%20with%20a%20roll%20no..JPG)


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



## Suggestion and Contribution

I welcome any suggestions or contributions to improve this project. Feel free to submit a pull request or open an issue on the GitHub repository.


## 🚀 About Me
Hi there! I'm a passionate full-stack developer with expertise in HTML, CSS, React, JavaScript, Python, and Flask. I love building web applications that are not only visually appealing but also highly functional and user-friendly.

My experience in front-end development allows me to create responsive and intuitive user interfaces using HTML and CSS. I'm proficient in JavaScript and React, enabling me to develop interactive and dynamic web applications that enhance user experiences.

On the back-end, I have extensive knowledge of Python and Flask, which enables me to build robust server-side applications. I'm skilled in designing RESTful APIs, handling data management, and implementing authentication systems.

I'm constantly exploring new technologies and staying up-to-date with the latest industry trends to deliver high-quality and innovative solutions. I'm always eager to tackle new challenges and find creative ways to solve problems.

If you have any questions, suggestions, or would like to collaborate on a project, feel free to reach out to me at arscien04@gmail.com. I'm open to exciting opportunities and would be happy to connect with you.



