from tkinter import *
from chatting import get_response, bot_name

BG_GRAY="#ABB2B9"
BG_COLOR = "#17202A"
BG_MSG_BOX = "#2C3E50"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class application:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()


    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        #text area
        self.text_area = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,font=FONT, padx=5, pady=5)
        self.text_area.place(relheight=0.75, relwidth=1, rely=0.08)
        self.text_area.configure(cursor="arrow", state=DISABLED)

        #scrollbar
        scrollbar = Scrollbar(self.text_area)
        scrollbar.place(relheight=1, relx=0.95)
        scrollbar.configure(command=self.text_area.yview)

        #bottom label
        bottom_lablel = Label(self.window, bg=BG_GRAY, height=80)
        bottom_lablel.place(relwidth=1, rely=0.8)

        # message box
        self.message = Entry(bottom_lablel, bg=BG_MSG_BOX, fg=TEXT_COLOR, font=FONT)
        self.message.place(relwidth=0.75, relheight=0.05, rely=0.01, relx=0.01)
        self.message.focus()
        self.message.bind("<Return>", self._on_pressed)

        #enter button
        enter_button = Button(bottom_lablel, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
        command=lambda: self._on_pressed(None))

        enter_button.place(relx = 0.78, rely=0.01, relheight=0.06, relwidth=0.20)


    def _on_pressed(self, event):
        msg = self.message.get()
        self._add_msg(msg, "You")

    def _add_msg(self, msg, sender):
        if not msg:
            return
        
        self.message.delete(0, END)
        dis_msg = f"{sender}: {msg}\n\n"
        self.text_area.configure(state=NORMAL)
        self.text_area.insert(END, dis_msg)
        self.text_area.configure(state=DISABLED)

        ret_msg = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_area.configure(state=NORMAL)
        self.text_area.insert(END, ret_msg)
        self.text_area.configure(state=DISABLED)

        self.text_area.see(END)



    def run(self):
        self.window.mainloop()



if __name__ == "__main__":
    app = application()
    app.run()
