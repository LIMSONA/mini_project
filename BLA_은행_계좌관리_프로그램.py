import random
import datetime
import time
all_id = list() #고객DB파일에 있는 모든 계좌리스트


#################################################
class Account:
    #계좌개설된 개수 저장
    accountCount= 0
    # 생성자    
    def __init__(self):
        # 추천 계좌번호 생성하기 3파트(2-6-6)로 구분                 
        first = '%02d'%random.randint(0,99)
        now = datetime.datetime.now()
        second = now.strftime("%Y%m%d")
        third = '%06d'%random.randint(0,999999)
        recommend = first + "-" + second + "-" + third
        
        self.custom_id = input("\n 추천 계좌 번호는 아래와 같습니다.\
                                \n << {} >>\
                                \n\n계좌 번호를 입력해주세요 : ".format(recommend))
        self.name = input("고객 이름을 입력해주세요 : ")
        self.balance =int(input("얼마를 넣으실 건가요?? : "))
        self.bank = "BLA 은행"
        # =====================================
        
        
        
 
    # 데이터 호출 함수
    def info(self):
        return "{0}:{1}:{2}\n".format(self.custom_id, self.name, self.balance)

   # 계좌번호 얻기
    def get_id(self):
        return self.custom_id
    
    # 입금
    def deposit(self, money):
        if money > 0 :
            self.balance += money
            return self.balance
    
    # 출금
    def withdraw(self, money):
        if self.balance < money:
            print("잔액이 부족합니다.")
            return self.balance, 0
        else:
            self.balance -= money
            return self.balance, money
    
    # 잔액 조회
    def getBalance(self):     
        return self.balance 

######################################################
# BLA 은행 고객DB 파일 입/출력
file = "BLA_custom.txt"
try:
    f= open(file,"r")
    
    while True:
        line = f.readline()
        if not line:
            break
        a,b,c = line.split(":")
        #고객DB파일에 있는 모든 계좌리스트로 넣기
        all_id.append(Account(a,b,int(c)))

except Exception as err:
    print("파일이 없습니다")
    print(err)
    
 
########################################################  
# 계좌정보를 이용하여 구현될 기능을 담고 있는 클래스 멤버필드 
  
class BankManager:
    memory = {}
    
    # 3번 출금처리 함수
    def withdraw(self,custom_id):    
        for i in all_id:
            if i.get_id() == custom_id:
                money = int(input("출금금액 : "))
                balance, moneyresult = i.withdraw(money)
                text = "{0}원 출금하셨습니다.".format(moneyresult)
                print(text)
                BankManager.memory[custom_id] = text
                print("잔액은 {0} 원 입니다.".format(balance))
                return 0
        print("해당하는 계좌가 없습니다.")
        
    # 2번 입금처리 함수
    def deposit(self,custom_id):     
        for i in all_id:
            if i.get_id() == custom_id:
                money = int(input("입금금액 : "))
                print("\n")
                text = "{}가 입금되었습니다 ^_^".format(money)
                print(text)
                BankManager.memory[custom_id] = text
                bal = i.deposit(money)
                print("잔액은 {0} 입니다.".format(bal))
                return 0
        print("일치하는 계좌번호가 존재하지 않습니다")
    
    # 1번 계좌번호의 중복여부를 확인 함수
    def new_id(self,user):             
        for i in all_id:
            if i.get_id() == user.get_id():
                return "입력하신 계좌번호는 이미 존재하는 계좌번호 입니다."
            
        all_id.append(user)
        return "계좌 개설이 완료되었습니다."   
    
    # 4번 잔액 조회
    def bal_inquiry(self,custom_id):             
        for i in all_id:
            if i.get_id() == custom_id:
                print("잔액은 {} 입니다.".format(i.getBalance()))
                
        
    # 5번 환율 조회
    def exchange_rate(self):
        print("환율조회")
        
    # 6번 입출금 기록 함수
    def dw_record(self, custom_id):
        print(BankManager.memory)
                 
    # 파일 저장 메서드
    def save(self):
        f = open(file,"w")
        for i in all_id:
            f.write(i.info())
            
        f.close()
    

###################################################
# 고객에게 보일 BLA_은행 사용화면
class BankingSystem:
    def run():
        while True:
            print("\n====== Thank you for visiting!! ======\
                \n====== This is BLA bank (●'◡'●) ======\n")
            print("1. 계좌 개설")
            print("2. 입금 처리")
            print("3. 출금 처리")
            print("4. 잔액 조회")
            print("5. 환율 조회")
            print("6. 입출금 기록")
            print("7. 프로그램 종료")
            print("\n======================================")
            
            try:            
                select = input("원하는 메뉴를 입력해주세요-! : ")
            except Exception as e:
                print("잘못 입력하셨습니다!(⊙ｏ⊙)!!!\
                    \n다시 입력해주세요 ")              
            
            else:
                if select == "1":       # 계좌개설
                    print("======== 계좌 개설 ========")
                    print(BankManager().new_id(Account()))
                    print("============================")
                    time.sleep(1)
                    
                elif select == "2":     # 입금
                    print("======== 입 금 ========")
                    custom_id = input("계좌번호 : ")
                    BankManager().deposit(custom_id)
                    print("============================")
                    time.sleep(1)
                    
                elif select == "3":    # 출금
                    print("======== 출 금 ========")
                    custom_id = input("계좌번호 : ")
                    BankManager().withdraw(custom_id)
                    time.sleep(1)
                    
                elif select == "4":
                    print("======== 잔액 조회 ========")
                    BankManager().bal_inquiry(custom_id)
                    print("============================")
                    time.sleep(1)
                    
                elif select == "5":
                    print("======== 환율 조회 ========")
                    BankManager().exchange_rate()
                    print("============================")
                    time.sleep(1) 
                    
                elif select == "6":
                    print("======== 입출금 기록 ========")
                    BankManager().dw_record(custom_id)
                    print("============================")
                    time.sleep(1) 
                     
                elif select == "7":
                    BankManager().save()
                    print("프로그램 종료")
                    break
                    time.sleep(1)
                    
##############################
if __name__ =='__main__':
    BankingSystem.run()