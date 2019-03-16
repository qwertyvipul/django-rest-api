### Getting started
```bash
# Creating the project directory
mkdir firstrest
cd firstrest

# Creating virtual environment
virtualenv ENV
source ENV/Scripts/activate # ENV\Scripts\activate for windows

# Install Django in the virtual environment
pip install django

# Starting the project
django-admin startproject firstrest . # Note the trailing '.' character

# Creating first app
mkdir apps
cd apps
django-admin startapp firstapp
```