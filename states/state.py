class State():
    def __init__(self, UI):
        self.window = UI
        self.prev_state = None

    def update(self, dt, actions):
        pass

    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.window.state_stack) > 1:
            self.prev_state = self.window.state_stack[-1]
        self.window.state_stack.append(self)

    def exit_state(self):
        self.window.state_stack.pop()