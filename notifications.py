class NotificationSystem:
    def __init__(self):
        self.notifications = []

    def add_notification(self, message):
        self.notifications.append(message)
        print(f"Notification added: {message}")

    def remove_notification(self, message):
        if message in self.notifications:
            self.notifications.remove(message)
            print(f"Notification removed: {message}")
        else:
            print(f"Notification not found: {message}")

    def get_notifications(self):
        return self.notifications

    def clear_notifications(self):
        self.notifications = []
        print("All notifications cleared")

# Example usage:
if __name__ == '__main__':
    notifications = NotificationSystem()
    notifications.add_notification('Player has joined the game')
    notifications.add_notification('Player has leveled up')
    print(notifications.get_notifications())
    notifications.remove_notification('Player has joined the game')
    print(notifications.get_notifications())
    notifications.clear_notifications()