class Car:
    instance_count = 0  # class 변수

    def __init__(self, size=10, color='black'):
        self.size = size  # 인스턴스 변수
        self.color = color  # 인스턴스 변수
        Car.instance_count = Car.instance_count + 1

    def __str__(self) -> str:
        return "[color {} size {}]".format(self.color, self.size)

    def set_speed(self, speed):
        self.speed = speed

    def auto_cruse(self):  # 인스턴스 메소드
        print("자율 주행 모드")
        print("{} 속도로 자율주행".format(self.speed))

    # 스태틱은 스태틱만 호출 가능
    @staticmethod
    def check_type(model_code):
        if model_code >= 20:
            print("이 자동차는 전기차")
        elif 10 <= model_code < 20:
            print("이 자동차는 가솔린차")
        else:
            print("이 자동차는 디젤차")

    @classmethod
    def count_instance(cls):
        print("자동차 생산대수 : {}".format(Car.instance_count))

