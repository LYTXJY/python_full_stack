import win32com.client
speaker = win32com.client.Dispatch("SAPI.SPVOICE")
#dispatch:派遣，分配

i = 0
while i < 5:
    print(i)
    speaker.Speak("岂曰无衣，与子同袍。这是第" + str(i) + "次")
    i += 1