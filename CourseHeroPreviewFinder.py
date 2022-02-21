from selenium import webdriver
from colorama import Fore, init
import time, os
init()
os.system("mode 800")

os.system("title Course Hero Tool -By Dreamer#5114")
def getPreviews(url):
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])

    try:
        driver = webdriver.Chrome("PATH HERE, EXAMPLE: C:\\Users\\USER\\OneDrive\\Desktop\\chromedriver\\chromedriver.exe", options=option) #Put chromedriver.exe file loction between quotation marks using double back slashes.
    except Exception as DriverError:
        print(f"\n{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Invalid File Location For Chrome Driver Or File Location Hasn't Been Set Yet. Remember To Use Double Slashes. Make Sure Chrome Driver Is Same Version As Chrome\n    Line: 14\n    Stopped Program.\n")
        print(f"{Fore.RED}{DriverError}{Fore.RESET}\n")
        input(f"{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Press Enter To Exit")
        exit()

    print(f"\n{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Getting Link's HTML...")
    try:
        driver.get(url)
    except:
        print(f"{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}] Invalid Course Hero URL Or Network Issues Or You're Temporarily Blacklisted (If So, Connect To A New IP With A VPN Or Try Again In A Few Minutes).")
        input(f"{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Press Enter To Exit...")
        exit()
    time.sleep(4)
    html = driver.page_source

    if ">Request unsuccessful." in html:
        print(f"\n{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] A Captcha Was Given\n")
        while True:
            print(f"{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Please Solve The Captcha. Type \"y\" Once You Did")
            captcha_solved = input(f"{Fore.WHITE}[{Fore.CYAN}>>>{Fore.WHITE}] ")
            if captcha_solved == "y":
                html = driver.page_source
                if ">Request unsuccessful." not in html:
                    print(f"\n{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Successfully Got The HTML!")
                    break
                else:
                    print(f"\n{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}] Failed To Get The Page's HTML, Try Solving It Again.\n{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}] (If Not, Get A New IP With A VPN And Retry Or Try Again In A Few Minutes. You Most Likely Are Blacklisted Temporarily Due To Using This Too Much).\n")

    Link1 = html.find('url(/doc-asset/bg')
    Link2 = Link1
    print(html[Link1:Link2])
    while 1 == 1:
        Link2 += 1
        if html[Link2] == ")":
            break

    endLink = html[Link1:Link2]
    endLink = endLink.replace("background-image:", "")
    endLink = endLink.replace("url(", "")
    endLink = endLink.replace("-html-bg", "")
    endLink = endLink.replace(" ", "")
    endLink = endLink.replace(endLink[endLink.find("split-")::], "")

    dataRsidIndex1 = endLink.find('splits/')
    dataRsidIndex2 = dataRsidIndex1 + 7

    while 1 == 1:
        dataRsidIndex2 += 1
        if endLink[dataRsidIndex2] == "/":
            break

    dataRSID = endLink[dataRsidIndex1+7:dataRsidIndex2]

    if "v9" in endLink:
        numberDataRsid = False
    else:
        numberDataRsid = True

    #get pageAmount
    if "<label>Pages</label>" in html:
        pageAmountIndex1 = html.find("<label>Pages</label>")
        pageAmountIndex2 = pageAmountIndex1 + 25
        while 1 == 1:
            pageAmountIndex2 += 1
            if html[pageAmountIndex2] == "<":
                break
        pageAmount = int(html[pageAmountIndex1+25:pageAmountIndex2])
        pageAmountgot = True
    else:
        pageAmountgot = False
        print(f"{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Couldn't Successfully Get Page's Page Amount.\n")

    print(f"{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] File's Info")
    print(f"    {Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Data-RSID: {dataRSID}\n    {Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Page-Amount: {pageAmount}\n    {Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Path: {endLink}")
    print(f"\n{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Generating Possible Preview Links...\n")
    #generating possible links
    generatedPageList = []
    validLinks = 0
    page = 0
    pageUrlbegin1 = f"https://www.coursehero.com{endLink}".replace(dataRSID, "v9")
    pageUrlbegin2 = f"https://www.coursehero.com{endLink}".replace(dataRSID, "v9.2")

    if numberDataRsid == True: #If the given file does have an actual data rsid
        pageUrlbegin = f"https://www.coursehero.com{endLink}"
        pageUrlbegin3 = f"https://www.coursehero.com{endLink}".replace(dataRSID, str(int(dataRSID)-1))
        pageUrlbegin4 = f"https://www.coursehero.com{endLink}".replace(dataRSID, str(int(dataRSID)+1))

        while int(page) < int(pageAmount):
            page += 1
            generatedPageList.append(pageUrlbegin + f"split-{page-1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin1 + f"split-{page-1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-{page-1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin3 + f"split-{page-1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin4 + f"split-{page-1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-0-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-1-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-2-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin + f"split-{page-2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin1 + f"split-{page-2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-{page-2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin3 + f"split-{page-2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin4 + f"split-{page-2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-0-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-1-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-2-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin + f"split-{page-3}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin1 + f"split-{page-3}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-{page-3}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin3 + f"split-{page-3}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin4 + f"split-{page-3}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-0-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-1-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-2-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin + f"split-{page+0}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin1 + f"split-{page+0}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-{page+0}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin3 + f"split-{page+0}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin4 + f"split-{page+0}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-0-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-1-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-2-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin + f"split-{page+1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin1 + f"split-{page+1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-{page+1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin3 + f"split-{page+1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin4 + f"split-{page+1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-0-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-1-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-2-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin + f"split-{page+2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin1 + f"split-{page+2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-{page+2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin3 + f"split-{page+2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin4 + f"split-{page+2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-0-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-1-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-2-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin + f"split-{page+3}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin1 + f"split-{page+3}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-{page+3}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin3 + f"split-{page+3}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin4 + f"split-{page+3}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-0-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-1-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-2-page-{page}.jpg")

    elif numberDataRsid == False: #If the given file doesn't have an actual Data-RSID...
        while int(page) < int(pageAmount):
            page += 1
            generatedPageList.append(pageUrlbegin1 + f"split-{page-1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-{page-1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin1 + f"split-{page-2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-{page-2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin1 + f"split-{page+0}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-{page+0}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin1 + f"split-{page+1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-{page+1}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin1 + f"split-{page+2}-page-{page}.jpg")
            generatedPageList.append(pageUrlbegin2 + f"split-{page+2}-page-{page}.jpg")

    print(f"\n{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Generated {len(generatedPageList)} Possible Links.\n{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Testing Generated Links...")
    print(f"{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] This Will Take About {round((len(generatedPageList)*5)/60)} Minutes Since I Don't Want You Getting Blacklisted (You Can Change It In The Code On Line #189).")
    pagesTried = 0

    for examineURL in generatedPageList:
        pagesTried += 1
        try:
            driver.get(examineURL)
            pageStatus = driver.title

            if "Page missing!" not in pageStatus:
                validLinks += 1
                print(f"\n{Fore.WHITE}[{Fore.LIGHTGREEN_EX}>{Fore.WHITE}] Valid Preview: {examineURL} ({pagesTried}/{len(generatedPageList)})")
            time.sleep(5)

        except:
            print(f"\n{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}] {Fore.LIGHTRED_EX}You Stopped The Program Or Network Issues Or Your Probably Temporarily Blacklisted, Try Connecting To A New IP With A VPN Or Try Again In A Few Minutes. (Checked {pagesTried} Links And Only {validLinks} Links Were Valid.)\n")
            input(f"{Fore.WHITE}[{Fore.RED}>{Fore.WHITE}] {Fore.LIGHTRED_EX}Program Stopped...")
            time.sleep(99999)

    print(f"\n{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Generated {len(generatedPageList)} Possible Links, But Only {validLinks} Links Were Valid\n")
    print(f"{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Refreshing In 5 Second, Scroll Back Up For The Valid Links")
    time.sleep(5)
    print(os.get_terminal_size().lines*"\n")

while True:
    bigText = f"""
{" "*round(os.get_terminal_size().columns/2-60)} ██████╗ ██████╗ ██╗   ██╗██████╗ ███████╗███████╗    ██╗  ██╗███████╗██████╗  ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
{" "*round(os.get_terminal_size().columns/2-60)}██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝    ██║  ██║██╔════╝██╔══██╗██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
{" "*round(os.get_terminal_size().columns/2-60)}██║     ██║   ██║██║   ██║██████╔╝███████╗█████╗      ███████║█████╗  ██████╔╝██║   ██║       ██║   ██║   ██║██║   ██║██║     
{" "*round(os.get_terminal_size().columns/2-60)}██║     ██║   ██║██║   ██║██╔══██╗╚════██║██╔══╝      ██╔══██║██╔══╝  ██╔══██╗██║   ██║       ██║   ██║   ██║██║   ██║██║     
{" "*round(os.get_terminal_size().columns/2-60)}╚██████╗╚██████╔╝╚██████╔╝██║  ██║███████║███████╗    ██║  ██║███████╗██║  ██║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
{" "*round(os.get_terminal_size().columns/2-60)} ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
""".replace('█', f'{Fore.WHITE}█{Fore.BLUE}')

    print(bigText)

    print(f"""{Fore.WHITE}
{" "*round(os.get_terminal_size().columns/2-31)}╔════════════════════════════════════════════════════════════╗
{" "*round(os.get_terminal_size().columns/2-31)}║       {Fore.LIGHTBLUE_EX}Discord: {Fore.WHITE}Dreamer#5114                                {Fore.WHITE}║
{" "*round(os.get_terminal_size().columns/2-31)}║       {Fore.LIGHTBLUE_EX}Github : {Fore.WHITE}https://github.com/OriginalAlien            {Fore.WHITE}║
{" "*round(os.get_terminal_size().columns/2-31)}║       {Fore.LIGHTBLUE_EX}Credits: {Fore.WHITE}https://www.youtube.com/watch?v=47PUtH4ZhIc {Fore.WHITE}║
{" "*round(os.get_terminal_size().columns/2-31)}╚════════════════════════════════════════════════════════════╝
""")

    print(f"{' '*round(os.get_terminal_size().columns/2-32)}{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] This Tool Gets Available Hidden Previews For Coursehero. {Fore.WHITE}[{Fore.CYAN}<{Fore.WHITE}]")
    print(f"{' '*round(os.get_terminal_size().columns/2-28)}{Fore.WHITE}[{Fore.YELLOW}>{Fore.WHITE}] Recommended: USE A VPN TO NOT GET IP BLACKLISTED {Fore.WHITE}[{Fore.YELLOW}<{Fore.WHITE}]")
    URL_input = input(f"\n\n{Fore.WHITE}[{Fore.CYAN}>>>{Fore.WHITE}] Coursehero File URL: ")

    if "coursehero.com/file" not in URL_input.lower(): #makes sure you actually put a valid url
        while "coursehero.com/file" not in URL_input.lower():
            print(f"{Fore.WHITE}[{Fore.LIGHTRED_EX}>{Fore.WHITE}] Enter An Actual Coursehero Link")
            URL_input = input(f"\n{Fore.WHITE}[{Fore.CYAN}>>>{Fore.WHITE}] Coursehero File URL: ")
            if "coursehero.com/file" in URL_input.lower():
                print(f"\n{Fore.WHITE}[{Fore.CYAN}>{Fore.WHITE}] Opening Chrome Driver...\n")
                getPreviews(URL_input)
                break

    elif "coursehero.com/file" in URL_input.lower(): #gig
        getPreviews(URL_input)
