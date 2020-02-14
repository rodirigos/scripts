from pynput import keyboard

kb_controller = keyboard.Controller()

def execute_indent_xaml():
    kb_controller.press(keyboard.Key.end)
    kb_controller.release(keyboard.Key.end)
    kb_controller.press(keyboard.Key.delete)
    kb_controller.release(keyboard.Key.delete)
    kb_controller.press(keyboard.Key.enter)
    kb_controller.release(keyboard.Key.enter)

def on_press(key):
    try:
        pass
    except AttributeError:
        pass
    
listener = keyboard.Listener(
    on_press=on_press)
listener.start()

with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.num_lock:
            execute_indent_xaml()
        if event.key == keyboard.Key.esc:
            break
