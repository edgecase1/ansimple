

import json
import logging




import subprocess
import os
class AptHandler:

    provider = "apt"

    def __init__(self):
        self._check_env()
        return

    def _check_env(self):
        pass

    def apply(self, item):
        data = item[self.provider]
        if os.geteuid() != 0:
            raise Exception("not effective user ID 0! run with sudo")

        cmd = [ "apt-get", "install", "-y", data["name"] ]
        logger.debug("running '{0}'".format(cmd))
        process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)
        logger.debug(process.stdout.read())
        process.communicate()
        if process.returncode != 0: raise Exception("error running process {0} - rc={1}".format(cmd[0], process.returncode))

        return

    def __repr__(self):
        return self.provider

class ItemHandlerFactory:

    def __init__(self):
        self.handlers = {}

    def add_handler(self, handler):
        self.handlers[handler.provider] = handler

    def create_by_type(self, item):
        requested_provider = list(item.keys())[0]
        if requested_provider in self.handlers.keys():
            return self.handlers[requested_provider]
        else:
            return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("main")
    playbook = []
    with open("playbook.yml", "r") as f:
        playbook = json.load(f)
    logger.debug("parsed playbook:" + str(playbook))

    factory = ItemHandlerFactory()     
    factory.add_handler(AptHandler())
    for item in playbook:
        handler = factory.create_by_type(item)
        try:
            handler.apply(item)
        except Exception as e:
            logger.error("error running handler {1} with data {0}". format(item, handler))
            logger.error(e)
    logger.debug("done") 
