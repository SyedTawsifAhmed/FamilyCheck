import Menu
from Login import login_user, signup_user


class LoginPresenter:
    def __init__(self, loginGUI):
        self.gui = loginGUI

    def check_submit(self):
        if login_user(self.gui.get_login_info()[0],
                      self.gui.get_login_info()[1]) == "-1":

            print("Invalid email or password")
            self.gui.failed_login()
        else:
            print(f"{self.gui.username.text} logged in!")
            self.gui.manager.current = 'menu'
            self.gui.manager.get_screen('menu').set_email(self.gui.username.text)
            self.gui.manager.get_screen('fam').set_email(self.gui.username.text)

    def check_signup(self):
        prompt = signup_user(self.gui.get_signup_info()[0],
                             self.gui.get_signup_info()[1],
                             self.gui.get_signup_info()[2],
                             self.gui.get_signup_info()[3],
                             self.gui.get_signup_info()[4],
                             self.gui.get_signup_info()[5],
                             self.gui.get_signup_info()[6])

        if prompt != 'success':
            print(prompt)
            if prompt is None:
                prompt = "Invalid email"
            self.gui.failed_signup(prompt)

        else:
            print("Signup Successful")

    def check_family(self):
        if Menu.add_family(self.gui.manager.get_screen('fam').user,
                           self.gui.manager.get_screen('fam').user_input.text):
            self.gui.manager.get_screen('fam').successful_add()
        else:
            self.gui.manager.get_screen('fam').failed_add()

    def runGUI(self):
        self.gui.run()
