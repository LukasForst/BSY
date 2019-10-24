import argparse
import subprocess
import time
import random
import uuid

LOG_FILE = ""


def log(to_log):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(to_log + "\n")


def load_ips(path):
    with open(path, "r", encoding="utf-8") as file:
        return [x.strip() for x in file.readlines()]


def run_ncats(ip, port, msg):
    try:
        command = ["echo", f'\"{msg}\"', "|", "ncat", ip, port, "-u"]
        log(f"Exec: {command}")
        subprocess.run(command)
    except Exception as e:
        log("Exception occurred: " + str(e))
        print("Exception occurred: " + str(e))


def generate_message(ip):
    suffix_options = [".bin", "", ".exe", ".txt", ""]
    return f"PUSHING /files/ff/{uuid.uuid4().hex}{random.choice(suffix_options)}"


def generate_random_port(ip):
    return str(random.randint(0, 65535))


def execute_spam(ips):
    for ip in ips:
        run_ncats(ip, generate_random_port(ip), generate_message(ip))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip-addresses', dest='ip_path', type=str,
                        help="Path to file with IP addresses")
    parser.add_argument('-l', '--logfile', dest='log_path', type=str, default="",
                        help="Path to file where all logs should be stored")
    args = parser.parse_args()

    if args.log_path:
        LOG_FILE = args.log_path
    else:
        LOG_FILE = "/home/class/ncat_spammer/ncat_spammer.log"

    ips = load_ips(args.ip_path)
    ips_log = "\n".join(ips)
    log(f"Spamming following addresses:{ips_log}")

    while True:
        execute_spam(ips)
        time.sleep(10)
