import kivy
import kivy_gradient
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config

#Kivy Settings
Config.set('graphics', 'resizable', False)
Builder.load_file('login.kv')

class LoginScreen(Widget):

    username = ObjectProperty(None)
    pw = ObjectProperty(None)
    pw_prompt = ObjectProperty(None)

    def submit(self):
        username = self.username.text
        pw = self.pw.text
        print(username, pw)

    def clear(self):
        self.username.text = ""
        self.pw.text = ""
        print("clear")


class LoginApp(App):
    def build(self):
        return LoginScreen()


def get_login_info(screen):
    return screen.username, screen.password


def failed_login(screen):
    screen.pw_prompt.text = "Invalid username or password."
    return None


def request_signup():
    return None


def failed_signup():
    return None


def get_signup_info():
    return None
