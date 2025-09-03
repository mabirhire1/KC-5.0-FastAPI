# Job Application Tracker with Secure Access

## Features
* Authentication with BasicAuth (username + password).

* Register users (store in users.json).

* Add job applications (POST /applications/).

* View job applications (GET /applications/) — each user sees only their own.

* Store all data in JSON files (users.json and applications.json).

## File Structure
job_tracker/
│── main.py
│── auth.py
│── models.py
│── applications.json
│── users.json
│── README.md
│── requirements.txt