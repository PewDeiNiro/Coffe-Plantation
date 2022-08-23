import bs4 as bs
from page import Page

organizations = {"1" : "Полиция ЛС", "2" : "Областная полиция", "3" : "ФБР", "4": "Полиция СФ", "5" : "Больница ЛС", "6" : "Правительство", "7" : "Тюрьма Строгого Режима", "8" : "Больница СФ", "9" : "Автошкола", "10" : "СМИ ЛС",
                 "11" : "Грув стрит", "12" : "Вагосы", "13" : "Балласы", "14" : "Ацтеки", "15" : "Рифа", "16" : "Русская мафия", "17" : "Якудза", "18" : "ЛКН", "19" : "Байкеры", "20" : "Армия ЛС",
                 "21" : "Центральный Банк", "22" : "Больница ЛВ", "23" : "СВАТ", "24" : "СМИ ЛВ", "25" : "Ночные волки", "26" : "СМИ СФ", "27" : "Армия СФ", "28" : "Темное Братство", "29" : "Страховая Компания"
}
def getMessageAboutOrg(orgId):
    page = Page("https://apitest.arizona-rp.com/mon/fraction/11/" + str(orgId))
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    table = soup.find("tbody")
    countOnline = 0
    isLeaderOnline = False
    notSetted = True
    leader = ""
    deputy = []
    countOffline = 0
    for tr in table.find_all("tr"):
        if "_" in str(tr.find_all("td")[1]) and not str(tr.find_all("td")[3]).replace("<td>", "").replace("</td>", "") == "Сейчас играет":
            countOffline += 1
        if "_" in str(tr.find_all("td")[1]) and str(tr.find_all("td")[3]).replace("<td>", "").replace("</td>","") == "Сейчас играет" and str(tr.find_all("td")[2]).replace("<td>", "").replace("</td>","") == "Лидер":
            if notSetted:
                isLeaderOnline = True
                notSetted = False
        if str(tr.find_all("td")[2]).replace("<td>", "").replace("</td>","") == "Лидер":
            if leader == "":
                leader = str(tr.find_all("td")[1]).replace("<td>", "").replace("</td>","")
        if "_" in str(tr.find_all("td")[1]) and str(tr.find_all("td")[2]).replace("<td>", "").replace("</td>", "") == "9":
            nick = str(tr.find_all("td")[1]).replace("<td>", "").replace("</td>","")
            isOnline = False
            if str(tr.find_all("td")[3]).replace("<td>", "").replace("</td>","") == "Сейчас играет":
                isOnline = True
            deputy.append([nick, isOnline])
        if "_" in str(tr.find_all("td")[1]) and str(tr.find_all("td")[3]).replace("<td>", "").replace("</td>", "") == "Сейчас играет":
            countOnline += 1
    if leader == "":
        leader = "Отсутствует"
    message = "🔎Информация об организации " + "\"" + organizations[str(orgId)] + "\"🔍\nОнлайн организации - " + str(countOnline) + "🌕\nОффлайн организации - " + str(countOffline) + "🌑\nЛидер организации:👑\n" + leader + " - "
    if isLeaderOnline:
        message = message + "Онлайн🌕\n👷‍♂Заместители:👷‍♂\n"
    else:
        message = message + "Оффлайн🌑\n👷‍♂Заместители:👷‍♂\n"
    for deput in deputy:
        if deput[1]:
            message = message + deput[0] + " - " + "Онлайн🌕\n"
        else:
            message = message + deput[0] + " - " + "Оффлайн🌑\n"
    info = [message, str(countOnline)]
    return info