class EmailDescriptor:

    def __get__(self, obj, objtype=None):
        return obj._email
    
    def __set__(self, obj, value):
        if "@" in value:
            result = value.split("@")
            if len(result) == 2:
                if result[0][len(result[0]) - 1] == "-":
                    print("Префікс не може закінчуватись -")
                    obj._email = None
                elif ".." in result[0]:
                    print("Префікс не може містити ..")
                    obj._email = None
                elif result[0][0] == ".":
                    print("Префікс не може починатись з .")
                    obj._email = None
                elif "#" in result[0]:
                    print("Префікс не може містити #")
                    obj._email = None
                elif result[1][len(result[1]) - 2] == "." or result[1][len(result[1]) - 1] == ".":
                    print("Домен повинен містити не менше 2 символів після крапки")
                    obj._email = None
                elif "#" in result[1]:
                    print("Домен не може містити #")
                    obj._email = None
                elif not ("." in result[1]):
                    print("Домен повинен містити .")
                    obj._email = None
                elif ".." in result[1]:
                    print("Домен не може містити ..")
                    obj._email = None
                else:
                    obj._email = "@".join(result)
            else:
                print("@ може бути лише одна")
                obj._email = None
        else:
            print("Нема @")
            obj._email = None

class Checker:

    email = EmailDescriptor()

    def __init__(self, email):
        self.email = email

checker1 = Checker("username@company.com")
print(checker1.email)