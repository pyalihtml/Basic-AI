import os
import random
import sys
import subprocess as sb
import webbrowser
import datetime
from time import sleep


if os.name != 'nt':
    print("Kusura bakmayın! Bu programı yalnızca \n Windows'ta kullanabilirsiniz!")
    sys.exit(0)
    raise SystemExit
    os._exit(0)
    exit()
    quit()

else:
    print("________________________________")
    print('Hoşgeldin Windows kullanıcısı!')

    

# Burada, kullandığımız modüllerimizi import ettik.
Tr = "Turkish"
En = "English"
s = "skip"

print("________________________________________________________________________________")
print("You can skip typing skip if you want, but the language will remain English.")
print("________________________________________________________________________________")
text1=input("Select language : ")
print("")

if text1 == Tr:
    print("____________________________________________")
    print("Konuşmalar hazırlanıyor...", end = "", flush = True)
    sleep(2)
    print("\r                                      ", end = "")
    print("")
    print("____________________________________________")
    print("Merhaba, Ben senin özel asistanın Aliarc")
    print("____________________________________________")
    print("Bana istediğin bir web siteyi açtırabilirsin!\nŞuanlık sadece belirli web siteleri var.\nToplamda 13 site bulunmaktadır.\n+ 1 Tane de etkinlik bulunmaktadır.")
    print("____________________________________________")
    sleep(2)
    print("")
    print("____________________________________________")
    print("Sistem Yükleniyor...", end = "", flush = True)
    sleep(2)
    print("\r                                      ", end = "")
    print("")


elif text1 == En:
    print("____________________________________________")
    print("Speeches are being prepared...", end = "", flush = True)
    sleep(2)
    print("\r                                      ", end = "")
    print("")
    print("____________________________________________")
    print("Hello, I'm your personal assistant Aliarc")
    print("____________________________________________")
    print("You can make me open any website you want!\nThere are only certain websites for now.\nThere are 13 sites in total.\n+1 There are also events.")
    sleep(2)
    print("")
    print("System Loading...", end = "", flush = True)
    sleep(2)
    print("\r                                      ", end = "")
    print("")

elif text1 == s :
    print("_________________")
    print("ok")
    print("_________________")
    

        

else:
    print("_________________________________________________________________________________")
    print("Maalesef ki Aliarc hakkında bilgi alamayacaksınız.")
    print("_________________________________________________________________________________")
    print("Unfortunately, you will not be able to receive information about Aliarc.")

    #Burada da yapay zekamız Aliarc kendini tanıtıyor.

funny = "Say something funny"
a = "anything"
choice = "Open youtube" 
choice1 = "Open instagram"
choice2 = "Open tinkercad"
choice3 = "Open figma web"
choice4 = "Open youtube music"
choice5 = "Open spotify"
choice6 = "Open steam"
choice7 = "Open unity web"
choice8 = "How is the weather forecast"
choice9 = "Coronavirus chart"
choice10 = "Open translation"
choice11 = "Open google"
choice12 = "Open webtekno"
choice13 = "Open whatsapp web"
choice14 = "Open trendyol"
choice15 = "Open hepsiburada"
date = "What is today's date"
application = "Open notepad"
application1 = "Open paint"
application2 = "Open screenshot taker"
application3 = "My pc"
surprise = "Surprise me"


# Kullanıcının Aliarc'tan açmasını isteyebileceği bazı siteler ve uygulamalar.
sleep(2)
print("____________________________________________")
text1=input("Write your request : ")
print("____________________________________________")

# Kullanıcının isteği sorulur ve yazması için input yazılır.

if text1 == choice:
    webbrowser.open("https://www.youtube.com")
    print("Opening...") # Mendebur lemur'un videosu *denemek için*

elif text1 == choice1:
    webbrowser.open("https://www.instagram.com/?hl=tr")
    print("Opening...")

elif text1 == choice2:
    webbrowser.open("https://www.tinkercad.com/dashboard")
    print("Opening...")

elif text1 == choice3:
    webbrowser.open("https://www.figma.com/")
    print("Opening...")

elif text1 == choice4:
    webbrowser.open("https://music.youtube.com/")
    print("Opening...")

elif text1 == choice5:
    webbrowser.open("https://open.spotify.com/")
    print("Opening...")

elif text1 == choice6:
    webbrowser.open("https://store.steampowered.com/?l=turkish")
    print("Opening...")

elif text1 == choice7:
    webbrowser.open("https://unity.com/")
    print("Opening...")

