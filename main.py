from youtubesearchpython import VideosSearch
import webbrowser
import pygame, os, time
from states.start_window import Title_Window


youtube_url = 'http://www.youtube.com/results?search_query='
screen_width = 1920
screen_height = 1080

class UI():
    def __init__(self):
        pygame.init()
        self.width = 1920
        self.height = 1080
        self.canvas = pygame.Surface((self.width, self.height))
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.playing = True
        self.actions = {"YouTube": False, "Google": False}
        self.dt = 0
        self.prev_time = 0
        self.state_stack = []
        self.load_states()

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.actions["YouTube"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.actions["Youtube"] = False

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)

    def render(self):
        self.state_stack[-1].render(self.canvas)
        self.screen.blit(pygame.transform.scale(self.canvas, (self.width,self.height)), (0,0))
        pygame.display.flip()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def draw_text(self, surface, text, color, x, y, size):
        self.font = pygame.font.SysFont('Tahoma', size)
        text_surface = self.font.render(text, True, color)
        #text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        surface.blit(text_surface, text_rect)

    def load_states(self):
        self.title_screen = Title_Window(self)
        self.state_stack.append(self.title_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    


def main():
    window = UI()
    while window.running:
        window.game_loop()
    



    return

if __name__ == '__main__':
    main()

#webbrowser.open()

#videoSearch = VideosSearch('ludwig', limit = 2)

#print(videoSearch)