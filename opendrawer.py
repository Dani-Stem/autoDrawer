import cv2
import speech_recognition as sr
import serial
import time


def speech_to_text():
	r = sr.Recognizer()

	with sr.Microphone() as source:
    	print("Speak now...")
    	audio = r.listen(source)
	text = ""
	try:
    	text = r.recognize_google(audio)
    	print("You said:", text)
	except sr.UnknownValueError:
    	print("Could not understand audio")
	except sr.RequestError as e:
    	print("Could not request results; {0}".format(e))
	return text

if __name__ == "__main__":
	#speech_to_text()
	user_input = speech_to_text()
	print(user_input)

if user_input == "open":
	ser = serial.Serial('/dev/ttyACM0', 9600)  # Replace 'COM3' with your Arduino's port and 9600 with the baud rate


	#ser.open()


	ser.write(b'open\n')


	data = ser.readline().decode().strip()
	print(data)


	ser.close()
