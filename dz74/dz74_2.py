from abc import ABC, abstractmethod


class Subscriber(ABC):

    @abstractmethod
    def update(self, context):
        pass


class Channel:

    def __init__(self):
        self.__subscribers = []
        self.__videos = []

    def subscribe(self, s: Subscriber):
        self.__subscribers.append(s)

    def unsubscribe(self, s: Subscriber):
        self.__subscribers.remove(s)

    def notify(self, context):
        for s in self.__subscribers:
            s.update(context)

    def add_video(self, name: str):
        self.__videos.append(name)
        self.notify(context=name)


class Concrete_Sub(Subscriber):

    def __init__(self, login):
        self.login = login

    def update(self, context):
        print(f"Сповіщення для  {self.login}:  Додано нове відео '{context}' ")
# Метод підписки для користовича на канал
    def subscribe(self,cannel:Channel):
        return cannel.subscribe(self)


channel_video=Channel()
s1=Concrete_Sub("user1")
s2=Concrete_Sub("user2")
s3=Concrete_Sub("user3")
channel_video.subscribe(s1)
channel_video.subscribe(s2)
s3.subscribe(channel_video)
channel_video.add_video("Діти і морозиво")
channel_video.add_video("Як з'їсти багато морозива ,поки мама не бачить!")

