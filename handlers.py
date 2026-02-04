# handlers.py

# Message Handling and Registration Logic

class MessageHandler:
    def __init__(self):
        self.handlers = {}

    def register_handler(self, message_type, handler_function):
        self.handlers[message_type] = handler_function

    def handle_message(self, message_type, message):
        if message_type in self.handlers:
            return self.handlers[message_type](message)
        else:
            raise ValueError(f"No handler for message type: {message_type}")

    def unregister_handler(self, message_type):
        if message_type in self.handlers:
            del self.handlers[message_type]