class Animal:
    # 파이썬에선 생성자 함수 이름을 통일했어요.
    # 자바에 있는 생성자 오버로딩 없어요
    def __init__(self,leg=4,fur=True):

        pass
    

bird=Animal()
dog=Animal()

print(bird.leg)