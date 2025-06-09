import tkinter as tk
import tkintermapview

playgrounds = []
employees = []
users = []

def add_playground():
    try:
        name = entry_name.get().strip()
        lat = float(entry_lat.get())
        lon = float(entry_lon.get())
        if not name:
            return
        playground = {"name": name, "lat": lat, "lon": lon}
        playgrounds.append(playground)
        map_widget.set_marker(lat, lon, text=name)
        entry_name.delete(0, tk.END)
        entry_lat.delete(0, tk.END)
        entry_lon.delete(0, tk.END)
        entry_name.focus()
        update_list()
    except ValueError:
        print("Błąd: współrzędne muszą być liczbami")

def update_list():
    listbox.delete(0, tk.END)
    for idx, p in enumerate(playgrounds):
        listbox.insert(idx, f"{p['name']} ({p['lat']}, {p['lon']})")

def add_employee():
    try:
        name = entry_emp_name.get().strip()
        surname = entry_emp_surname.get().strip()
        lat = float(entry_emp_lat.get())
        lon = float(entry_emp_lon.get())
        playground = entry_emp_playground.get().strip()
        if not name or not surname:
            return
        employee = {"name": name, "surname": surname, "lat": lat, "lon": lon, "playground": playground}
        employees.append(employee)
        map_widget.set_marker(lat, lon, text=f"{name} {surname}")
        entry_emp_name.delete(0, tk.END)
        entry_emp_surname.delete(0, tk.END)
        entry_emp_lat.delete(0, tk.END)
        entry_emp_lon.delete(0, tk.END)
        entry_emp_playground.delete(0, tk.END)
        entry_emp_name.focus()
        update_employee_list()
    except ValueError:
        print("Błąd: współrzędne muszą być liczbami")

def update_employee_list():
    employee_listbox.delete(0, tk.END)
    for idx, emp in enumerate(employees):
        employee_listbox.insert(idx, f"{emp['name']} {emp['surname']} ({emp['lat']}, {emp['lon']}) [{emp['playground']}]")

def add_user():
    try:
        name = entry_user_name.get().strip()
        surname = entry_user_surname.get().strip()
        lat = float(entry_user_lat.get())
        lon = float(entry_user_lon.get())
        playground = entry_user_playground.get().strip()
        if not name or not surname:
            return
        user = {"name": name, "surname": surname, "lat": lat, "lon": lon, "playground": playground}
        users.append(user)
        map_widget.set_marker(lat, lon, text=f"{name} {surname}")
        entry_user_name.delete(0, tk.END)
        entry_user_surname.delete(0, tk.END)
        entry_user_lat.delete(0, tk.END)
        entry_user_lon.delete(0, tk.END)
        entry_user_playground.delete(0, tk.END)
        entry_user_name.focus()
        update_user_list()
    except ValueError:
        print("Błąd: współrzędne muszą być liczbami")

def update_user_list():
    user_listbox.delete(0, tk.END)
    for idx, user in enumerate(users):
        user_listbox.insert(idx, f"{user['name']} {user['surname']} ({user['lat']}, {user['lon']}) [{user['playground']}]")

root = tk.Tk()
root.geometry("1200x800")
root.title("Zarządzanie danymi")

frame_form = tk.Frame(root, padx=10, pady=10)
frame_form.grid(row=0, column=0, sticky="nw")

ramka_formularz = tk.Frame(root, padx=10, pady=10)
ramka_formularz.grid(row=1, column=0, sticky="sw")

ramka_uzytkownicy = tk.Frame(root, padx=10, pady=10)
ramka_uzytkownicy.grid(row=2, column=0, sticky="sw")

ramka_mapa = tk.Frame(root, padx=10, pady=10)
ramka_mapa.grid(row=0, column=1, rowspan=3, sticky="ne")

