Firstly Create This directory (wastemanagement)for making virtual enviroment
----------------------------
mkdir /c/wastemanagement/
---------------------------


change from PWD to this directory
--------------------------
cd /c/wastemanagement/
--------------------------


now use below command to create virtual enviroment named virt 
-------------------------
python -m venv virt
---------------------------


now activate the virtual env with below code
---------------------------
source virt/Scripts/activate
now pip install requirement.txt
-------------------------------------



use this command to start the project
-----------------------------------
 django-admin startproject wastemgt
---------------------------------
after starting the project clone the project or copy and paste wastemgt folder





now change the directory to
-------------
cd wastemgt/
------------



After cd using below code to start the app
------------------------------------------------
python manage.py startapp waste_reduction_buddy
--------------------------------------



after starting create SQL database for which SQL server should be up and running
---------------------------
python mydbms.py
python manage.py migrate
----------------------------


After creating the database crate superuser named: binod.raut@wastebuddy.com
for admin access this email should be the same
-------------------------------------
winpty python manage.py createsuperuser
----------------------------------------



now after seting up the super user you can start the django server using
 -------------------------
python manage.py runserver
---------------------------
localhost:8000 is the port for the django
