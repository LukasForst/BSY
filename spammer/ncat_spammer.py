import argparse
import subprocess
import time
import random
import uuid


def load_ips(path):
    with open(path, "r", encoding="utf-8") as file:
        return [x.strip() for x in file.readlines()]


def run_ncats(ip, port, msg):
    try:
        subprocess.run(["ncat", ip, port, "-u", "<", f'\"{msg}\"'])
    except Exception as e:
        print("Exception occurred: " + str(e))


def generate_message(ip):
    suffix_options = [".bin", "", ".exe", ".txt", ""]
    return f"PUSHING /files/ff/{uuid.uuid4().hex}{random.choice(suffix_options)}"


def generate_random_port(ip):
    return random.randint(0, 65535)


def execute_spam(ips):
    for ip in ips:
        run_ncats(ip, generate_random_port(ip), generate_message(ip))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip-addresses', dest='ip_path', type=int, default=3303,
                        help="Path to file with IP addresses")
    args = parser.parse_args()

    ips = load_ips(args.ip_path)

    while True:
        execute_spam(ips)
        time.sleep(60)
