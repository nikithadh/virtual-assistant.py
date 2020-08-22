import os
import pyttsx3

pyttsx3.speak(" WELCOME TO MENU DRIVEN PROGRAM ")
print(" \n                                   WELCOME                         \n ")
pyttsx3.speak(" HI I AM YOUR VIRTUAL ASSISTANT ")
print(" \n                       HI I AM YOUR VIRTUAL ASSISTANT              \n ")
pyttsx3.speak("HERE IS THE LIST OF APPLICATIONS IN WHICH I CAN HELP YOU ON YOUR SYSTEM ")
print("\n                   LIST OF APPLICATIONS , I CAN HELP YOU IN         \n ")
print()
print("\n                          1. CHROME                                 \n")
print("\n                          2. INTERNET EXPLORER                      \n")
print("\n                          3. ITUNES                                 \n")
print("\n                          4. VLC PLAYER                             \n")
print("\n                          5. WINDOWS MEDIA PLAYER                   \n")
print("\n                          6. REAL PLAYER                            \n")
print("\n                          7. ACROBAT READER DC                      \n")
print("\n                          8. WORD PAD                               \n")
print("\n                          9. CONTROL PANEL                          \n")
print("\n                          10. MS PAINT                              \n")
print("\n                          11. CODE BLOCKS                           \n")
print("\n                          12. VIEW MATE                             \n")
print("\n                          13. WEB CAM                               \n")
print("\n                          14. KEILUV4                               \n")
print("\n                          15. NOTEPAD                               \n")
print()
while True:
	print("                              HOW CAN I HELP YOU?? :", end=""            )
	pyttsx3.speak(" how can i help you ")
	p=input()
	if(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("chrome" in p):
		pyttsx3.speak("\n launching chrome \n")
		os.system(" chrome ")
		print()
	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("explore" in p):
		pyttsx3.speak("\n launching internet explore \n")
		os.system(" iexplore ")
		print()
	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("itune" in p):
		pyttsx3.speak("\n launching itunes \n")
		os.system(" itunes ")
		print()
	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("vlc" in p):
		pyttsx3.speak("\n launching vlc player\n")
		os.system(" vlc ")
		print()
	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("window media player" in p):
		pyttsx3.speak("\n launching windows media player \n ")
		os.system(" wmplayer ")
		print()
	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("real player" in p):
		pyttsx3.speak("\n launching realplay \n")
		os.system(" realplay ")
		print()
	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("adobe" in p):
		pyttsx3.speak("\n launching adobe acrobat reader \n ")
		os.system(" acrord32 ")
		print()
	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and ("wordpad" in p):
		pyttsx3.speak("\n launching wordpad \n ")
		os.system(" wordpad ")
		print()

	
	







