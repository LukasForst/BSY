#!/usr/bin/python

import sys
import ipaddress as ips
import pandas as pd

def read_ips_file(file):
    with open(file, mode='r', encoding='UTF-8') as f:
        [x.strip() for x in f]

def read_ips_stdin():
    return [x.strip() for x in sys.stdin.readlines()]

def build_df(file = None):
    addresses = read_ips_file(file) if file else read_ips_stdin()
    df = pd.DataFrame()

    df['ips'] = [ips.ip_address(x) for x in addresses]
    df['is_public'] = df['ips'].apply(lambda x: not x.is_private)
    return df

if __name__ == "__main__":
    df = build_df()
    print(df)