import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from datetime import datetime

main_token = "e4128d88581696f9382e18f3d1852b9b463041116389f16f0b27d6c055d1dd923514e1eab8a1586369746"
vk_session = vk_api.VkApi(token=main_token)

bot_id = 213622107

longpoll = VkBotLongPoll(vk_session, bot_id)

save_file = "C:\\Users\\pewde\\PycharmProjects\\Coffe-Plantation\\bot\\load.txt"
log_file = "C:\\Users\\pewde\\PycharmProjects\\Coffe-Plantation\\bot\\log.txt"

status = "main"

gsv = "@zhenya_bruna(ГСВ)"
gcv = "@zhenya_bruna(ГКВ)"
st = "@zhenya_bruna(СТ)"
judge = "@zhenya_bruna(Судья)"
gp = "@zhenya_bruna(ГП)"
guber = "@zhenya_bruna(Губернатор)"
gcl = "1"
stk = "@zhenya_bruna(СтК)"
cb = "@zhenya_bruna(ЦБ)"
lspd = "@zhenya_bruna(ЛСПД)"
sfpd = "@zhenya_bruna(СФПД)"
swat = "@zhenya_bruna(СВАТ)"
rcsd = "@zhenya_bruna(РКШД)"
fbi = "@zhenya_bruna(ФБР)"
lsmc = "@zhenya_bruna(ЛСМЦ)"
sfmc = "@zhenya_bruna(СФМЦ)"
lvmc = "@zhenya_bruna(ЛВМЦ)"
lsa = "@zhenya_bruna(ЛСа)"
sfa = "@zhenya_bruna(ВМС)"
msp = "@zhenya_bruna(ТСР)"
rls = "@zhenya_bruna(СМИ ЛС)"
rsf = "@zhenya_bruna(СМИ СФ)"
rlv = "@zhenya_bruna(СМИ ЛВ)"


# Developer

access_dev = ["342420933"]

# ГС/ЗГС ГОС

access_full = ["475362255", "342420933"]

# Government

access_full_government = ["608273181", "450908343"]
access_spec_government = ["665664706"]

# Central Office

access_full_co = ["342420933", "471076385"]
access_spec_co = ["543775126", "489856771", "100437381"]

# Department of Justice

access_full_justice = ["360669127", "481698071"]
access_spec_justice = ["454427393", "435861554", "561978801", "30732603"]

# Department of Health

access_full_health = ["676100115", ""]
access_spec_health = ["466657339", "450908343", "482497386"]

# Departament of Defense

access_full_defense = ["341995691", ""]
access_spec_defense = ["709048695", "522188393"]

# Mass Media

access_full_media = ["454108081", "572994700"]
access_spec_media = ["482497386"]

statuses = ["main", "menu government", "menu co", "menu juctice", "menu health", "menu defense", "menu media"]

def checkValidId(id):
    if id.isdigit() and len(id) == 9:
        return True
    else:
        return False

def log(text):
    file = open(log_file, "a")
    current_datetime = datetime.now()

    day = str(current_datetime.day)
    if len(day) < 2:
        day = "0" + day
    month = str(current_datetime.month)
    if len(month) < 2:
        month = "0" + month
    hour = str(current_datetime.hour)
    if len(hour) < 2:
        hour = "0" + hour
    minute = str(current_datetime.minute)
    if len(minute) < 2:
        minute = "0" + minute
    second = str(current_datetime.second)
    if len(second) < 2:
        second = "0" + second

    text = "[" + day + "." + month + "." + str(current_datetime.year) + " " + hour + ":" + minute + ":" + second + "] " + text + "\n"
    file.write(text)
    file.close()

def clearVariables():
    access_full.clear()
    access_full_government.clear()
    access_spec_government.clear()
    access_full_co.clear()
    access_spec_co.clear()
    access_full_justice.clear()
    access_spec_justice.clear()
    access_full_health.clear()
    access_spec_health.clear()
    access_full_defense.clear()
    access_spec_defense.clear()
    access_full_media.clear()
    access_spec_media.clear()

def saveVariables():
    file = open(save_file, 'w')
    for el in access_full:
        file.write("af " + el + "\n")
    for el in access_full_government:
        file.write("afg " + el + "\n")
    for el in access_spec_government:
        file.write("asg " + el + "\n")
    for el in access_full_co:
        file.write("afc " + el + "\n")
    for el in access_spec_co:
        file.write("asc " + el + "\n")
    for el in access_full_justice:
        file.write("afj " + el + "\n")
    for el in access_spec_justice:
        file.write("asj " + el + "\n")
    for el in access_full_health:
        file.write("afh " + el + "\n")
    for el in access_spec_health:
        file.write("ash " + el + "\n")
    for el in access_full_defense:
        file.write("afd " + el + "\n")
    for el in access_spec_defense:
        file.write("asd " + el + "\n")
    for el in access_full_media:
        file.write("afm " + el + "\n")
    for el in access_spec_media:
        file.write("asm " + el + "\n")
    file.write("gsv " + gsv + "\n")
    file.write("gcv " + gcv + "\n")
    file.write("st " + st + "\n")
    file.write("judge " + judge + "\n")
    file.write("guber " + guber + "\n")
    file.write("gp " + gp + "\n")
    file.write("gcl " + gcl + "\n")
    file.write("stk " + stk + "\n")
    file.write("cb " + cb + "\n")
    file.write("lspd " + lspd + "\n")
    file.write("sfpd " + sfpd + "\n")
    file.write("rcsd " + rcsd + "\n")
    file.write("swat " + swat + "\n")
    file.write("fbi " + fbi + "\n")
    file.write("lsmc " + lsmc + "\n")
    file.write("sfmc " + sfmc + "\n")
    file.write("lvmc " + lvmc + "\n")
    file.write("lsa " + lsa + "\n")
    file.write("sfa " + sfa + "\n")
    file.write("msp " + msp + "\n")
    file.write("rls " + rls + "\n")
    file.write("rsf " + rsf + "\n")
    file.write("rlv " + rlv + "\n")
    file.close()


def getFunctionalVkId(msg):
    result = msg.split("|")[1].replace("]", "")
    return result

def loadVariables():
    clearVariables()
    file = open(save_file, 'r')
    for line in file:
        if line.startswith("af "):
            line = line.replace("af ", "")
            line = line.strip()
            access_full.append(line)
        if line.startswith("afg "):
            line = line.replace("afg ", "")
            line = line.strip()
            access_full_government.append(line)
        if line.startswith("asg "):
            line = line.replace("asg ", "")
            line = line.strip()
            access_spec_government.append(line)
        if line.startswith("afc "):
            line = line.replace("afc ", "")
            line = line.strip()
            access_full_co.append(line)
        if line.startswith("asc "):
            line = line.replace("asc ", "")
            line = line.strip()
            access_spec_co.append(line)
        if line.startswith("afj "):
            line = line.replace("afj ", "")
            line = line.strip()
            access_full_justice.append(line)
        if line.startswith("asj "):
            line = line.replace("asj ", "")
            line = line.strip()
            access_spec_justice.append(line)
        if line.startswith("afh "):
            line = line.replace("afh ", "")
            line = line.strip()
            access_full_health.append(line)
        if line.startswith("ash "):
            line = line.replace("ash ", "")
            line = line.strip()
            access_spec_health.append(line)
        if line.startswith("afd "):
            line = line.replace("afd ", "")
            line = line.strip()
            access_full_defense.append(line)
        if line.startswith("asd "):
            line = line.replace("asd ", "")
            line = line.strip()
            access_spec_defense.append(line)
        if line.startswith("afm "):
            line = line.replace("afm ", "")
            line = line.strip()
            access_full_media.append(line)
        if line.startswith("asm "):
            line = line.replace("asm ", "")
            line = line.strip()
            access_spec_media.append(line)
        if line.startswith("gsv "):
            line = line.replace("gsv ", "").replace("\n", "")
            global gsv
            gsv = line
        if line.startswith("gcv "):
            line = line.replace("gcv ", "").replace("\n", "")
            global gcv
            gcv = line
        if line.startswith("st "):
            line = line.replace("st ", "").replace("\n", "")
            global st
            st = line
        if line.startswith("judge "):
            line = line.replace("judge ", "").replace("\n", "")
            global judge
            judge = line
        if line.startswith("guber "):
            line = line.replace("guber ", "").replace("\n", "")
            global guber
            guber = line
        if line.startswith("gp "):
            line = line.replace("gp ", "").replace("\n", "")
            global gp
            gp = line
        if line.startswith("gcl "):
            line = line.replace("gcl ", "").replace("\n", "")
            global gcl
            gcl = line
        if line.startswith("stk "):
            line = line.replace("stk ", "").replace("\n", "")
            global stk
            stk = line
        if line.startswith("cb "):
            line = line.replace("cb ", "").replace("\n", "")
            global cb
            cb = line
        if line.startswith("lspd "):
            line = line.replace("lspd ", "").replace("\n", "")
            global lspd
            lspd = line
        if line.startswith("sfpd "):
            line = line.replace("sfpd ", "").replace("\n", "")
            global sfpd
            sfpd = line
        if line.startswith("rcsd "):
            line = line.replace("rcsd ", "").replace("\n", "")
            global rcsd
            rcsd = line
        if line.startswith("swat "):
            line = line.replace("swat ", "").replace("\n", "")
            global swat
            swat = line
        if line.startswith("fbi "):
            line = line.replace("fbi ", "").replace("\n", "")
            global fbi
            fbi = line
        if line.startswith("lsmc "):
            line = line.replace("lsmc ", "").replace("\n", "")
            global lsmc
            lsmc = line
        if line.startswith("sfmc "):
            line = line.replace("sfmc ", "").replace("\n", "")
            global sfmc
            sfmc = line
        if line.startswith("lvmc "):
            line = line.replace("lvmc ", "").replace("\n", "")
            global lvmc
            lvmc = line
        if line.startswith("lsa "):
            line = line.replace("lsa ", "").replace("\n", "")
            global lsa
            lsa = line
        if line.startswith("sfa "):
            line = line.replace("sfa ", "").replace("\n", "")
            global sfa
            sfa = line
        if line.startswith("msp "):
            line = line.replace("msp ", "").replace("\n", "")
            global msp
            msp = line
        if line.startswith("rls "):
            line = line.replace("rls ", "").replace("\n", "")
            global rls
            rls = line
        if line.startswith("rsf "):
            line = line.replace("rsf ", "").replace("\n", "")
            global rsf
            rsf = line
        if line.startswith("rlv "):
            line = line.replace("rlv ", "").replace("\n", "")
            global rlv
            rlv = line
    file.close()

