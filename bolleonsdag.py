from subprocess import call
import random


def sendImessage(message, receivers):
    for receiver in receivers:
        __send__(message, receiver)


def __send__(message, receiver):
    command = 'tell application "Messages" to send "' + message + '" to buddy "' + receiver + '"'
    call(["osascript", "-e", command])


messages = ["Kanelbolleonsdag!!!", "Bro, det er kanelbolleonsdag idag!", "Bolle, bolle, bolle, bolle",
            "Du vet hvilken dag det er idag??!", "Booooolleeeeonsdag brusj!", "Skal vi bolle?"]

receivers = ["Sigmund Eggen Holm", "Eirik Vale Aase"]

message = messages[random.randint(0, len(messages) - 1)]

sendImessage(message, receivers)
