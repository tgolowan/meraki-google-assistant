## Meraki google-assistant adding Guest Wi-Fi


### 1.Web server with a Python script.

1. Sign up on https://www.pythonanywhere.com/
2. Go to Web
3. Add a new web app
4. Next
5. Flask
6. Python 3.8 (Flask 1.1.1)
7. Next (leave everything at default)
8. Next



By default, your web app is going to have the following URL:
USERNAME.pythonanywhere.com.

1. Copy this URL somewhere, we are going to use it later to configure webhooks
2. Scroll down to Source code
3. /home/USERNAME/mysite
4. Click Go to directory
5. Locate and open flask_app.py

>The flask_app.py file is going to contain the code which is going to parse the webhooks from IFTTT and send API calls to Meraki Dashboard. Let’s open it and a separate browser tab and copy from flask.app.py from github repository

### 2.IFTTT Applet.

2.Sign up on https://ifttt.com with your Google account

  Connect Google Assistant service:
   1. Explore
   2. Google Assistant
   3. Services (Tab)
   4. Select Google Assistant
   5. Connect
>We will create guest SSID: one is to enable and another one to disable guest SSID

First, let’s create an applet which is going to enable your wifi:
  1. Create
  2. Click on THIS
  3. Choose Google Assistant
  4. Say a simple phrase
  5. Fill out the fields
  6. Create Trigger

  Automatically brings us to “If THIS then THAT” statement

**What do you want to say?**
  Enable guest wifi
**What do you want the Assistant to say in response?**
  Sure, will do.

  1. Click on THAT
  2. Webhooks
  3. Make a web request
  4. Fill in the fields
  5. Create action
  6. Finish.

**URL:** Paste URL from PythonAnywhere http://USERNAME.pythonanywhere.com/enable_ssid

**Method:** POST

**Content Type:** text/plain

**Body:** enable_ssid


Now, let’s create an applet which is going to disable your wifi:
  1. Create
  2. Click on THIS
  3. Choose Google Assistant
  4. Say a simple phrase
  5. Fill out the fields
  6. Create Trigger

  Automatically brings us to “If THIS then THAT” statement,

**What do you want to say?**
  Disable guest wifi
**What do you want the Assistant to say in response?**
  Sure, will do.

  1. Click on THAT
  2. Webhooks
  3. Make a web request
  4. Fill in the fields
  5. Create action
  6. Finish.

**URL:** Paste URL from PythonAnywhere http://USERNAME.pythonanywhere.com/disable_ssid

**Method:** POST

**Content Type:** text/plain

**Body:** disable_ssid

### 3.Meraki API

Now you can use flask.app.py file and copy paste it to pythonanywhere

Put the API key , SSID Number and Network ID
