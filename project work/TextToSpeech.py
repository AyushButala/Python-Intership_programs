from gtts import gTTS

message = input("Enter Message : ")

data = gTTS(message,lang="en")
data.save('textAudio.mp3')