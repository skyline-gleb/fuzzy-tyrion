import argparse


class App(object):

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(prog="fuzzer", description="HTTP API fuzzer")
        parser.add_argument("-c", "--config", help="set configuration file", required=True)
        parser.add_argument("-r", "--report", help="set report file")
        parser.add_argument("-v", "--verbose", help="turn on verbose logging", action="store_true")
        return parser.parse_args()

    @staticmethod
    def init():
        App.args = App.get_args()
