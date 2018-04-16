#!/usr/bin/python3
#
# NAME - win_user_gen
# Version 1.0
#
# SYNOPSIS
# python3 ./win_user_gen.py
#
# DESCRIPTION
# Creates random user accounts on windows
#
# AUTHOR
# Juan Ortega
#
# HISTORY:
#
# Date(YYYY/MM/DD):     Version:        Modified By:    Description of Change:
# 2018/04/16             1.0            Juan Ortega     First version of script

from subprocess import check_output
import logging
from faker import Faker
fake = Faker()

def main():
    while True:
        try:
            user_amount = int(input("How many fake users do you want to create? \n"))
            break
        except:
            print("Error: Input must be an integer \n")

    while True:

        for _ in range(user_amount):
            try:
                username = fake.user_name()
                password = fake.password(length=8, special_chars=True, digits=True, upper_case=False, lower_case=True)
                cmd = "net user /add {} \"{}\"".format(str(username),password)
                run_win_cmd(cmd)
                logger.info(str(username) + "," + str(password))
            except:
                pass
        break


def run_win_cmd(cmd):
    check_output(cmd, shell=True).decode()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    hdlr = logging.FileHandler('user_list.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    hdlr.setLevel(logging.INFO)
    logger.addHandler(hdlr)
    main()
