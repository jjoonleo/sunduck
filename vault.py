class Vault:
    def __init__(self):
        self.__password = "1234"
        self.__is_vault_opened = False
        self.__content = None

    @property
    def is_vault_opened(self):
        return self.__is_vault_opened

    def open_vault(self):
        password_input = input('금고를 열기 위해서 비밀번호를 입력하세요. 초기 비밀번호는 1234입니다.\n')
        if self.__password == password_input:
            self.__is_vault_opened = True
        else:
            print("비밀번호가 일치하지 않습니다.")

    def get_content(self):
        if (self.__content == None):
            print("금고가 비어있습니다. 물건을 넣어주세요\n")
        else:
            print(f"금고에 들어있는 물건은 아래와 같습니다. \n\n {self.__content}")

    def put_content(self):
        if (self.__content == None):
            self.__content = input("금고에 넣으실 물건을 알려주세요")
        else:
            print("금고가 비어있지 않습니다. 먼저 물건을 삭제해 주세요")

    def delete_content(self):
        self.__content = None
        print("물건이 삭제되었습니다.")

    def change_password(self):
        while True:
            tmp_password = input("변경할 새 비밀번호를 입력해주세요")
            if tmp_password == input("비밀번호를 한 번 더 입력해 주세요"):
                self.__password = tmp_password
                break
            else:
                print("비밀 번호가 일치하지 않습니다.")
