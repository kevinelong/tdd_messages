"""
A Subscriber must be able to handle an incoming message.
"""
from m01_message import Message


class Subscriber:
    def __init__(self):
        self.last_received = None

    def handle_message(self, message: Message):
        self.last_received = message


if __name__ == "__main__":
    assert "Subscriber" in globals()
    assert hasattr(Subscriber(), 'handle_message')
