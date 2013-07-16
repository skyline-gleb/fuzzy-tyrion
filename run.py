#!/usr/bin/env python3

from frontend import App
from frontend import Config
from frontend import Fuzzer


def main():
    App.init()

    Config.load(App.args.config)

    fuzzer = Fuzzer(Config.api_url, Config.rps,
                    Config.headers, Config.parameters)

    fuzzer.test_methods(Config.methods)


if __name__ == '__main__':
    main()
