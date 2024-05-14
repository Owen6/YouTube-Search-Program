from states.state import State
from states.youtube_window import youtube_window


class Title_Window(State):
    def __init__(self, UI):
        State.__init__(self,UI)
        self.bg_color = (255,255,255)

    def update(self, dt, actions):
        if actions["YouTube"]:
            new_state = youtube_window(self.window)
            new_state.enter_state()
        self.window.reset_keys()

    def render(self,display):
        display.fill(self.bg_color)
        self.window.draw_text(display, "Title Window", (0,0,0), self.window.width/2, self.window.width/2,20)