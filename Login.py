import pyrebase
import LoginGUI

firebaseConfig = {'apiKey': "AIzaSyC2LCENKnFLqlnojcWT8CDhTp09sFyothI",
                  'authDomain': "familycheck-14b96.firebaseapp.com",
                  'projectId': "familycheck-14b96",
                  'storageBucket': "familycheck-14b96.appspot.com",
                  'messagingSenderId': "483052018275",
                  'appId': "1:483052018275:web:ceebcd7a3c8f2f8d90f656",
                  'measurementId': "G-YCW48KPJPX",
                  'databaseURL': "https://familycheck-14b96-default-rtdb.firebaseio.com/"}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

db = firebase.database()


def login_user():
    """The function takes in user information, email and password in order to get the user logged in"""

    email, password = LoginGUI.get_login_info()
    try:
        auth.sign_in_with_email_and_password(email, password)
        option = LoginGUI.successful_login()
        print("Successfully logged in!")
        login_menu(option, email)
    except:
        LoginGUI.failed_login()
        print("Invalid email or password")


def CreateProfile(email):
    name, age, vaccine_status = LoginGUI.get_profile_info()
    data = {'email': email, 'Name': name, 'Age': age, 'Vaccination Status': vaccine_status}
    db.child("Profiles").push(data)


def signup_user():
    """ takes up the email and password of the user, the confirms the password to get the user signed up"""

    email, password, confirm = LoginGUI.get_signup_info()
    if password == confirm:
        try:
            auth.create_user_with_email_and_password(email, password)
            print("Signup Successful")
            CreateProfile(email)
        except:
            LoginGUI.failed_signup()
            print("Signup Failed")
    else:
        LoginGUI.failed_signup()
        print("Password and confirm do not match")


def add_family(email):
    """adds family members to the login menu or proceeds to the menu when no other family members"""
    other = LoginGUI.get_family_info()
    profiles = db.child('Profiles').get()
    for profile in profiles.each():
        if profile.val()['email'] == other:
            # Add existing member
            for person in profiles.each():
                if person.val()['email'] == email:
                    db.child('Profiles').child(person.key()).child('family').push({'email': other})
                    return
    # Failed to find family member
    LoginGUI.failed_add()


def UpdateEveryone(text):
    pass


def ask_question(email):
    """ asks questions from the questionnaire to decide if one has symptoms or not"""

    answers = LoginGUI.questionnaire()
    profiles = db.child("Profiles").get()
    name = ''  # placeholder
    for profile in profiles.each():
        if profile.val()['email'] == email:
            name = profile.val()['Name']
    if answers[0]:
        # Danger
        LoginGUI.danger()
        text = "FamilyCheck Update: Your family member/friend " + name + \
               " has been advised to go to their nearest emergency department based of their COVID-19 screening." \
               " Please check your symptoms and take your COVID-19 screening again if you see any changes."
        UpdateEveryone(text)
    if answers[1]:
        # Isolation/Testing
        LoginGUI.isolation()
        text = "FamilyCheck Update: Your family member/friend " + name + \
               " has been advised to get a COVID-19 (non rapid antigen) test and self-isolate. " \
               " Please check your symptoms and take your COVID-19 screening again if you see any changes."
        UpdateEveryone(text)
    if answers[2]:
        # Warning
        LoginGUI.warning()
        text = "FamilyCheck Update: Your family member/friend " + name + \
               " has been advised to get a PCR test or to monitor their health for any changes. " \
               " Please check your symptoms and take your COVID-19 screening again if you see any changes."
        UpdateEveryone(text)
    else:
        # Safe
        print("You do not need to self-isolate or get tested!")


def login_menu(option, email):
    if option == 1:
        # Add family/friend
        add_family(email)
    else:
        # Do questionnaire
        ask_question(email)


def RunGUI():
    LoginGUI.LoginScreen().run()
