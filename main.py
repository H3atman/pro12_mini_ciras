from nicegui import ui

@ui.page('/encode',dark=True)
def page_layout():
    # Header
    with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
        ui.label('PRO 12 Mini CIRAS')



    # Body
    ui.label('PRO 12 CRIME INCIDENTS RECORDING').tailwind.font_size('4xl').font_weight('extrabold').align_self('center')
    # font_size('text-9xl').font_weight('extrabold')


    with ui.tabs().classes('w-full') as tabs:
        one = ui.tab('Complainant / Victim\'s Profile').style('background-color: #3874c8')
        two = ui.tab('Suspect/s Profile')
        three = ui.tab('Case Detail')
        four = ui.tab('Offense')
    with ui.tab_panels(tabs, value=two).classes('w-full'):

        with ui.tab_panel(one):
            ui.label('First tab')


        with ui.tab_panel(two):
            ui.label('Second tab')


    # Footer
    with ui.footer().style('background-color: #3874c8'):
        ui.label('This is a Footer')


# Run the whole app
page_layout()


ui.run(host="127.0.0.1",port=8001, title="PRO 12 CIRAS", reload=True)
