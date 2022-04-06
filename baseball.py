from random import randint

answer_list = []
guess_list = []
correct = 0

def make_answer():
    while len(answer_list) < 4 :  # 4자리수 생성
        i = 0   # counter
        new_num = randint(0, 9)  # 0에서 9까지 랜덤으로 수 하나 생성
        if i == 0 : # 맨 앞자리가 0이 아니기 위함
            if new_num == 0:
                continue 
            else:
                if new_num not in answer_list: # 중복 수 배제
                    answer_list.append(new_num)
                    i += 1
                    continue
                else:
                    continue
        if new_num not in answer_list: # 중복 수 배제
            answer_list.append(new_num)
            i += 1
    

def guess():
    user_input_count = 1

    while len(guess_list) < 4 : # 4자리수로 맞추기
        number_input = input('{}번째 자리수를 입력해주세요>'.format(user_input_count))
        if len(number_input) >= 2: # 한자리수인지 검증
            print('한자리 정수를 입력해주세요.')
            continue
        else:
            try:
                int(number_input) # 숫자를 입력했는지 검증
            except:
                print('한자리 정수를 입력해주세요')
                continue
            else:
                if len(guess_list) == 0:  # 첫번째 자리수가
                    if int(number_input) == 0:
                        print('첫번째 자리수는 0이 아닙니다.') # 0인지 검증
                        continue
                if int(number_input) not in guess_list : # 사용자가 중복된 수를 입력하는 것을 방지
                    user_input_count += 1
                    guess_list.append(int(number_input))
                    continue
                else:
                    print('이미 입력한 숫자입니다. 중복된 숫자는 없습니다.')
                    continue


def check():
    strike = 0
    ball = 0
    if guess_list == answer_list: # 두 숫자(여기서는 리스트)가 일치할 경우 정답임을 표현후 종료
        print('정답입니다! 축하합니다~~')
        return
    for i in range (0, 4):
        if guess_list[i] in answer_list: # 일단 숫자가 있으면 ball 카운트 하나 증가
            ball += 1
            if guess_list[i] == answer_list[i]: # 그 숫자가 strike면 ball 카운트 하나 감소, strike 카운트 하나 증가)
                ball -= 1
                strike += 1
    print('예상한 숫자 :', ''.join(str(number) for number in guess_list)) # 자기가 입력한(생각한) 숫자 보여주기
    print('strike 개수 :', strike)
    print('ball 개수 :', ball)
    print('다시 한번 맞춰보세요~')
    guess_list.clear() # 예상 숫자 리스트 제거
    guess() # 예상하는 과정 반복
    check()

def restart():
    while True :
        user_ask = input('한판 더 하시겠습니까? ')
        if user_ask.casefold() == 'yes' :    # 대/소문자 구분없이 yes 판별
            answer_list.clear()
            guess_list.clear()
            game_start()
            break
        elif user_ask.casefold() == 'no' :   # 대/소문자 구분없이 no 판별
            print('게임을 종료합니다.')
            break
        else:
            print('yes 혹은 no로 입력해 주십시오.') # yes나 no가 아닐경우

def game_start():
    make_answer()
    guess()
    check()
    restart()

# 게임 실행
game_start()






        
         

