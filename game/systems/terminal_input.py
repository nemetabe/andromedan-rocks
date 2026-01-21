import sys
import select
import tty
import termios


class TerminalInput():
    """
    reads player input and updates player velocity
    """
    def __init__(self, world):
        self.world = world
        self._old_settings = None
        self.pressed_keys = []

    def start(self):
        self._old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    def stop(self):
        if self._old_settings:
            termios.tcsetattr(
                sys.stdin,
                termios.TCSADRAIN,
                self._old_settings
            )

    def poll(self):
        """
        update pressed_keys state (non-blocking)
        """
        if select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.read(1).lower()
            self.pressed_keys.append(key)

    def clear(self):
        """
        clear keys after frame is processed
        """
        self.pressed_keys.clear()
