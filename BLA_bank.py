import datetime #계좌 
import random # 계좌 third



print("안녕하세요! 가장 친절한 BLA 은행입니다.")
print("BLA은행이 처음이신가요? ")



class BLA_bank:
    
    def __init__(self, name, birth, account=0):
        self.name = name
        self.birth = birth
        self.bank = "BLA 은행"
        self.account = account
        self.custom_dict= {}



    
#     # 1번 은행 맨 처음 방문인지?
#     def custom_q():
#         while True:
#             print("맞으시면 y, 아니면 n를 입력해주세요")
#             q1 = input()
#             if not q1 =="y" and not q1=="n": #잘못입력
#                 print("정확히 입력해주세요!")
#                 continue
#             elif q1 =="n": #기존고객
#                 print("기존고객이시네요!")
#                 break
#             elif q1=="y": #신규고객
#                 print("처음이시네요!")
#                 break

# class New_custom:   
#     # 2번 신규고객일 경우 입력
#     def new_custom_input(**kwargs):
#         new_custom={"이름":None,"생년월일":None}
#         new_info = input("이름과 생년월일을 입력하십시오. 공백으로 구분해주세요\
#             \n 예시: 홍길동 220107").split()
#         new_custom["이름"] = new_info[0]
#         new_custom["생년월일"] = new_info[1]
#         return new_custom

#     # 개좌 개설하기
#     # 어떤 업무를 하는지 물어보고 계좌 생성 후 키로 사용
    def account_num(self):
        ## 추가하기: 잘못 누를 경우
        type = int(input("어떤 업무를 하시겠습니까??"))
        
        first = '%02d'%type
        now = datetime.datetime.now()
        second = now.strftime("%Y%m%d")
        third = '%06d'%random.randint(0,999999)
        
        self.account_num = first + "-" + second + "-" + third
        
        return self.account_num
        
        
#     # 신규고객 정보 받아서 고객리스트에 넣기 
#     # (사전: 어떤 업무를 하는지 물어보고 계좌 생성 후 키로 사용)
#     def new_custom(self):
#         cus_dict_key = self.account()
#         cus_dict_value = self.new_custom_input()
#         self.custom_dict.update(cus_dict_key,cus_dict_value)
#         print(self.custom_dict)
        
        
        
        


# # custom= {} q
# # {"이름": ,"생년월일", "계좌번호":}


    



# class BLA_:
    
#     account_cnt= 0 #계좌번호 만든 순서
    
