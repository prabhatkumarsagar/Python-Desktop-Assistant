#chat operations go here!
import requests 
import voice_io
import usr_signup
import random
import datetime
import assistant_settings
import mailer

#jokes
def joke():  
    res_j = requests.get(
        'https://icanhazdadjoke.com/',
        headers={"Accept":"application/json"}
    )
    if res_j.status_code == requests.codes.ok:
        voice_io.show('Here is an awesome one for you! ') 
        voice_io.show(str(res_j.json()['joke'])) 
    else:
        voice_io.show("Oops! it looks like i ran out of my jokes, why don't you try again later.")

#joke()

#help
#1. Services Help
def srvc_help():
    print("Alright, here goes my domain of expertise. \")")
    print("1. I can open all sorts of websites and fetch web queries for you.")
    print("2. I can open and close apps for you.")
    print("3. I can open, rename, move and delete files and folders for you.")
    print("4. I can read out today's news for you.")
    print("5. I can tell you the current weather and the weather forecast for the next 7 days.")
    print("6. I can manage your Notes and Reminders for you.")
    print("7. I can send emails to your mail contacts for you.")
    print("8. I can perform some calculations for you.")
    print("9. I can play songs and even read out the date and time for you.")
    print("10. Alas, I can even chit-chat with you :)")
    return

