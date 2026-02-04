class PlayerRegistrationState:
    WAITING_FOR_TITLE = 'waiting_for_title'
    WAITING_CONFIRMATION = 'waiting_confirmation'
    WAITING_GROUP_JOIN = 'waiting_group_join'
    WAITING_REFERRER = 'waiting_referrer'


class StateManager:
    def __init__(self):
        self.state = PlayerRegistrationState.WAITING_FOR_TITLE
        self.current_title = None
        self.registration_data = {}

    def get_player_state(self):
        return self.state

    def set_player_state(self, state):
        self.state = state

    def clear_player_state(self):
        self.state = PlayerRegistrationState.WAITING_FOR_TITLE
        self.current_title = None
        self.registration_data.clear()