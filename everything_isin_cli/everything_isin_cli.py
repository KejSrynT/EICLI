import os 
import time
#import speedtest
import calendar
from datetime import datetime
import shutil



os.system('cls')

def hava_durumu() :
    while True :
        try :
            os.system('cls')
            print("\033[31mWarning! Write Province or Region names consisting of two or more words in a compound.\033[0m")
            a = input("Which Province or Region Do You Live in ? : ")     
            print("Receiving Weather Information...")
            time.sleep(2)
            os.system('cls')
            os.system(f'curl wttr.in/{a}')
            
            tekrar_sec = input("\033[33m \n\nDo you want to view the weather forecast for another Province or Region again? [y/n] : \033[0m")
            
            if tekrar_sec == "E" or tekrar_sec == "y" :
                os.system('cls')
                print("outer space is being cleared...")
                time.sleep(1)
                continue
            
            elif tekrar_sec == "n" or tekrar_sec == "N" :
                os.system('cls')
                print("Returning home...")
                print("""\n
 |\/\/\/|  
 |      |  
 |      |  
 | (o)(o)  
 C      _) 
  | ,___|  
  |   /    
 /____\    
/      \
""")
                time.sleep(1.5)
                os.system('cls')
                break
            else :
                input("Please enter a valid value!\nPress any key to continue...")
                continue
                

        except :
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue
        

def check_up() :
    while True :
        try :
            os.system('cls')
            print("Checking all upgrades...")
            time.sleep(1.5)
            os.system('cls')
            print("All upgrades are checked.\n\n")
            os.system('winget upgrade')
            print("\033[33m\n\nIf you received a winget error, see this article. (https://phoenixnap.com/kb/install-winget)\033[0m")
            tri_c = input("\033[36m\n[a] : Update all \033[0m \033[32m\n[d] : Update according to ID \033[0m \033[35m\n[e] : Exit without update\033[0m\n------------------------------> Selection : ")

            if tri_c == "a" :
                os.system('cls')
                print("All available updates are being upgraded...\n")
                os.system('winget upgrade --all')
                print("All available updates have been upgraded.\n")
                input("\nPress Enter to continue...")
                os.system('cls')
                continue

            elif tri_c == "d" :
                os.system('cls')
                print("Checking all upgrades...")
                time.sleep(1.5)
                print("All upgrades are checked.\n")
                os.system('winget upgrade')
                print("\n\033[31mWarning! If the wrong id is entered, the version will not be updated.\033[0m")
                idd = input("\n\nEnter the ID of the version you want to update (only 1 ID is valid) : ")

                print("\nChecking ID...")
                time.sleep(1)
                print("Updating ID...\n")
                os.system(f'winget upgrade {idd}')
                
                input("\n\nPress Enter to continue...")
                continue

            elif tri_c == "e" :
                os.system('cls')
                print("\033[34mReturning home...\033[0m")
                print("""\n\n\033[36m
                      
                               ____       ____
  /  _/__    / __/__  ___ ________   ___  ___    ___  ___  ___
 _/ // _ \  _\ \/ _ \/ _ `/ __/ -_) / _ \/ _ \  / _ \/ _ \/ -_)
/___/_//_/ /___/ .__/\_,_/\__/\__/ /_//_/\___/  \___/_//_/\__/
 _______ ____ /_// /  ___ ___ _____  __ _____  __ __
/ __/ _ `/ _ \  / _ \/ -_) _ `/ __/ / // / _ \/ // /
\__/\_,_/_//_/ /_//_/\__/\_,_/_/    \_, /\___/\_,_/
  ______ ___ _____ ___ ______      /___/
 (_-< _ `/ // / -_) -_)_ / -_)   ....
/___|_, /\_,_/\__/\__//__|__/    /   `.
     /_/                        |      `,
                                 -.   ,'
                                   `-/ \
                                  ,'    ;
                                ,'     /      ____
                        ______,i     __-  ,'''__  `._
                       /        `-,-'  `-+ /''XX`-.. `.
                      /    ,'-._    ``-.i,'XXXXXXXX`.  :
                     /  .--  ._ `-,_     \XXXXXXXXXX/ |
                     |   `.  `.  /XX`..   \XXXXXXXX| .'
                   ,'|  .i> `. .'XXXXXX/-. -._XXX_/ ,'
                 ,'  ',.:>_.'','XXXXXX/  ,`-. `. _,'\  _
               ,'    /   _ `./XXXXXX,'  / /  `. '.  ,+' `.
             ,'     /   -_` /XXXXXX/  ,',',- , `.<-'    ,'
           ,'      /   :- ;'XXXXXX/  /,',' ,',  ,-.   ,'
         ,'       :  ._ `,'XXXXXX/ ,'/,'_,',',-'XX,-,'
       ,'        _ `-.  /XXXXXXX/ /,;',',-','XXX,:`
      `    _,'-,- `-..i`.XXXXX,' /`/,',',-'XX_X'  `,
       `.,'   ,'      \  `=.X,',' ;',','XX,,'\\  ,:
            ,'`.       |,;' `-.  - i,'XXX,'    -' |
          ,'    `    ,' .i     `-,'XXXX,'`.    ,-'
         /         ,' ,'  `-..    ;-,,;'   `,,'
       ,'    `.  ,' ,-        \ ,'  ,:    ,'
      |        ,' ,'       .  ,'  ,'  `-<'
    ,-._     ,' ,'     -.  ,-'  ,'
  ,'       ,'_,'   _    ,`'    |
 \       ,','       `,-:    _,/
 \     ,' '       ,-'   --''
  '`-<' ,'   \ ,-'
        |    ,'
        \  _'
         '-
\033[0m""")
                time.sleep(3)
                os.system('cls')
                break

            else :
                os.system('cls')
                input("\033[31mPlease enter a valid value!\033[0m\n\nPress any key to continue...")
                continue





        except :
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue

