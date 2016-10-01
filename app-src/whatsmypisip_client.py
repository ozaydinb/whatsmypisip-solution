import oaipaddress
import config
import oaclient
import console
import time
import sys
import fcntl
import os


def loop(interval_seconds):
    fl = fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
    fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, fl | os.O_NONBLOCK)

    while True:
        current = oaipaddress.get_ip_address()
        last = oaclient.get_last_ip_address()

        if last != "CONNFAIL" and current != "CONNFAIL":
            if current != last:
                oaclient.save_current_ip_address(current)
            else:
                console.log("IP not changed")
        try:
            user_break_input = sys.stdin.read()
            if user_break_input == "exit\n" or user_break_input == "q\n":
                console.log("Application terminated")
                break
        except TypeError:  # debug mode false
            pass

        time.sleep(interval_seconds)


if __name__ == "__main__":
    interval_seconds = int(config.get_value("interval"))
    loop(interval_seconds)
