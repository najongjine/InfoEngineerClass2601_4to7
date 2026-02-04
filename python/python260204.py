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
    leg=4

dog=Animal2();
cat=Animal2();
Animal2.leg=2


print(f"dog.leg:{dog.leg}")
print(f"cat.leg:{cat.leg}")



    