def speedtest() :
    import speedtest
    os.system('cls')
    print("\033[32mActivating speedtest...\033[0m")
    st = speedtest.Speedtest()

    print("Servers are listed and the best server is selected...")
    st.get_best_server()

    print("\033[31m>>> Testing download speed...\033[0m")
    download_s = st.download() / 1_000_000

    print("\033[33m>>> Testing upload speed...\033[0m")
    upload_s = st.upload() / 1_000_000

    print("\033[32m>>> Testing ping...\033[0m")
    ping_s = st.results.ping
    time.sleep(2)

    os.system('cls')
    print("\033[36mSpeedtest completed. Results;\n\033[0m")

    print(f"Download speed : {download_s:.2f} Mbps")
    print(f"Upload speed : {upload_s:.2f} Mbps")
    print(f"Ping : {ping_s:.2f} ms")

    input("\n\nPress any key to continue...")
    os.system('cls')
    print("\033[34mReturning home...\033[0m")
    print("""\n\n\n\033[35m
 _   _                 _                       _                       
| \ | | _____   ____ _| |   _   _  ___ _   _  (_)___   _ __ ___  _   _ 
|  \| |/ _ \ \ / / _` | |  | | | |/ __| | | | | / __| | '_ ` _ \| | | |
| |\  | (_) \ V / (_| | |__| |_| | (__| |_| | | \__ \ | | | | | | |_| |
|_| \_|\___/ \_/ \__,_|_____\__,_|\___|\__, | |_|___/ |_| |_| |_|\__, |
                           _   _     _ |___/                     |___/ 
  _____   _____ _ __ _   _| |_| |__ (_)_ __   __ _                                              
 / _ \ \ / / _ \ '__| | | | __| '_ \| | '_ \ / _` |                    
|  __/\ V /  __/ |  | |_| | |_| | | | | | | | (_| |_ _ _               
 \___| \_/ \___|_|   \__, |\__|_| |_|_|_| |_|\__, (_|_|_)                  
                     |___/                   |___/                      
\033[31m
,d88b.d88b,
88888888888
`Y8888888Y'
  `Y888Y'    -I love u-
    `Y'               \033[0m     
\033[0m""")
    
    time.sleep(2)
    os.system('cls')


