from vault import Vault

vault = Vault()
while True:
    if vault.is_vault_opened:
        option = input(
            '금고가 열렸습니다. 다음중 하나의 숫자를 입력하세요.\n1. 물건 확인하기\n2. 물건 넣기\n3. 물건 삭제하기\n4. 비밀번호 변경\n5. 금고 잠그기고 종료하기\n')
        try:
            match int(option):
                case 1:
                    vault.get_content()
                case 2:
                    vault.put_content()
                case 3:
                    vault.delete_content()
                case 4:
                    vault.change_password()
                case _:
                    raise ValueError()
        except:
            print("올바른 값을 입력해 주세요")
            continue

    else:
        vault.open_vault()
