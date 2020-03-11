import win32com.client
#系统客户端包

speaker = win32com.client.Dispatch("SAPI.SPVOICE")#系统接口
speaker.Speak('''
君住长江头
我住长江尾
夜夜思君不见君
共饮长江水

''')

speaker.Speak("Wakanda forever")