# Pracownicy
tk.Label(frame_form, text="Dodaj pracownika", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2)
tk.Label(frame_form, text="Imię:").grid(row=1, column=0, sticky=tk.W)
entry_emp_name = tk.Entry(frame_form)
entry_emp_name.grid(row=1, column=1)
tk.Label(frame_form, text="Nazwisko:").grid(row=2, column=0, sticky=tk.W)
entry_emp_surname = tk.Entry(frame_form)
entry_emp_surname.grid(row=2, column=1)
tk.Label(frame_form, text="Szerokość (lat):").grid(row=3, column=0, sticky=tk.W)
entry_emp_lat = tk.Entry(frame_form)
entry_emp_lat.grid(row=3, column=1)
tk.Label(frame_form, text="Długość (lon):").grid(row=4, column=0, sticky=tk.W)
entry_emp_lon = tk.Entry(frame_form)
entry_emp_lon.grid(row=4, column=1)
tk.Label(frame_form, text="Plac zabaw:").grid(row=5, column=0, sticky=tk.W)
entry_emp_playground = tk.Entry(frame_form)
entry_emp_playground.grid(row=5, column=1)
tk.Button(frame_form, text="Dodaj pracownika", command=add_employee).grid(row=6, column=0, columnspan=2, pady=10)
tk.Label(frame_form, text="Lista pracowników:").grid(row=7, column=0, columnspan=2)
employee_listbox = tk.Listbox(frame_form, width=50, height=6)
employee_listbox.grid(row=8, column=0, columnspan=2)

# Place zabaw
tk.Label(ramka_formularz, text="Dodaj plac zabaw", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2)
tk.Label(ramka_formularz, text="Nazwa placu:").grid(row=1, column=0, sticky=tk.W)
entry_name = tk.Entry(ramka_formularz)
entry_name.grid(row=1, column=1)
tk.Label(ramka_formularz, text="Szerokość (lat):").grid(row=2, column=0, sticky=tk.W)
entry_lat = tk.Entry(ramka_formularz)
entry_lat.grid(row=2, column=1)
tk.Label(ramka_formularz, text="Długość (lon):").grid(row=3, column=0, sticky=tk.W)
entry_lon = tk.Entry(ramka_formularz)
entry_lon.grid(row=3, column=1)
tk.Button(ramka_formularz, text="Dodaj plac", command=add_playground).grid(row=4, column=0, columnspan=2, pady=10)
tk.Label(ramka_formularz, text="Lista placów zabaw:").grid(row=5, column=0, columnspan=2)
listbox = tk.Listbox(ramka_formularz, width=40, height=6)
listbox.grid(row=6, column=0, columnspan=2)

# Użytkownicy
tk.Label(ramka_uzytkownicy, text="Dodaj użytkownika", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2)
tk.Label(ramka_uzytkownicy, text="Imię:").grid(row=1, column=0, sticky=tk.W)
entry_user_name = tk.Entry(ramka_uzytkownicy)
entry_user_name.grid(row=1, column=1)
tk.Label(ramka_uzytkownicy, text="Nazwisko:").grid(row=2, column=0, sticky=tk.W)
entry_user_surname = tk.Entry(ramka_uzytkownicy)
entry_user_surname.grid(row=2, column=1)
tk.Label(ramka_uzytkownicy, text="Szerokość (lat):").grid(row=3, column=0, sticky=tk.W)
entry_user_lat = tk.Entry(ramka_uzytkownicy)
entry_user_lat.grid(row=3, column=1)
tk.Label(ramka_uzytkownicy, text="Długość (lon):").grid(row=4, column=0, sticky=tk.W)
entry_user_lon = tk.Entry(ramka_uzytkownicy)
entry_user_lon.grid(row=4, column=1)
tk.Label(ramka_uzytkownicy, text="Plac zabaw:").grid(row=5, column=0, sticky=tk.W)
entry_user_playground = tk.Entry(ramka_uzytkownicy)
entry_user_playground.grid(row=5, column=1)
tk.Button(ramka_uzytkownicy, text="Dodaj użytkownika", command=add_user).grid(row=6, column=0, columnspan=2, pady=10)
tk.Label(ramka_uzytkownicy, text="Lista użytkowników:").grid(row=7, column=0, columnspan=2)
user_listbox = tk.Listbox(ramka_uzytkownicy, width=50, height=6)
user_listbox.grid(row=8, column=0, columnspan=2)

map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=800, height=600, corner_radius=0)
map_widget.pack()
map_widget.set_position(52.23, 21.01)
map_widget.set_zoom(6)

root.mainloop()
