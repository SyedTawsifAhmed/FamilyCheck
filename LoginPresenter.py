from Login import login_user, signup_user


class LoginPresenter:
    def __init__(self, loginGUI):
        self.gui = loginGUI

    def check_submit(self):
        if login_user(self.gui.get_login_info()[0],
        self.gui.get_login_info()[1]) == self.gui.get_login_info()[0]:
            print("Successfully logged in!")
        else:
            print("Invalid email or password")
            self.gui.failed_login()

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

    def runGUI(self):
        self.gui.run()

