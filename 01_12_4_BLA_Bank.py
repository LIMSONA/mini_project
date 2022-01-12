# 환율

import os.path
import sys
import datetime
import time
import random
import requests
from bs4 import BeautifulSoup

class AccountCreate:
    def __init__(self, userAccount, userName, userBalance=0):
        self.userAccount = userAccount
        self.userName = userName
        self.userBalance = userBalance
        
        bankinform.append([userAccount,userName,userBalance]) # 계좌 이름 잔액 저장
        allAccount.append(userAccount)
        
        # 최초 입금 기록 저장
        accountfile = userAccount + ".txt"
        with open(accountfile, 'a', encoding="UTF-8") as f:
            time = datetime.datetime.now()
            f.write("{}\t{} 원 입금하였습니다".format(time, self.userBalance))
            f.write("\n")

class BankManager:

    # 계좌 확인
    def accountCheck(account):
        if account in allAccount:
            print("계좌 생성 실패")
            print("이미 존재하는 계좌번호입니다.")
        else:
            return True
        
    # 1번 계좌 개설
    def create():
        #추천계좌 생성
        first = '%02d'%random.randint(0,99)
        now = datetime.datetime.now()
        second = now.strftime("%Y%m%d")
        third = '%06d'%random.randint(0,999999)
        recommend = first + "-" + second + "-" + third
        print("* 원하는 번호로 계좌를 생성 할 수 있습니다.\
            \n\n 추천 계좌 번호는 아래와 같습니다.\
                \n<< {} >>\
                    \n===========================================".format(recommend))
        account = input(" - 계좌 번호: ")
        if BankManager.accountCheck(account):
            name = input(" - 이름 입력: ")
            print("\n* 소정의 금액을 입금해주셔야 통장이 개설완료 됩니다 \
                \n* 얼마를 입금하시겠습니까?\n")
            bal = int(input(" - 첫 입금 금액: "))
            print("\n* 개설이 완료 되셨습니다. 첫화면으로 이동합니다.")
            # 입력 받은 데이터를 AccountCreate 클래스로 
            AccountCreate(account, name, bal)
            
       
    # 2번 입금 
    def deposit():
        print("* 입금처리를 진행할 계좌번호를 입력해주세요\n")
        inputaccount = input(" - 계좌 번호: ") # 계좌번호 입력
        if inputaccount in allAccount: # 계좌번호가 존재하면 금액 입력
            inputmoney = int(input(" - 입금 금액: ")) # 금액 입력
            for account in bankinform: # 계좌번호 찾기 
                if inputaccount == account[0]: # 
                    account[2] = int(account[2]) + inputmoney # 계좌번호 잔액에 금액 추가
                    print("* {}원 입금이 완료 되었습니다. 첫화면으로 이동합니다.".format(inputmoney))            
                       
            # 입금 내역 기록
            myaccount = inputaccount + ".txt"
            with open(myaccount, 'a', encoding='UTF-8') as f:
                time = datetime.datetime.now()
                f.write("{}\t{}원 입금하였습니다".format(time, inputmoney))
                f.write("\n")
                
        # 계좌번호 없을 경우
        else:
            print("===== [!] 없는 계좌번호 입니다 =====")
            print("* 첫 화면으로 돌아갑니다 ")
            
        
    # 3번 출금
    def withdraw():
        print("* 출금처리를 진행할 계좌번호를 입력해주세요\n")
        inputaccount = input(" - 계좌 번호: ")
        if inputaccount in allAccount:
            inputmoney = int(input(" - 출금 금액: "))
            for account in bankinform:
                if inputaccount == account[0]:
                    if int(account[2]) >= inputmoney:
                        account[2] = int(account[2]) - inputmoney
                        print("* {}원 출금이 완료 되었습니다. 첫화면으로 이동합니다.".format(inputmoney))            
                      
                        #출금내역 기록
                        myaccount = inputaccount + ".txt"
                        with open(myaccount, 'a', encoding='UTF-8') as f:    
                            time = datetime.datetime.now()
                            f.write("{}\t{}원 출금하였습니다".format(time, inputmoney))
                            f.write("\n")
                        
                    else: #잔액이 모자랄 경우
                        print("===== [!] 잔액이 모자랍니다  =====")
                        print("* 첫 화면으로 돌아갑니다 ")
                    
                else:
                    pass # 다음꺼 찾기
        else: # 없는 계좌일 경우
            print("===== [!] 없는 계좌번호 입니다 =====")
            print("* 첫 화면으로 돌아갑니다")
        
            
    # 4번 잔액조회
    def showBalance():
        print("* 잔액조회 하고 싶은 계좌번호를 입력해주세요\n")
        inputaccount = input("계좌를 입력해주세요: ")
        if inputaccount in allAccount:
            for account in bankinform:
                if inputaccount == account[0]:
                    print("\n\t- [ {} ]계좌의 잔액은 [ {} ]원입니다".format(account[0], account[2]))
                    print("\n* 첫 화면으로 돌아갑니다")
        else: # 없는 계좌일 경우
            print("===== [!] 없는 계좌번호 입니다 =====")
            print("* 첫 화면으로 돌아갑니다")
         
    # 5번 환율 조회
    def exchangeCurrent( ):
        address = f'https://finance.naver.com'
        addition = '/marketindex/?tabSel=exchange#tab_section'
        res = requests.get(address +addition)
        soup = BeautifulSoup(res.content, 'html.parser')

        frame = soup.find('iframe', id="frame_ex1")
        frameaddr = address+frame['src'] #frame내의 연결된 주소 확인 

        res1 = requests.get(frameaddr) # frame내의 연결된 주소를 읽어오기 
        frame_soup = BeautifulSoup(res1.content, 'html.parser')
        items = frame_soup.select('body > div > table > tbody > tr')

        for item in items:
            name = item.select('td')[0].text.replace("\n","")
            name = name.replace("\t", "")
            print(name + "\t" + item.select('td')[1].text)
               
                    
    # 6번 계좌 입출금 이력 조회
    def accountInfo():
        print("* 입출금 이력을 조회할 계좌번호를 입력해주세요\n")
        inputaccount = input("- 계좌 번호: ")
        accountfile = inputaccount + '.txt'
        if os.path.isfile(accountfile):
            with open(accountfile, 'r', encoding='UTF-8') as f:
                datas = f.readlines()
            cnt=0
            for data in datas:
                cnt+=1
                print('[{}]\t{}'.format(cnt,data),end="")
                  
        else:
            print("====== [!] 이력이 없습니다 ======")
            print("* 첫 화면으로 돌아갑니다 ")
        


