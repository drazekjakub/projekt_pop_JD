import tkinter as tk
from tkinter import ttk
import tkintermapview

playgrounds = []
employees = []
users = []

playground_id_counter = 1

root = tk.Tk()
root.geometry("1200x800")
root.title("Zarzadzanie danymi")

selected_playground_id = tk.StringVar(root)

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
    global playground_id_counter
    name = entry_name.get().strip()
    try:
        lat = float(entry_lat.get())
        lon = float(entry_lon.get())
    except ValueError:
        return
    if not name:
        return
    playground = {"id": playground_id_counter, "name": name, "lat": lat, "lon": lon}
    playground_id_counter += 1
    playgrounds.append(playground)
    map_widget.set_marker(lat, lon, text=name)
    clear_entries([entry_name, entry_lat, entry_lon])
    update_listbox(playground_listbox, playgrounds, lambda p: f"{p['name']} ({p['lat']}, {p['lon']})")
    playground_combobox["values"] = [f"{p['id']} - {p['name']}" for p in playgrounds]

def get_selected_playground_id():
    try:
        return int(selected_playground_id.get().split(" - ")[0])
    except:
        return None

def add_employee():
    pid = get_selected_playground_id()
    if pid is None:
        return
    if create_entity([entry_emp_name, entry_emp_surname, entry_emp_lat, entry_emp_lon],
                     ["name", "surname", "lat", "lon"], employees, "{name} {surname}"):
        employees[-1]["playground_id"] = pid
        update_listbox(employee_listbox, employees, lambda e: f"{e['name']} {e['surname']} ({e['lat']}, {e['lon']}) [Plac ID: {e['playground_id']}]")

def add_user():
    pid = get_selected_playground_id()
    if pid is None:
        return
    if create_entity([entry_user_name, entry_user_surname, entry_user_lat, entry_user_lon],
                     ["name", "surname", "lat", "lon"], users, "{name} {surname}"):
        users[-1]["playground_id"] = pid
        update_listbox(user_listbox, users, lambda u: f"{u['name']} {u['surname']} ({u['lat']}, {u['lon']}) [Plac ID: {u['playground_id']}]")

def show_on_map(source, label_template):
    pid = get_selected_playground_id()
    if pid is None:
        return
    map_widget.delete_all_marker()
    for item in source:
        if item.get("playground_id") == pid:
            map_widget.set_marker(item["lat"], item["lon"], text=label_template.format(**item))

frame_form = tk.Frame(root)
frame_form.grid(row=0, column=0, sticky="nw")

frame_map = tk.Frame(root)
frame_map.grid(row=0, column=1, rowspan=3, sticky="ne")

entry_emp_name = tk.Entry(frame_form); tk.Label(frame_form, text="Imie:").grid(row=0, column=0); entry_emp_name.grid(row=0, column=1)
entry_emp_surname = tk.Entry(frame_form); tk.Label(frame_form, text="Nazwisko:").grid(row=1, column=0); entry_emp_surname.grid(row=1, column=1)
entry_emp_lat = tk.Entry(frame_form); tk.Label(frame_form, text="Szerokosc (lat):").grid(row=2, column=0); entry_emp_lat.grid(row=2, column=1)
entry_emp_lon = tk.Entry(frame_form); tk.Label(frame_form, text="Dlugosc (lon):").grid(row=3, column=0); entry_emp_lon.grid(row=3, column=1)
tk.Button(frame_form, text="Dodaj pracownika", command=add_employee).grid(row=4, column=0, columnspan=2)
employee_listbox = tk.Listbox(frame_form, width=50, height=5)
employee_listbox.grid(row=5, column=0, columnspan=2)

entry_name = tk.Entry(frame_form); tk.Label(frame_form, text="Nazwa placu:").grid(row=6, column=0); entry_name.grid(row=6, column=1)
entry_lat = tk.Entry(frame_form); tk.Label(frame_form, text="Szerokosc (lat):").grid(row=7, column=0); entry_lat.grid(row=7, column=1)
entry_lon = tk.Entry(frame_form); tk.Label(frame_form, text="Dlugosc (lon):").grid(row=8, column=0); entry_lon.grid(row=8, column=1)
tk.Button(frame_form, text="Dodaj plac", command=add_playground).grid(row=9, column=0, columnspan=2)
playground_listbox = tk.Listbox(frame_form, width=50, height=5)
playground_listbox.grid(row=10, column=0, columnspan=2)

entry_user_name = tk.Entry(frame_form); tk.Label(frame_form, text="Imie:").grid(row=11, column=0); entry_user_name.grid(row=11, column=1)
entry_user_surname = tk.Entry(frame_form); tk.Label(frame_form, text="Nazwisko:").grid(row=12, column=0); entry_user_surname.grid(row=12, column=1)
entry_user_lat = tk.Entry(frame_form); tk.Label(frame_form, text="Szerokosc (lat):").grid(row=13, column=0); entry_user_lat.grid(row=13, column=1)
entry_user_lon = tk.Entry(frame_form); tk.Label(frame_form, text="Dlugosc (lon):").grid(row=14, column=0); entry_user_lon.grid(row=14, column=1)
tk.Button(frame_form, text="Dodaj uzytkownika", command=add_user).grid(row=15, column=0, columnspan=2)
entry_user_playground = None  # usuwamy pole, bo teraz wybór placu jest przez combobox
user_listbox = tk.Listbox(frame_form, width=50, height=5)
user_listbox.grid(row=16, column=0, columnspan=2)

playground_combobox = ttk.Combobox(frame_form, textvariable=selected_playground_id)
playground_combobox.grid(row=17, column=0, columnspan=2)
tk.Button(frame_form, text="Pokaż pracownikow placu", command=lambda: show_on_map(employees, "{name} {surname}")).grid(row=18, column=0, columnspan=2)
tk.Button(frame_form, text="Pokaż uzytkownikow placu", command=lambda: show_on_map(users, "{name} {surname}")).grid(row=19, column=0, columnspan=2)

map_widget = tkintermapview.TkinterMapView(frame_map, width=800, height=600, corner_radius=0)
map_widget.pack()
map_widget.set_position(52.23, 21.01)
map_widget.set_zoom(6)

root.mainloop()