#2. Operations Help
def op_help():
    print("Alright, So What operations do you need help with? (just enter the operation, for example 'news', and i'll tell you its general syntax and what it does too.)")
    x=input()
    x=x.lower()
    if "news" in x:
        print("With the News operation you can ask me to read out the top 15 news headlines of the moment.")
        print("The General Syntax of this operation is: \n")
        print("\"Python tell me today's news\" OR \"Hey read out today's top headlines\" OR \"PDA NEWS!\" (YOU GET THE IDEA)")
        return
    elif "website" in x:
        print("With the website operation you can ask me to open certain websites in your default browser.")
        print("The General Syntax of this operation is: \n")
        print("\"Python Open Youtube\" (BASIC WEBSITE OPENING) OR \"Open Instagram PDA\" (BASIC WEBSITE OPENING) OR \"Hey What is slavery?\" (WIKIPEDIA) OR  \"Define 'nuance'\" (GOOGLE SEARCH)")
        return
    elif "email" in x:
        print("With this operation you can ask me to send an email to a contact of yours. Note: for this to function properly you must enter your email and password at the time of Sign Up. If you haven't correctly or want to change the same, use help.")
        print("The General Syntax of this operation is: \n")
        print("\"Python help me send an email\" OR \"Hey i need you to send an email\" (OR ANY OTHER SORT OF EMAIL QUERY)")
        return
    elif "song" in x:
        print("With the website operation you can ask me to play both online and offline songs. Note: for offline songs, make sure that there are songs in the root Music Directory of your PC and in case of online songs, the song won't play automatically but instead you'll see a youtube page opened up with your song searched and you'll have to click on the first result yourself. SORRY FOR THE INCONVINIENCE, THIS WILL MOST LIKELY BE RECTIFIED IN THE COMING UPDATES. :D")
        print("The General Syntax of this operation is: \n")
        print("\"Python Play Offline Songs\" OR \"PDA Play Genda Phool by Badshah\" OR \"Hey Play Arijit Singh's Songs\" (YOU GET THE IDEA)")
        return
    elif "weather" in x:
        print("With this operation you can ask me about the current weather or the weather forecast for the next 7 days.")
        print("The General Syntax of this operation is: \n")
        print("\"Hey tell me the weather?\" OR \"What's the weather forecast for tomorrow?\" OR \"Python what's the temperature outside?\" OR \"PDA how's the josh?\" OR \"Tell me the weather forecast for the next 7 days\" (OR LITERALLY ANY OTHER WEATHER/WEATHER FORECAST/TEMPERATURE... QUERY)")
        return
    elif "time" in x or "date" in x:
        print("With this operation you can ask me the current time and date.")
        print("The General Syntax of this operation is: \n")
        print("\"Hey tell me the time?\" OR \"What's the time?\" OR \"Python what's the time?\" OR \"PDA what's the time?\" OR \"Tell me the current time!\" (OR LITERALLY ANYTHING ELSE BUT JUST MAKE SURE \"TIME\" IS A PART OF THE QUERY)")
        print("\"Hey tell me the date?\" OR \"What's today's date?\" OR \"Python what's the date?\" OR \"PDA what day is it?\" OR \"Tell me what month it is!\" (OR LITERALLY ANYTHING ELSE BUT JUST MAKE SURE \"DATE\"/\"DAY\"/\"MONTH\"/\"YEAR\" IS A PART OF THE QUERY)")
        return
    elif "calculation" in x:
        print("With this you can ask me to perform mathematical operations like addition, subtraction and the likes.")
        print("The General Syntax of this operation is: \n")
        print("\"Hey what is 5 times 2?\" OR \"What is the square root of 25\" OR \"Python what's the cube of 69\" OR \"PDA what is 5 time 27 divided by 3\" (OR LITERALLY ANYTHING ELSE BUT JUST MAKE SURE THAT IT IS A MATHEMATICAL QUERY)")
        return
    elif "notes" in x or "reminders" in x:
        print("With this operation you can ask me to save your notes and remind you of your reminders? haha.")
        print("The General Syntax of this operation is: \n")
        print("\"Python save a Note\" OR \"Save a Reminder PDA\" OR \"Python Add a Note\" (YOU GET THE IDEA)")
        return
    elif "joke" in x:
        print("With the joke operation you can ask me to joke?")
        print("The General Syntax of this operation is: \n")
        print("\"PDA tell me a joke\" OR \"Hey joke!!!\" OR \"Python i tell me something funny!\" OR ...")
        return
    elif "help" in x:
        print("With the help operation you can ask me to help you around.")
        print("The General Syntax of this operation is: \n")
        print("\"PDA help\" OR \"Python help me\" OR \"Hey help me out\" OR ...")
        return
    elif "open file" in x:
        print("With this operation you can ask me to open a file from a certain location for you.")
        print("The General Syntax of this operation is: \n")
        print("Open filename from foldername/location")
        return
    elif "open folder" in x:
        print("With this operation you can ask me to open a folder from a certain location for you.")
        print("The General Syntax of this operation is: \n")
        print("Open foldername from foldername/location")
        return
    elif "close file" in x:
        print("With this operation you can ask me to close an already opened file for you.")
        print("The General Syntax of this operation is: \n")
        print("Close filename")
        return
    elif "close folder" in x:
        print("With this operation you can ask me to close an already opened folder for you.")
        print("The General Syntax of this operation is: \n")
        print("Close foldername")
        return
    elif "rename file" in x:
        print("With this operation you can ask me to rename a file from a certain location for you.")
        print("The General Syntax of this operation is: \n")
        print("Rename filename from foldername/location to newfilename")
        return
    elif "rename folder" in x:
        print("With this operation you can ask me to rename a folder from a certain location for you.")
        print("The General Syntax of this operation is: \n")
        print("Rename foldername from foldername/location to newfoldername")
        return
    elif "delete file" in x:
        print("With this operation you can ask me to delete a file from a certain location for you.")
        print("The General Syntax of this operation is: \n")
        print("Delete filename from foldername/location")
        return
    elif "delete folder" in x:
        print("With this operation you can ask me to delete a folder from a certain location for you.")
        print("The General Syntax of this operation is: \n")
        print("Delete foldername from foldername/location")
        return
    elif "move file" in x:
        print("With this operation you can ask me to move a file from a certain location to another for you.")
        print("The General Syntax of this operation is: \n")
        print("Move filename from foldername/location to newfoldername/newlocation")
        return
    elif "move folder" in x:
        print("With this operation you can ask me to move a folder from a certain location to another for you.")
        print("The General Syntax of this operation is: \n")
        print("Move foldername from foldername/location to newfoldername/newlocation")
        return
    else:
        print("Sorry i don't think i can help you with that, make sure you're entering a valid operation name as an input, which is supposed to be one of the following: \n")
        print("1. News")
        print("2. Website")
        print("3. Email")
        print("4. Song")
        print("5. Weather")
        print("6. Time/Date")
        print("7. Calculation")
        print("8. Notes/Reminders")
        print("9. Joke")
        print("10. Help")
        print("11. Open file")
        print("12. Open folder")
        print("13. Close file")
        print("14. Close folder")
        print("15. Rename file")
        print("16. Rename folder")
        print("17. Delete file")
        print("18. Delete folder")
        print("19. Move file")
        print("20. Move folder")
        return

