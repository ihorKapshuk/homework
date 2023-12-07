class Checker:

    def __init__(self, email : str):
        self.validate(email)

    def validate(self, email : str):
        if "@" in email:
            result = email.split("@")
            if len(result) == 2:
                if result[0][len(result[0]) - 1] == "-":
                    print("Префікс не може закінчуватись -")
                    self.email = None
                elif ".." in result[0]:
                    print("Префікс не може містити ..")
                    self.email = None
                elif result[0][0] == ".":
                    print("Префікс не може починатись з .")
                    self.email = None
                elif "#" in result[0]:
                    print("Префікс не може містити #")
                    self.email = None
                elif result[1][len(result[1]) - 2] == "." or result[1][len(result[1]) - 1] == ".":
                    print("Домен повинен містити не менше 2 символів після крапки")
                    self.email = None
                elif "#" in result[1]:
                    print("Домен не може містити #")
                    self.email = None
                elif not ("." in result[1]):
                    print("Домен повинен містити .")
                    self.email = None
                elif ".." in result[1]:
                    print("Домен не може містити ..")
                    self.email = None
                else:
                    self.email = "@".join(result)
            else:
                print("@ може бути лише одна")
                self.email = None
        else:
            print("Нема @")
            self.email = None

checker1 = Checker("username@company.com")
print(checker1.email)