import pyrebase

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


def login_user(email, pw):
    """The function takes in user information, email and password in order to get the user logged in.
     Return the email if successfully logged in"""
    try:
        auth.sign_in_with_email_and_password(email, pw)
        return email
    except:
        return ''

def CreateProfile(email, name, phone_num, age, vaccine_status):
    data = {'email': email, 'phone number': phone_num, 'Name': name, 'Age': age,
            'Vaccination Status': vaccine_status}
    db.child("Profiles").push(data)


def signup_user(email, password, confirm, name, phone_num, age, vaccine_status):
    """ takes up the email and password of the user,
    the confirms the password to get the user signed up"""

    text = name.replace(" ", "")
    if not text.isalpha():
        return 'Invalid name'
    if not age.isnumeric() or int(age) < 0:
        return 'Invalid age'
    if not phone_num.isnumeric() or len(phone_num) != 10:
        return 'Invalid phone number'

    if password == "":
        return 'Please enter a password'
    elif password == confirm:
        try:
            auth.create_user_with_email_and_password(email, password)
            print("Signup Successful")
            CreateProfile(email, name, "+1" + phone_num,
                          int(age), vaccine_status)
            return 'success'
        except:
            return 'Invalid email'
    else:
        return 'Password and confirm password do not match'