#3. Python Desktop Assistant Help (pda_help)
def pda_help():
    print("Select from the following Settings which can i help you with?")
    print("1. Assistant Settings Update")
    print("2. Assitant Settings Reset")
    print("3. User Data Update")    
    x=input("Enter Choice: ")
    if x=="1":
        assistant_settings.ass_settings_update()
    elif x=="2":
        assistant_settings.ass_settings_reset()
    elif x=="3":
        usr_signup.info_update()
    else:
        print("Invalid Input! Please make sure you're entering a valid input!")

#feedback()
def feedback():
    mailer.feedback_sender()


def help():
    while True:
        print("Hello Hello! What is it that i can help you with, today?")
        print("1. Assistant Settings")
        print("2. Assistant Services")
        print("3. Assistant Operations")
        print("4. Feedback (Suggest Improvements/Report Bugs/...)")
        print("5. Exit")
        x=input("Enter Choice: ")
        if x=="1":
            pda_help()
            continue
        elif x=="2":
            srvc_help()
            continue
        elif x=="3":
            op_help()
            continue
        elif x=="4":
            feedback()
            continue
        elif x=="5":
            exit()
        else:
            print("Invalid Input! Please Try Again!")
            continue


#greet
def gnd():
    if usr_signup.info_out("gender")=="Female":
        gndff=["Ma'am","Madam","Miss","Master"]
        return gndff[random.randint(0,3)]
    else:
        gndmm=["Sir","Mister","Master"]
        return gndmm[random.randint(0,2)]
gnd=gnd()

def greet():
    global gnd
    def gnd_hello(): 
        print("Hello "+gnd)
        return

    def tm_hello():
        time=datetime.datetime.now().strftime("%H")  
        time=int(time)
        if time < 12:
            tm="Morning"
        elif 12 <= time < 18:
            tm="Afternoon"
        else:
            tm="Evening"
        print("Good",tm,gnd)

    def talk():
        pass
    #tbdl
        
    #tm_hello()
    
#greet()  

#chat
#query=input("What you say: ")
def chat(query):
    query=query.lower()
    if "hello" in query:
        gnd_hello()
        return
    elif "good" in query:
        tm_hello()
        return
    elif "who are you" in query or "tell me about yourself" in query:
        print("I am your Personal Desktop Assistant, here to help you with your day to day tasks and queries. Why don't you try asking me something and i'll show you by practically doing it or not, hehe. ")
        return
    elif "who made you" in query or "who is your developer" in query or "who's your creator" in query or "who's your maker" in query or "who created you" or "who's your daddy" in query:
        print("I was made by Anirban Dutta and Prabhat Kumar Sagar as a part of their Computer Science School Project. Would you like to know more about them?")
        x=input()
        x=x.lower()
        if "yes" in x or "ok" in x or "yeah" in x:
            print("Alright!")
            webbrowser.open("https://github.com/prabhatkumarsagar")
            webbrowser.open("https://github.com/DuttaAB-dev")
            return
        elif "no" in x or "nope" in x or "not" in x:
            print("Alright!")
            return
        else:
            return

    elif "how are you" in query or "how do you do" in query or "how you doing" in query:
        print("Oh I am Grand, How are you master?")
        x=input()
        x=x.lower()
        if "good" in x or "great" in x or "fine" in x or "well" in x or "grand" in x or "nice" in x or "ok" in x or "okay" in x:
            print("Good to hear! Keep having fun!")
            return
        else:
            print("Well everything will be good soon, just keep smiling, it suits you.")
            return
    else:
        print("Well well well, i don't think i can help you with that?")
        return


#chat("heElO bitch")