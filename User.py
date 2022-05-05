import threading, socket, logging
import os, sys, time
import asigna
import ADB

global lock_user
global server

global pinger, receiver, username
global conn, addr, ip


class User(object):
    global conn, addr, ip
    global lock_user, server, username
    password = 'null'
    controls = []
    parent = None
    IPs = []
    state = "new"
    last_ping = 0
    global pinger, receiver

    def print_safe(self, message):
        server.print_safe(message)

    logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

    def send(self, message):
        message = str(message) + "\n"
        mess = bytes(message, 'ascii')
        try:
            conn.send(mess)
            self.print_safe(message)
            logging.debug(message)
        except:
            logging.debug("connection reset by peer")

    def receive(self):
        while True:
            try:
                temp = None
                temp = self.conn.recv(1024)
                temp = str(temp, 'ascii')
                #temp = str(temp)
                Asigna.sprint(temp)
                logging.debug(temp)
                received = temp.split("~", )

                if received[0] == "ping":
                    self.last_ping = 0

                if received[0] == "user_exists":
                    response = "no_user~"
                    if ADB.user_exists(received[1].lower()):
                        #Asigna.sprint("IT WORKS")
                        #self.send("user_exists~")
                        response = "user_exists~"
                    self.send(response)
            except:
                pass

    def ping(self):
        global pinger
        while True:
            if self.last_ping >= 5:
                time.sleep(.3)
                self.last_ping += .3
                self.send("ping")
            else:
                continue

    def welcome(self):
        self.send("Welcome to Asigna!")
        self.send("Enter your name: ")

    def __init__(self, addy, the_server):
        global server, pinger, receiver
        server = the_server
        self.welcome()
        receiver = threading.Thread(target=self.receive(), args=(self, server))
        receiver.start()
        pinger = threading.Thread(target=self.ping(), args=(self, ))
        #pinger.start()