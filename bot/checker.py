import bs4 as bs
from page import Page


def getAllOnlineOrgMembers(orgId):
    page = Page("https://apitest.arizona-rp.com/mon/fraction/11/" + str(orgId))
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    table = soup.find("tbody")
    result = []
    for tr in table.find_all("tr"):
        if "_" in str(tr.find_all("td")[1]) and str(tr.find_all("td")[3]).replace("<td>", "").replace("</td>", "") == "Сейчас играет":
            result.append(str(tr.find_all("td")[1]).replace("<td>", "").replace("</td>",""))
    return result


def isLeaderOnline(orgId):
    page = Page("https://apitest.arizona-rp.com/mon/fraction/11/" + str(orgId))
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    table = soup.find("tbody")
    for tr in table.find_all("tr"):
        if "_" in str(tr.find_all("td")[1]) and str(tr.find_all("td")[3]).replace("<td>", "").replace("</td>","") == "Сейчас играет" and str(tr.find_all("td")[2]).replace("<td>", "").replace("</td>","") == "Лидер":
            return True
    return False

def getDeputy(orgId):
    page = Page("https://apitest.arizona-rp.com/mon/fraction/11/" + str(orgId))
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    table = soup.find("tbody")
    result = []
    for tr in table.find_all("tr"):
        if "_" in str(tr.find_all("td")[1]) and str(tr.find_all("td")[2]).replace("<td>", "").replace("</td>", "") == "9":
            result.append(str(tr.find_all("td")[1]).replace("<td>", "").replace("</td>", ""))
    return result

def getDeputyOnline(orgId):
    page = Page("https://apitest.arizona-rp.com/mon/fraction/11/" + str(orgId))
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    table = soup.find("tbody")
    result = []
    for tr in table.find_all("tr"):
        if "_" in str(tr.find_all("td")[1]) and str(tr.find_all("td")[3]).replace("<td>", "").replace("</td>","") == "Сейчас играет" and str(tr.find_all("td")[2]).replace("<td>", "").replace("</td>", "") == "9":
            result.append(str(tr.find_all("td")[1]).replace("<td>", "").replace("</td>",""))
    return result

