from RealtimeSTT import AudioToTextRecorder

def process_text(text, control_vars):
    if "end recording" in text.lower():
        control_vars['listen'] = False
        print(text)
        print("\nStopping...")
        return
    print(text)

if __name__ == '__main__':
    recorder = AudioToTextRecorder()
    control_vars = {'listen': True}

    while control_vars['listen']:
        recorder.text(lambda text: process_text(text, control_vars))