def ip_co() :
    import time
    while True :
          try :
            os.system('cls')
            ip_sec = int(input("\033[36m[1] : Show ipconfig info \033[0m \033[32m\n[2] : Show all ipconfig info \033[0m\n\033[35m[3] : Show public ip !(Don't share with others.)! \033[0m\n\033[31m[4] : Exit \033[0m\n------------------------------> Selection : "))
            if ip_sec < 1 or ip_sec > 4 :
                os.system('cls')
                raise Exception("The number you enter must be between 1 and 4 !!!")
                
            elif ip_sec == 1 :
              os.system('cls')
              print("Showing ipconfig info...")
              time.sleep(1.5)
              os.system('cls')
              os.system('ipconfig')
              input("\n\033[32mPress any key to continue...\033[0m")
              os.system('cls')
              continue
          
            elif ip_sec == 2 :
              os.system('cls')
              print("Showing all ipconfig info...")
              time.sleep(1.5)
              os.system('cls')
              os.system('ipconfig/all')
              input("\n\033[32mPress any key to continue...\033[0m")
              os.system('cls')
              continue
          
            elif ip_sec == 3 :
              os.system('cls')
              print("Showing public ip \033[31m!(Don't share with others.)!..\033[0m")
              time.sleep(1.5)
              print("Here is your public ip adress ; \n")
              os.system('curl ifconfig.me')
              input("\n\n\033[32mPress any key to continue...\033[0m")
              os.system('cls')
              continue
            
            elif ip_sec == 4 :
              os.system('cls')
              print("\033[34mReturning home...\033[0m")
              print("""\n
    ____
   (__  '.
    /_____)
   ()- - )))
    'C ,()(()
    ,.'_'.' \
 __/ )   (--'
'._./     \
   (_._._._)
    _|| ||_
   (__,),__)

""")
            time.sleep(2)
            os.system('cls')
            break
          
          except Exception as hata :
              os.system('cls')
              print("An error has occurred! --> ",hata)
              time.sleep(3)
          
          except :
              print("An error has occurred! Please try again.")
              time.sleep(1.5)
              continue
              
            
        
def ping_to() :
    while True :
        try :
                os.system('cls')
                print("Collecting packages...")
                time.sleep(1.5)
                os.system('cls')
                to_w = int(input("\033[33m[1] : Ping with IP address \033[0m\n\033[36m[2] : Ping with domain\033[0m\n\033[31m[3] : Exit \033[0m\n------------------------------> Selection : "))

                if to_w < 1 or to_w > 3 :
                    raise Exception("The number you enter must be between 1 and 3 !!!")
                
                elif to_w == 1 :
                  os.system('cls')
                  get_ip = input("Please enter a valid IP address : ")
                  octets = get_ip.split(".")
                  ip_int = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])
                  os.system(f'ping {ip_int}')
                  input("\n\n\033[32mPress any key to continue...\033[0m")
                  os.system('cls')
                  continue

                elif to_w == 2 :
                    os.system('cls')
                    get_dom = input("Please enter a valid Domain name : ")
                    print("\n")
                    os.system(f'ping {get_dom}')
                    input("\n\n\033[32mPress any key to continue...\033[0m")
                    os.system('cls')
                    continue
                
                elif to_w == 3 :
                    os.system('cls')
                    print("\033[34mReturning home...\033[0m")
                    print("""\n\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⣋⣉⡙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠮⡞⠁⠀⠈⢢⠷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢠⢤⣇⠀⡇⠀⠀⠀⢸⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⡏⢰⠙⠚⢧⣀⢀⣠⠞⠓⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  OOOO YEAAAHHH 
⠀⠀⠀⠀⠀⠀⠀⡸⠀⡎⠀⣀⡤⠏⠉⠧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢠⠃⢰⡵⠊⠁⠀⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢸⡀⠀⣀⡠⡆⠀⠀⠀⠀⠀⣆⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⡇⠀⠀⠀⠀⠀⡏⢣⡀⠘⣄⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢸⠀⠙⢤⡈⢦⡀⠀⠀⠀⠀⠀⠀ 
⠀⠀⢠⠖⣒⣶⠖⠒⠒⠒⠲⠷⣒⠒⠒⠒⠒⣺⣶⠖⠒⠓⢤⣹⠶⣒⠲⡄⠀⠀ 
⠀⢠⠏⣞⣟⠉⠀⣖⠒⣲⠀⠀⠈⣳⠀⠀⡎⡞⠉⠀⣖⢒⣢⠀⠀⠈⡇⠹⡄⠀ 
⢠⠏⠀⠘⠪⢅⣀⣀⠉⣀⣀⡠⠔⠁⠀⠀⠙⠮⣇⣀⣀⠉⣀⣀⡤⠖⠁⠀⠹⡄ 
⡟⠒⠒⠒⠒⠒⠒⠓⠛⠚⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠚⠛⠛⠒⠒⠒⠒⠒⠒⢻ 
⣇⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣸


""")

                    time.sleep((2))
                    os.system('cls')
                    break
                else :
                    print("An error has occurred! Please try again.")
                    time.sleep(1.5)
                    continue
                

        except Exception as hata3 :
            os.system('cls')
            print("An error has occurred! --> ",hata3)
            time.sleep(1.5)
            continue
        except :
            pass
    

