import pywhatkit
import datetime

with open(r"<path>", "r") as phones_file:
    phones_list = phones_file.read().split("\n")
    for phone_number in phones_list:
        now = datetime.datetime.now()
        date_time_str = now.strftime("%y-%m-%d %H:%M:%S")
        time_list = date_time_str[9:].split(":")
        hour = int(time_list[0])
        minute = int(time_list[1])
        pywhatkit.sendwhatmsg(phone_number, "message automation with python", hour, minute + 1)


