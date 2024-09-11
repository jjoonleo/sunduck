is_vault_opened = False
password = '1234'
content = None
while True:
  if is_vault_opened:
    option = input('금고가 열렸습니다. 다음중 하나의 숫자를 입력하세요.\n1. 물건 확인하기\n2. 물건 넣기\n3. 물건 삭제하기\n4. 비밀번호 변경\n5. 금고 잠그기\n')
    try:
      match int(option):
        case 1:
          if(content == None):
            print("금고가 비어있습니다. 물건을 넣어주세요\n")
          else:
            print(f"금고에 들어있는 물건은 아래와 같습니다. \n\n {content}")
        case 2:
          if(content == None):
            content = input("금고에 넣으실 물건을 알려주세요")
          else:
            print("금고가 비어있지 않습니다. 먼저 물건을 삭제해 주세요")
        case 3:
          content = None
          print("물건이 삭제되었습니다.")
        case 4:
          while True:
            tmp_password = input("변경할 새 비밀번호를 입력해주세요")
            if tmp_password == input("비밀번호를 한 번 더 입력해 주세요"):
              password = tmp_password
              break
            else:
              print("비밀 번호가 일치하지 않습니다.")
        case 5:
          is_vault_opened = False
          print("금고를 잠급니다.")
        case _:
          raise ValueError()
    except:
      print("올바른 값을 입력해 주세요")
      continue

  else:
    password_input = input('금고를 열기 위해서 비밀번호를 입력하세요. 초기 비밀번호는 1234입니다.\n')
    if password == password_input:
      is_vault_opened = True
    else:
      print("비밀번호가 일치하지 않습니다.")