class BankSystem:
    def lobby():
        while True:
            print("\n====== Thank you for visiting!! ======\
                \n====== This is BLA bank (●'◡'●) ======\n")
            print(" [1] 계좌 개설")
            print(" [2] 입금 처리")
            print(" [3] 출금 처리")
            print(" [4] 잔액 조회")
            print(" [5] 환율 조회")
            print(" [6] 입출금 기록")
            print(" [7] 프로그램 종료")
            print("\n======================================")
        
            try:
                work = input("원하시는 번호를 입력하세요!   ")
            except Exception:
                print(" 잘못 입력하셨습니다 !!!! 번호를 다시 확인해주세요")
            else:
                if work == "1":
                    print("\n============= [1] 계좌 개설 ===============")
                    BankManager.create()
                    print("============================================")
                    time.sleep(2)
                elif work == "2":
                    print("\n============= [2] 입금 처리 ===============")
                    BankManager.deposit()
                    print("============================================")
                    time.sleep(2)
                elif work == "3":
                    print("\n============= [3] 출금 처리 ===============")
                    BankManager.withdraw()
                    print("============================================")
                    time.sleep(2)
                elif work == "4":
                    print("\n============= [4] 잔액 조회 ===============")
                    BankManager.showBalance()
                    print("============================================")
                    time.sleep(2)
                elif work == "5":
                    print("\n============= [5] 환율 조회 ===============")
                    BankManager.exchangeCurrent()
                    print("============================================")
                    time.sleep(2)
                elif work == "6":
                    print("\n============= [6] 입출금 기록 ===============")
                    BankManager.accountInfo()
                    print("\n============================================")
                    time.sleep(2)
                elif work == "7":
                    print("=============================================")
                    with open('bankaccountlist.txt', 'w') as f:
                        for data in bankinform:
                            save = str(data[0]) + ":" + str(data[1]) + ":" + str(data[2]) + "\n"
                            f.write(save)
                    print("종료합니다")
                    sys.exit()
            


bankinform = []
allAccount = []

if __name__ == "__main__":
    if os.path.isfile('bankaccountlist.txt'): # 이전 정보 확인
        with open('bankaccountlist.txt', 'r') as f:
            datas = f.readlines()

            # bankinform에는 실제 [[계좌,이름,금액],[계좌,이름,금액]]형식으로 들어가있음          
            for data in datas:
                bankinform.append(data[:-1].split(":")) #줄바꿈은 제외하기위해서 -1까지

        for account in bankinform: # 계좌번호 리스트 저장
            allAccount.append(account[0])
    else:
        pass

    BankSystem.lobby()
