"""
    A message includes a topic and a payload.

    A topic is a text identifier used in routing.
    Topics must start with a letter and must not contain an '='

    A payload is a dictionary but the keys and values have special rules.

    Neither Keys must not contain any newline or return characters e.g '\n' or '\r'.

    Keys must not be blank.
    Payload may be blank.
"""


class Message:
    def __init__(self, topic=None, payload=None):
        self.topic: str = topic if topic is not None else ""
        self.payload: dict = payload if payload is not None else {}


if __name__ == "__main__":
    assert "Message" in globals()
    m = Message("example")
    assert hasattr(m, 'topic')
    assert hasattr(m, 'payload')
    assert type(m.topic) == str
    assert type(m.payload) == dict
    for key in m.payload:
        value = m.payload[key]
        assert type(key) == str
        assert type(value) == str
        assert key.find('\n') == -1
        assert key.find('\r') == -1
        assert value.find('\n') == -1
        assert value.find('\r') == -1
