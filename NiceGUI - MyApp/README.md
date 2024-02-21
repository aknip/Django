
docker-compose up
http://localhost

- This runs 'main.py'
- For execuitng a different .py-file use: APP=form-demo.py docker-compose up
- Single page app router (no reload) based on https://github.com/zauberzeug/nicegui/tree/main/examples/single_page_app 

# Open in gitpod.io:
https://gitpod.io/#https://github.com/aknip/Python-Webdev-Django-Streamsync



# Infos
- Browser hot reload => Change in .py file reloads browser automatically
- Works in Docker and locally
- Uses a customized Docker config for pip install etc.
