# Придумайте свой примеры видов полиморфизма. Прикрепите скриншоты или файл с ними.

class Future:
    def __init__(self,street):
        self.__street = street

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self,d):
        self.__street = d

    def info(self):
        print("Future")
        print("Street: " + self.__street)

class Present(Future):

    def __init__(self,sunny,rain,street):
        super().__init__(street)
        self.__sunny = sunny
        self.__rain = rain

    @property
    def sunny(self):
        return self.__sunny

    @sunny.setter
    def sunny(self,s):
        if s =="Yes":
            self.__sunny = s
        else:
            raise ValueError

    @property
    def rain(self):
        return self.__rain

    @rain.setter
    def rain(self,r):
        if r =="Yes":
            self.__rain = r
        else:
            raise ValueError

    def info(self):
        print("Present")
        print("Street: " + self.street)
        print("Sunny: " + str(self.sunny))
        print("Rain: " + str(self.rain))
        print("Weather: " + str(self.weather()))

    def weather(self):
        return self.__sunny + self.__rain

# Посмотрим как это работает
    fut = Future("cloudy")
    fut.info()

pres = Present("Yes","Yes","wet")
pres.info()
