from tkinter import *
import tkinter.ttk as ttk
import sqlite3


root = Tk()
root.title("Logbook")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
X = (screen_width/2) - (width/2)
Y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, X, Y))



# Databases
# Create the database or connect to one
conn = sqlite3.connect('logbook.db')

# Create cursor
c = conn.cursor()



# Create table
'''
c.execute("""CREATE TABLE logs(
        date text,
        odo integer,
        tripOdo real,
        liters real,
        ppl real,
        garage text
        )""")
'''

# Create submit function

def submit():
    # Create the database or connect to one
    conn = sqlite3.connect('logbook.db')

    # Create cursor
    c = conn.cursor()

    # Insert into Table


    c.execute("INSERT INTO logs VALUES(:date, :odo, :tripOdo, :liters, :ppl, :garage)",
              {
                  'date': date.get(),
                  'odo': odo.get(),
                  'tripOdo': tripOdo.get(),
                  'liters': liters.get(),
                  'ppl': ppl.get(),
                  'garage': garage.get()

              }



              )

    conn.commit()

    conn.close()

    # clear the text boxes
    date.delete(0, END)
    odo.delete(0, END)
    tripOdo.delete(0, END)
    liters.delete(0, END)
    ppl.delete(0, END)
    garage.delete(0, END)



# econ function

def econ():
    global t
    t = 0
            # Create the database or connect to one
    conn = sqlite3.connect('logbook.db')

    # Create cursor
    c = conn.cursor()

    #Query database
    c.execute("SELECT date, odo, tripOdo, round(liters,2), ppl, round(tripOdo/liters,2) AS  kpl, garage, round(liters*ppl,2) AS total  FROM logs ORDER BY kpl DESC")
    records = c.fetchall()
    print(records)
    tree.delete(*tree.get_children())
    for data in records:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
        t += 1
    conn.commit()

    conn.close()
    




# expens function

def expens():
        # Create the database or connect to one
    conn = sqlite3.connect('logbook.db')

    # Create cursor
    c = conn.cursor()

    #Query database
    c.execute("SELECT date, odo, tripOdo, round(liters,2), ppl, round(tripOdo/liters,2) AS  kpl, garage, round(liters*ppl,2) AS total  FROM logs ORDER BY Total DESC")
    records = c.fetchall()
    print(records)
    tree.delete(*tree.get_children())
    for data in records:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))

    conn.commit()

    conn.close()



# Create query function
def query():
    # Create the database or connect to one
    conn = sqlite3.connect('logbook.db')

    # Create cursor
    c = conn.cursor()

    #Query database
    # Can't do the round to 2 decimals
    
    c.execute("SELECT date, odo, tripOdo, round(liters,2), ppl, round(tripOdo/liters,2) AS  kpl, garage, round(liters*ppl,2) AS total  FROM logs")
    records = c.fetchall()
    print(records)
    tree.delete(*tree.get_children())
    for data in records:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))

    conn.commit()

    conn.close()


# Entries
date = Entry(root, width=30)
date.grid(row=0, column=1, padx=20, pady=5)
odo = Entry(root, width=30)
odo.grid(row=1, column=1, pady=5)
tripOdo = Entry(root, width=30)
tripOdo.grid(row=2, column=1, pady=5)
liters = Entry(root, width=30)
liters.grid(row=3, column=1, pady=5)
ppl = Entry(root, width=30)
ppl.grid(row=4, column=1, pady=5)
garage = Entry(root, width=30)
garage.grid(row=5, column=1, pady=5)

# Labels
date_label = Label(root, text="Date(dd-mm-yyyy):")
date_label.grid(row=0, column=0)
odo_label = Label(root, text="Odo meter:")
odo_label.grid(row=1, column=0)
trip_label = Label(root, text="Trip meter")
trip_label.grid(row=2, column=0)
liters_label = Label(root, text="Liters:")
liters_label.grid(row=3, column=0)
ppl_label = Label(root, text="Price per liter:")
ppl_label.grid(row=4, column=0)
garage_label = Label(root, text="Garage:")
garage_label.grid(row=5, column=0)

# Create Submit button
submit_btn = Button(root, text="Submit log", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# query button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Best economy button
econ_btn = Button(root, text="Best economy", command=econ)
econ_btn.grid(row=7, column=0, pady=5, padx=5)

# Most expesive button
expens_btn = Button(root, text="Most expensive trip", command=expens)
expens_btn.grid(row=7, column=1, pady=5, padx=5)


# Create list view
tree = ttk.Treeview(root, columns=("Date","ODO","Trip","Liters","Price per liter","Km/L" , "Garage", "Total"), selectmode="extended", height=20)

tree.heading('#0', text="Date", anchor=W)
tree.heading('Date', text="Date", anchor=W)
tree.heading('ODO', text="ODO", anchor=W)
tree.heading('Trip', text="Trip", anchor=W)
tree.heading('Liters', text="Liters", anchor=W)
tree.heading("#5", text="Price per liter", anchor=W)
tree.heading("#6", text="Km/L", anchor=W)
tree.heading('Garage', text="Garage", anchor=W)
tree.heading("#8", text="Total", anchor=W)

tree.column('#0', stretch=NO, minwidth=0, width=5)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=80)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.column('#8', stretch=NO, minwidth=0, width=80)
tree.grid(row=100, column=0, columnspan=100)





# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()


