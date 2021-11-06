import pyrebase
import LoginGUI

firebaseConfig = {'apiKey': "AIzaSyC2LCENKnFLqlnojcWT8CDhTp09sFyothI",
                  'authDomain': "familycheck-14b96.firebaseapp.com",
                  'projectId': "familycheck-14b96",
                  'storageBucket': "familycheck-14b96.appspot.com",
                  'messagingSenderId': "483052018275",
                  'appId': "1:483052018275:web:ceebcd7a3c8f2f8d90f656",
                  'measurementId': "G-YCW48KPJPX",
                  'databaseURL': " "}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

storage = firebase.storage()


def login_user():
    """The function takes in user information, email and password in order to get the user logged in"""

    (email, password) = LoginGUI.get_login_info()
    try:
        auth.sign_in_with_email_and_password(email, password)
        LoginGUI.successful_login()
        print("Successfully logged in!")
    except:
        LoginGUI.failed_login()
        print("Invalid email or password")


def signup_user():
    """ takes up the email and password of the user, the confirms the password to get the user signed up"""

    (email, password, confirm) = LoginGUI.get_signup_info()
    if password == confirm:
        try:
            auth.create_user_with_email_and_password(email, password)
        except:
            LoginGUI.failed_signup()
            print("Signup Failed")
    else:
        LoginGUI.failed_signup()
        print("Password and confirm do not match")


def AddFamily():
    pass


def AskQuestion():
    answers = LoginGUI.Questionnaire()
    numYes = 0
    for answer in answers:
        if answer:
            numYes += 1

    if numYes == 0:
        # Safe
        pass
    if numYes == 1:
        # Warning
        pass
    if numYes == 2:
        # Isolation
        pass
    else:
        # Danger
        pass


def login_menu(option):
    if option == 1:
        # Add family/friend
        AddFamily()
    else:
        # Do questionnaire
        AskQuestion()

