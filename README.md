# Crypto Project based on Alphavantage API

This Project is purely based on Pyhon and their webframework Django with Alphavantage API.

The purpose of this project is to fetch the price of BTC/USD from the Alphavantage API everyhour, stores the data in Postgre Database.
The API must be secured mean you need to pass an API key to use it. We provided here two Endpoints : GET/api/v1/quotes which returns exchnage rate and POST/api/v1/quotes which triggers force requesting of the price from Alphavantage API. An API Key is required to run this project.

We used here Docker to containerize API and DB. You have to use your Alphavantage APIKEY to run this program.

Please go through the **Requirements.txt file:https://github.com/ankurpython/crypto/blob/master/requirements.txt** and install all the requirements.

## Required

* Install **the Docker:** **https://docs.docker.com/docker-for-windows/install/ (for Windows) and for other environment https://docs.docker.com/engine/install/**
* **Docker-compose: https://docs.docker.com/compose/install/**

## Steps to Run 
> 1. Download or Clone the Repository:    **git clone https://github.com/ankurpython/crypto.git**
> 2. Go to the Dockerfile change the APIKEY to your APIKEY:    **APIKEY == Your-API-KEY.**
> 3. Run the container: **sudo docker-compose up**
> 4. Create the superuser using this command Run the: **docker exec -it container_id python manage.py createsuperuser**
> 5. Login with username and password.**http://localhost:8000/admin_login**. This will return the access token.
> 6. Request with Bearer token using this endpoint: **http://localhost:8000/api/v1/quotes**
> 7. For the GET and POST request 

## Steps to build the Docker(if it's not build)
>  Build the Docker container by using:   **docker-compose build**

## Screenshot

### 1. **Login Page**

![login](https://user-images.githubusercontent.com/48859058/137621082-f8131c79-652f-4748-8e3b-675e3ec6b46c.png)



### 2. **Returning all the data through GET request**

![Screenshot from 2021-10-17 12-23-31](https://user-images.githubusercontent.com/48859058/137621357-63d1bc26-e300-4e31-9cda-8c17dd44227b.png)


### 2. **Returning the data through POST request**

![Screenshot from 2021-10-18 10-49-07](https://user-images.githubusercontent.com/48859058/137682291-f660860a-f4e0-45f7-a100-8a8188c285a4.png)



## Thank You


