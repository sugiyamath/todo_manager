import time
import pygame
from datetime import datetime


class PomodoroTimer:
    def __init__(self, sound_file):
        self.sound_file = sound_file
        self.previous_flag = None
        pygame.mixer.init()

    def play_sound(self):
        pygame.mixer.music.load(self.sound_file)
        pygame.mixer.music.play()

    def counter(self):
        now = datetime.now()
        if 12 <= now.hour and now.hour < 13:
            return False, int(60 - now.minute)
        else:
            v = int(30 - now.minute % 30)
            if v <= 5:
                return False, v
            else:
                return True, v

    def run(self):
        while True:
            flag, c = self.counter()
            if flag:
                s = "work"
            else:
                s = "rest"
            print(f"\r{s}: {c}", end='', flush=True)
            if self.previous_flag is not None and self.previous_flag != flag:
                self.play_sound()
            self.previous_flag = flag
            time.sleep(1)


if __name__ == "__main__":
    timer = PomodoroTimer('bell.wav')
    timer.run()
