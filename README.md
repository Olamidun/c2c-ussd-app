# c2c-ussd-app

Technologies used:
- Django
- Ngrok to expose localhost url to the internet for the sake of development. The purpose of this is so I can use it as the callback url for my USSD channel on Africastalking

## Running this project locally
- Clone the project
- run `pip install requirements.txt` to install all the required dependencies
- download [ngrok](https://ngrok.com/download) and extract the file to your project folder, click on the commandline application and run `ngrok http 8000` (assuming your port is 8000). This will display a url you can use as the callback url for your USSD application on Africastalking. The callback url is in this format: <url_gotten_from_ngrok>/ussd
- run `python manage.py runserver` in the project root folder

  
