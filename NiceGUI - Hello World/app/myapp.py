from nicegui import ui
from nicegui.events import ValueChangeEventArguments


#ui.dark_mode().enable()
ui.colors(primary='#94a3b8')


ui.add_head_html('''
    <style>
        header {
            padding-left: 15vw!important;
            height: 88px;
            padding-top: 40px;
        }
        aside {
            margin-left: 15vw!important
        }
        .q-page {
            margin-left: 15vw!important
        }
    </style>
''')

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')


def appB(ui):
    ui.label('Content of B')
    ui.button('Button', on_click=lambda: ui.notify('Click'))
    with ui.row():
        ui.checkbox('Checkbox', on_change=show)
        ui.switch('Switch', on_change=show)
    ui.radio(['A', 'B', 'C'], value='A', on_change=show).props('inline')
    with ui.row():
        ui.input('Text input', on_change=show)
        ui.select(['One', 'Two'], value='One', on_change=show)
    ui.link('And many more...', '/documentation').classes('mt-8')

with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.tabs() as tabs:
        ui.tab('A')
        ui.tab('B')
        ui.tab('C')

with ui.footer(value=False) as footer:
    ui.label('Footer')

with ui.left_drawer().classes('bg-gray-100') as left_drawer:
    ui.label('Side menu')

with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    ui.button(on_click=footer.toggle, icon='contact_support').props('fab')

with ui.tab_panels(tabs, value='A').classes('w-full'):
    with ui.tab_panel('A'):
        ui.label('Content of A')
    with ui.tab_panel('B'):
        appB(ui)
    with ui.tab_panel('C'):
        ui.label('Content of C')

ui.run()






from nicegui import ui
from nicegui.events import ValueChangeEventArguments