def trace_to() :
    while True :
        try :
                os.system('cls')
                print("Collecting packages...")
                time.sleep(1.5)
                os.system('cls')
                to_w = int(input("\033[33m[1] : Trace with IP address \033[0m\n\033[36m[2] : Trace with domain\033[0m\n\033[31m[3] : Exit \033[0m\n------------------------------> Selection : "))

                if to_w < 1 or to_w > 3 :
                    raise Exception("The number you enter must be between 1 and 3 !!!")
                
                elif to_w == 1 :
                  os.system('cls')
                  get_ip = input("Please enter a valid IP address : ")
                  octets = get_ip.split(".")
                  ip_int = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])
                  os.system(f'tracert {ip_int}')
                  input("\n\n\033[32mPress any key to continue...\033[0m")
                  os.system('cls')
                  continue

                elif to_w == 2 :
                    os.system('cls')
                    get_dom = input("Please enter a valid Domain name : ")
                    print("\n")
                    os.system(f'tracert {get_dom}')
                    input("\n\n\033[32mPress any key to continue...\033[0m")
                    os.system('cls')
                    continue
                
                elif to_w == 3 :
                    os.system('cls')
                    print("\033[34mReturning home...\033[0m")
                    print("""
              .:.               
             .::::.             
..         ..::::::''::         
::::..  .::''''':::    ''.      
':::::::'         '.  ..  '.    
 ::::::'            : '::   :   
  :::::     .        : ':'   :  
  :::::    :::       :.     .'. 
 .::::::    ':'     .' '.:::: : 
 ::::::::.         .    ::::: : 
:::::    '':.... ''      '''' : 
':::: .:'              ...'' :  
 ..::.   '.........:::::'   :   
  '':::.   '::'':'':::'   .'    
        '..  ''.....'  ..'      
           ''........''
""")

                    time.sleep((2))
                    os.system('cls')
                    break
                else :
                    print("An error has occurred! Please try again.")
                    time.sleep(1.5)
                    continue
                

        except Exception as hata3 :
            os.system('cls')
            print("An error has occurred! --> ",hata3)
            time.sleep(1.5)
            continue
        except :
            pass

def nslook() :
    while True :
        try :
            os.system('cls')
            print("Connecting to DNS servers...")
            time.sleep(1.5)
            os.system('cls')
            nsch = int(input("\033[32m[1] : Nslookup with domain\033[0m\n\033[31m[2] : Exit \033[0m\n------------------------------> Selection : "))
            os.system('cls')
            if nsch < 1 or nsch > 2 :
                raise Exception("The number you enter must be between 1 and 2 !!!")
            
            elif nsch =="" or nsch ==" " :
                continue
            elif nsch == 1 :
                nsdo = input("Please input a valid domain name : ") #!
                
                if nsdo == "" or nsdo == " " :
                    continue
                elif nsdo.isdigit() :
                  raise ValueError("The data entered is an integer! - Please enter a valid domain name.")
            
            
                os.system(f'nslookup {nsdo}')
                input("\n\n\033[32mPress any key to continue...\033[0m")
                os.system('cls')
                continue

            elif nsch == 2 :
              os.system('cls')
              print("\033[34mReturning home...\033[0m")
              print("""\n\n
           .-"-.                          .-"-.
          "     "--.                 (((("     "
           ".. ( ()()_O            O_()() ) .."
        .-"-./( \_____)            (_____/ )\.-"-.
       "     \_______/              \_______/     "
        "..."___|__\____           ___/  |__ "..."
           /\__||__||__/\         /\_ \__/ _/\
           \\ /_    _\ //         \\/      \//
          _/_)(_)  (_)(_\_       _/_)//////(_\_
              \__/\__/           (_(_(_()_)_)_)
               //  \\               (__)(__)
            .-.\\  //.-.          .-.||  ||.-.
           (_____)(_____)        (____)  (____)

""")          
              time.sleep(2)
              os.system('cls')
              break

        except Exception as hata6 :
            os.system('cls')
            print("An error has occurred! --> ",hata6)
            time.sleep(1.5)
            continue

            
        except ValueError as hata5 :
            os.system('cls')
            print("An error has occurred! --> ",hata5)
            time.sleep(2)
            continue
            
        except:
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue


