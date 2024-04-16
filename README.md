# livingarchive
Wagtail Living Archive
# Place install notes here - how to setup Wagtail server

python3 -m venv env

source env/bin/activate for mac or

.\env\Scripts\activate.bat for windows
 

pip install -r requirements.txt

add .env file to livingarchive/settings/ with API_KEY=

#
env\Scripts\activate    #activating in windows

# To update database
python3 manage.py makemigrations

python manage.py migrate 

python manage.py runserver
