import pyttsx3 as pys
import os


print("Welcome!")
pys.speak("Welcome     I am very happy to help you")
print("-----------------------------------------------------------")
pys.speak("What you want me to do")


while True:


  app = input("What you want me to do : ")


  if ("open" in app) or ("start" in app) or ("execute" in app) or ("launch" in app) or ("run" in app) or ("use" in app) or ("play" in app):
  
    if ("chrome" in app) or ("browser" in app) or ("search engine" in app) or ("search" in app) or ("internet" in app) or ("net" in app) or ("google" in app):
      if ("firefox" in app) or ("fox" in app):
        pys.speak("Opening firefox for you")
        os.system("firefox")
      elif ("explorer" in app):
        pys.speak("Opening explorer for you")
        os.system("iexplore")
      elif ("yahoo" in app):
        pys.speak("Opening yahoo for you")
        os.system("yahoo")
      elif ("bing" in app):
        pys.speak("Opening bing for you")
        os.system("bing") 
      else:
        pys.speak("Opening chrome for you")
        os.system("chrome")
    elif ("adobe" in app):
      if ("cloud" in app) or ("creative" in app):
        pys.speak("Opening adobe creative cloud for you")
        os.system("creative cloud")
      elif ("camera" in app) or ("lens" in app):
        pys.speak("Opening adobe lens for you")
        os.system("adobelens")
      else:
        pys.speak("Opening adobe reader for you")
        os.system("reader")
    elif ("anaconda" in app) or ("anaconda3" in app) or ("conda" in app):
      pys.speak("Opening anaconda navigator for you")
      os.system("conda")
    elif ("notepad" in app) or ("notpad" in app) or ("note" in app):
      pys.speak("Opening notepad for you")
      os.system("notepad")
    elif ("whatsapp" in app) or ("watsap" in app) or ("whatsap" in app):
      pys.speak("Opening whatsapp for you")
      os.system("whatsapp")
    elif ("c" in app) or ("turbo" in app) or ("turboc++" in app):
      pys.speak("Opening turbo C++ for you")
      os.system("tc_dos") 
    elif ("telegram" in app):
      pys.speak("Opening telegram for you")
      os.system("telegram")
    elif ("microsoft" in app) or ("ms" in app) or ("word" in app) or ("powerpoint" in app) or ("office" in app) or ("msoffice" in app):
      if ("word" in app):
        pys.speak("Opening microsoft word for you")
        os.system("winword")
      elif ("powerpoint" in app) or ("microsoft powerpoint" in app) or ("ppt" in app) or ("presentation" in app):
        pys.speak("Opening microsoft powerpoint for you")
        os.system("powerpnt")
      elif ("excel" in app) or ("sheet" in app) or ("spreadsheet" in app) or ("graph" in app):
        pys.speak("Opening microsoft excel for you")
        os.system("xlicons")
      elif ("publish" in app) or ("publisher" in app):
        pys.speak("Opening microsoft publisher for you")
        os.system("mspub")
      elif ("access" in app) or ("msaccess" in app):
        pys.speak("Opening microsoft access for you")
        os.system("msaccess")
    elif ("file manager" in app) or ("files" in app) or ("file" in app):
      pys.speak("Opening file manger for you")
      os.system("manager")
    elif ("message" in app) or ("sms" in app):
      pys.speak("Opening messages for you")
      os.system("sms")
    elif ("outlook" in app) or ("microsoft" in app):
      pys.speak("Opening microsoft outlook for you")
      os.system("outlook")
    elif ("conference" in app) or ("meeting" in app) or ("meet" in app) or ("schedule" in app) or ("zoom" in app) or ("skype" in app) or ("team" in app) or ("class" in app):
      if ("zoom" in app):
        pys.speak("Opening zoom for you")
        os.system("zoom")
      elif ("meet" in app):
        pys.speak("Opening google meet for you")
        os.system("meet")
      elif ("skype" in app):
        pys.speak("Opening skype for you")
        os.system("skype")
      elif ("go to meeting" in app):
        pys.speak("Opening go to meeting for you")
        os.system("gotomeeting")
      elif ("teams" in app) or ("microsoft team" in app):
        pys.speak("Opening microsoft teams for you")
        os.system("teams")
      else:
        pys.speak("Sorry this app is not in my database")
        pys.speak("Sorry for in convinience!")
    elif ("media" in app) or ("player" in app) or ("music" in app) or ("video" in app) or ("videos" in app) or ("songs" in app) or ("song" in app):
      if ("window" in app) or ("wmplayer" in app):
        pys.speak("Opening window media player for you")
        os.system("wmplayer")
      elif ("vlc" in app):
        pys.speak("Opening vlc media player for you")
        os.system("vlcplayer")
      elif ("savvan" in app) or ("savan" in app):
        pys.speak("Opening savvn for you")
        os.system("savvan")
      elif ("wynk" in app) or ("vink" in app):
        pys.speak("Opening wynk for you")
        os.system("wynk")
      else: 
         pys.speak("Please specify from which app you want to play")
         print("Please specify from which app you want to play")
    elif ("facebook" in app) or ("fb" in app):
      pys.speak("Opening facebook for you")
      os.system("facebook")
    elif ("instagram" in app) or ("insta" in app):
      pys.speak("Opening instagram for you")
      os.system("instagram")
  elif ("exit" in app) or ("close" in app) or ("shut" in app) or ("bye" in app) or ("down" in app):
    print("Thank You!") 
    pys.speak("Thank You I am very glad after helping you") 
    break
  else:
    pys.speak("The app you have selected is not in my database")
    pys.speak("Sorry for inconvinience")
