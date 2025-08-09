from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Rectangle
import random

class RunnerGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.runner = Rectangle(pos=(100, 100), size=(50, 50))
        self.obstacles = []
        with self.canvas:
            self.runner
        Clock.schedule_interval(self.update, 1/60)

    def on_touch_down(self, touch):
        self.runner.pos = (self.runner.pos[0], self.runner.pos[1] + 100)

    def update(self, dt):
        # Basit engel mantığı
        if random.randint(1, 60) == 1:
            ob = Rectangle(pos=(800, 100), size=(30, 30))
            self.obstacles.append(ob)
            self.canvas.add(ob)
        # Engel hareketi
        for ob in self.obstacles:
            ob.pos = (ob.pos[0] - 5, ob.pos[1])

class RunnerApp(App):
    def build(self):
        return RunnerGame()

if __name__ == '__main__':
    RunnerApp().run()