elif text1 == choice8:
    webbrowser.open("https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=%C4%B0stanbul")
    print("Opening...")

elif text1 == choice9:
    webbrowser.open("https://www.google.com/search?q=korona&oq=korona&aqs=chrome..69i57j0i512j0i10i433j0i512l4j0i10i131i433j0i512j0i10i433.1982j0j7&sourceid=chrome&ie=UTF-8#wptab=s:H4sIAAAAAAAAAONgVuLVT9c3NMwySk6OL8zJecRowS3w8sc9YSn9SWtOXmPU5OIKzsgvd80rySypFJLmYoOyBKX4uVB18uxi4vZITcwpyQguSSwpXsQqlZ1flJ-XWJZZdHhPsUJmMVAUSGRm56QWAQCgE2OkdwAAAA&colocmid=/m/02j71&coasync=0")
    print("Opening...")

elif text1 == choice10:
    webbrowser.open("https://www.google.com/search?q=%C3%A7eviri&oq=%C3%A7eviri&aqs=chrome.0.69i59j0i512j0i10i131i433j0i512l3j69i61l2.1437j0j7&sourceid=chrome&ie=UTF-8")
    print("Opening...")

elif text1 == funny:
    print("Haha I'm sure you'll laugh at these")
    print("____________________________________________")
    sleep(2)
    print("____________________________________________")
    print("*knock knock*\n-Who's there\n+hawai\n-hawai who?\n-I'm good how are you :D")
    sleep(2)
    print("")
    print("Ketchup and mayonnaise are racing one day\nand ketchup is losing.What does mayonnaise say?\n+You can't *catch up*")
    print("____________________________________________")


elif text1 == choice11:
        webbrowser.open("https://www.google.com/")
        print("Opening...")
    
elif text1 == choice12:
    webbrowser.open("https://www.webtekno.com/")
    print("Opening...")

elif text1 == a:
    webbrowser.open("https://osu-web.com/") or webbrowser.open ("https://www.youtube.com/channel/UCXin0u5SrVEBjn5LhOoG97A"), print("Opening...")

elif text1 == date:
    date = datetime.datetime.today()
    print("_______________________________________")
    print("Today's date : ", date)
    print("_______________________________________")

    
elif text1 == application:
    sb.call('notepad.exe')
    print("Opening...")

elif text1 == application1:
    sb.call('mspaint.exe')
    print("Opening...")

elif text1 == application2:
    sb.call('SnippingTool.exe')
    print("Opening...")

elif text1 == application3:
    import platform
    print("_______________________________________________________________")
    print("İşletim Sisteminiz:")
    # İşletim Sistemini Öğrenmek.
    print(platform.system())
    print("_______________________________________________________________")


    print("İşlemciniz:")
    # İşlemci Bilgisini Öğrenmek.
    print(platform.processor())
    print("_______________________________________________________________")


    print("Python Versiyonunuz:")
    # Python Versiyonunu Öğrenmek.
    print(platform.python_version())
    print("_______________________________________________________________")


    print("Bilgisayardaki Kullanıcı Adınız:")
    # Bilgisayarın Kullanıcı Adını Öğrenmek.
    print(platform.node())
    print("_______________________________________________________________")


    print("Python Compiler Bilgisi :")
    # Python Compiler Bilgisini Öğrenmek.
    print(platform.python_compiler())
    print("_______________________________________________________________")
    print("Python İmplementasyonu:")
    # Python İmplementasyonunu Öğrenmek.
    print(platform.python_implementation())
    print("_______________________________________________________________")


elif text1 == surprise:
    print ("                       Matrix                      ")
    print ("__________________________________________________________")
    sleep(5)
    a =1010110101011010001100101010101011110101010100101010101001010010010101010
    1010101010101010101010101010101010101010101001010101010010101000101011001101
    1010010110101010101010101010101010101010101010101100110101101010101010101010 
    b =1010110101011010001100101010101011110101010100101010101001010010010101010
    1010101010101010101010101011010101010101010101001011010010101010101010101010
    
    for i in range(10):
        print (a)
        sleep(0.5)
        print (b)

    print("You are now in the universe of the Matrix")
    sleep(5)

    

#Burada aslında Aliarc'ın kalbi diyebileceğimiz kodlarımız var. Bu kodlar hangi siteyi açmak isterseniz ona göre seçiliyor ve açılıyor.

else:
 print("Please give correct answer")

 #Kullanıcı random olarak yazarsa kafasının karışmaması için "Lütfen doğru cevap verin" demesini istiyorum.