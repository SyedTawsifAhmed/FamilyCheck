import kivy
import kivy_gradient
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix import checkbox

from LoginPresenter import LoginPresenter
from kivy.uix.screenmanager import ScreenManager, Screen

# Kivy Settings
Config.set('input', 'mouse', 'mouse, multitouch_on_demand')
Config.set('graphics', 'resizable', False)
Builder.load_file('login.kv')


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loginPresenter = LoginPresenter(self)

    # Setting up variables for kv file
    username = ObjectProperty(None)
    pw = ObjectProperty(None)
    pw_prompt = ObjectProperty(None)

    def submit(self):
        """checks the username and password

        :return:
        """
        self.loginPresenter.check_submit()
        print(self.username.text, self.pw.text)

    def get_login_info(self):
        return self.username.text, self.pw.text

    def failed_login(self):
        self.pw_prompt.text = "Invalid username or password."
        return None


class SignUpScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.loginPresenter = LoginPresenter(self)

    # Setting up variables for kv file
    email = ObjectProperty(None)
    pw = ObjectProperty(None)
    confirm = ObjectProperty(None)
    fullname = ObjectProperty(None)
    phone_num = ObjectProperty(None)
    age = ObjectProperty(None)
    vaccine_status = ""
    fail_prompt = ObjectProperty(None)

    def get_signup_info(self):
        """returns the inputted signup info of a user, which includes their
        email, password, confirm password, fullname, phone_num, age and
        vaccine status"""
        print(self.email.text)
        return self.email.text, self.pw.text, self.confirm.text, \
               self.fullname.text, self.phone_num.text, \
               self.age.text, self.vaccine_status

    def submit(self):
        """checks the email, password, confirm password, fullname, phone number,
        age and vaccine_status of a user signing up
        """
        self.loginPresenter.check_signup()

    def checkbox_click(self, instance, value, status):
        """
        :param value: checkbox is active when value is True
        :param status: the string "Yes" or "No"
        """
        if value:
            self.vaccine_status = status

    def failed_signup(self, prompt):
        self.fail_prompt.text = prompt


class LoginApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignUpScreen(name='signup'))
        return sm
