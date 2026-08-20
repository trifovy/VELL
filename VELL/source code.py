# HAHAHAHAHAHAHAH



import os
import requests
from colorama import init, Fore

init()

us = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Sec-Ch-Ua": '"Google Chrome";v="151", "Chromium";v="151", "Not=A?Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Upgrade-Insecure-Requests": "1"
}
logo = r"""
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
  __                 _____ 
_/  |________  _____/ ____\
\   __\_  __ \/  _ \   __\ 
 |  |  |  | \(  <_> )  |   
 |__|  |__|   \____/|__| VERS 0.1  
                         

⠀⠀⠀"""

while True:
    os.system('cls||clear')
    print(Fore.RED + logo)

    print(Fore.GREEN, end="")
    df = input('Check nickname: ').strip()


    print(Fore.RED, end="")

    dff = df.lstrip('@/').replace(' ', '').replace('_', '').replace('.', '').replace('-', '').lower()

    if not dff:
        continue


    with open("results.txt", "w", encoding="utf-8") as f:
        f.write(f"=== Результаты для: {dff} ===\n\n")


    #============TikTok Search==========1
    def tikTok():
        try:
            res = requests.get(f'https://tiktok.com/@{dff}', headers=us, timeout=10)
            if res.status_code == 200:
                print(f'[+] https://tiktok.com/@{dff}')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] https://tiktok.com/@{dff}\n")
            else:
                print(f'[-] TikTok')
        except:
            print(f'[!] TikTok Error')





    tikTok()


    #######pinterest Search#######2
    def pinterest():
        try:
            rss = requests.get(f'https://pinterest.com/{dff}/', headers=us, timeout=10)
            if rss.status_code == 200:
                print(f'[+] https://pinterest.com/{dff}/')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] https://pinterest.com/{dff}/\n")
            else:
                print(f'[-] Pinterest')
        except:
            print(f'[!] Pinterest Error')


    pinterest()


    ##########github Search##########3
    def github():
        try:
            ress = requests.get(f'https://github.com/{dff}', headers=us, timeout=10)
            if ress.status_code == 200:
                print(f'[+] https://github.com/{dff}')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] https://github.com/{dff}\n")
            else:
                print(f'[-] https://github.com/{dff}')
        except:
            print(f'[!] GitHub Error')


    github()


    # =========facebook search===========4
    def facebook():
        try:
            rsd = requests.get(f'https://facebook.com/{dff}', headers=us, timeout=10)
            if rsd.status_code == 200:
                print(f'[+] https://facebook.com/{dff}')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] https://facebook.com/{dff}\n")
            else:
                print(f'[-] https://facebook.com/{dff}')
        except:
            print(f'[!] Facebook Error')


    facebook()


    # =========instagram search==========5
    def instagram():
        try:
            dfg = requests.get(f'https://instagram.com/{dff}/', headers=us, timeout=10)
            if dfg.status_code == 200:
                print(f'[+] https://instagram.com/{dff}/')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] https://instagram.com/{dff}/\n")
            else:
                print(f'[-] https://instagram.com/{dff}/')
        except:

            print(f'[!] Instagram Error')


    instagram()


    # ===========youtube search==========6
    def youtube():
        try:
            rere = requests.get(f'https://youtube.com/@{dff}', headers=us, timeout=10)
            if rere.status_code == 200:
                print(f'[+] https://youtube.com/@{dff}')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] https://youtube.com/@{dff}\n")
            else:
                print(f'[-] https://youtube.com/@{dff}')
        except:
            print(f'[!] YouTube Error')


    youtube()


    # =========telegram search===========7
    def telegram():
        try:
            cjh = requests.get(f'https://t.me/{dff}', headers=us, timeout=10)
            if cjh.status_code == 200:
                print(f'[+] https://t.me/{dff}')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] https://t.me/{dff}\n")
            else:
                print(f'[-] https://t.me/{dff}')
        except:
            print(f'[!] Telegram Error')


    telegram()


    # ===========vk search==========8
    def vk():
        try:
            idb = requests.get(f'https://vk.com/{dff}', headers=us, timeout=10)
            if idb.status_code == 200:
                print(f'[+] https://vk.com/{dff}')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] https://vk.com/{dff}\n")
            else:
                print(f'[-] https://vk.com/{dff}')

        except:
            print(f'[!] VK Error')


    vk()


    # =========twitch search########9
    def twitch():
        try:
            ljdb = requests.get(f'https://twitch.tv/{dff}', headers=us, timeout=10)
            if ljdb.status_code == 200:
                print(f'[+] https://twitch.tv/{dff}')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] https://twitch.tv/{dff}\n")
            else:
                print(f'[-] https://twitch.tv/{dff}')

        except:
            print(f'[!] Twitch Error')


    twitch()


    # =======roblox search########10
    def roblox():
        try:
            ref = requests.get(f'https://roblox.com/{dff}', headers=us, timeout=10)
            if ref.status_code == 200:
                print(f'[+] https://roblox.com/{dff}')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] https://roblox.com/{dff}\n")
            else:
                print(f'[-] https://roblox.com/{dff}')

        except:
            print(f'[!] Roblox Error')


    roblox()


    # =========snapchat search########11
    def snapchat():
        try:
            jn = requests.get(f'https://snapchat.com/{dff}', headers=us, timeout=10)
            if jn.status_code == 200:
                print(f'[+] https://snapchat.com/{dff}')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] https://snapchat.com/{dff}\n")
            else:
                print(f'[-] https://snapchat.com/{dff}')
        except:
            print(f'[!] Snapchat Error')


    snapchat()


    # ==========Reddit search==========12
    def reddit():
        url = f'https://www.reddit.com/user/{dff}/'
        try:
            fgfg = requests.get(url, headers=us, timeout=10)

            if fgfg.status_code == 200:
                print(f'[+] {url}')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] {url}\n")
            else:
                print(f'[-] {url} (Status: {fgfg.status_code})')

        except requests.exceptions.RequestException:
            print(f'[!] reddit Error')


    reddit()



    # ===========twitter search==========13
    def twitter():
        try:
            fd = requests.get(f'https://twitter.com{dff}', headers=us, timeout=10)
            if fd.status_code == 200:
                print(f'[+] https://twitter.com{dff}')
                with open("results.txt", "a", encoding="utf-8") as f:
                    f.write(f"[+] https://twitter.com{dff}\n")
            else:
                print(f'[-] https://twitter.com{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] twitter Error')
    twitter()



    #==========spotify serch==========14
    def spotify():
        try:
            bn = requests.get(f'https://open.spotify.com/user/{dff}', headers=us, timeout=10)
            if bn.status_code == 200:
                print(f'https://open.spotify.com/user/{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://open.spotify.com/user/{dff}')
            else:
                print(f'[-] https://open.spotify.com/user/{dff}')
        except requests.exceptions.RequestException:
            print('[!] spotify Error')




    #===========soundcloud search===========15
    def soundcloud():
        try:
            kl = requests.get(f'https://soundcloud.com/{dff}', headers=us, timeout=10)
            if kl.status_code == 200:
                print(f'[+] https://soundcloud.com/{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://soundcloud.com/{dff}')
            else:
                print(f'[-] https://soundcloud.com/{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] soundcloud Error')

    soundcloud()




    #==========steam search==============16
    def steam():
        try:
            kll = requests.get(f'https://steamcommunity.com/id/{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://steamcommunity.com/id/{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://steamcommunity.com/id/{dff}')
            else:
                print(f'[-] https://steamcommunity.com/id/{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] steam Error')


    steam()



    # ==========yandex_music search==============17
    def yandex_music():
        try:
            kllsd = requests.get(f'https://yandex.ru{dff}/playlists', headers=us, timeout=10)
            if kllsd.status_code == 200:
                print(f'[+] https://yandex.ru{dff}/playlists')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://yandex.ru{dff}/playlists\n')
            else:
                print(f'[-] https://yandex.ru{dff}/playlists')
        except requests.exceptions.RequestException:
            print(f'[!] yandex_music Error')


    yandex_music()


    # ==========yandex_market search==============18
    def yandex_market():
        try:
            klerl = requests.get(f'https://yandex.ru{dff}', headers=us, timeout=10)
            if klerl.status_code == 200:
                print(f'[+] https://yandex.ru{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://yandex.ru{dff}\n')
            else:
                print(f'[-] https://yandex.ru{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] yandex_market Error')

    yandex_market()


    # ==========ebay search==============19
    def ebay():
        try:
            klsl = requests.get(f'https://ebay.com{dff}', headers=us, timeout=10)
            if klsl.status_code == 200:
                print(f'[+] https://ebay.com{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://ebay.com{dff}\n')
            else:
                print(f'[-] https://ebay.com{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] ebay Error')


    ebay()



    # ==========mail_ru search==============20
    def mail_ru():
        try:
            klssl = requests.get(f'https://my.mail.ru/mail/{dff}', headers=us, timeout=10)
            if klssl.status_code == 200:
                print(f'[+] https://my.mail.ru/mail/{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://my.mail.ru/mail/{dff}\n')
            else:
                print(f'[-] https://my.mail.ru/mail/{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] mail_ru Error')


        mail_ru()


    # ==========tenchat search==============21
    def tenchat():
        try:
            klsssl = requests.get(f'https://tenchat.ru/{dff}', headers=us, timeout=10)
            if klsssl.status_code == 200:
                print(f'[+] https://tenchat.ru/{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://tenchat.ru/{dff}\n')
            else:
                print(f'[-] https://tenchat.ru/{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] tenchat Error')

    tenchat()







    # ==========paypal search==============22
    def paypal():
        try:
            kll = requests.get(f'https://www.paypal.me/{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://www.paypal.me/{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://www.paypal.me/{dff}\n')
            else:
                print(f'[-] https://www.paypal.me/{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] paypal Error')

    paypal()


    # ==========dzen search==============23
    def dzen():
        try:
            klddl = requests.get(f'https://dzen.ru/{dff}', headers=us, timeout=10)
            if klddl.status_code == 200:
                print(f'[+] https://dzen.ru/{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://dzen.ru/{dff}\n')
            else:
                print(f'[-] https://dzen.ru/{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] dzen Error')

    dzen()


    # ==========patreon search==============24
    def patreon():
        try:
            kll = requests.get(f'https://patreon.com{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://patreon.com{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://patreon.com{dff}\n')
            else:
                print(f'[-] https://patreon.com{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] patreon Error')


    patreon()


    # ==========habr search==============25
    def habr():
        try:
            kll = requests.get(f'https://habr.com{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://habr.com{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://habr.com{dff}\n')
            else:
                print(f'[-] https://habr.com{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] habr Error')


    habr()


    # ==========habr_career search==============26
    def habr_career():
        try:
            kll = requests.get(f'https://career.habr.com/{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://career.habr.com/{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://career.habr.com/{dff}\n')
            else:
                print(f'[-] https://career.habr.com/{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] habr_career Error')


    # ==========pikabu search==============27
    def pikabu():
        try:
            kll = requests.get(f'https://pikabu.ru@{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://pikabu.ru@{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://pikabu.ru@{dff}\n')
            else:
                print(f'[-] https://pikabu.ru@{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] pikabu Error')


        pikabu()


    # ==========vc_ru search==============28
    def vc_ru():
        try:
            kll = requests.get(f'https://vc.ru{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://vc.ru{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://vc.ru{dff}\n')
            else:
                print(f'[-] https://vc.ru{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] vc_ru Error')

    vc_ru()
    habr_career()


    # ==========itch_io search==============29
    def itch_io():
        try:
            kll = requests.get(f'https://{dff}.itch.io', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://{dff}.itch.io')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://{dff}.itch.io\n')
            else:
                print(f'[-] https://{dff}.itch.io')
        except requests.exceptions.RequestException:
            print(f'[!] itch_io Error')


    # ==========kwork search==============30
    def kwork():
        try:
            kll = requests.get(f'https://kwork.ru{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://kwork.ru{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://kwork.ru{dff}\n')
            else:
                print(f'[-] https://kwork.ru{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] kwork Error')


    kwork()


    # ==========otvet_mail search==============31
    def otvet_mail():
        try:
            kll = requests.get(f'https://mail.ru{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://mail.ru{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://mail.ru{dff}\n')
            else:
                print(f'[-] https://mail.ru{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] otvet_mail Error')


    otvet_mail()


    # ==========ok_ru search==============32
    def ok_ru():
        try:
            kll = requests.get(f'https://ok.ru{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://ok.ru{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://ok.ru{dff}\n')
            else:
                print(f'[-] https://ok.ru{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] ok_ru Error')



    # ==========rutube search==============33
    def rutube():
        try:
            kll = requests.get(f'https://rutube.ru{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://rutube.ru{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://rutube.ru{dff}\n')
            else:
                print(f'[-] https://rutube.ru{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] rutube Error')


        rutube()





    ok_ru()

    itch_io()


    # ==========boosty search==============34
    def boosty():
        try:
            kll = requests.get(f'https://boosty.to{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://boosty.to{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://boosty.to{dff}\n')
            else:
                print(f'[-] https://boosty.to{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] boosty Error')


    boosty()


    # ==========substack search==============35
    def substack():
        try:
            kll = requests.get(f'https://substack.com@{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://substack.com@{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://substack.com@{dff}\n')
            else:
                print(f'[-] https://substack.com@{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] substack Error')


    substack()


    # ==========gitlab search==============36
    def gitlab():
        try:
            kll = requests.get(f'https://gitlab.com{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://gitlab.com{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://gitlab.com{dff}\n')
            else:
                print(f'[-] https://gitlab.com{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] gitlab Error')

    gitlab()


    # ==========ask_fm search==============37
    def ask_fm():
        try:
            kll = requests.get(f'https://ask.fm{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://ask.fm{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://ask.fm{dff}\n')
            else:
                print(f'[-] https://ask.fm{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] ask_fm Error')


    ask_fm()




    # ==========codeforces search==============38
    def codeforces():
        try:
            kll = requests.get(f'https://codeforces.com{dff}', headers=us, timeout=10)
            if kll.status_code == 200:
                print(f'[+] https://codeforces.com{dff}')
                with open(f'results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'[+] https://codeforces.com{dff}\n')
            else:
                print(f'[-] https://codeforces.com{dff}')
        except requests.exceptions.RequestException:
            print(f'[!] codeforces Error')




    codeforces()

    print(Fore.YELLOW + "\n Results saved to results.txt")

    print(Fore.GREEN, end="")
    input('Enter = Menu')
