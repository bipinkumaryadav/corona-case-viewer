from tkinter import *
import tkinter.messagebox as msg
import urllib.request
from bs4 import BeautifulSoup
from tkinter import ttk

conf_case = ""
active_case = ""
recv_case = ""
death_case = ""

def main(state):
    url = "https://coronaclusters.in/"+state
    response = urllib.request.urlopen(url)

    soup = BeautifulSoup(response, "html.parser")
    value = soup.findAll('h5', {'class': 'card-title text-md text-md-lg'})
    return value[0].text, value[1].text, value[2].text, value[3].text


def case(case1, case2, case3, case4):
    conf_label.configure(text=f"Confirmed Cases\n{case1}")
    active_label.configure(text=f"Active Cases\n{case2}")
    recv_label.configure(text=f"Recovered Cases\n{case3}")
    death_label.configure(text=f"Deaths\n{case4}")


def submit():
    state_key = state_var.get()
    state = state_dic[state_key]
    try:
        conf, active, recv, death = main(state)
        case(conf, active, recv, death)
    except:
        msg.showerror("Error", "Don't get the data \nMaybe there is no data on website")


win = Tk()
win.title("CORONA CASES VIEWER")
win.maxsize(500, 400)
win.minsize(500, 400)
state_dic = {'Maharashtra': 'maharashtra', 'Kerala': 'kerala', 'Karnataka': 'karnataka',
             'Delhi': 'delhi', 'Uttar Pradesh': 'uttar-pradesh', 'Telangana': 'telangana',
             'Gujarat': 'gujarat', 'Rajasthan': 'rajasthan', 'Tamil Nadu': 'tamil-nadu',
             'Madhya Pradesh': 'madhya-pradesh', 'Jammu and Kashmir': 'jammu-and-kashmir',
             'Punjab': 'punjab', 'Haryana': 'haryana', 'Andhra Pradesh': 'andhra-pradesh',
             'West Bengal': 'west-bengal', 'Bihar': 'Bihar', 'Ladakh': 'ladakh',
             'Andaman and Nicobar Islands': 'andaman-and-nicobar-islands', 'Chandigarh': 'chandigarh',
             'Chhattisgarh': 'chhattisgarh', 'Uttarakhand': 'uttarakhand', 'Goa': 'goa',
             'Himachal Pradesh': 'himachal-pradesh', 'Odisha': 'odisha', 'Manipur': 'manipur',
             'Mizoram': 'mizoram', 'Puducherry': 'puducherry', 'Arunachal Pradesh': 'arunachal-pradesh',
             'Assam': 'Assam', 'Dadra and Nagar Haveli': 'dadra-and-nagar-haveli', 'Daman and Diu': 'daman-and-diu',
             'Jharkhand': 'jharkhand', 'Lakshadweep': 'lakshadweep', 'Meghalaya': 'meghalaya',
             'Nagaland': 'nagaland', 'Sikkim': 'sikkim', 'Tripura': 'tripura'}

state_var = StringVar()
state_var.set('State')

entry_label = Label(win, text="State", font=("Courier", 16))
entry_label.pack(anchor='n', pady=7)
options = ttk.Combobox(win, width=75, textvariable=state_var)
options['value'] = (
    'Maharashtra', 'Kerala', 'Karnataka', 'Delhi', 'Uttar Pradesh', 'Telangana', 'Gujarat', 'Rajasthan',
    'Tamil Nadu', 'Madhya Pradesh', 'Jammu and Kashmir', 'Punjab',
    'Haryana', 'Andhra Pradesh', 'West Bengal', 'Bihar', 'Ladakh',
    'Andaman and Nicobar Islands', 'Chandigarh', 'Chhattisgarh', 'Uttarakhand', 'Goa',
    'Himachal Pradesh', 'Odisha', 'Manipur', 'Mizoram', 'Puducherry',
    'Arunachal Pradesh', 'Assam', 'Dadra and Nagar Haveli', 'Daman and Diu',
    'Jharkhand', 'Lakshadweep', 'Meghalaya', 'Nagaland', 'Sikkim', 'Tripura'
)
options.pack()

but = Button(win, text="Submit", command=submit)
but.pack()

F1 = Frame(win)
F1.pack()
conf_label = Label(F1, text="Confirmed Cases\n", font=("Courier", 16))
conf_label.pack(side=LEFT, anchor='nw', pady=20, padx=20)

active_label = Label(F1, text="Active Cases\n", font=("Courier", 16))
active_label.pack(side=RIGHT, anchor='ne', pady=20, padx=10)

F2 = Frame(win)
F2.pack(side=LEFT, anchor='n')
recv_label = Label(F2, text="Recovered Cases", font=("Courier", 16))
recv_label.pack(side=LEFT, anchor='nw', pady=20, padx=50)

death_label = Label(F2, text="Deaths", font=("Courier", 16))
death_label.pack(side=RIGHT, anchor='ne', pady=20, padx=10)

win.mainloop()
