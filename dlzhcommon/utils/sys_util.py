import logging
import os
import platform
import signal


def handle_signal():
    def handle_kill(sig, frame):
        raise SystemExit

    signal.signal(signal.SIGTERM, handle_kill)


def logging_config():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)s %(levelname)-8s %(message)s'
    )


def get_env(key, default_val):
    val = os.getenv(key)
    if val is None:
        return default_val
    return val


def get_host_name():
    return platform.uname().node
