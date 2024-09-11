init:

    define inventory_items = {}
    define item_description = ""
    define objectives = {}
    define objective_description = ""

    ### Backgrounds
    image home_office = 'office.jpg'

    ### Screen Init
    $ config.window_title = 'Chinatown Detective'

    ### Inventory System
    screen inventory_display:
        zorder 92
        frame:
            background "#9F99"
            xalign 0.05
            yalign 0.1

        hbox:
            textbutton "Inventory":
                action ToggleScreen("inventory_description")
                style "inv_button"
            textbutton "Objectives":
                action ToggleScreen("current_objectives")
                style "inv_button"

        on "hide" action Hide("inventory_description")



    style inv_button is frame:
        xsize 200
        ysize 100

    style inv_button_text:
        xalign 0.5
        yalign 0.5

    screen inventory_description:
        
        window:
            background "#AAA9"
            xsize 600
            ysize 150
            xalign 0.5
            yalign 0.1
            text item_description:
                xfill True
                yfill True

        window:
            background "#99F9"
            xsize 1290
            ysize 600
            xalign 0.5
            yalign 0.7
            hbox:
                box_wrap True
                box_wrap_spacing 10
                spacing 10
                xoffset 20
                yoffset 20
                style_prefix "inv"
                for item in inventory_items:
                    textbutton item:
                        action SetVariable("item_description", inventory_items.get(item))
                        selected False

        on "hide" action SetVariable("item_description", "")

    ### Objectives
    screen current_objectives:

        window:
            background "#AAA9"
            xsize 600
            ysize 150
            xalign 0.5
            yalign 0.1

        window: 
            background "#99F9"
            xsize 1290
            ysize 600
            xalign 0.5
            yalign 0.7
            hbox:
                box_wrap True
                box_wrap_spacing 10
                spacing 10
                xoffset 20
                yoffset 20
                style_prefix "obj"
                for objective in objectives:
                    textbutton objective:
                        action SetVariable("objective_description", objectives.get(objective))
                        selected False

        on "hide" action SetVariable("objective_description", "")