loadVariables()




accesses = access_full + access_full_government + access_spec_government + access_full_co + access_spec_co + access_full_justice + access_spec_justice + access_full_health + access_spec_health + access_full_defense + access_spec_defense + access_full_media + access_spec_media
accesses_full = access_full + access_full_government + access_full_co + access_full_justice + access_full_health + access_full_defense + access_full_media

statuses_menu_organizations = ["menu gcl", "menu stk", "menu cb", "menu lspd", "menu sfpd", "menu swat", "menu fbi", "menu rcsd", "menu lsmc", "menu sfmc", "menu lvmc", "menu lsa", "menu sfa", "menu msp", "menu rls", "menu rsf", "menu rlv"]


def check_status(status):
    for string in statuses_menu_organizations:
        if string == str(status):
            return True
    return False



def check_access(user_id, list):
    for id in list:
        if str(id).strip() == str(user_id).strip():
            return True
    return False


def sender(text, id, keyboard=None):
    if keyboard != None:
        vk_session.method("messages.send",
                          {"user_id": id, "message": text, "random_id": 0, "keyboard": keyboard.get_keyboard()})
    else:
        vk_session.method("messages.send", {"user_id": id, "message": text, "random_id": 0})


def send_noaccess_message(id, isAuth=True):
    if isAuth:
        sender(
            "Отказано в доступе! Вы не являетесь следящим за данным министерством! Если это не так, то отпишите @id342420933(Жене Ветрову) для получения доступа!",
            int(id))
    else:
        sender(
            "Отказано в доступе! Если вы являетесь следящим за гос. структурой, то отпишите @id342420933(Жене Ветрову) для получения доступа!",
            int(id))


def chat_sender(text, id):
    vk_session.method("messages.send", {"chat_id": id, "message": text, "random_id": 0})


