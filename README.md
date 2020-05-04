# Introduction
Hey guys, this took me a vastly amount of time to make and a lot of trial and error to do. There was no tutorials out there to make something like this conceivable out there. I did get inspired by an Instagram post of a person creating this same applicaton but the catch was you had to pay for an API which is COMPLETELY BOGUS. This is why I have created a free version of this same annoying software to annoy your friends!!! :)
Currently you can send the entire shrek movie, test message or everyone's favorite: THE BEE MOVIE!!! Word for word, it'll annoy your friends life!
Here's a quick demonstration of the app [running.](https://media.giphy.com/media/XHMmIbq8JbzvH6OKmK/giphy.gif)

Support me: <a href="https://ko-fi.com/jaydevelops" target="_blank"> </a>

# Installation

### Have a Mac running MacOS
As of right now, this script only works with a mac machine, other methods of this working on universal machines will require a dedicated API to send mesages to recipient. If you want to request this feature, open a pull request on this github otherwise if you have decided to implement this feature on yourself and want to share it with this repository then open a pull request and I'll get back to you ASAP.

### Make Sure Python Is Installed on Your Mac
A good text resource is by clicking [here.](https://docs.python-guide.org/starting/install3/osx/)
A good online video to install python on mac is by clicking [here.](https://www.youtube.com/watch?v=TgA4ObrowRg)

### Install Inquirer
Enter the following command on your terminal.
	```
	pip install inquirer
	```
Or simply read [here](https://magmax.org/python-inquirer/installation.html)

### Install My software
Install this repo either by doing a quick git clone or download the zip file onto your Mac and make sure it's on a folder if it isn't already.

### Find Your "Service ID" From Your Own "Messages" Application on Your Own Mac
This one may be a bit confusing but I will walk through you each step here so you are not lost.

1. Open the application "Script Editor".
This can be done by opening your Applications or Launchpad. The app should look like [this](https://ibb.co/99RP9HP)

2. Click "New Document" button which looks like [this](https://ibb.co/pd9L9sX)


3. Enter the following script on the terminal like you see [here](https://ibb.co/Ssx0s4G)
```
tell application "Messages"
	get every service
end tell
```

4. Get the first "servicce id" number you see, copy and paste it into "credentials.py" located on the files you download from this repository.
Instructions are in there to replace it, or else you're going to get on infinite loop mode...

5. On the same "credentials.py" file, enter your own phone  number which you own. Otherwise you will go into ifininite loop mode


### CD Into the Directory and Run
1. CD into where you placed my software into
2. Run the following command onto your terminal
	```
	python main.py
	```
3. Follow the on command screens.

	```
	Phone number format should be like this: 3231235678
	Don't include parantheses, dashes or '+1'.
	The script has you covered for it
	```

4. Hit your keyboard control arrows to select which script you want to send to your friends!

5. The script will send you a confirmation of what movie you have chosen to your phone number

6. Leave your terminal and messages app open at all time.

7. Enjoy annoying your friends!

### Running to Errors Or If You Want To Stop The Script (MUST READ)
When you run into errors (or infinite loops), hit CTRL + C on your mac keyboard when your terminal open

If this doesn't work hit CTRl + Z and enter "kill %1" on your terminal.

If all of these don't work, you're going to have to restart your Mac machine again. This is possible by clicking the follwoing kestroke.
	```
	CTRL + CMD + ESC (POWER BUTTON)
	```
### Special Thanks
I want to thank this [blog post](https://leancrew.com/all-this/2013/03/combining-python-and-applescript/) for having a great library called 'applescript' for python which bridges python and apple script functionality to do some devlish work!
Everything else was all things I found online and I had to come up with. There's literally no apple documentation out there on how to use Applescript language which I had to learn in an afternoon.
If you like what I'm doing, buy me a coffee below.

<a href="https://ko-fi.com/jaydevelops" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;"></a>
