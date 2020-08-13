"""
A Publisher needs a message bus to publish it's messages.
"""
from m03_message_bus import MessageBus


class Publisher:
    def __init__(self, message_bus: MessageBus):
        self.message_bus = message_bus

    def publish_message(self, message):
        self.message_bus.publish_message(message)


if __name__ == "__main__":
    assert "Publisher" in globals()
    assert hasattr(Publisher(MessageBus()), 'message_bus')
    assert hasattr(Publisher(MessageBus()), 'publish_message')
