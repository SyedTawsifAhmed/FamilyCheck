import pyrebase
import MenuGUI

firebaseConfig = {'apiKey': "AIzaSyC2LCENKnFLqlnojcWT8CDhTp09sFyothI",
                  'authDomain': "familycheck-14b96.firebaseapp.com",
                  'projectId': "familycheck-14b96",
                  'storageBucket': "familycheck-14b96.appspot.com",
                  'messagingSenderId': "483052018275",
                  'appId': "1:483052018275:web:ceebcd7a3c8f2f8d90f656",
                  'measurementId': "G-YCW48KPJPX",
                  'databaseURL': "https://familycheck-14b96-default-rtdb.firebaseio.com/"}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()


def add_family(email):
    """adds family members to the login menu or proceeds to the menu when no other family members"""
    other = MenuGUI.get_family_info()
    profiles = db.child('Profiles').get()
    for profile in profiles.each():
        if profile.val()['email'] == other:
            # Add existing member
            for person in profiles.each():
                if person.val()['email'] == email:
                    db.child('Profiles').child(person.key()).child('family').push({'email': other})
                    return
    # Failed to find family member
    MenuGUI.failed_add()


def UpdateEveryone(text):
    pass


def ask_question(email):
    """ asks questions from the questionnaire to decide if one has symptoms or not"""

    answers = MenuGUI.questionnaire()
    profiles = db.child("Profiles").get()
    name = ''  # placeholder
    for profile in profiles.each():
        if profile.val()['email'] == email:
            name = profile.val()['Name']
    if answers[0]:
        # Danger
        MenuGUI.danger()
        text = "FamilyCheck Update: Your family member/friend " + name + \
               " has been advised to go to their nearest emergency department based of their COVID-19 screening." \
               " Please check your symptoms and take your COVID-19 screening again if you see any changes."
        UpdateEveryone(text)
    if answers[1]:
        # Isolation/Testing
        MenuGUI.isolation()
        text = "FamilyCheck Update: Your family member/friend " + name + \
               " has been advised to get a COVID-19 (non rapid antigen) test and self-isolate. " \
               " Please check your symptoms and take your COVID-19 screening again if you see any changes."
        UpdateEveryone(text)
    if answers[2]:
        # Warning
        MenuGUI.warning()
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


def run_MenuGUI():
    MenuGUI.MenuScreen.run()