# create a virtual environment named 'venv' if it doesn't already exist
python -m venv venv

# activate the virtual environment
source venv/bin/activate

python pip install -U pip

# install all deps in the venv
pip3 install -r requirements.txt

python manage.py makemigrations --noinput
python manage.py migrate --noinput

# collect static files using the Python interpreter from venv
python manage.py collectstatic --noinput


# [optional] Start the application here 
python manage.py runserver