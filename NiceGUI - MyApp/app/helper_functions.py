from nicegui import app, ui, background_tasks, helpers 
from nicegui.events import ValueChangeEventArguments
import sys, os, shutil
import json
from typing import Callable, Dict, Union
from loguru import logger

class RouterFrame(ui.element, component='router_frame.js'):
    pass

class Router():

    def __init__(self) -> None:
        self.routes: Dict[str, Callable] = {}
        self.content: ui.element = None

    def add(self, path: str):
        def decorator(func: Callable):
            self.routes[path] = func
            return func
        return decorator

    def open(self, target: Union[Callable, str]) -> None:
        if isinstance(target, str):
            path = target
            builder = self.routes[target]
        else:
            path = {v: k for k, v in self.routes.items()}[target]
            builder = target

        async def build() -> None:
            with self.content:
                ui.run_javascript(f'''
                    if (window.location.pathname !== "{path}") {{
                        history.pushState({{page: "{path}"}}, "", "{path}");
                    }}
                ''')
                result = builder()
                if helpers.is_coroutine_function(builder):
                    await result
        self.content.clear()
        background_tasks.create(build())

    def frame(self) -> ui.element:
        self.content = RouterFrame().on('open', lambda e: self.open(e.args))
        return self.content


def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')


def init_settings(settings_file_path):
    # Check for saved settings
    if os.path.exists(settings_file_path):
        logger.info('Settings file found:')
        f= open(settings_file_path,'r')
        contents =f.read()
        f.close()
        settings_data = json.loads(contents)
    else:
        logger.info('Settings file not found, using defaults:')
        settings_data = {
            'name': 'Bob', 
            'age': 17,
            'OpenAI-Key': 'sk-1234'
        }     
    settings_data['settings_file_path'] = settings_file_path # form global var, see above  
    logger.info(settings_data)
    return settings_data


# Logger
def init_logger():
    logger.remove()  # Remove all handlers added so far, including the default one.

    # custom function as log handler - will be executed with every log call
    def custom_function(msg):
      msg_obj = json.loads(msg)
      message = msg_obj['record']['message'] #print(msg_obj['text'])
      level = msg_obj['record']['level']['name']
      #print('+++ FROM LOGGER: ' + message)
      app.storage.general['global_logs']['loguru'] = '<li class="log_loguru">' + msg_obj['text'] + '</li>' + app.storage.general['global_logs']['loguru']
    logger.add(custom_function, level="TRACE", format="{time:HH:mm:ss} | {level: <10} | {message}", serialize=True)
    logger.add(sys.stderr, level="TRACE", format="{time:HH:mm:ss} | {level: <10} | {message}")


    #logger.trace("A trace message.")
    #logger.debug("A debug message.")
    #logger.info("An info message.")
    #logger.success("A success message.")
    #logger.warning("A warning message.")
    #logger.error("An error message.")
    #logger.critical("A critical message.")
