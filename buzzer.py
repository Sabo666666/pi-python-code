import RPi.GPIO as GPIO
import time

# Define pin for buzzer
pinBuzzer = 23  # Change this to your actual GPIO pin number

# Define frequencies for the notes
frequencyA4s = 466
frequencyB4 = 494
frequencyC5 = 523
frequencyC5S = 554
frequencyD5 = 587
frequencyD5s = 622
frequencyE5 = 659
frequencyF5 = 698
frequencyF5s = 740
frequencyG5 = 784
frequencyG5s = 831
frequencyA5 = 880
frequencyA5s = 932
frequencyB5 = 988
frequencyC6 = 1047
frequencyC6s = 1109
frequencyD6 = 1175
frequencyD6s = 1245
frequencyE6 = 1319
frequencyF6 = 1397
frequencyF6s = 1480
stop = 0

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBuzzer, GPIO.OUT)
pwm = GPIO.PWM(pinBuzzer, 100)  # Initialize PWM on pinBuzzer 100Hz frequency

def play_tone(note, duration):
    pwm.ChangeFrequency(note)
    pwm.start(80)  # 50% duty cycle
    time.sleep(duration)
    pwm.stop()
    time.sleep(0.02)  # Short pause between notes

def play_note_sequence():
    print("Playing tones")
    play_tone(frequencyB5, 0.2)
    play_tone(frequencyA5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyG5s, 0.2)
    play_tone(frequencyG5s, 0.2)
    play_tone(frequencyA5s, 0.2)
    play_tone(frequencyB5, 0.2)
    play_tone(frequencyC6s, 0.2)
    play_tone(frequencyA5s, 0.4)
    play_tone(frequencyF5s, 0.4)
    play_tone(frequencyE6, 0.4)
    play_tone(frequencyC6s, 0.4)
    play_tone(frequencyC6s, 0.3)
    play_tone(frequencyC6s, 0.3)
    play_tone(frequencyD6s, 0.2)
    pwm.stop()
    time.sleep(0.2)

    play_tone(frequencyB5, 0.2)
    play_tone(frequencyA5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyG5s, 0.2)
    play_tone(frequencyG5s, 0.2)
    play_tone(frequencyA5s, 0.2)
    play_tone(frequencyB5, 0.2)
    play_tone(frequencyC6s, 0.2)
    play_tone(frequencyG5s, 0.4)
    pwm.stop()
    time.sleep(0.4)
    play_tone(frequencyG5s, 0.2)
    play_tone(frequencyA5s, 0.2)
    play_tone(frequencyB5, 0.2)
    play_tone(frequencyC6s, 0.2)
    play_tone(frequencyA5s, 0.3)
    play_tone(frequencyF5s, 0.3)
    play_tone(frequencyD5s, 0.2)
    pwm.stop()
    time.sleep(0.2)

    play_tone(frequencyB5, 0.2)
    play_tone(frequencyA5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyG5s, 0.2)
    play_tone(frequencyG5s, 0.2)
    play_tone(frequencyA5s, 0.2)
    play_tone(frequencyB5, 0.2)
    play_tone(frequencyC6s, 0.2)
    play_tone(frequencyA5s, 0.4)
    play_tone(frequencyF5s, 0.4)
    play_tone(frequencyE6, 0.4)
    play_tone(frequencyC6s, 0.4)
    play_tone(frequencyC6s, 0.3)
    play_tone(frequencyC6s, 0.3)
    play_tone(frequencyD6s, 0.2)
    pwm.stop()
    time.sleep(0.2)

    play_tone(frequencyB5, 0.2)
    play_tone(frequencyA5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyG5s, 0.2)
    play_tone(frequencyG5s, 0.2)
    play_tone(frequencyA5s, 0.2)
    play_tone(frequencyB5, 0.2)
    play_tone(frequencyC6s, 0.2)
    play_tone(frequencyG5s, 0.4)
    pwm.stop()
    time.sleep(0.4)
    play_tone(frequencyG5s, 0.2)
    play_tone(frequencyA5s, 0.2)
    play_tone(frequencyB5, 0.2)
    play_tone(frequencyC6s, 0.2)
    play_tone(frequencyA5s, 0.4)
    play_tone(frequencyF5s, 0.4)
    play_tone(frequencyD5s, 0.4)
    play_tone(frequencyF5s, 0.4)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyG5s, 0.1)
    play_tone(frequencyG5s, 0.3)
    play_tone(frequencyB5, 0.2)
    play_tone(frequencyA5s, 0.2)
    play_tone(frequencyF5s, 0.1)
    play_tone(frequencyD5s, 0.3)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.2)
    play_tone(frequencyF5s, 0.1)
    play_tone(frequencyF5s, 0.3)
    pwm.stop()
    time.sleep(0.2)

try:
    while True:
        play_note_sequence()
        time.sleep(2)  # Delay before repeating the song
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
