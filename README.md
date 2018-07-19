# Snap
A personal gallery application that I display photos for others to see.

#### By **Immanuel Mugambi**

## User Requirements

1. View different photos that interest me.
2. View photos based on the location they were taken.
3. View photos based on the different categories.
4. Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
5. Copy a link to the photo to share with my friends.

## Admin Requirements
1. Post photos, categories and location
2. Delete and update photos


## Behaviour of the application
### Admin
The admin is responsible for adding photos, deleting and updating various fields.

### View
All photos appear on the homepage and can be view in different categories or locations.

### Search
A user can search based on categories and locations listed.


## Development and Setup.

### prerequisites
+ First clone the project to your camputer. ```git clone https://github.com/Imma7/Snap.git```
+ Ensure python3 is installed.
+ Install virtual environment by running ```pip3 install virtualenv```
+ Create a virtualenvironment by running ``` virtualenv <name of environment>``` on the terminal and once its activated by running ``` source <name of environment>/bin/activate``` then install all the packages by running ```pip3 install -r requirements.txt```
+ Then create a superuser by running ```python manage.py createsuperuser``` so that as an admin yul be able to manage ```CRUD``` operations to the application.
+ Then start the server by running ```python3 manage.py runserver```.
+ Copy the link and paste in any browser ```http://localhost:8000```

## Technology and Tools Used

+ Python3.6 - 
- Django 1.11
- Git - Version control
- Postgres - Database
- HTML
- CSS and Bootstrap

## Test Driven Development

Testing was done using python inbuild test tool called **unittest** to test database connections ,forms and models.

## License ([MIT License](http://choosealicense.com/licenses/mit/))
This project is licensed under the MIT Open Source license, (c) [Immanuel Mugambi](https://github.com/Imma7)