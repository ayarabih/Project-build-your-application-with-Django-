# Project-build-your-application-with-Django-
![image](https://user-images.githubusercontent.com/109382355/203650864-0c62451d-1410-4688-93ea-10a15ddba52e.png)

![image](https://user-images.githubusercontent.com/109382355/203650481-7d896cee-77b9-4eed-bfb7-1a47d7ffc575.png)

#Install Python 3
1.	sudo apt update
2.	sudo apt install software-properties-common
3.	sudo add-apt-repository ppa:deadsnakes/ppa
4.	sudo apt update
5.	sudo apt install python3.8
6.	python --version
we will Installing MySQL on Ubuntu
1.	sudo apt update
2.	sudo apt upgrade
3.	sudo apt install mysql-server
4.	mysql --version

#Installing MySQL on Ubuntu: Configure the MySQL Installation
1)	sudo mysql_secure_installation
2)	you will chose your level security
There are three levels of password validation policy:
LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary                  file
Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG:2
Please set the password for root here.
3)	New password:
       Re-enter new password:
4)	Estimated strength of the password: 100
     5   )Do you wish to continue with the password provided? (Press y|Y for Yes, any other  key for No) : Y  
     6   )sudo mysql
     7)   CREATE USER 'ayarabih'@'localhost' IDENTIFIED by '*******';

