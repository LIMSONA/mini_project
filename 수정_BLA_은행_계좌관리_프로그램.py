import random
import datetime
import time
import pickle
all_id = list() #고객DB파일에 있는 모든 계좌리스트


#################################################
class Account:
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
        
        # =====================================
        
   # 1번 계좌번호 얻기
    def get_id(self):
        return self.custom_id
    
    # 2번 입금
    def deposit(self, money):
        if money > 0 :
            self.balance += money
            return self.balance
    
    # 3번 출금
    def withdraw(self, money):
        if self.balance < money:
            print("잔액이 부족합니다.")
            return self.balance, 0
        else:
            self.balance -= money
            return self.balance, money
    
    # 4번 잔액 조회
    def getBalance(self):     
        return self.balance 

    # 7번 데이터 저장 양식
    def info(self):
        return "{0}\t{1}\t{2}\n".format(self.custom_id, self.name, self.balance)


######################################################
class file:
    def __init__(self):
        file1 = "BLA_custom.txt"
        file2 = "dw_record.txt"
    
    def fopen(self):
        # 파일이있는지 여부를 파악(있으면 굳이 만들지 x / 없으면 만들고)    
        try:
            f1 = open(self.file1,"r")
            f2 = open(self.file2,"rb")
        except:
            ff1 = open(self.file1,"w")
            ff2 = open(self.file2,"wb")
        else:
            ff1 = f1.read()
            ff2 = pickle.load(f2) 
    
    def go(self): 
        ff1 = open(self.file1,"wa")
        ff2 = open(self.file2,"wa")
        


# BLA 은행 고객DB 파일 입/출력
# file1 = "BLA_custom.txt"
# file2 = "dw_record.txt"


# try:
#     f1= open(file1,"r")
#     f2= open(file2,"rb")
    
#     while True:
#         line1 = f1.readline()
#         # f1에 대한
#         if not line1:
#             break
#         a,b,c = line1.split("\t")
#         #고객DB파일에 있는 모든 계좌리스트로 넣기
#         all_id.append(Account(a,b,int(c)))

        
    # while True:    
    #     line2 = pickle.load(f2)
    #     # f2에 대한
    #     if not line2:
    #         break
        
        
        
# except Exception as err:
#     print("파일이 없습니다")
#     print(err)
    
 
########################################################  
# 계좌정보를 이용하여 구현될 기능을 담고 있는 클래스 멤버필드 
  
class BankManager:
    
    # 1번 계좌번호의 중복여부를 확인 함수
    def new_id(self,custom):             
        for i in all_id:
            if i == custom.get_id():
                return "입력하신 계좌번호는 이미 존재하는 계좌번호 입니다."
        all_id.append(custom)
          # 계좌 개설 시 딕셔너리 생성
        ff2.write(setdefault(custom.get_id(),[]
        return "계좌 개설이 완료되었습니다."
        
            
            
    # 2번 입금처리 함수
    def deposit(self,custom_id):     
        for i in all_id:
            if i.get_id() == custom_id:
                money = int(input("입금금액 : "))
                print("\n")
                text = "{}원 입금되었습니다. ".format(money)
                print(text)
                memory_value = memory[custom_id]
                memory_value.append(text)
                bal = i.deposit(money)
                print("잔액은 {0} 입니다.".format(bal))
                return 0
        print("일치하는 계좌번호가 존재하지 않습니다")
    
    # 3번 출금처리 함수
    def withdraw(self,custom_id):    
        for i in all_id:
            if i.get_id() == custom_id:
                money = int(input("출금금액 : "))
                balance, moneyresult = i.withdraw(money)
                text = "{0}원 출금하셨습니다.".format(moneyresult)
                print(text)
                memory_value = memory[custom_id]
                memory_value.append(text)
                print("잔액은 {0} 원 입니다.".format(balance))
                return 0
        print("해당하는 계좌가 없습니다.")
            
    # 4번 잔액 조회
    def bal_inquiry(self,custom_id):             
        for i in all_id:
            if i.get_id() == custom_id:
                print()
                print("잔액은 {} 입니다.".format(i.getBalance()))
                
        
    # 5번 환율 조회
    def exchange_rate(self):
        
        
    # 6번 입출금 기록 함수
    def dw_record(self, custom_id):
        for i in all_id:
            if i.get_id() == custom_id:
                num = 0
                for line in memory[custom_id]:
                    num+=1
                    print("[{}]  {}".format(num, line))
                    
        
    # 7번 프로그램 종료 - 파일 저장 메서드
    # def save(self):
    #     f1 = open(ff1,"wa")
    #     for i in all_id:
    #         f1.write(i.info())
    #     f1.close()
        
        # f2 = open(file2,"wb")
        # pickle.dump(memory)
        # f2.close()

###################################################
# 고객에게 보일 BLA_은행 사용화면
class BankingSystem:
    def run():
        file.fopen() 
                          
        while True:
            print("\n====== Thank you for visiting!! ======\
                \n====== This is BLA bank (●'◡'●) ======\n")
            print("= 이용하시기 원하는 메뉴번호를 입력해주세요=")
            print(" [1] 계좌 개설")
            print(" [2] 입금 처리")
            print(" [3] 출금 처리")
            print(" [4] 잔액 조회")
            print(" [5] 환율 조회")
            print(" [6] 입출금 기록")
            print(" [7] 프로그램 종료")
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
                    print("============================")
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
                    # BankManager().save()
                    print("프로그램 종료")
                    break
                    time.sleep(1)
                    
##############################
# 메인함수 선언해주기
if __name__ =='__main__':
    BankingSystem.run()