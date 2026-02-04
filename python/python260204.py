class Animal:
    """ 
    파이썬에선 생성자 함수 이름을 __init__ 으로 통일했어요.
    __init__(self) 생성자 에서 self 키워드는 무조건 넣어 줘야해요
    자바에 있는 생성자 오버로딩 없어요
    """
    def __init__(self,leg=4,fur=True):
        self.leg=leg
        pass
    

bird=Animal()
dog=Animal()

print(bird.leg)