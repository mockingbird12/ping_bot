import config
import time
import telebot
import talking
from config import ip_list, my_ip_list
from service_lib import check_internet, ping
from telebot import apihelper


isWorking = False
isRunning = False
bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['ping'])
def ping_servers(message):
    bot.send_message(message.chat.id, 'pinging servers')
    for ip in ip_list:
        bot.send_message(message.chat.id, ping(ip))


@bot.message_handler(commands=['info'])
def show_ips(message):
    ip_str = '\n '.join(ip for ip in ip_list)
    bot.send_message(message.chat.id, ip_str)


@bot.message_handler(commands=['stop'])
def stop_monitoring(message):
    global isRunning
    isRunning = False
    bot.send_message(message.chat.id, 'Stop monitoring')


@bot.message_handler(commands=['start'])
def start_checking(message):
    global isWorking
    global isRunning
    if not isWorking:
        isWorking = True
        isRunning = True
        bot.send_message(message.chat.id,talking.start_message)
        print(message.chat.id)
        error_list = []
        while isRunning:
            if time.asctime().split()[3].split(':')[1] == '00':
                print('Bot is working')
                bot.send_message(message.chat.id, 'Bot is working')
            for ip in ip_list:
                if check_internet(ip):
                    if ip in error_list:
                        error_list.remove(ip)
                        print('%s - is working' % ip)
                        bot.send_message(message.chat.id, '%s - is working since %s' % (ip, time.asctime()))
                else:
                    if ip not in error_list:
                        error_list.append(ip)
                        print('%s - is down' % ip)
                        bot.send_message(message.chat.id, '%s - is down since %s' % (ip, time.asctime()))
            time.sleep(config.sleep)
            print('Error list - ', error_list)
    else:
        bot.send_message(message.chat.id, 'Monitoring already working')


@bot.message_handler(content_types=['text'])
def repeat(message):
    hello_message = talking.hello_message
    bot.send_message(message.chat.id, hello_message)
    bot.send_message(message.chat.id,talking.help_message )


if __name__=='__main__':
    print('Starting bot')
    apihelper.proxy = { 'https': 'socks5://127.0.0.1:9050'}
    bot.polling()