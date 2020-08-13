A Message is the currency of many architectures.
Message based architectures enable tests by decoupling actions and responses.
A generic message accomplishes decoupling by using only primitives.
Most messages only use the most generic primitive the string.

We'll use messages to interact and test program we created to be testable.

A message carries two things.
    The name of the thing that happened and,
     then also any details.

In many ways the web and its HTTP protocol are just a transport layer for messages.

Example Topics:
    "user_registered" - A user registered.
    "button_clicked" - A button was clicked.
    "record_saved" - A record was saved.

Content would contain serialized details.

REQUIREMENTS:
Create a data structure to hold a generic message that includes a single topic,
 and a payload that contains a text representation of its payload.
 topics must start with a letter and must not contain an '='
 The payload may contain anything a string can contain other than "\n" or "\r".
