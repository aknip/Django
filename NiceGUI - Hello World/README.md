
docker-compose up
http://localhost

- This runs 'main.py'
- For execuitng a different .py-file use: APP=form-demo.py docker-compose up

# Open in gitpod.io:
https://gitpod.io/#https://github.com/aknip/Python-Webdev-Django-Streamsync


# Infos
- Browser hot reload => Change in .py file reloads browser automatically
- Works in Docker and locally


# Global variables (across all pages, for all users)
- Example:
	- app.storage.general['my_var'] = 0 
	- app.storage.general['my_var'] = app.storage.general['my_var'] + 1
# see https://nicegui.io/documentation/section_action_events#storage

# Build your own components (Vue)
- https://github.com/zauberzeug/nicegui/tree/main/examples/custom_vue_component

# REST API: Provide and consume API
- https://github.com/zauberzeug/nicegui/tree/main/examples/fastapi




# Code Examples

Sources:
- https://github.com/zauberzeug/nicegui/tree/main/examples
- https://github.com/zauberzeug/nicegui/wiki#community-projects

- File Download (txt)
	https://github.com/zauberzeug/nicegui/tree/main/examples/download_text_as_file

- File Upload: 
	https://github.com/zauberzeug/nicegui/tree/main/examples/ai_interface

- Editable table / grid:
	https://github.com/zauberzeug/nicegui/tree/main/examples/editable_ag_grid

- List, searchable, items can be added / deleted ('mobile look and feel'):
	https://github.com/zauberzeug/nicegui/tree/main/examples/table_and_slots
	https://github.com/zauberzeug/nicegui/tree/main/examples/todo_list

- Drag and drop:
	https://github.com/zauberzeug/nicegui/tree/main/examples/trello_cards

- OpenAI Whisper: Fileupload
	https://github.com/zauberzeug/nicegui/tree/main/examples/ai_interface

- Stable Diffusion: Prompt + Image Display: 
	https://github.com/zauberzeug/nicegui/tree/main/examples/ai_interface

- Login, Check and route to Welcoome page:
	https://github.com/zauberzeug/nicegui/tree/main/examples/authentication
	Auth with descope.com : https://github.com/zauberzeug/nicegui/tree/main/examples/descope_auth

- OpenAI chat, with tab navigation for viewing logs:
	https://github.com/zauberzeug/nicegui/tree/main/examples/chat_with_ai