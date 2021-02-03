### Meraki google-assistant adding Guest Wi-Fi


##### 1.Web server with a Python script.
Sign up on https://www.pythonanywhere.com/


Go to Web >
![](https://github.com/tgolowan/meraki-google-assistant/blob/main/images/pythonannywhere-web.png)

Add a new web app >


![](https://github.com/tgolowan/meraki-google-assistant/blob/main/images/Pythonanywhere-addwebapp.25.09%20PM.png)

Next > Flask > Python 3.8 (Flask 1.1.1) > Next (leave everything at default) > Next



By default, your web app is going to have the following URL USERNAME.pythonanywhere.com. Copy this URL somewhere, we are going to use it later to configure webhooks
Scroll down to Source code: /home/USERNAME/mysite > Click Go to directory >

![](https://github.com/tgolowan/meraki-google-assistant/blob/main/images/pythonanywhere-directory.png)


Locate and open flask_app.py

![](https://github.com/tgolowan/meraki-google-assistant/blob/main/images/pythonanywhere-flask.png)


The flask_app.py file is going to contain the code which is going to parse the webhooks from IFTTT and send API calls to Meraki Dashboard. Let’s open it and a separate browser tab and copy from flask.app.py from github repository

##### 2.IFTTT Applet.

2.Sign up on https://ifttt.com with your Google account


Connect Google Assistant service: Explore > Google Assistant > Services (Tab) > Select Google Assistant > Connect
Connect Google Assistant service: Explore > Webhooks > Services (Tab) > Select Webhooks > Connect
We will create guest SSID: one is to enable and another one to disable guest SSID
First, let’s reate an applet which is going to enable your wifi: Create > Click on THIS > Choose Google Assistant > Say a simple phrase > Fill out the fields > Create Trigger > Automatically brings us to “If THIS then THAT” statement

What do you want to say? Enable guest wifi
What do you want the Assistant to say in response? Sure, will do.

Click on THAT > Webhooks > Make a web request > Fill in the fields > Create action > Finish.

URL: Paste URL from PythonAnywhere http://USERNAME.pythonanywhere.com/enable_ssid

Method: POST

Content Type: text/plain

Body: enable_ssid


Now, let’s create an applet which is going to disable your wifi: Create > Click on THIS > Choose Google Assistant > Say a simple phrase > Fill out the fields > Create Trigger > Automatically brings us to “If THIS then THAT” statement,
What do you want to say? Disable guest wifi
What do you want the Assistant to say in response? Sure, will do.
Click on THAT > Webhooks > Make a web request > Fill in the fields > Create action > Finish.

URL: Paste URL from PythonAnywhere http://USERNAME.pythonanywhere.com/disable_ssid

Method: POST

Content Type: text/plain

Body: disable_ssid

##### 3.Meraki API

Now you can use flask.app.py file and copy paste it to pythonanywhere

Put the API key , SSID Number and Network ID
