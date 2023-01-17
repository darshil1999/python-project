import requests, re
from tkinter import *
import tkinter as tk
from tkinter import ttk

class RealTimeConverter():
    def __init__(self,url):
        self.data = requests.get(url)
        self.currences = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

class App(tk.Tk):
    def __init__(self,converter):
        tk.Tk.__init__(self)
        self.title = "Currency Converter"
        self.currency_converter = converter

        self.geometry("500x200")

        self.intro_label = Label(self, text="Welcome to Real Time Currency Converter", fg="blue", relief=tk.RAISED, borderwidth=3)
        self.intro_label.config(font=('Courier',15,'bold'))

        self.date_label = Label(self, text=f"1 Indian Repee equals = {self.currency_converter.convert('IND','USD',1)} USD \n Date: {self.currency_converter.date['date']}", relief=tk.GROOVE, borderwidth=5)
        
        self.intro_label.place(x=10, y=5)
        self.date_label.place(x=160, y=50)

        valid = (self.register(self.restrictNum),'%d','%P')
        self.amount_entry = Entry(self, bd=3, relief=tk.RIDGE, justify= tk.CENTER, validate='key', validatecommand=valid)
        self.converted_amount_label = Label(self, text='', fg='black', bg='white', relief=tk.RIDGE, justify=tk.CENTER,width=17, borderwidth=3)

        self.from_currency_value = StringVar(self)
        self.from_currency_value.set("INR") # default value
        self.to_currency_value = StringVar(self)
        self.to_currency_value.set("USD") # default value

        font = ("courier", 12, "bold")
        self.option_add("*TCombobox*Listbox.font", font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_value, values=list(self.currency_converter.currencies.keys()), font=font, state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_value, values=list(self.currency_converter.currencies.keys()), font=font, state='readonly', width=12, justify=tk.CENTER)

        self.convert_button = Button(self, text="Convert", fg="black", command=self.perform)
        self.convert_button.config(font=("courier", 10, "bold"))
        self.convert_button.place(x=225, y=135)

    def perform(self):
        amount = float(self.amount_entry.get())
        from_curr = self.from_currency_value.get()
        to_curr = self.to_currency_value.get()

        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        comverted_amoint = round(converted_amount, 2)

        self.converted_amount_label.config(text = str(converted_amount))

    def restricNum(self,action,string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <=1 and result is not None))



if __name__ == '__main__':
    # url = 'https://v6.exchangerate-api.com/v6/7ebc225413b1d3846a9a0042/latest/USD'
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeConverter(url)

    App(converter)
    mainloop()