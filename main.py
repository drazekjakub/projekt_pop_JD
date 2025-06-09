import tkinter as tk
import tkintermapview

playgrounds = []
employees = []
users = []

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
root.title("Zarządzanie użytkownikami")

frame_form = tk.Frame(root, padx=10, pady=10)
frame_form.grid(row=0, column=0, sticky="nw")

frame_map = tk.Frame(root, padx=10, pady=10)
frame_map.grid(row=0, column=1, sticky="ne")

tk.Label(frame_form, text="Dodaj użytkownika", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=(0, 10))
tk.Label(frame_form, text="Imię:").grid(row=1, column=0, sticky=tk.W)
entry_user_name = tk.Entry(frame_form)
entry_user_name.grid(row=1, column=1)
tk.Label(frame_form, text="Nazwisko:").grid(row=2, column=0, sticky=tk.W)
entry_user_surname = tk.Entry(frame_form)
entry_user_surname.grid(row=2, column=1)
tk.Label(frame_form, text="Szerokość (lat):").grid(row=3, column=0, sticky=tk.W)
entry_user_lat = tk.Entry(frame_form)
entry_user_lat.grid(row=3, column=1)
tk.Label(frame_form, text="Długość (lon):").grid(row=4, column=0, sticky=tk.W)
entry_user_lon = tk.Entry(frame_form)
entry_user_lon.grid(row=4, column=1)
tk.Label(frame_form, text="Plac zabaw:").grid(row=5, column=0, sticky=tk.W)
entry_user_playground = tk.Entry(frame_form)
entry_user_playground.grid(row=5, column=1)
tk.Button(frame_form, text="Dodaj użytkownika", command=add_user).grid(row=6, column=0, columnspan=2, pady=10)
tk.Label(frame_form, text="Lista użytkowników:").grid(row=7, column=0, columnspan=2, pady=(10, 0))
user_listbox = tk.Listbox(frame_form, width=50, height=10)
user_listbox.grid(row=8, column=0, columnspan=2)

map_widget = tkintermapview.TkinterMapView(frame_map, width=800, height=600, corner_radius=0)
map_widget.pack()
map_widget.set_position(52.23, 21.01)
map_widget.set_zoom(6)

root.mainloop()
