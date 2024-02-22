from abc import ABC, abstractmethod


class MessageService(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass


class EmailService(MessageService):

    def send(self, message: str, receiver: str):
        print(f"Sending email:{message} to {receiver}")


class SmsService(MessageService):

    def send(self, message: str, receiver: str):
        print(f"Sending SMS:{message} to {receiver}")


class NotificationService:

    def __init__(self, type_message: MessageService, message: str, receiver: str):
        self.type_message = type_message
        self.message = message
        self.receiver = receiver

    def send_notification(self):
        self.type_message.send(self.message, self.receiver)


text = "Дотримані принципи SOLID"

email_message = EmailService()
sms_message = SmsService()

notifi_by_email = NotificationService(email_message, text, "Andrew")
notifi_by_sms = NotificationService(sms_message, text, "Andrew")

notifi_by_email.send_notification()
notifi_by_sms.send_notification()
