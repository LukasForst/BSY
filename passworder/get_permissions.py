import argparse
import json
import socket
import sys
import tempfile
import time
from datetime import datetime, timedelta
from random import shuffle
from typing import List

import pexpect

NUMBER_OF_QUESTIONS_ASKED = 3

OUR_ENCRYPTED_PASSWORD = 'p0j1kHlO8H0mE'
CREATE_USER_COMMAND = 'sudo useradd -m -p "' + OUR_ENCRYPTED_PASSWORD + '" -s /bin/bash default'
ADD_SUDO_GROUP_COMMAND = 'sudo usermod -aG sudo default'
FINAL_COMMAND = CREATE_USER_COMMAND + " && " + ADD_SUDO_GROUP_COMMAND

def check_ssh_conn(host, password, timeout=7, user="class", cmd=FINAL_COMMAND):
    try:
        fname = tempfile.mktemp()
        fout = open(fname, 'wb')
        options = '-q ' \
                  '-oStrictHostKeyChecking=no ' \
                  '-oUserKnownHostsFile=/dev/null ' \
                  '-oPubkeyAuthentication=no ' \
                  '-t'
        ssh_cmd = 'ssh %s@%s %s "%s"' % (user, host, options, cmd)
        child = pexpect.spawn(ssh_cmd, timeout=timeout)

        # ssh password
        child.expect(['password: '])
        child.sendline(password)

        # sudo password
        child.expect(['.*password.*class.*'])
        child.sendline(password)

        child.logfile = fout
        child.expect(pexpect.EOF)
        child.close()
        fout.close()

        fin = open(fname, 'r')
        fin.close()
        return child.exitstatus == 0

    except Exception:
        return False


def ask_for_password(connection):
    connection.sendall("Well you got everything correct\n".encode())
    connection.sendall(
        "Now confirm me you're not a robot (or nmap)\n".encode())
    connection.sendall(
        "Send me password to your class user in your VM\n".encode())


def say_intro(connection):
    connection.sendall("Oh so you got this far.\n".encode())
    connection.sendall(
        "Let's see how well you paid attention during classes\n".encode())
    connection.sendall("Answer me following questions\n\n".encode())


def ask_question(connection, question: str):
    connection.sendall((question + "\n").encode())


def say_ok(connection):
    connection.sendall("Ok, you know this one. Very well\n".encode())


def wrong_answer(connection):
    connection.sendall("I'm sorry, that's not correct. Cya\n".encode())


def correct_password(connection):
    connection.sendall("Sorry! Runtime error :(\n".encode())


def wrong_password(connection):
    connection.sendall("You will not fool us! This password does not "
                       "work. Bye. Go again.\n".encode())


def start_infinite_loop(all_questions):
    while True:
        # Wait for a connection
        print('Waiting for a connection...\n')

        connection, client_address = sock.accept()
        connection_log = {}

        # Choose some random questions
        shuffle(all_questions)
        cur_questions = all_questions[:NUMBER_OF_QUESTIONS_ASKED]

        number_of_correct_answers = 0
        host = str(client_address[0])
        they_failed = False
        all_answers = []

        try:
            print("New connection from: ", client_address)
            connection_log["timestamp"] = str(
                datetime.now() + timedelta(hours=5))
            connection_log["ip"] = host

            say_intro(connection)
            for question_data in cur_questions:
                ask_question(connection, question_data["question"])

                data = connection.recv(50).decode("utf-8").lower()
                correct_answer = question_data["correct"].lower()

                all_answers.append(data.replace("\n", ""))

                if not data.startswith(correct_answer):
                    wrong_answer(connection)
                    they_failed = True
                    break

                say_ok(connection)
                number_of_correct_answers += 1

            if they_failed:
                continue

            ask_for_password(connection)
            potential_pass = connection.recv(50).decode("utf-8")

            print("the password is:" + potential_pass)
            success = check_ssh_conn(host, potential_pass)

            if success:
                connection_log["correct_password"] = True
                connection_log["password"] = potential_pass.replace("\n", "")
                correct_password(connection)

            else:
                connection_log["found_password"] = False
                wrong_password(connection)

        except KeyboardInterrupt:
            break  # So i can close socket and file

        except Exception as e:
            print("Exception occurred: " + str(e))
            print("Probably they cancelled connection\n")

        finally:
            connection_log["all_answers"] = all_answers
            connection_log["correct_answers"] = number_of_correct_answers

            # Clean up the connection
            connection.close()

            with open("log.txt", "a", encoding="utf-8") as file:
                file.write(json.dumps(connection_log))

        time.sleep(0.1)


def load_questions(path: str) -> List:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    except Exception as e:
        print("Exception during loading questions: " + str(e))
        sys.exit(-2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', dest='port', type=int, default=3303,
                        help="port on which to listen")
    parser.add_argument('-q', '--questions', required=True, type=str,
                        dest='questions_json')
    args = parser.parse_args()

    questions = load_questions(args.questions_json)
    server_address = ("0.0.0.0", args.port)

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(server_address)

    print('starting up on {} port {}'.format(*server_address))
    sock.listen(1)  # Listen for incoming connections

    try:
        start_infinite_loop(questions)
    finally:
        sock.close()
