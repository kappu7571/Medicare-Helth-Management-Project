# Medicare-Helth-Management-Project
This project is a Django-based web application for managing medications and health-related activities. 
It allows users to keep track of their medications, set reminders, and log their daily activities.

# Features
Medication management: Add, view, and delete medications.
Reminder management: Create reminders for medication intake.
Activity tracking: Log daily activities with date and duration.
Activity management: Add, view, and delete activities.

# Installation
Clone the repository to your local machine: git clone https://github.com/kappu7571/Medicare-Helth-Management-Project.git
Install the required dependencies: pip install -r requirements.txt
Apply database migrations: python manage.py migrate
Run the development server: python manage.py runserver
The application will be accessible at  http://127.0.0.1:8000/

# API End Point
API endpoints are available for interacting with the application:

GET /medications/: Get a list of all medications.

GET /reminders/: Get a list of all reminders.

POST /medications/create/: Create a new medication
.
POST /reminders/create/: Create a new reminder.

DELETE /medications/delete/<medication_id>/: Delete a medication.

DELETE /reminders/delete/<reminder_id>/: Delete a reminder.

GET /activities/: Get a list of all activities.

POST /activities/log/: Log a new activity.

DELETE /activities/delete/<log_id>/: Delete an activity log.

# Credits
This project was developed by Kapil Kumar.
# Contact 
For any inquiries or issues, please contact sharmakapilkumar97@gmail.com.
