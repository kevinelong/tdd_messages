"""
Messages are:
    published by Publishers;
    handled by Subscribers;
    Publishers and Subscribers do not communicate directly.

    A MessageBus has a collection of Publishers and Subscribers and brokers messages.

    A subscriber subscribes to a specific Topic.
    Any publisher can put something on the message bus.
    A Message has a topic.

"""
from m01_message import Message
from m02_subscriber import Subscriber
from m03_message_bus import MessageBus
from m04_publisher import Publisher

if __name__ == "__main__":
    assert "MessageBus" in globals()
    assert hasattr(MessageBus, "subscribe_to_topic")
    assert hasattr(MessageBus, "publish_message")

    # IMAGINED USE
    s = Subscriber()
    mb = MessageBus()
    mb.subscribe_to_topic("abc", s)
    p = Publisher(mb)
    p.publish_message(Message("abc", "xyz"))
    assert type(s.last_received) == Message
    assert s.last_received.topic == "abc"
    assert s.last_received.payload == "xyz"
