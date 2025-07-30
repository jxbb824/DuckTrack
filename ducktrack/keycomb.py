import keyboard


class KeyCombinationListener:
    """
    Key combination listener using the 'keyboard' library.
    """

    def __init__(self):
        self.hotkeys = []

    def add_comb(self, keys, callback):
        hotkey_string = "+".join(keys)
        # Using suppress=True to prevent the key combination from being passed to other applications
        hotkey = keyboard.add_hotkey(hotkey_string, callback, suppress=True)
        self.hotkeys.append(hotkey)

    def start(self):
        # The 'keyboard' library starts listening automatically
        # when a hotkey is registered.
        pass

    def stop(self):
        keyboard.unhook_all_hotkeys()