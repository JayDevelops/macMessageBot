# Import all the necessary modules
from applescript import asrun, asquote
from credentials import serviceID, yourPhoneNumber
from movies import movieDictionary
import inquirer
import time


# TODO: Ask the user for the phone number they want to spam and movie type
inquiry = [
    inquirer.Text('phoneNum', message='Please enter the phone number you want to spam'),
    inquirer.List('movieType', message='Please select which movie you want to use\n Use your arrow keys to choose one', choices=['beeMovie', 'shrekMovie', 'testMessage'])
]

answers = inquirer.prompt(inquiry)

areaCode = "+1"  # Manually edit if you live outside the USA
messageContent = movieDictionary[answers['movieType']]
recipientPhoneNum = areaCode + answers['phoneNum']

# TODO: Let the user know the script has executed
userMessage = "The devilish script has been executed, we'll let you know once it's complete. You will send the following message word for word: " + messageContent
executeScript = '''
tell application "Messages"
    set textbuddy to buddy {0} of service id {1}
    send {2} to textbuddy
end tell
'''.format(asquote(yourPhoneNumber), asquote(serviceID), asquote(userMessage))
asrun(executeScript)

# Wait for 3 seconds
time.sleep(3)

# TODO: Remove all punctuation from the string
punctuations = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
cleanMessage = ""

for char in messageContent:
    if char not in punctuations:
        cleanMessage = cleanMessage + char


# TODO: Make the new message into an array of words, AKA a list. Store it to 'convertedMessage'
def convertToList(string):
    li = list(string.split(" "))
    return li

convertedMessage = convertToList(cleanMessage)

# Wait for 3 seconds
time.sleep(3)

# TODO: Loop each word to write a new applescript, in order to send a one word message of your HUGE MESSAGE
for word in range(len(convertedMessage)):
    applescript = '''
    tell application "Messages"
        activate
        set textbuddy to buddy {0} of service id {1}
        send {2} to textbuddy
    end tell
    '''.format(asquote(recipientPhoneNum), asquote(serviceID), asquote(convertedMessage[word]))
    # The {0}, {1}, and {2} are the indeces of the .format() method
    # asrun runs the script in a loop
    asrun(applescript)

# Wait for 3 seconds
time.sleep(3)

# TODO: Once the loop has finished, let the sender know the devlish script has finished
finishedMessage = "The devilish script has completed, you're such a devilish being. Yes you are, goodbye."
finishedScript = '''
tell application "Messages"
    set textbuddy to buddy {0} of service id {1}
    send {2} to textbuddy
end tell
'''.format(asquote(yourPhoneNumber), asquote(serviceID), asquote(finishedMessage))
asrun(finishedScript)
