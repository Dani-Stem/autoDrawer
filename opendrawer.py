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
	try:
		ser = serial.Serial('/dev/ttyACM0', 9600)  # Replace 'COM3' with your Arduino's port and 9600 with the baud rate
	except ValueError:
		print("Check parameters")
		exit(1)
	except serial.SerialException:
		print("Could not connect to Arduino")
		exit(1)

	while True:
		user_input = speech_to_text()
		print(user_input)

		if user_input == "open":
			ser.write(b'open\n')
			time.sleep(1)
			data = ser.readline().decode().strip()
			print(data)
			time.sleep(5) # Wait for Arduino to completely open/close

		elif user_input == "close":
			ser.write(b'close\n')
			time.sleep(1)
			data = ser.readline().decode().strip()
			print(data)
			time.sleep(5) # Wait for Arduino to completely open/close

		elif user_input == "exit":
			ser.close()
			exit(0)

		else:
			print("Bad input")
