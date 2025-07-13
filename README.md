# Divar App

This Is The [Divar](https://divar.ir/) Clone Project Developed By Django Framework

# Installation

## First Step

Create Divar Directory:

```bash
mkdir divar
```


Go To Divar Directory:

```bash
cd divar
```

## Second Step

Clone The Project:

```bash
git clone https://github.com/shayanostovari/Divar-Clone.git
```

Create Virtualenv In Divar Directory: 

```bash
virtualenv divar
```

Then Activate The divar_Venv:
```bash
source divar_venv/bin/activate
```

## Third Step

Go To Project Directory:
```bash
cd Divar-Clone
```
Install Requirements: 
```bash
pip install -r requirements.txt
```

## Fourth Step
Now you Need To Fill Some Variables in Settings.py:

##### SECRET_KEY = '<django secret key (you can generate from this [site](https://djecrety.ir/)) >'
##### DEBUG = True
##### ALLOWED_HOSTS = ['*']

Then MakeMigration With:

```bash
python manage.py makemigrations
```

Then Migrate With:
```bash
python manage.py migrate
```



## Last Step
Now Run the Project:
```bash
python manage.py runserver
```
