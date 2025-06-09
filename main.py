import tkinter as tk
import tkintermapview

# --- Dane ---
employees = []

# --- Funkcje ---

def add_employee():
    try:
        name = entry_emp_name.get().strip()
        surname = entry_emp_surname.get().strip()
        lat = float(entry_emp_lat.get())
        lon = float(entry_emp_lon.get())
        playground = entry_emp_playground.get().strip()

        if not name or not surname:
            print("Imię i nazwisko są wymagane")
            return

        employee = {
            "name": name,
            "surname": surname,
            "lat": lat,
            "lon": lon,
            "playground": playground
        }

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

# --- GUI ---

root = tk.Tk()
root.geometry("1200x800")
root.title("Pracownicy placów zabaw")

# --- Ramki ---

frame_form = tk.Frame(root, padx=10, pady=10)
frame_form.grid(row=0, column=0, sticky="nw")

frame_map = tk.Frame(root, padx=10, pady=10)
frame_map.grid(row=0, column=1, sticky="ne")

# --- Formularz pracownika ---

tk.Label(frame_form, text="Dodaj pracownika", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

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

# --- Lista pracowników ---
tk.Label(frame_form, text="Lista pracowników:").grid(row=7, column=0, columnspan=2, pady=(10, 0))
employee_listbox = tk.Listbox(frame_form, width=50, height=10)
employee_listbox.grid(row=8, column=0, columnspan=2)

# --- Mapa ---
map_widget = tkintermapview.TkinterMapView(frame_map, width=800, height=600, corner_radius=0)
map_widget.pack()
map_widget.set_position(52.23, 21.01)  # Centrum Polski
map_widget.set_zoom(6)

# --- Uruchomienie ---
root.mainloop()