def sys_info() :
    while True :
        try :
            os.system('cls')
            print("Getting system information...")
            time.sleep(0.5)
            os.system('cls')
            sys_cho = int(input("\033[32m[1] : Get system info from CLI \033[0m\n\033[33m[2] : Get System info from DXDIAG \033[33m\n\033[31m[3] : Exit \033[0m\n------------------------------> Selection : "))
            if sys_cho < 1 or sys_cho > 3  :
                raise Exception("The number you enter must be between 1 and 3 !!!")


            elif sys_cho == 1 :
                os.system('cls')
                os.system('systeminfo')
                input("\n\n\033[32mPress any key to continue...\033[0m")
                continue

            elif sys_cho == 2 :
                os.system('cls')
                print("Opening DXDIAG...")
                time.sleep(0.5)
                os.system('dxdiag')
                input("\n\n\033[32mPress any key to continue...\033[0m")
                continue

            elif sys_cho == 3 :
                os.system('cls')
                print("\033[34mReturning home...\033[0m")
                print("""\n\n
                   __
                  / _)
         _.----._/ /
        /         /      >>> Where am I..
     __/ (  | (  |
    /__.-'|_|--|_|
""")
                time.sleep(2)
                os.system('cls')
                break
                



        except Exception as hata7 :
            os.system('cls')
            print("An error has occurred! --> ",hata7)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue


def calender() :
    import calendar
    from datetime import datetime
    while True :
        try :
            os.system('cls')
            print("Getting calendar information...")
            time.sleep(0.5)
            os.system('cls')
            clan_ch = int(input("\033[32m[1] : Yearly calendar \033[0m\n\033[33m[2] : According to the month \033[0m\n\033[31m[3] : Exit \033[0m\n------------------------------> Selection : "))
            if clan_ch < 1 or clan_ch > 3  :
                raise Exception("The number you enter must be between 1 and 3 !!!")
            
            elif clan_ch == 1 :
                os.system('cls')
                now = datetime.now()
                yil = now.year
                print("Getting date information...")
                time.sleep(0.5)
                os.system('cls')
                print(calendar.calendar(yil))
                input("\n\n\033[32mPress any key to continue...\033[0m")
                continue

            elif clan_ch == 2 :
                os.system('cls')
                print("Getting date information...")
                time.sleep(0.5)
                os.system('cls')
                now = datetime.now()
                yilal2 = now.year
                ayal = int(input("Please select a month, [1-12] : "))
                if ayal < 1 or ayal > 12 :
                    raise Exception("The number you enter must be between 1 and 12 !!!")
                print(calendar.month(yilal2, ayal))
                input("\n\n\033[32mPress any key to continue...\033[0m")
                continue
                

            elif clan_ch == 3 :
                os.system('cls')
                print("\033[34mReturning home...\033[0m")
                print("""
 /\_/\                              
( o.o )    *What happened??                                 
 > ^ <                          
""")
                time.sleep(1.5)
                os.system('cls')
                break


        except Exception as hata8 :
            os.system('cls')
            print("An error has occurred! --> ",hata8)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue



