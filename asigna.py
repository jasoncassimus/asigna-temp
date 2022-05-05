import os, sys, time

import globals
import Server
from Server import *
import World
from User import *
from World import *
# from globals import *
import globals

gameloop = None
lock = threading.Lock()
users = []


def add_user(new_user):
    users.append(new_user)


def sprint(message):
    lock.acquire()
    print(message)
    lock.release()


def ping():
    for user in asigna.users:
        user.send("ping")

    if len(asigna.users) > 0:
        asigna.users[0].send("bobobo")


def clear_screen():
    os.system('clear')


def reset_screen():
    os.system('reset')


def menu():
    sprint("""
    Welcome to the Asigna Server:
        0) Big Bang the World
        1) Start/Restart Service
        2) Stop Serving Asigna Mud
    """)
    choice = input("    Enter menu choice:")
    handle_input(choice)


def zero():     #0) Big Bang the World
    globals.world = None
    globals.world = World()


def one():      # 1) Start/Restart Service
    globals.server = None
    globals.server = Server()
    globals.server.start()


def two():      # 2) Stop Serving Asigna Mud
    pass


def handle_input(choice):
    switcher = {
        0: zero(),
        1: one(),
        2: two(),
    }
    func = switcher.get(choice, menu())
    return func()


def main():
    globals.gameloop = threading.Thread(target=asigna)
    globals.gameloop.start()


def asigna():
    while True:
        time.sleep(.3)
        ping()


if __name__ == "__main__":
    globals.world = World()
    globals.server = Server()
    main()
    menu()