<SimpleRoot>:
    orientation: "vertical"
    padding: root.width * .02, root.height * .02
    spacing: "10dp"

    # We create the widgets
    Label:
        id: label_text
        text: "0"
        font_size: "30dp"
    BoxLayout:
        orientation: "horizontal"
        spacing: "30dp"
        Button:
            text: "Add"
            on_release: label_text.text = str(int(label_text.text) + 1)
        Button:
            text: "Subtract"
            on_release: label_text.text = str(int(label_text.text) - 1)

    # Start of second part
    TextInput:
        id: text_input
        hint_text: "Enter Name"
        font_size: "30dp"

    Button:
        text: "Press Me"
        on_release: root.on_our_btn_release(text_input.text)