import requests, random, time #gig
#RECOMMEND TO USE VPN
#READ BEFORE USING: I recommend to add more user agents in useragents.txt so more easy requests, get free ones at https://developers.whatismybrowser.com/useragents/explore/operating_system_name/windows/
def getPages(url):

    headersList = open("useragents.txt").read().splitlines()
    header = {"User-Agent": str(random.choice(headersList))}
    proxiesList = open("proxies.txt").read().splitlines()
    proxy = {"http": str(random.choice(proxiesList))}

    html = requests.get(url, headers=header, proxies=proxy)
    html = str(html.content)
    print(f"\nUsing Proxy {proxy}...")
    print(f"\nUsing User-Agent {header}...\n")

    print("\n\nGetting File Info...\n")
    #get dataRsid
    if "data-rsid=" in html:
        dataRsidIndex1 = html.find("data-rsid=")
        dataRsidIndex2 = dataRsidIndex1 + 10
        while 1 == 1:
            dataRsidIndex2 += 1
            if html[dataRsidIndex2] == ">":
                break
        dataRsid = html[dataRsidIndex1+10:dataRsidIndex2]
    else:
        print("Couldn't Successfully Get The Page's Data RSID. Line #13")


    #get filehash
    if "filehash" in html:
        filehashIndex1 = html.find("data-filehash=\"")
        filehashIndex2 = filehashIndex1 + 15
        while 1 == 1:
            filehashIndex2 += 1
            if html[filehashIndex2] == "\"":
                break
        filehash = html[filehashIndex1+15:filehashIndex2]
    else:
        print("Couldn't Successfully Get The Page's File Hash. Line #26")
    
    #get pageAmount
    if "<label>Pages</label>" in html:
        pageAmountIndex1 = html.find("<label>Pages</label>")
        pageAmountIndex2 = pageAmountIndex1 + 38 #38
        while 1 == 1:
            pageAmountIndex2 += 1
            if html[pageAmountIndex2] == "\\":
                break
        pageAmount = html[pageAmountIndex1+38:pageAmountIndex2]
    else:
        print("Couldn't Successfully Get Page's Page Amount. Line #38")
    try:
        print(f"File Info:\n    Data-RSID: {dataRsid}\n    File-Hash: {filehash}\n    Page-Amount: {pageAmount}\n")
    except:
        print("\nCouldn't Get HTML Successfully, Solutions: Connect To A VPN To Change Your IP And Retry.\nOr Update Your HTTP Proxies and User-Agents.")
        input()
        exit()

    print("\nGetting Possible Preview Links...\n")

    generatedPageList = []

    validLinks = 1
    page = 0

    pageUrlbegin = f"https://www.coursehero.com/doc-asset/bg/{filehash}/splits/{dataRsid}/"

    generatedPageList.append(pageUrlbegin + f"split-{page+0}-page-{page}.jpg")
    generatedPageList.append(pageUrlbegin + f"split-{page+1}-page-{page}.jpg")
    generatedPageList.append(pageUrlbegin + f"split-{page+2}-page-{page}.jpg")
    page += 1
    generatedPageList.append(pageUrlbegin + f"split-{page-1}-page-{page}.jpg")
    generatedPageList.append(pageUrlbegin + f"split-{page+0}-page-{page}.jpg")
    generatedPageList.append(pageUrlbegin + f"split-{page+1}-page-{page}.jpg")
    generatedPageList.append(pageUrlbegin + f"split-{page+2}-page-{page}.jpg")
    page += 1
    generatedPageList.append(pageUrlbegin + f"split-{page-1}-page-{page}.jpg")
    generatedPageList.append(pageUrlbegin + f"split-{page-2}-page-{page}.jpg")
    generatedPageList.append(pageUrlbegin + f"split-{page+0}-page-{page}.jpg")
    generatedPageList.append(pageUrlbegin + f"split-{page+1}-page-{page}.jpg")
    generatedPageList.append(pageUrlbegin + f"split-{page+2}-page-{page}.jpg")
    page += 1
    #generating possible extra previews
    while int(page) < int(pageAmount):
        page += 1
        generatedPageList.append(pageUrlbegin + f"split-{page-1}-page-{page}.jpg")
        generatedPageList.append(pageUrlbegin + f"split-{page-2}-page-{page}.jpg")
        generatedPageList.append(pageUrlbegin + f"split-{page+0}-page-{page}.jpg")
        generatedPageList.append(pageUrlbegin + f"split-{page+1}-page-{page}.jpg")
        generatedPageList.append(pageUrlbegin + f"split-{page+2}-page-{page}.jpg")

    print(f"Generated {len(generatedPageList)} Possible Links, And {page} Pages\nTesting {len(generatedPageList)} Links...\n\nNote: This Can Take A Long Time If It Has Lots Of Pages.\n")
    #checking if the generated possible previews are valid or not
    for examineURL in generatedPageList:
        try:
            time.sleep(2)
            header = {"User-Agent": f'{str(random.choices(headersList))}'}
            proxy = {"http": str(random.choice(proxiesList))}
            requestStatus = requests.get(examineURL, headers=header, proxies=proxy)
        except:
            time.sleep(2)
            requestStatus = requests.get(examineURL, headers=header)
            header = {"User-Agent": f'{str(random.choices(headersList))}'}
            proxy = {"http": str(random.choice(proxiesList))}

        if requestStatus.ok:
            print(f"\nValid Preview: {examineURL} ({validLinks}/{len(generatedPageList)})")
            validLinks += 1
        
        time.sleep(random.randint(1,3))
    
    #prints it out
    print(f"\n\nGenerated {len(generatedPageList)} Links, Only {validLinks} Were Valid\n")

while True:
    print("_________________________________________________________________________________________")
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║       Made By Dreamer#5114                                 ║
    ║       Credits: https://www.youtube.com/watch?v=47PUtH4ZhIc ║
    ║       Since It Helped Me Making This                       ║
    ║       Github: https://github.com/OriginalAlien             ║
    ║       Enjoy!                                               ║
    ╚════════════════════════════════════════════════════════════╝
""")
    print(f"---About---")
    print("\nThis Tool Gets All Available Previews For Coursehero.\n\nRecommended: Use VPN, Update HTTP Proxies, Update User Agents.\n\nFREE USER-AGENTS: https://developers.whatismybrowser.com/useragents/explore/\nFREE HTTP PROXY: https://proxyscrape.com/free-proxy-list")
    print("---Input---")
    URL_input = input("\n[>>>] URL: ")

    if "coursehero.com/file" not in URL_input.lower(): #makes sure you actually put a valid url
        while "coursehero.com/file" not in URL_input.lower():
            print("[>] Enter An Actual Coursehero  Link...")
            URL_input = input("\n[>>>] URL: ")
            if "coursehero.com/file" in URL_input.lower():
                getPages(URL_input)
                break

    elif "coursehero.com/file" in URL_input.lower(): #gig
        getPages(URL_input)
