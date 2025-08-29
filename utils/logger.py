import logging
import sys

def setup_logging(level=logging.INFO):
    root = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    fmt = '%(asctime)s %(levelname)s [%(name)s] %(message)s'
    handler.setFormatter(logging.Formatter(fmt))
    root.addHandler(handler)
    root.setLevel(level)
