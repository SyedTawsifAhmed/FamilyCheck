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

if LoginGUI.requestLogin():
    (email, password) = LoginGUI.getLoginInfo()
    try:
        auth.sign_in_with_email_and_password(email, password)
        LoginGUI.successfulLogin()
        print("Successfully logged in!")
    except:
        LoginGUI.failedLogin()
        print("Invalid email or password")
