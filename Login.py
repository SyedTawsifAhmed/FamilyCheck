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
    """The function takes in user information, email and password in order to get the user logged in.
     Return the email if successfully logged in"""

    email, password = LoginGUI.get_login_info()
    try:
        auth.sign_in_with_email_and_password(email, password)
        LoginGUI.successful_login()
        print("Successfully logged in!")
        return email
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


def run_LoginGUI():
    LoginGUI.LoginScreen().run()
