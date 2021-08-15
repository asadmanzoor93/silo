# Crover Silo APP

[![Python 3.6.5](https://img.shields.io/badge/python-3.6.5-blue.svg)](https://www.python.org/downloads/release/python-365/)

A central entry point of the application.

## Prerequisites

- Minimum [Python 3.6.5](https://docs.python.org/3/)

## How do I run this project?

The project includes all the basic configurations necessary to get you starting.

## Setup Instructions:

1. Assuming you have minimum python 3.6.5 installed, create a python 3.6.5 virtual environment

```bash
virtualenv -p python3 panel_env
source panel_env/bin/activate
```
2. Clone this project:

```bash
git clone https://github.com/asadmanzoor93/silo.git
cd silo
git fetch
```
3. Install requirements:

```bash
pip install -r requirements.txt
```
4. Create database and run migrations:

```bash
python manage.py migrate
```
5. Create an admin user to access django admin:

```bash
python manage.py createsuperuser
```
6. Serve the app on localhost at port 8000

```bash
python manage.py runserver
```

## Functionalities Implemented:
1. User can view line graph for all the data available.
2. User can upload csv for temperature data import.
3. User can create temperature data record.
4. User can delete existing temperature data record.
5. All data is stored in SQL database.

## Functionalities Implemented:
1. I have used existing library plotly for fast implementation of graph instead of recommended dangjo or graph related libraries i.e chart.js
2. Instead of installing package i have used CDN for fast loading of plotly library.
3. I have tried to add keep things simple i.e Class based views for all the CRUD related operations associating them with model and simple views for upload csv and index page feature.
4. Added listing view for data to facilitate user in getting understanding of data set available and also added delete button to give user freedom to delete individual record.
5. I have used form for creating temperature model record and added custom html implementation.
6. I have used bootstrap along with some custom CSS to improve view of screens.

## Application ScreenShots

### Data Graph Screen
![screencapture-127-0-0-1-8000-2021-08-15-19_46_21](https://user-images.githubusercontent.com/17013371/129483067-8d4fd488-3b0e-4808-b45a-a482b88b5c72.png)

### Data Listing Screen
![screencapture-127-0-0-1-8000-dashboard-2021-08-15-19_46_06](https://user-images.githubusercontent.com/17013371/129483073-9c7f7a06-09d2-42f0-8a7f-f1f3de92e442.png)

### Data Upload Screen
<img width="1198" alt="Screenshot 2021-08-15 at 8 05 51 PM" src="https://user-images.githubusercontent.com/17013371/129483075-66bf0188-2433-4b9c-84fd-5552493fd489.png">

### Data Add Screen
![screencapture-127-0-0-1-8000-create-2021-08-15-20_04_22](https://user-images.githubusercontent.com/17013371/129483071-62da6f38-9bea-4ee3-b647-ababac6df47f.png)

### Data Delete Screen
<img width="1400" alt="Screenshot 2021-08-15 at 8 05 36 PM" src="https://user-images.githubusercontent.com/17013371/129483074-994f3970-34b8-4364-81aa-de42622026be.png">
