"""
A Message Bus allows topics to be subscribed to,
and publishes messages from publishers to subscribers.
"""
from m02_subscriber import Subscriber


class MessageBus:

    def __init__(self):
        self.topics: {str: [Subscriber]} = {}

    def subscribe_to_topic(self, topic, subscriber: Subscriber):
        if topic not in self.topics:
            self.topics[topic] = []
        self.topics[topic].append(subscriber)

    def publish_message(self, message):
        if message.topic in self.topics:
            for s in self.topics[message.topic]:
                s.handle_message(message)


if __name__ == "__main__":
    assert "MessageBus" in globals()
    assert hasattr(MessageBus, "subscribe_to_topic")
    assert hasattr(MessageBus, "publish_message")
