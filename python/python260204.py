class Animal:
    """ 
    파이썬에선 생성자 함수 이름을 __init__ 으로 통일했어요.
    __init__(self) 생성자 에서 self 키워드는 무조건 넣어 줘야해요
    자바에 있는 생성자 오버로딩 없어요
    매개변수 옆에 =  이건 매개변수 안줬을시, 갔다쓰는 default 값
    """
    def __init__(self,leg=4,fur=True):
        # self.뭐뭐  이게 클래스의 속성 만들기
        self.leg=leg
        self.fur=fur
        self.eye="눈 2개"
    def makesound(self,str1="으르렁"):
        print(str1)
    

bird=Animal()
dog=Animal()
dog.makesound()

class Animal2:
    # 클래스 변수. 자바의 static 약간 비슷
    leg=4

dog=Animal2();
cat=Animal2();
""" 
객체.뭐뭐
파이썬은 자바처럼 클래스 안에 속성 일일히 적지 않아도,
생성자 따로 만들고 그딴짓 안해도,
객체.변수이름
이러면 맴버변수를 지가 알아서 만든다
파이썬은 인스턴트 변수를 먼저 뒤지고, 없으면 클래스변수를 뒤진다.
맴버변수랑 클래스변수랑 같이 있으면, shadowing 기능이 발동해서
클래스변수 접근이 뒷전이 된다.
"""
dog.leg=2
dog.eye=2
Animal2.leg=4

print(f"dog.leg:{dog.leg}") # 2
print(f"cat.leg:{cat.leg}") # 4






    