def getMainKeyboard():
    status = "main"
    keyboard = VkKeyboard()
    keyboard.add_button("Меню Пра-Во", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню ЦА", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню МЮ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню МЗ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню МО", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню СМИ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню настройки", VkKeyboardColor.PRIMARY)
    return keyboard


def getGovernmentKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню предов", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Меню выговоров", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Позвать всех в игру!", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getGovernmentPredsKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Пред ГСВ", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Пред ГКВ", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Пред СТ", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Пред Судье", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Пред Губернатору", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Пред ГП", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getGovernmentVigsKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Выговор ГСВ", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Выговор ГКВ", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Выговор СТ", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Выговор Судье", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Выговор Губернатору", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Выговор ГП", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getCoKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню ГЦЛ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню СтК", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню ЦБ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Позвать всех в игру!", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getJusticeKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню ЛСПД", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню СФПД", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню СВАТ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню РКШД", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню ФБР", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Позвать всех в игру!", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getHealthKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню ЛСМЦ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню СФМЦ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню ЛВМЦ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Позвать всех в игру!", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getDefenseKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню ЛСа", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню СФа", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню ТСР", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Позвать всех в игру!", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getMediaKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Меню СМИ ЛС", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Меню СМИ СФ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Меню СМИ ЛВ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Позвать всех в игру!", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getOrgKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Выдача преда", VkKeyboardColor.NEGATIVE)
    keyboard.add_button("Выдача выговора", VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button("Выдача нормы", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Выдача нормы дискорда", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Сообщение в орг. беседу", VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getPunishKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getSettingsKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Поставить лидера", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Снять лидера", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Поставить следящего", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Снять следящего", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Поставить ГСа или ЗГСа", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Снять ГСа или ЗГСа", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getSettingsLeaderKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("Пра-во", VkKeyboardColor.PRIMARY)
    keyboard.add_button("ЦА", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("МЮ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("МЗ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("МО", VkKeyboardColor.PRIMARY)
    keyboard.add_button("СМИ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getGovernmentSettingsKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("ГСВ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("ГКВ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("СТ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("Судья", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Губернатор", VkKeyboardColor.PRIMARY)
    keyboard.add_button("ГП", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getCoSettingsKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("ГЦЛ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("СтК", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("ЦБ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getJusticeSettingsKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("ЛСПД", VkKeyboardColor.PRIMARY)
    keyboard.add_button("СФПД", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("РКШД", VkKeyboardColor.PRIMARY)
    keyboard.add_button("СВАТ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("ФБР", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getHealthSettingsKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("ЛСМЦ", VkKeyboardColor.PRIMARY)
    keyboard.add_button("СФМЦ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("ЛВМЦ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getDefenceSettingsKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("ЛСа", VkKeyboardColor.PRIMARY)
    keyboard.add_button("ВМС", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("ТСР", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getMediaSettingsKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("СМИ ЛС", VkKeyboardColor.PRIMARY)
    keyboard.add_button("СМИ СФ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("СМИ ЛВ", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard

def getChoosingAccessKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button("ГСа", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("ЗГСа", VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button("Обратно", VkKeyboardColor.PRIMARY)
    return keyboard


def getKeyboardByStatus():
    if status == "main":
        return getMainKeyboard()
    elif status == "menu government":
        return getGovernmentKeyboard()
    elif status == "menu co":
        return getCoKeyboard()
    elif status == "menu justice":
        return getJusticeKeyboard()
    elif status == "menu health":
        return getHealthKeyboard()
    elif status == "menu defense":
        return getDefenseKeyboard()
    elif status == "menu media":
        return getMediaKeyboard()
    elif status == "settings":
        return getSettingsKeyboard()
    elif "settings government" in status:
        return getGovernmentSettingsKeyboard()
    elif "settings co" in status:
        return  getCoSettingsKeyboard()
    elif "settings justice" in status:
        return getJusticeSettingsKeyboard()
    elif "settings health" in status:
        return getHealthSettingsKeyboard()
    elif "settings defence" in status:
        return getDefenceSettingsKeyboard()
    elif "settings media" in status:
        return getMediaSettingsKeyboard()
    elif "choosing access" in status or "choosing set" in status:
        return getChoosingAccessKeyboard()
    elif check_status(status):
        return getOrgKeyboard()
    elif status == "pred government":
        return getGovernmentPredsKeyboard()
    elif status == "vig government":
        return getGovernmentVigsKeyboard()
    elif status.startswith("pred") or status.startswith("vig") or status.startswith("waiting") or status.startswith("set gs") or status.startswith("set zgs"):
        return getPunishKeyboard()
    elif status == "set leader" or status == "del leader" or status == "set spectator" or status == "del spectator" or status == "set full spectator" or status == "del full spectator":
        return getSettingsLeaderKeyboard()


def makePunish(in_status, isPred, msg, id):
    target = getTarget(in_status)
    if isPred:
        chat_sender(target + ", +предупреждение за " + msg, 1)
        log("@id" + str(id) + "(Администратор) выдал предупреждение " + target + " за " + msg)
    else:
        chat_sender(target + ", +выговор за " + msg, 1)
        log("@id" + str(id) + "(Администратор) выдал выговор " + target + " за " + msg)



def getTarget(status):
    target = ""
    if "gcv" in status:
        target = gcv
    elif "gsv" in status:
        target = gsv
    elif "stk" in status:
        target = stk
    elif "judge" in status:
        target = judge
    elif "guber" in status:
        target = guber
    elif "gp" in status:
        target = gp
    elif "gcl" in status:
        target = gcl
    elif "st" in status:
        target = st
    elif "cb" in status:
        target = cb
    elif "lspd" in status:
        target = lspd
    elif "sfpd" in status:
        target = sfpd
    elif "swat" in status:
        target = swat
    elif "rcsd" in status:
        target = rcsd
    elif "fbi" in status:
        target = fbi
    elif "lsmc" in status:
        target = lsmc
    elif "sfmc" in status:
        target = sfmc
    elif "lvmc" in status:
        target = lvmc
    elif "lsa" in status:
        target = lsa
    elif "sfa" in status:
        target = sfa
    elif "msp" in status:
        target = msp
    elif "rls" in status:
        target = rls
    elif "rsf" in status:
        target = rsf
    elif "rlv" in status:
        target = rlv
    return target

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_chat:
                    id = event.chat_id
                    msg = event.object.message["text"]
                else:
                    id = event.object.message["from_id"]
                    message = event.object.message["text"]
                    msg = message.lower()
                    if msg == "обновить":
                        status = "main"
                        sender("Бот успешно обновил свою работу!", id, getKeyboardByStatus())
                    if check_access(id, accesses):
                        if msg == "откат":
                            status = "main"
                            sender("Работаем", id, getKeyboardByStatus())
                        if status == "main":
                            if msg == "меню пра-во":
                                if check_access(id, access_full_government) or check_access(id,
                                                                                            access_spec_government) or check_access(
                                        id, access_full):
                                    status = "menu government"
                                    sender("Перехожу в ваше меню", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "меню ца":
                                if check_access(id, access_full_co) or check_access(id, access_spec_co) or check_access(
                                        id, access_full):
                                    status = "menu co"
                                    sender("Перехожу в ваше меню", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "меню мю":
                                if check_access(id, access_full_justice) or check_access(id,
                                                                                          access_spec_justice) or check_access(
                                        id, access_full):
                                    status = "menu justice"
                                    sender("Перехожу в ваше меню", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "меню мз":
                                if check_access(id, access_full_health) or check_access(id,
                                                                                        access_spec_health) or check_access(
                                        id, access_full):
                                    status = "menu health"
                                    sender("Перехожу в ваше меню", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "меню мо":
                                if check_access(id, access_full_defense) or check_access(id,
                                                                                         access_spec_defense) or check_access(
                                        id, access_full):
                                    status = "menu defense"
                                    sender("Перехожу в ваше меню", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "меню сми":
                                if check_access(id, access_full_media) or check_access(id,
                                                                                       access_spec_media) or check_access(
                                        id, access_full):
                                    status = "menu media"
                                    sender("Перехожу в ваше меню", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "меню настройки":
                                if check_access(id, access_dev) or check_access(id, accesses_full) or check_access(accesses_full):
                                    status = "settings"
                                    sender("Перехожу в меню настроек", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав! Чтобы получить доступ отпишите @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                        elif status == "menu government":
                            if msg == "обратно":
                                status = "main"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                            elif msg == "позвать всех в игру!":
                                chat_sender("@all, В ИГРУ!", 1)
                                sender("Позвал", id, getKeyboardByStatus())
                            elif msg == "меню предов":
                                status = "pred government"
                                sender("Перехожу в меню предов", id, getKeyboardByStatus())
                            elif msg == "меню выговоров":
                                status = "vig government"
                                sender("Перехожу в меню выговоров", id, getKeyboardByStatus())
                        elif status == "menu co":
                            if msg == "меню гцл":
                                status = "menu gcl"
                                sender("Переходим в меню ГЦЛ", id, getKeyboardByStatus())
                            elif msg == "меню стк":
                                status = "menu stk"
                                sender("Переходим в меню СтК", id, getKeyboardByStatus())
                            elif msg == "меню цб":
                                status = "menu cb"
                                sender("Переходим в меню ЦБ", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "main"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                            elif msg == "позвать всех в игру!":
                                chat_sender("@all, В ИГРУ!", 1)
                                sender("Позвал", id, getKeyboardByStatus())
                        elif status == "menu justice":
                            if msg == "меню лспд":
                                status = "menu lspd"
                                sender("Переходим в меню ЛСПД", id, getKeyboardByStatus())
                            elif msg == "меню сфпд":
                                status = "menu sfpd"
                                sender("Переходим в меню СФПД", id, getKeyboardByStatus())
                            elif msg == "меню сват":
                                status = "menu swat"
                                sender("Переходим в меню СВАТ", id, getKeyboardByStatus())
                            elif msg == "меню фбр":
                                status = "menu fbi"
                                sender("Переходим в меню ФБР", id, getKeyboardByStatus())
                            elif msg == "меню ркшд":
                                status = "menu rcsd"
                                sender("Переходим в меню РКШД", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "main"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            elif msg == "позвать всех в игру!":
                                chat_sender("@all, В ИГРУ!", 1)
                                sender("Позвал", id, getKeyboardByStatus())
                        elif status == "menu health":
                            if msg == "меню лсмц":
                                status = "menu lsmc"
                                sender("Переходим в меню ЛСМЦ!", id, getKeyboardByStatus())
                            elif msg == "меню сфмц":
                                status = "menu sfmc"
                                sender("Переходим в меню СФМЦ!", id, getKeyboardByStatus())
                            elif msg == "меню лвмц":
                                status = "menu lvmc"
                                sender("Переходим в меню ЛВМЦ", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "main"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            elif msg == "позвать всех в игру!":
                                chat_sender("@all, В ИГРУ!", 1)
                                sender("Позвал", id, getKeyboardByStatus())
                        elif status == "menu defense":
                            if msg == "меню лса":
                                status = "menu lsa"
                                sender("Переходим в меню ЛСа", id, getKeyboardByStatus())
                            elif msg == "меню сфа":
                                status = "menu sfa"
                                sender("Переходим в меню СФа", id, getKeyboardByStatus())
                            elif msg == "меню тср":
                                status = "menu msp"
                                sender("Переходим в меню ТСР", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "main"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            elif msg == "позвать всех в игру!":
                                chat_sender("@all, В ИГРУ!", 1)
                                sender("Позвал", id, getKeyboardByStatus())
                        elif status == "menu media":
                            if msg == "меню сми лс":
                                status = "menu rls"
                                sender("Переходим в меню СМИ ЛС", id, getKeyboardByStatus())
                            elif msg == "меню сми сф":
                                status = "menu rsf"
                                sender("Переходим в меню СМИ СФ", id, getKeyboardByStatus())
                            elif msg == "меню сми лв":
                                status = "menu rlv"
                                sender("Переходим в меню СМИ ЛВ", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "main"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            elif msg == "позвать всех в игру!":
                                chat_sender("@all, В ИГРУ!", 1)
                                sender("Позвал", id, getKeyboardByStatus())
                        elif status == "pred government":
                            if msg == "пред гсв":
                                status = "pred gsv"
                                sender("Идем давать пред ГСВ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "пред гкв":
                                status = "pred gcv"
                                sender("Идем давать пред ГКВ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "пред ст":
                                status = "pred st"
                                sender("Идем давать пред СТ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "пред судье":
                                status = "pred judge"
                                sender("Идем давать пред Судье", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "пред губернатору":
                                status = "pred guber"
                                sender("Идем давать пред Губернатору", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "пред гп":
                                status = "pred gp"
                                sender("Идем давать пред ГП", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu government"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                        elif status == "vig government":
                            if msg == "выговор гсв":
                                status = "vig gsv"
                                sender("Идем давать выговор ГСВ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выговор гкв":
                                status = "vig gcv"
                                sender("Идем давать выговор ГКВ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выговор ст":
                                status = "vig st"
                                sender("Идем давать выговор СТ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выговор судье":
                                status = "vig judge"
                                sender("Идем давать выговор Судье", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выговор губернатору":
                                status = "vig guber"
                                sender("Идем давать выговор Губернатору", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выговор гп":
                                status = "vig gp"
                                sender("Идем давать выговор ГП", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu government"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                        elif status == "menu gcl":
                            if msg == "выдача преда":
                                status = "pred gcl"
                                sender("Идем давать пред ГЦЛ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig gcl"
                                sender("Идем давать выговор ГЦЛ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(gcl + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС", 1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + gcl)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(gcl + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС", 1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + gcl)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg gcl"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu co"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu stk":
                            if msg == "выдача преда":
                                status = "pred stk"
                                sender("Идем давать пред СтК", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig stk"
                                sender("Идем давать выговор СтК", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(stk + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС", 1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + stk)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(stk + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС", 1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + stk)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg stk"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu co"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu cb":
                            if msg == "выдача преда":
                                status = "pred cb"
                                sender("Идем давать пред ЦБ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig cb"
                                sender("Идем давать выговор ЦБ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(cb + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС", 1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + cb)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(cb + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС", 1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + cb)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg cb"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu co"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu lspd":
                            if msg == "выдача преда":
                                status = "pred lspd"
                                sender("Идем давать пред ЛСПД", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig lspd"
                                sender("Идем давать выговор ЛСПД", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(lspd + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + lspd)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(lspd + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + lspd)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg lspd"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu justice"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu sfpd":
                            if msg == "выдача преда":
                                status = "pred sfpd"
                                sender("Идем давать пред СФПД", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig sfpd"
                                sender("Идем давать выговор СФПД", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(sfpd + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + sfpd)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(sfpd + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + sfpd)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg sfpd"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu justice"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu rcsd":
                            if msg == "выдача преда":
                                status = "pred rcsd"
                                sender("Идем давать пред РКШД", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig rcsd"
                                sender("Идем давать выговор РКШД", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(rcsd + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + rcsd)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(rcsd + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + rcsd)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg rcsd"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu justice"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu swat":
                            if msg == "выдача преда":
                                status = "pred swat"
                                sender("Идем давать пред СВАТ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig swat"
                                sender("Идем давать выговор СВАТ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(swat + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + swat)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(swat + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + swat)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg swat"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu justice"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu fbi":
                            if msg == "выдача преда":
                                status = "pred fbi"
                                sender("Идем давать пред ФБР", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig fbi"
                                sender("Идем давать выговор ФБР", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(fbi + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + fbi)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(fbi + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + fbi)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg fbi"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu justice"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu lsmc":
                            if msg == "выдача преда":
                                status = "pred lsmc"
                                sender("Идем давать пред ЛСМЦ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig lsmc"
                                sender("Идем давать выговор ЛСМЦ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(lsmc + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + lsmc)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(lsmc + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + lsmc)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg lsmc"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu health"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu sfmc":
                            if msg == "выдача преда":
                                status = "pred sfmc"
                                sender("Идем давать пред СФМЦ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig sfmc"
                                sender("Идем давать выговор СФМЦ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(sfmc + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + sfmc)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(sfmc + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + sfmc)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg sfmc"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu health"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu lvmc":
                            if msg == "выдача преда":
                                status = "pred lvmc"
                                sender("Идем давать пред ЛВМЦ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig lvmc"
                                sender("Идем давать выговор ЛВМЦ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(lvmc + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + lvmc)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(lvmc + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + lvmc)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg lvmc"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu health"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu lsa":
                            if msg == "выдача преда":
                                status = "pred lsa"
                                sender("Идем давать пред ЛСа", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig lsa"
                                sender("Идем давать выговор ЛСа", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(lsa + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + lsa)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(lsa + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + lsa)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg lsa"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu defense"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu sfa":
                            if msg == "выдача преда":
                                status = "pred sfa"
                                sender("Идем давать пред ВМС", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig sfa"
                                sender("Идем давать выговор ВМС", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(sfa + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + sfa)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(sfa + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + sfa)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg sfa"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu defense"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu msp":
                            if msg == "выдача преда":
                                status = "pred msp"
                                sender("Идем давать пред ТСР", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig msp"
                                sender("Идем давать выговор ТСР", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(msp + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + msp)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(msp + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + msp)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg lsa"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu defense"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu rls":
                            if msg == "выдача преда":
                                status = "pred rls"
                                sender("Идем давать пред СМИ ЛС", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig rls"
                                sender("Идем давать выговор СМИ ЛС", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(rls + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + rls)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(rls + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + rls)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg rls"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu media"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu rsf":
                            if msg == "выдача преда":
                                status = "pred rsf"
                                sender("Идем давать пред СМИ СФ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig rsf"
                                sender("Идем давать выговор СМИ СФ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(rsf + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + rsf)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(rsf + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + rsf)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg rsf"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu media"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "menu rlv":
                            if msg == "выдача преда":
                                status = "pred rlv"
                                sender("Идем давать пред СМИ ЛВ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За...)", id, getKeyboardByStatus())
                            elif msg == "выдача выговора":
                                status = "vig rlv"
                                sender("Идем давать выговор СМИ ЛВ", id, getKeyboardByStatus())
                                sender("За что вы хотите дать наказание?(За ...)", id, getKeyboardByStatus())
                            elif msg == "выдача нормы":
                                chat_sender(rlv + ", 120 минут на поднятие нормы онлайна. По истечении срока скриншот попыток или /members следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму онлайна " + rlv)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "выдача нормы дискорда":
                                chat_sender(rlv + ", 120 минут на поднятие нормы онлайна в дискорде. По истечении срока скриншот попыток или дискорд канала следящим в ЛС",1)
                                log("@id" + str(id) + "(Администратор) выдал норму дискорда " + rlv)
                                sender("Выдал норму!", id, getKeyboardByStatus())
                            elif msg == "сообщение в орг. беседу":
                                status = "msg rlv"
                                sender("Какое сообщение вы хотите отправить?", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "menu media"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif "pred" in status:
                            if msg != "обратно":
                                makePunish(status, True, msg, id)
                                status = status.replace("pred", "menu").replace("gcv", "government").replace("gsv", "government").replace("judge", "government").replace("guber", "government").replace("gp", "government")
                                if not ("stk" in status) and "st" in status:
                                    status = status.replace("st", "government")
                                sender("Выдано!", id, getKeyboardByStatus())
                            else:
                                status = status.replace("pred", "menu").replace("gcv", "government").replace("gsv", "government").replace("judge", "government").replace("guber", "government").replace("gp", "government")
                                if not ("stk" in status) and "st" in status:
                                    status = status.replace("st", "government")
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif "vig" in status:
                            if msg != "обратно":
                                makePunish(status, False, msg, id)
                                status = status.replace("vig", "menu").replace("gcv", "government").replace("gsv", "government").replace("judge", "government").replace("guber", "government").replace("gp", "government")
                                if not ("stk" in status) and "st" in status:
                                    status = status.replace("st", "government")
                                sender("Выдано!", id, getKeyboardByStatus())
                            else:
                                status = status.replace("vig", "menu").replace("gcv", "government").replace("gsv", "government").replace("judge", "government").replace("guber", "government").replace("gp", "government")
                                if not ("stk" in status) and "st" in status:
                                    status = status.replace("st", "government")
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "settings":
                            if msg == "поставить лидера":
                                status = "set leader"
                                sender("Идем ставить лидера!", id, getKeyboardByStatus())
                            elif msg == "снять лидера":
                                status = "del leader"
                                sender("Идем снимать лидера!", id, getKeyboardByStatus())
                            elif msg == "поставить следящего":
                                status = "set spectator"
                                sender("Идем ставить следящего!", id, getKeyboardByStatus())
                            elif msg == "снять следящего":
                                status = "del spectator"
                                sender("Идем снимать следящего!", id, getKeyboardByStatus())
                            elif msg == "поставить гса или згса":
                                if check_access(id, access_dev) or check_access(id, access_full):
                                    status = "set full spectator"
                                    sender("Идем ставить ГСа/ЗГСа!", id, getKeyboardByStatus())
                            elif msg == "снять гса или згса":
                                if check_access(id, access_dev) or check_access(id, access_full):
                                    status = "del full spectator"
                                    sender("Идем снимать ГСа/ЗГСа!", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "main"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "set leader":
                            if msg == "пра-во":
                                if check_access(id, access_full) or check_access(id, access_full_government):
                                    status = "set settings government"
                                    sender("Переходим в меню настроек лидеров правительства!", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав доступа! За получением прав обратитесь к @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                            elif msg == "ца":
                                if check_access(id, access_full) or check_access(id, access_full_co):
                                    status = "set settings co"
                                    sender("Переходим в меню настроек лидеров ЦА!", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав доступа! За получением прав обратитесь к @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                            elif msg == "мю":
                                if check_access(id, access_full) or check_access(id, access_full_justice):
                                    status = "set settings justice"
                                    sender("Переходим в меню настроек лидеров МЮ!", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав доступа! За получением прав обратитесь к @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                            elif msg == "мз":
                                if check_access(id, access_full) or check_access(id, access_full_health):
                                    status = "set settings health"
                                    sender("Переходим в меню настроек лидеров МЗ!", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав доступа! За получением прав обратитесь к @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                            elif msg == "мо":
                                if check_access(id, access_full) or check_access(id, access_full_defense):
                                    status = "set settings defence"
                                    sender("Переходим в меню настроек лидеров МО!", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав доступа! За получением прав обратитесь к @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                            elif msg == "сми":
                                if check_access(id, access_full) or check_access(id, access_full_media):
                                    status = "set settings media"
                                    sender("Переходим в меню настроек лидеров СМИ!", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав доступа! За получением прав обратитесь к @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "settings"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "del leader":
                            if msg == "пра-во":
                                if check_access(id, access_full) or check_access(id, access_full_government):
                                    status = "del settings government"
                                    sender("Переходим в меню настроек лидеров правительства!", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав доступа! За получением прав обратитесь к @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                            elif msg == "ца":
                                if check_access(id, access_full) or check_access(id, access_full_co):
                                    status = "del settings co"
                                    sender("Переходим в меню настроек лидеров ЦА!", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав доступа! За получением прав обратитесь к @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                            elif msg == "мю":
                                if check_access(id, access_full) or check_access(id, access_full_justice):
                                    status = "del settings justice"
                                    sender("Переходим в меню настроек лидеров МЮ!", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав доступа! За получением прав обратитесь к @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                            elif msg == "мз":
                                if check_access(id, access_full) or check_access(id, access_full_health):
                                    status = "del settings health"
                                    sender("Переходим в меню настроек лидеров МЗ!", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав доступа! За получением прав обратитесь к @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                            elif msg == "мо":
                                if check_access(id, access_full) or check_access(id, access_full_defense):
                                    status = "del settings defence"
                                    sender("Переходим в меню настроек лидеров МО!", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав доступа! За получением прав обратитесь к @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                            elif msg == "сми":
                                if check_access(id, access_full) or check_access(id, access_full_media):
                                    status = "del settings media"
                                    sender("Переходим в меню настроек лидеров СМИ!", id, getKeyboardByStatus())
                                else:
                                    sender("У вас недостаточно прав доступа! За получением прав обратитесь к @zhenya_bruna(Жене Ветрову)", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "settings"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "set settings government":
                            if msg == "гсв":
                                status = "waiting gsv"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "гкв":
                                status = "waiting gcv"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "ст":
                                status = "waiting st"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "судья":
                                status = "waiting judge"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "губернатор":
                                status = "waiting guber"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "гп":
                                status = "waiting gp"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "set leader"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "set settings co":
                            if msg == "гцл":
                                status = "waiting gcl"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "стк":
                                status = "waiting stk"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "цб":
                                status = "waiting cb"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "set leader"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "set settings justice":
                            if msg == "лспд":
                                status = "waiting lspd"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "сфпд":
                                status = "waiting sfpd"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "ркшд":
                                status = "waiting rcsd"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "сват":
                                status = "waiting swat"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "фбр":
                                status = "waiting fbi"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "set leader"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "set settings health":
                            if msg == "лсмц":
                                status = "waiting lsmc"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "сфмц":
                                status = "waiting sfmc"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "лвмц":
                                status = "waiting lvmc"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "set leader"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "set settings defence":
                            if msg == "лса":
                                status = "waiting lsa"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "вмс":
                                status = "waiting sfa"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "тср":
                                status = "waiting msp"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "set leader"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "set settings media":
                            if msg == "сми лс":
                                status = "waiting rls"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "сми сф":
                                status = "waiting rsf"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "сми лв":
                                status = "waiting rlv"
                                sender("Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "set leader"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "del settings government":
                            if msg == "гсв":
                                log("@id" + str(id) + "(Администратор) снял с должности " + gsv)
                                gsv = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "гкв":
                                log("@id" + str(id) + "(Администратор) снял с должности " + gcv)
                                gcv = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "ст":
                                log("@id" + str(id) + "(Администратор) снял с должности " + st)
                                st = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "судья":
                                log("@id" + str(id) + "(Администратор) снял с должности " + judge)
                                judge = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "губернатор":
                                log("@id" + str(id) + "(Администратор) снял с должности " + guber)
                                guber = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "гп":
                                log("@id" + str(id) + "(Администратор) снял с должности " + gp)
                                gp = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "обратно":
                                status = "del leader"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "del settings co":
                            if msg == "гцл":
                                log("@id" + str(id) + "(Администратор) снял с должности " + gcl)
                                gcl = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "стк":
                                log("@id" + str(id) + "(Администратор) снял с должности " + stk)
                                stk = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "цб":
                                log("@id" + str(id) + "(Администратор) снял с должности " + cb)
                                cb = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "обратно":
                                status = "del leader"
                                sender("Возращаемся назад!", id, getKeyboardByStatus())
                        elif status == "del settings justice":
                            if msg == "лспд":
                                log("@id" + str(id) + "(Администратор) снял с должности " + lspd)
                                lspd = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "сфпд":
                                log("@id" + str(id) + "(Администратор) снял с должности " + sfpd)
                                sfpd = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "ркшд":
                                log("@id" + str(id) + "(Администратор) снял с должности " + rcsd)
                                rcsd = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "сват":
                                log("@id" + str(id) + "(Администратор) снял с должности " + swat)
                                swat = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "фбр":
                                log("@id" + str(id) + "(Администратор) снял с должности " + fbi)
                                fbi = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "обратно":
                                status = "del leader"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "del settings health":
                            if msg == "лсмц":
                                log("@id" + str(id) + "(Администратор) снял с должности " + lsmc)
                                lsmc = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "сфмц":
                                log("@id" + str(id) + "(Администратор) снял с должности " + sfmc)
                                sfmc = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "лвмц":
                                log("@id" + str(id) + "(Администратор) снял с должности " + lvmc)
                                lvmc = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "обратно":
                                status = "del leader"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "del settings defence":
                            if msg == "лса":
                                log("@id" + str(id) + "(Администратор) снял с должности " + lsa)
                                lsa = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "вмс":
                                log("@id" + str(id) + "(Администратор) снял с должности " + sfa)
                                sfa = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "тср":
                                log("@id" + str(id) + "(Администратор) снял с должности " + msp)
                                msp = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "обратно":
                                status = "del leader"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "del settings media":
                            if msg == "сми лс":
                                log("@id" + str(id) + "(Администратор) снял с должности " + rls)
                                rls = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "сми сф":
                                log("@id" + str(id) + "(Администратор) снял с должности " + rsf)
                                rsf = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "сми лв":
                                log("@id" + str(id) + "(Администратор) снял с должности " + rlv)
                                rlv = "Снят"
                                sender("Лидер успешно снят!", id, getKeyboardByStatus())
                                saveVariables()
                            elif msg == "обратно":
                                status = "del leader"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "waiting gsv":
                            if "@" in msg:
                                gsv = getFunctionalVkId(msg) + "(ГСВ)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + gsv)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings government"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting gcv":
                            if "@" in msg:
                                gcv = getFunctionalVkId(msg) + "(ГКВ)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + gcv)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings government"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting st":
                            if "@" in msg:
                                st = getFunctionalVkId(msg) + "(СТ)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + st)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings government"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting judge":
                            if "@" in msg:
                                judge = getFunctionalVkId(msg) + "(Судья)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + judge)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings government"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting guber":
                            if "@" in msg:
                                guber = getFunctionalVkId(msg) + "(Губернатор)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + guber.replace("Губернатор", "Губернатора"))
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings government"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting gp":
                            if "@" in msg:
                                gp = getFunctionalVkId(msg) + "(ГП)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + gp)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings government"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting gcl":
                            if "@" in msg:
                                gcl = getFunctionalVkId(msg) + "(ГЦЛ)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + gcl)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings co"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting stk":
                            if "@" in msg:
                                stk = getFunctionalVkId(msg) + "(СтК)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + stk)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings co"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting cb":
                            if "@" in msg:
                                cb = getFunctionalVkId(msg) + "(ЦБ)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + cb)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings co"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting lspd":
                            if "@" in msg:
                                lspd = getFunctionalVkId(msg) + "(ЛСПД)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + lspd)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings justice"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting sfpd":
                            if "@" in msg:
                                sfpd = getFunctionalVkId(msg) + "(СФПД)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + sfpd)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings justice"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting rcsd":
                            if "@" in msg:
                                rcsd = getFunctionalVkId(msg) + "(РКШД)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + rcsd)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings justice"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting swat":
                            if "@" in msg:
                                swat = getFunctionalVkId(msg) + "(СВАТ)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + swat)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings justice"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting fbi":
                            if "@" in msg:
                                fbi = getFunctionalVkId(msg) + "(ФБР)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + fbi)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings justice"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting lsmc":
                            if "@" in msg:
                                lsmc = getFunctionalVkId(msg) + "(ЛСМЦ)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + lsmc)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings health"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting sfmc":
                            if "@" in msg:
                                sfmc = getFunctionalVkId(msg) + "(СФМЦ)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + sfmc)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings health"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting lvmc":
                            if "@" in msg:
                                lvmc = getFunctionalVkId(msg) + "(ЛВМЦ)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + lvmc)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings health"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting lsa":
                            if "@" in msg:
                                lsa = getFunctionalVkId(msg) + "(ЛСа)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + lsa)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings defence"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting sfa":
                            if "@" in msg:
                                sfa = getFunctionalVkId(msg) + "(ВМС)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + sfa)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings defence"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting msp":
                            if "@" in msg:
                                msp = getFunctionalVkId(msg) + "(ТСР)"
                                log("@id" + str(id) + "(Администратор) поставил на должность " + msp)
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings defence"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting rls":
                            if "@" in msg:
                                rls = getFunctionalVkId(msg) + "(СМИ ЛС)"
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings media"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id,
                                           getKeyboardByStatus())
                        elif status == "waiting rsf":
                            if "@" in msg:
                                rsf = getFunctionalVkId(msg) + "(СМИ СФ)"
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings media"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "waiting rlv":
                            if "@" in msg:
                                rlv = getFunctionalVkId(msg) + "(СМИ ЛВ)"
                                saveVariables()
                                sender("Лидер успешно поставлен!", id, getKeyboardByStatus())
                            else:
                                if msg == "обратно":
                                    status = "set settings media"
                                    sender("Возращаемся назад!", id, getKeyboardByStatus())
                                else:
                                    sender("Ошибка! Отправьте ссылку на нового лидера в формате @vk_id", id, getKeyboardByStatus())
                        elif status == "del full spectator":
                            if msg == "пра-во":
                                status = "choosing access government"
                                sender("Выберите: ГСа или ЗГСа", id, getKeyboardByStatus())
                            elif msg == "ца":
                                status = "choosing access co"
                                sender("Выберите: ГСа или ЗГСа", id, getKeyboardByStatus())
                            elif msg == "мю":
                                status = "choosing access justice"
                                sender("Выберите: ГСа или ЗГСа", id, getKeyboardByStatus())
                            elif msg == "мз":
                                status = "choosing access health"
                                sender("Выберите: ГСа или ЗГСа", id, getKeyboardByStatus())
                            elif msg == "мо":
                                status = "choosing access defence"
                                sender("Выберите: ГСа или ЗГСа", id, getKeyboardByStatus())
                            elif msg == "сми":
                                status = "choosing access media"
                                sender("Выберите: ГСа или ЗГСа", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "settings"
                                sender("Возращаемся обратно", id, getKeyboardByStatus())
                        elif status == "choosing access government":
                            if msg == "гса":
                                sender(
                                    "Вас сняли с должности ГСа Пра-во!  Напишите \"Обновить\", чтоб бот продолжил работу",
                                    int(access_full_government[0]), getMainKeyboard())
                                log("@id" + str(id) + "(ГС/ЗГС ГОС) снял @id" + access_full_government[0] + "(ГСа Пра-во)")
                                access_full_government[0] = ""
                                saveVariables()
                                sender("Вы успешно сняли ГСа Пра-во", id, getKeyboardByStatus())
                            elif msg == "згса":
                                sender(
                                    "Вас сняли с должности ЗГСа Пра-во!  Напишите \"Обновить\", чтоб бот продолжил работу",
                                    int(access_full_government[1]), getMainKeyboard())
                                log("@id" + str(id) + "(ГС/ЗГС ГОС) снял @id" + access_full_government[1] + "(ЗГСа Пра-во)")
                                access_full_government[1] = ""
                                saveVariables()
                                sender("Вы успешно сняли ЗГСа Пра-во", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "del full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "choosing access co":
                            if msg == "гса":
                                sender(
                                    "Вас сняли с должности ГСа ЦА!  Напишите \"Обновить\", чтоб бот продолжил работу",
                                    int(access_full_co[0]), getMainKeyboard())
                                log("@id" + str(id) + "(ГС/ЗГС ГОС) снял @id" + access_full_co[
                                    0] + "(ГСа ЦА)")
                                access_full_co[0] = ""
                                saveVariables()
                                sender("Вы успешно сняли ГСа ЦА", id, getKeyboardByStatus())
                            elif msg == "згса":
                                sender(
                                    "Вас сняли с должности ЗГСа ЦА!  Напишите \"Обновить\", чтоб бот продолжил работу",
                                    int(access_full_co[1]), getMainKeyboard())
                                log("@id" + str(id) + "(ГС/ЗГС ГОС) снял @id" + access_full_co[
                                    1] + "(ЗГСа ЦА)")
                                access_full_co[1] = ""
                                saveVariables()
                                sender("Вы успешно сняли ЗГСа ЦА", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "del full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "choosing access health":
                            if msg == "гса":
                                sender(
                                    "Вас сняли с должности ГСа МЗ!  Напишите \"Обновить\", чтоб бот продолжил работу",
                                    int(access_full_health[0]), getMainKeyboard())
                                log("@id" + str(id) + "(ГС/ЗГС ГОС) снял @id" + access_full_health[
                                    0] + "(ГСа МЗ)")
                                access_full_health[0] = ""
                                saveVariables()
                                sender("Вы успешно сняли ГСа МЗ", id, getKeyboardByStatus())
                            elif msg == "згса":
                                sender(
                                    "Вас сняли с должности ЗГСа МЗ!  Напишите \"Обновить\", чтоб бот продолжил работу",
                                    int(access_full_health[1]), getMainKeyboard())
                                log("@id" + str(id) + "(ГС/ЗГС ГОС) снял @id" + access_full_health[
                                    1] + "(ЗГСа МЗ)")
                                access_full_health[1] = ""
                                saveVariables()
                                sender("Вы успешно сняли ЗГСа МЗ", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "del full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "choosing access justice":
                            if msg == "гса":
                                sender(
                                    "Вас сняли с должности ГСа МЮ!  Напишите \"Обновить\", чтоб бот продолжил работу",
                                    int(access_full_justice[0]), getMainKeyboard())
                                log("@id" + str(id) + "(ГС/ЗГС ГОС) снял @id" + access_full_justice[
                                    0] + "(ГСа МЮ)")
                                access_full_justice[0] = ""
                                saveVariables()
                                sender("Вы успешно сняли ГСа МЮ", id, getKeyboardByStatus())
                            elif msg == "згса":
                                sender(
                                    "Вас сняли с должности ЗГСа МЮ!  Напишите \"Обновить\", чтоб бот продолжил работу",
                                    int(access_full_justice[1]), getMainKeyboard())
                                log("@id" + str(id) + "(ГС/ЗГС ГОС) снял @id" + access_full_justice[
                                    1] + "(ЗГСа МЮ)")
                                access_full_justice[1] = ""
                                saveVariables()
                                sender("Вы успешно сняли МЮ", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "del full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "choosing access defence":
                            if msg == "гса":
                                sender(
                                    "Вас сняли с должности ГСа МО!  Напишите \"Обновить\", чтоб бот продолжил работу",
                                    int(access_full_defense[0]), getMainKeyboard())
                                log("@id" + str(id) + "(ГС/ЗГС ГОС) снял @id" + access_full_defense[
                                    0] + "(ГСа МО)")
                                access_full_defense[0] = ""
                                saveVariables()
                                sender("Вы успешно сняли ГСа МО", id, getKeyboardByStatus())
                            elif msg == "згса":
                                sender(
                                    "Вас сняли с должности ЗГСа МО!  Напишите \"Обновить\", чтоб бот продолжил работу",
                                    int(access_full_defense[1]), getMainKeyboard())
                                log("@id" + str(id) + "(ГС/ЗГС ГОС) снял @id" + access_full_defense[
                                    1] + "(ЗГСа МО)")
                                access_full_defense[1] = ""
                                saveVariables()
                                sender("Вы успешно сняли МО", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "del full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "choosing access media":
                            if msg == "гса":
                                sender(
                                    "Вас сняли с должности ГСа СМИ!  Напишите \"Обновить\", чтоб бот продолжил работу",
                                    int(access_full_media[0]), getMainKeyboard())
                                log("@id" + str(id) + "(ГС/ЗГС ГОС) снял @id" + access_full_media[
                                    0] + "(ГСа СМИ)")
                                access_full_media[0] = ""
                                saveVariables()
                                sender("Вы успешно сняли ГСа СМИ", id, getKeyboardByStatus())
                            elif msg == "згса":
                                sender(
                                    "Вас сняли с должности ЗГСа СМИ!  Напишите \"Обновить\", чтоб бот продолжил работу",
                                    int(access_full_media[1]), getMainKeyboard())
                                log("@id" + str(id) + "(ГС/ЗГС ГОС) снял @id" + access_full_media[
                                    1] + "(ЗГСа СМИ)")
                                access_full_media[1] = ""
                                saveVariables()
                                sender("Вы успешно сняли ЗГСа СМИ", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "del full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "set spectator":
                            if msg == "пра-во":
                                if check_access(id, access_full) or check_access(id, access_full_government):
                                    status = "waiting set spectator government"
                                    sender("Идем ставить следящего пра-во", id, getKeyboardByStatus())
                                    sender("Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "ца":
                                if check_access(id, access_full) or check_access(id, access_full_co):
                                    status = "waiting set spectator co"
                                    sender("Идем ставить следящего ЦА", id, getKeyboardByStatus())
                                    sender("Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "мю":
                                if check_access(id, access_full) or check_access(id, access_full_justice):
                                    status = "waiting set spectator justice"
                                    sender("Идем ставить следящего МЮ", id, getKeyboardByStatus())
                                    sender("Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "мз":
                                if check_access(id, access_full) or check_access(id, access_full_health):
                                    status = "waiting set spectator health"
                                    sender("Идем ставить следящего МЗ", id, getKeyboardByStatus())
                                    sender("Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "мо":
                                if check_access(id, access_full) or check_access(id, access_full_defense):
                                    status = "waiting set spectator defence"
                                    sender("Идем ставить следящего МО", id, getKeyboardByStatus())
                                    sender("Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "сми":
                                if check_access(id, access_full) or check_access(id, access_full_media):
                                    status = "waiting set spectator media"
                                    sender("Идем ставить следящего СМИ", id, getKeyboardByStatus())
                                    sender("Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id, getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "обратно":
                                status = "settings"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "waiting set spectator government":
                            if checkValidId(msg):
                                access_spec_government.append(msg)
                                log("@id" + str(id) + "(ГС/ЗГС Пра-во) поставил @id" + str(msg) + "(Администратора) на слежку пра-во")
                                saveVariables()
                                status = "set spectator"
                                sender("Вы успешно поставили следящего за пра-во!", id, getKeyboardByStatus())
                                sender("Вас поставили на слежку за пра-во! Напишите \"Обновить\", чтоб бот продолжил работу", msg, getMainKeyboard())
                            elif msg == "обратно":
                                status = "set spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id, getKeyboardByStatus())
                        elif status == "waiting set spectator co":
                            if checkValidId(msg):
                                access_spec_co.append(msg)
                                log("@id" + str(id) + "(ГС/ЗГС ЦА) поставил @id" + str(msg) + "(Администратора) на слежку ЦА")
                                saveVariables()
                                status = "set spectator"
                                sender("Вы успешно поставили следящего за ЦА!", id, getKeyboardByStatus())
                                sender("Вас поставили на слежку за ЦА! Напишите \"Обновить\", чтоб бот продолжил работу", msg, getMainKeyboard())
                            elif msg == "обратно":
                                status = "set spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id, getKeyboardByStatus())
                        elif status == "waiting set spectator justice":
                            if checkValidId(msg):
                                access_spec_justice.append(msg)
                                log("@id" + str(id) + "(ГС/ЗГС МЮ) поставил @id" + str(msg) + "(Администратора) на слежку МЮ")
                                saveVariables()
                                status = "set spectator"
                                sender("Вы успешно поставили следящего за МЮ!", id, getKeyboardByStatus())
                                sender("Вас поставили на слежку за МЮ! Напишите \"Обновить\", чтоб бот продолжил работу", msg, getMainKeyboard())
                            elif msg == "обратно":
                                status = "set spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id, getKeyboardByStatus())
                        elif status == "waiting set spectator health":
                            if checkValidId(msg):
                                access_spec_health.append(msg)
                                log("@id" + str(id) + "(ГС/ЗГС МЗ) поставил @id" + str(msg) + "(Администратора) на слежку МЗ")
                                saveVariables()
                                status = "set spectator"
                                sender("Вы успешно поставили следящего за МЗ!", id, getKeyboardByStatus())
                                sender("Вас поставили на слежку за МЗ! Напишите \"Обновить\", чтоб бот продолжил работу", msg, getMainKeyboard())
                            elif msg == "обратно":
                                status = "set spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id, getKeyboardByStatus())
                        elif status == "waiting set spectator defence":
                            if checkValidId(msg):
                                access_spec_defense.append(msg)
                                log("@id" + str(id) + "(ГС/ЗГС МО) поставил @id" + str(msg) + "(Администратора) на слежку МО")
                                saveVariables()
                                status = "set spectator"
                                sender("Вы успешно поставили следящего за МО!", id, getKeyboardByStatus())
                                sender("Вас поставили на слежку за МО! Напишите \"Обновить\", чтоб бот продолжил работу", msg, getMainKeyboard())
                            elif msg == "обратно":
                                status = "set spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id, getKeyboardByStatus())
                        elif status == "waiting set spectator media":
                            if checkValidId(msg):
                                access_spec_media.append(msg)
                                log("@id" + str(id) + "(ГС/ЗГС СМИ) поставил @id" + str(msg) + "(Администратора) на слежку СМИ")
                                saveVariables()
                                status = "set spectator"
                                sender("Вы успешно поставили следящего за СМИ!", id, getKeyboardByStatus())
                                sender("Вас поставили на слежку за СМИ! Напишите \"Обновить\", чтоб бот продолжил работу", msg, getMainKeyboard())
                            elif msg == "обратно":
                                status = "set spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id, getKeyboardByStatus())
                        elif status == "del spectator":
                            if msg == "пра-во":
                                if check_access(id, access_full) or check_access(id, access_full_government):
                                    status = "waiting del spectator government"
                                    sender("Идем снимать следящего пра-во", id, getKeyboardByStatus())
                                    sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                           getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "ца":
                                if check_access(id, access_full) or check_access(id, access_full_co):
                                    status = "waiting del spectator co"
                                    sender("Идем снимать следящего ЦА", id, getKeyboardByStatus())
                                    sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                           getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "мю":
                                if check_access(id, access_full) or check_access(id, access_full_justice):
                                    status = "waiting del spectator justice"
                                    sender("Идем снимать следящего МЮ", id, getKeyboardByStatus())
                                    sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                           getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "мз":
                                if check_access(id, access_full) or check_access(id, access_full_health):
                                    status = "waiting del spectator health"
                                    sender("Идем снимать следящего МЗ", id, getKeyboardByStatus())
                                    sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                           getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "мо":
                                if check_access(id, access_full) or check_access(id, access_full_defense):
                                    status = "waiting del spectator defence"
                                    sender("Идем ставить следящего МО", id, getKeyboardByStatus())
                                    sender("Отправьте ссылку на нового следящего в формате id вк, например: 454427393", id,
                                           getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "сми":
                                if check_access(id, access_full) or check_access(id, access_full_media):
                                    status = "waiting del spectator media"
                                    sender("Идем снимать следящего СМИ", id, getKeyboardByStatus())
                                    sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                           getKeyboardByStatus())
                                else:
                                    send_noaccess_message(id)
                            elif msg == "обратно":
                                status = "settings"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "waiting del spectator government":
                            if checkValidId(msg):
                                log("@id" + str(id) + "(ГС/ЗГС Пра-во) снял @id" + str(msg) + "(Администратора) со слежки пра-во")
                                access_spec_government.remove(str(msg))
                                saveVariables()
                                status = "del spectator"
                                sender("Вы успешно сняли следящего пра-во!", id, getKeyboardByStatus())
                                sender("Вас сняли со слежки пра-во! Напишите \"Обновить\", чтоб бот продолжил работу", msg, getMainKeyboard())
                            elif msg == "обратно":
                                status = "del spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                        elif status == "waiting del spectator co":
                            if checkValidId(msg):
                                log("@id" + str(id) + "(ГС/ЗГС ЦА) снял @id" + str(msg) + "(Администратора) со слежки ЦА")
                                access_spec_co.remove(str(msg))
                                saveVariables()
                                status = "del spectator"
                                sender("Вы успешно сняли следящего ЦА!", id, getKeyboardByStatus())
                                sender("Вас сняли со слежки ЦА! Напишите \"Обновить\", чтоб бот продолжил работу", msg, getMainKeyboard())
                            elif msg == "обратно":
                                status = "del spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                        elif status == "waiting del spectator justice":
                            if checkValidId(msg):
                                log("@id" + str(id) + "(ГС/ЗГС МЮ) снял @id" + str(msg) + "(Администратора) со слежки МЮ")
                                access_spec_justice.remove(str(msg))
                                saveVariables()
                                status = "del spectator"
                                sender("Вы успешно сняли следящего МЮ!", id, getKeyboardByStatus())
                                sender("Вас сняли со слежки МЮ! Напишите \"Обновить\", чтоб бот продолжил работу", msg, getMainKeyboard())
                            elif msg == "обратно":
                                status = "del spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                        elif status == "waiting del spectator health":
                            if checkValidId(msg):
                                log("@id" + str(id) + "(ГС/ЗГС МЗ) снял @id" + str(msg) + "(Администратора) со слежки МЗ")
                                access_spec_health.remove(str(msg))
                                saveVariables()
                                status = "del spectator"
                                sender("Вы успешно сняли следящего МЗ!", id, getKeyboardByStatus())
                                sender("Вас сняли со слежки МЗ! Напишите \"Обновить\", чтоб бот продолжил работу", msg, getMainKeyboard())
                            elif msg == "обратно":
                                status = "del spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                        elif status == "waiting del spectator defence":
                            if checkValidId(msg):
                                log("@id" + str(id) + "(ГС/ЗГС МО) снял @id" + str(msg) + "(Администратора) со слежки МО")
                                access_spec_defense.remove(str(msg))
                                saveVariables()
                                status = "del spectator"
                                sender("Вы успешно сняли следящего МО!", id, getKeyboardByStatus())
                                sender("Вас сняли со слежки МО! Напишите \"Обновить\", чтоб бот продолжил работу", msg, getMainKeyboard())
                            elif msg == "обратно":
                                status = "del spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                        elif status == "waiting del spectator media":
                            if checkValidId(msg):
                                log("@id" + str(id) + "(ГС/ЗГС СМИ) снял @id" + str(msg) + "(Администратора) со слежки СМИ")
                                access_spec_media.remove(str(msg))
                                saveVariables()
                                status = "del spectator"
                                sender("Вы успешно сняли следящего СМИ!", id, getKeyboardByStatus())
                                sender("Вас сняли со слежки СМИ! Напишите \"Обновить\", чтоб бот продолжил работу", msg, getMainKeyboard())
                            elif msg == "обратно":
                                status = "del spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                        elif status == "set full spectator":
                            if msg == "пра-во":
                                status = "choosing set access government"
                                sender("Выберите: ГСа или ЗГСа", id, getKeyboardByStatus())
                            elif msg == "ца":
                                status = "choosing set access co"
                                sender("Выберите: ГСа или ЗГСа", id, getKeyboardByStatus())
                            elif msg == "мю":
                                status = "choosing set access justice"
                                sender("Выберите: ГСа или ЗГСа", id, getKeyboardByStatus())
                            elif msg == "мз":
                                status = "choosing set access health"
                                sender("Выберите: ГСа или ЗГСа", id, getKeyboardByStatus())
                            elif msg == "мо":
                                status = "choosing set access defence"
                                sender("Выберите: ГСа или ЗГСа", id, getKeyboardByStatus())
                            elif msg == "сми":
                                status = "choosing set access media"
                                sender("Выберите: ГСа или ЗГСа", id, getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "settings"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "choosing set access government":
                            if msg == "гса":
                                status = "set gs government"
                                sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                            elif msg == "згса":
                                status = "set zgs government"
                                sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "set full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "choosing set access co":
                            if msg == "гса":
                                status = "set gs co"
                                sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                            elif msg == "згса":
                                status = "set zgs co"
                                sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "set full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "choosing set access justice":
                            if msg == "гса":
                                status = "set gs justice"
                                sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                            elif msg == "згса":
                                status = "set zgs justice"
                                sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "set full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "choosing set access health":
                            if msg == "гса":
                                status = "set gs health"
                                sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                            elif msg == "згса":
                                status = "set zgs health"
                                sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "set full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "choosing set access defence":
                            if msg == "гса":
                                status = "set gs defence"
                                sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                            elif msg == "згса":
                                status = "set zgs defence"
                                sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "set full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status == "choosing set access media":
                            if msg == "гса":
                                status = "set gs media"
                                sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                            elif msg == "згса":
                                status = "set zgs media"
                                sender("Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                            elif msg == "обратно":
                                status = "set full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                        elif status.startswith("set gs"):
                            target = status.replace("set gs ", "")
                            if checkValidId(msg):
                                if target == "government":
                                    access_full_government[0] = msg
                                    saveVariables()
                                    status = "set full spectator"
                                    log("@id" + str(id) + "(ГС/ЗГС ГОС) поставил @id" + str(msg) + "(ГСа Пра-во)")
                                    sender("Вы успешно поставили ГСа пра-во", id, getKeyboardByStatus())
                                    sender("Вас поставили на ГСа пра-во! Напишите \"Обновить\", чтоб бот продолжил работу", int(access_full_government[0]), getMainKeyboard())
                                elif target == "co":
                                    access_full_co[0] = msg
                                    log("@id" + str(id) + "(ГС/ЗГС ГОС) поставил @id" + str(msg) + "(ГСа ЦА)")
                                    saveVariables()
                                    status = "set full spectator"
                                    sender("Вы успешно поставили ГСа ЦА", id, getKeyboardByStatus())
                                    sender("Вас поставили на ГСа ЦА! Напишите \"Обновить\", чтоб бот продолжил работу", int(access_full_co[0]), getMainKeyboard())
                                elif target == "justice":
                                    access_full_justice[0] = msg
                                    log("@id" + str(id) + "(ГС/ЗГС ГОС) поставил @id" + str(msg) + "(ГСа МЮ)")
                                    saveVariables()
                                    status = "set full spectator"
                                    sender("Вы успешно поставили ГСа МЮ", id, getKeyboardByStatus())
                                    sender("Вас поставили на ГСа МЮ! Напишите \"Обновить\", чтоб бот продолжил работу", int(access_full_justice[0]), getMainKeyboard())
                                elif target == "health":
                                    access_full_health[0] = msg
                                    log("@id" + str(id) + "(ГС/ЗГС ГОС) поставил @id" + str(msg) + "(ГСа МЗ)")
                                    saveVariables()
                                    status = "set full spectator"
                                    sender("Вы успешно поставили ГСа МЗ", id, getKeyboardByStatus())
                                    sender("Вас поставили на ГСа МЗ! Напишите \"Обновить\", чтоб бот продолжил работу", int(access_full_health[0]), getMainKeyboard())
                                elif target == "defence":
                                    access_full_defense[0] = msg
                                    log("@id" + str(id) + "(ГС/ЗГС ГОС) поставил @id" + str(msg) + "(ГСа МО)")
                                    saveVariables()
                                    status = "set full spectator"
                                    sender("Вы успешно поставили ГСа МО", id, getKeyboardByStatus())
                                    sender("Вас поставили на ГСа МО! Напишите \"Обновить\", чтоб бот продолжил работу", int(access_full_defense[0]), getMainKeyboard())
                                elif target == "media":
                                    access_full_media[0] = msg
                                    log("@id" + str(id) + "(ГС/ЗГС ГОС) поставил @id" + str(msg) + "(ГСа СМИ)")
                                    saveVariables()
                                    status = "set full spectator"
                                    sender("Вы успешно поставили ГСа СМИ", id, getKeyboardByStatus())
                                    sender("Вас поставили на ГСа СМИ! Напишите \"Обновить\", чтоб бот продолжил работу", int(access_full_media[0]), getMainKeyboard())
                            elif msg == "обратно":
                                status = "set full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())
                        elif status.startswith("set zgs"):
                            target = status.replace("set zgs ", "")
                            if checkValidId(msg):
                                if target == "government":
                                    access_full_government[1] = msg
                                    log("@id" + str(id) + "(ГС/ЗГС ГОС) поставил @id" + str(msg) + "(ЗГСа Пра-во)")
                                    saveVariables()
                                    status = "set full spectator"
                                    sender("Вы успешно поставили ЗГСа пра-во", id, getKeyboardByStatus())
                                    sender("Вас поставили на ЗГСа пра-во! Напишите \"Обновить\", чтоб бот продолжил работу", int(access_full_government[1]), getMainKeyboard())
                                elif target == "co":
                                    access_full_co[1] = msg
                                    log("@id" + str(id) + "(ГС/ЗГС ГОС) поставил @id" + str(msg) + "(ЗГСа ЦА)")
                                    saveVariables()
                                    status = "set full spectator"
                                    sender("Вы успешно поставили ЗГСа ЦА", id, getKeyboardByStatus())
                                    sender("Вас поставили на ЗГСа ЦА! Напишите \"Обновить\", чтоб бот продолжил работу", int(access_full_co[1]), getMainKeyboard())
                                elif target == "justice":
                                    access_full_justice[1] = msg
                                    log("@id" + str(id) + "(ГС/ЗГС ГОС) поставил @id" + str(msg) + "(ЗГСа МЮ)")
                                    saveVariables()
                                    status = "set full spectator"
                                    sender("Вы успешно поставили ЗГСа МЮ", id, getKeyboardByStatus())
                                    sender("Вас поставили на ЗГСа МЮ! Напишите \"Обновить\", чтоб бот продолжил работу", int(access_full_justice[1]), getMainKeyboard())
                                elif target == "health":
                                    access_full_health[1] = msg
                                    log("@id" + str(id) + "(ГС/ЗГС ГОС) поставил @id" + str(msg) + "(ЗГСа СМИ)")
                                    saveVariables()
                                    status = "set full spectator"
                                    sender("Вы успешно поставили ЗГСа МЗ", id, getKeyboardByStatus())
                                    sender("Вас поставили на ЗГСа МЗ! Напишите \"Обновить\", чтоб бот продолжил работу", int(access_full_health[1]), getMainKeyboard())
                                elif target == "defence":
                                    access_full_defense[1] = msg
                                    log("@id" + str(id) + "(ГС/ЗГС ГОС) поставил @id" + str(msg) + "(ЗГСа МО)")
                                    saveVariables()
                                    status = "set full spectator"
                                    sender("Вы успешно поставили ЗГСа МО", id, getKeyboardByStatus())
                                    sender("Вас поставили на ЗГСа МО! Напишите \"Обновить\", чтоб бот продолжил работу", int(access_full_defense[1]), getMainKeyboard())
                                elif target == "media":
                                    access_full_media[1] = msg
                                    log("@id" + str(id) + "(ГС/ЗГС ГОС) поставил @id" + str(msg) + "(ЗГСа СМИ)")
                                    saveVariables()
                                    status = "set full spectator"
                                    sender("Вы успешно поставили ЗГСа СМИ", id, getKeyboardByStatus())
                                    sender("Вас поставили на ЗГСа СМИ! Напишите \"Обновить\", чтоб бот продолжил работу", int(access_full_media[1]), getMainKeyboard())
                            elif msg == "обратно":
                                status = "set full spectator"
                                sender("Возращаемся обратно!", id, getKeyboardByStatus())
                            else:
                                sender("Ошибка! Отправьте ссылку на следящего в формате id вк, например: 454427393", id,
                                       getKeyboardByStatus())

                    else:
                        send_noaccess_message(id, False)


    except Exception as e:
        print(e)
