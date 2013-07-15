#!/usr/bin/env python

import sys
sys.path.append("backend")
sys.path.append("frontend")
sys.path.append("frontend/core")
sys.path.append("frontend/config")
sys.path.append("frontend/http")
sys.path.append("frontend/log")
sys.path.append("frontend/vendor")
sys.path.append("frontend/utils")

from app import *
from config import *
from fuzzer import *


def main():
    App.init()

    Config.load(App.args.config)

    fuzzer = Fuzzer(Config.api_url, Config.rps,
                    Config.headers, Config.parameters)

    fuzzer.test_methods(Config.methods)


if __name__ == '__main__':
    main();
