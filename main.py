import tkinter as tk
from tkinter import ttk
import tkintermapview

playgrounds = []
employees = []
users = []

root = tk.Tk()
root.geometry("1200x800")
root.title("Zarzadzanie danymi")

selected_playground = tk.StringVar(root)


def clear_entries(entries):
    for entry in entries:
        entry.delete(0, tk.END)
    entries[0].focus()

def create_entity(entry_widgets, keys, storage, label_template):
    try:
        values = [entry.get().strip() for entry in entry_widgets]
        values[2] = float(values[2])
        values[3] = float(values[3])
        if not values[0] or not values[1]:
            return
        entity = dict(zip(keys, values))
        storage.append(entity)
        map_widget.set_marker(entity["lat"], entity["lon"], text=label_template.format(**entity))
        clear_entries(entry_widgets)
        return True
    except ValueError:
        return False

def update_listbox(listbox, storage, format_func):
    listbox.delete(0, tk.END)
    for idx, item in enumerate(storage):
        listbox.insert(idx, format_func(item))

def add_playground():
    if create_entity([entry_name, entry_lat, entry_lon], ["name", "lat", "lon"], playgrounds, "{name}"):
        update_listbox(playground_listbox, playgrounds, lambda p: f"{p['name']} ({p['lat']}, {p['lon']})")
        playground_combobox["values"] = [p["name"] for p in playgrounds]

def add_employee():
    if create_entity([entry_emp_name, entry_emp_surname, entry_emp_lat, entry_emp_lon, entry_emp_playground],
                     ["name", "surname", "lat", "lon", "playground"], employees, "{name} {surname}"):
        update_listbox(employee_listbox, employees, lambda e: f"{e['name']} {e['surname']} ({e['lat']}, {e['lon']}) [{e['playground']}]")

def add_user():
    if create_entity([entry_user_name, entry_user_surname, entry_user_lat, entry_user_lon, entry_user_playground],
                     ["name", "surname", "lat", "lon", "playground"], users, "{name} {surname}"):
        update_listbox(user_listbox, users, lambda u: f"{u['name']} {u['surname']} ({u['lat']}, {u['lon']}) [{u['playground']}]")

def show_on_map(source, label_template):
    map_widget.delete_all_marker()
    for item in source:
        if item["playground"] == selected_playground.get():
            map_widget.set_marker(item["lat"], item["lon"], text=label_template.format(**item))


frame_form = tk.Frame(root)
frame_form.grid(row=0, column=0, sticky="nw")

frame_map = tk.Frame(root)
frame_map.grid(row=0, column=1, rowspan=3, sticky="ne")

entry_emp_name = tk.Entry(frame_form); tk.Label(frame_form, text="Imie:").grid(row=0, column=0); entry_emp_name.grid(row=0, column=1)
entry_emp_surname = tk.Entry(frame_form); tk.Label(frame_form, text="Nazwisko:").grid(row=1, column=0); entry_emp_surname.grid(row=1, column=1)
entry_emp_lat = tk.Entry(frame_form); tk.Label(frame_form, text="Szerokosc (lat):").grid(row=2, column=0); entry_emp_lat.grid(row=2, column=1)
entry_emp_lon = tk.Entry(frame_form); tk.Label(frame_form, text="Dlugosc (lon):").grid(row=3, column=0); entry_emp_lon.grid(row=3, column=1)
entry_emp_playground = tk.Entry(frame_form); tk.Label(frame_form, text="Plac zabaw:").grid(row=4, column=0); entry_emp_playground.grid(row=4, column=1)
tk.Button(frame_form, text="Dodaj pracownika", command=add_employee).grid(row=5, column=0, columnspan=2)
employee_listbox = tk.Listbox(frame_form, width=50, height=5)
employee_listbox.grid(row=6, column=0, columnspan=2)

entry_name = tk.Entry(frame_form); tk.Label(frame_form, text="Nazwa placu:").grid(row=7, column=0); entry_name.grid(row=7, column=1)
entry_lat = tk.Entry(frame_form); tk.Label(frame_form, text="Szerokosc (lat):").grid(row=8, column=0); entry_lat.grid(row=8, column=1)
entry_lon = tk.Entry(frame_form); tk.Label(frame_form, text="Dlugosc (lon):").grid(row=9, column=0); entry_lon.grid(row=9, column=1)
tk.Button(frame_form, text="Dodaj plac", command=add_playground).grid(row=10, column=0, columnspan=2)
playground_listbox = tk.Listbox(frame_form, width=50, height=5)
playground_listbox.grid(row=11, column=0, columnspan=2)

entry_user_name = tk.Entry(frame_form); tk.Label(frame_form, text="Imie:").grid(row=12, column=0); entry_user_name.grid(row=12, column=1)
entry_user_surname = tk.Entry(frame_form); tk.Label(frame_form, text="Nazwisko:").grid(row=13, column=0); entry_user_surname.grid(row=13, column=1)
entry_user_lat = tk.Entry(frame_form); tk.Label(frame_form, text="Szerokosc (lat):").grid(row=14, column=0); entry_user_lat.grid(row=14, column=1)
entry_user_lon = tk.Entry(frame_form); tk.Label(frame_form, text="Dlugosc (lon):").grid(row=15, column=0); entry_user_lon.grid(row=15, column=1)
entry_user_playground = tk.Entry(frame_form); tk.Label(frame_form, text="Plac zabaw:").grid(row=16, column=0); entry_user_playground.grid(row=16, column=1)
tk.Button(frame_form, text="Dodaj uzytkownika", command=add_user).grid(row=17, column=0, columnspan=2)
user_listbox = tk.Listbox(frame_form, width=50, height=5)
user_listbox.grid(row=18, column=0, columnspan=2)

playground_combobox = ttk.Combobox(frame_form, textvariable=selected_playground)
playground_combobox.grid(row=19, column=0, columnspan=2)
tk.Button(frame_form, text="Pokaż pracownikow placu", command=lambda: show_on_map(employees, "{name} {surname}")).grid(row=20, column=0, columnspan=2)
tk.Button(frame_form, text="Pokaż uzytkownikow placu", command=lambda: show_on_map(users, "{name} {surname}")).grid(row=21, column=0, columnspan=2)

map_widget = tkintermapview.TkinterMapView(frame_map, width=800, height=600, corner_radius=0)
map_widget.pack()
map_widget.set_position(52.23, 21.01)
map_widget.set_zoom(6)

root.mainloop()