def neth_show() :
    while True :
        try :
            os.system('cls')
            print("Getting Wlan's information...")
            time.sleep(0.5)
            os.system('cls')
            neth_cho = int(input("\033[32m[1] : List all wlans \033[0m\n\033[33m[2] : List all properties of only 1 wlan (includes the password!) \033[0m\n\033[31m[3] : Exit \033[0m\n------------------------------> Selection : "))
            if neth_cho < 1 or neth_cho > 3  :
                raise Exception("The number you enter must be between 1 and 3 !!!")
            
            elif neth_cho == 1 :
                os.system('cls')
                print("Listing all wlans...")
                time.sleep(0.5)
                os.system('cls')
                os.system('netsh wlan show profiles')
                input("\n\n\033[32mPress any key to continue...\033[0m")
                continue

            elif neth_cho == 2 :
                os.system('cls')
                print("\033[33mListed all wlans.\033[0m\n")
                os.system('netsh wlan show profiles')
                
                neth_inf = input("\n\n\033[33mPlease enter the name of one of the wlans that appear in the list : \033[0m")
                    
                
                    
                os.system('cls')
                print(f"Showing '{neth_inf}' informations...")
                time.sleep(0.5)
                os.system('cls')
                os.system(f'netsh wlan show profile {neth_inf}')
                input("\n\n\033[32mPress any key to continue...\033[0m")
                continue

            elif neth_cho == 3 : 
                os.system('cls')
                print("\033[34mReturning home...\033[0m")
                print("""\n\n
  , _,
 (o,o)      HooOOoo... HOO... HooOOoo...
 { " }
  -"-"-
""")
                time.sleep(1.5)
                os.system('cls')
                break



        except Exception as hata8 :
            os.system('cls')
            print("An error has occurred! --> ",hata8)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue


def taskmg() :
    while True :
        try :
            os.system('cls')
            print("Connecting to the Task Manager...")
            time.sleep(0.5)
            os.system('cls')
            os.system('taskmgr.exe')
            input("\n\n\033[32mPress any key to continue...\033[0m")
            os.system('cls')
            break

        except Exception as hata8 :
            os.system('cls')
            print("An error has occurred! --> ",hata8)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue




def discer() :
    while True :
        try :
            os.system('cls')
            print("Connecting to the Disc Cleaner...")
            time.sleep(0.5)
            os.system('cls')
            os.system('cleanmgr.exe')
            input("\n\n\033[32mPress any key to continue...\033[0m")
            os.system('cls')
            break

        except Exception as hata8 :
            os.system('cls')
            print("An error has occurred! --> ",hata8)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue
        


def devman() : 
    while True :
        try :
            os.system('cls')
            print("Connecting to the Device Manager...")
            time.sleep(0.5)
            os.system('cls')
            os.system('devmgmt.msc')
            input("\n\n\033[32mPress any key to continue...\033[0m")
            os.system('cls')
            break

        except Exception as hata8 :
            os.system('cls')
            print("An error has occurred! --> ",hata8)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue


def aorp() :
    while True :
        try :
            os.system('cls')
            print("Connecting to the Add or Remove Programmes...")
            time.sleep(0.5)
            os.system('cls')
            os.system('appwiz.cpl')
            input("\n\n\033[32mPress any key to continue...\033[0m")
            os.system('cls')
            break

        except Exception as hata8 :
            os.system('cls')
            print("An error has occurred! --> ",hata8)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue



def paint() :
    while True :
        try :
            os.system('cls')
            print("Connecting to the Paint...")
            time.sleep(0.5)
            os.system('cls')
            os.system('mspaint.exe')
            input("\n\n\033[32mPress any key to continue...\033[0m")
            os.system('cls')
            break

        except Exception as hata8 :
            os.system('cls')
            print("An error has occurred! --> ",hata8)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue



def note() :
    while True :
        try :
            os.system('cls')
            print("Connecting to the NotePad...")
            time.sleep(0.5)
            os.system('cls')
            os.system('notepad.exe')
            input("\n\n\033[32mPress any key to continue...\033[0m")
            os.system('cls')
            break

        except Exception as hata8 :
            os.system('cls')
            print("An error has occurred! --> ",hata8)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue


def calc() :
    while True :
        try :
            os.system('cls')
            print("Connecting to the Calculator...")
            time.sleep(0.5)
            os.system('cls')
            os.system('calc.exe')
            input("\n\n\033[32mPress any key to continue...\033[0m")
            os.system('cls')
            break

        except Exception as hata8 :
            os.system('cls')
            print("An error has occurred! --> ",hata8)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue



def sckey():
    while True :
        try :
            os.system('cls')
            print("Connecting to the Screen Keyboard...")
            time.sleep(0.5)
            os.system('cls')
            os.system('osk.exe')
            input("\n\n\033[32mPress any key to continue...\033[0m")
            os.system('cls')
            break

        except Exception as hata8 :
            os.system('cls')
            print("An error has occurred! --> ",hata8)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue


