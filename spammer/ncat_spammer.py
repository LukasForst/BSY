import argparse
import subprocess
import time


def load_ips(path):
    with open(path, "r", encoding="utf-8") as file:
        return [x.strip() for x in file.readlines()]


def run_ncats(ip, port, msg):
    try:
        subprocess.run(["ncat", ip, port, "-u", msg])
    except Exception as e:
        print("Exception occurred: " + str(e))


def generate_attack_file_name(ip):
    return "random_file.txt"


def execute_spam(ips):
    for ip in ips:
        run_ncats(ip, '22', generate_attack_file_name(ip))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip-addresses', dest='ip_path', type=int, default=3303,
                        help="Path to file with IP addresses")
    args = parser.parse_args()

    ips = load_ips(args.ip_path)

    while True:
        execute_spam(ips)
        time.sleep(60)
