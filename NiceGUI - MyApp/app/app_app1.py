import json
from loguru import logger
from nicegui import app, ui
from helper_functions import show

#from subprocess import Popen
import subprocess
import shlex

def app_app1(ui, settings_data):
    ui.label('wget tests')
    ui.button('Run wget', on_click = lambda: runWget(settings_data))


async def runWget(settings_data):
    logger.info("wget started.")

    # see https://stackoverflow.com/questions/69337180/how-to-asynchronously-call-a-shell-script-from-python
    # https://medium.com/@techclaw/python-popen-understanding-subprocess-management-in-python-83cbc309e714
    # ggf. Alternative (10 Jahre alt) : ??? https://github.com/steveej/python-wget

    # invoke process   
    #command = 'ls -l'
    command = 'wget -rkpN -e robots=off https://bstackdemo.com'
    with subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as result:
        # collect output from process (stout)
        for line in result.stderr:
            logger.info(line)
    # bash-commands do not work, eg. 'ls'
    # use this variant:
    # result = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)       
    # for line in result.stdout:
    #    logger.info(line) #print (line.rstrip("\n"))


    #result.poll()  # this checks if the process is done but does not block
    #result.wait()  # this blocks until the process exits
    logger.info(f"p returncode = {result.returncode}")

    logger.info("wget finished.")