def reip() :
    while True :
        try :
            os.system('cls')
            print("\033[33mReleasing the ip address...\033[0m")
            time.sleep(0.5)
            os.system('ipconfig /release')
            time.sleep(1)
            os.system('cls')
            print("\033[33mGetting new ip address...\033[0m")
            os.system('ipconfig /renew')
            time.sleep(1)
            input("\n\n\033[32mPress any key to continue...\033[0m")
            os.system('cls')
            break

        except Exception as hata8 :
            os.system('cls')
            print("An error has occurred! --> ",hata8)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue



def clgame() :
    while True :
        try :
            os.system('cls')
            print("Connecting to the Game...")
            time.sleep(0.5)
            os.system('cls')
            os.system('ssh sshtron.zachlatta.com')
            input("\n\n\033[32mPress any key to continue...\033[0m")
            os.system('cls')
            break

        except Exception as hata8 :
            os.system('cls')
            print("An error has occurred! --> ",hata8)
            time.sleep(1.5)
            continue
        except :
            os.system('cls')
            print("An error has occurred! Please try again.")
            time.sleep(1.5)
            continue


def exit() :
    print("exiting...")
    time.sleep(0.2)
    os.system('exit')
    



while True:
    try :
        tercih = int(input("""\033[35m 
                            _   _     _               _       _          ____ _     ___ 
  _____   _____ _ __ _   _| |_| |__ (_)_ __   __ _  (_)___  (_)_ __    / ___| |   |_ _|
 / _ \ \ / / _ \ '__| | | | __| '_ \| | '_ \ / _` | | / __| | | '_ \  | |   | |    | | 
|  __/\ V /  __/ |  | |_| | |_| | | | | | | | (_| | | \__ \ | | | | | | |___| |___ | | 
 \___| \_/ \___|_|   \__, |\__|_|_|_|_|_|_|_|\__, | |_|___/ |_|_|_|_|  \____|_____|___|
              | |__  |___/  | |/ /___ (_) ___|___/_ _   _ _ _|_   _|                   
              | '_ \| | | | | ' // _ \| \___ \| '__| | | | '_ \| |                     
              | |_) | |_| | | . \  __/| |___) | |  | |_| | | | | |                     
              |_.__/ \__, | |_|\_\___|/ |____/|_|   \__, |_| |_|_|                     
                     |___/          |__/            |___/          \033[0m


        [1] : Weather Forecast                             [11] : Task Manager
        [2] : Check Upgrades                               [12] : Disc Cleaner
        [3] : SpeedTest                                    [13] : Device Manager
        [4] : IP information                               [14] : Add or Remove Programmes
        [5] : Ping to {IP Address or domain}               [15] : Paint
        [6] : Tracert to {Ip Address or domain}            [16] : Notepad
        [7] : Nslookup to {Domain name}                    [17] : Calculator
        [8] : Get system information                       [18] : Screen Keyboard
        [9] : Calender                                     [19] : Renew Ip Address(!)
        [10] : Show Wlan informations                      [20] : Little Game :-)
                           
                                        [0] : Exit                    
                                
                                Please select a task : """))
        if tercih < 0 or tercih > 20 :
            raise Exception("Please only enter numbers between 1-10")
          
        elif tercih == 1 :
          hava_durumu()

        elif tercih == 2 :
          check_up()

        elif tercih == 3 :
          speedtest()
    
        elif tercih == 4 :
          ip_co()

        elif tercih == 5 :
            ping_to()

        elif tercih == 6 :
            trace_to()
        
        elif tercih == 7 :
            nslook()
        
        elif tercih == 8 :
            sys_info()
        
        elif tercih == 9 :
            calender()

        elif tercih == 10 :
            neth_show()

        elif tercih == 11 :
            taskmg()
        
        elif tercih == 12 :
            discer()

        elif tercih == 13 :
            devman()

        elif tercih == 14 :
            aorp()

        elif tercih == 15 :
            paint()

        elif tercih == 16 :
            note()

        elif tercih == 17 :
            calc()

        elif tercih == 18 :
            sckey()

        elif tercih == 19 :
            reip()

        elif tercih == 20 :
            clgame()
        
        elif tercih == 0 :
            exit()
            break


    except Exception as hata2 :
        os.system('cls')
        print("An error has occurred! --> ",hata2)
        time.sleep(3)
        os.system('cls')
        continue
    except :
        os.system('cls')
        print("An error has occurred! Please try again.")
        time.sleep(1.5)
        os.system('cls')
        continue
    

        



                        # NovaKej<3