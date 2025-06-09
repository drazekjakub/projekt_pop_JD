import tkinter as tk
import tkintermapview

# Lista placów zabaw
playgrounds = []

# --- Funkcje ---

def add_playground():
    try:
        name = entry_name.get().strip()
        lat = float(entry_lat.get())
        lon = float(entry_lon.get())

        if not name:
            print("Nazwa nie może być pusta")
            return

        playground = {"name": name, "lat": lat, "lon": lon}
        playgrounds.append(playground)

        # Dodaj marker na mapie
        map_widget.set_marker(lat, lon, text=name)

        # Wyczyść pola
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

# --- GUI ---

root = tk.Tk()
root.geometry("1200x750")
root.title("Zarządzanie placami zabaw")

# --- Ramki ---

ramka_formularz = tk.Frame(root, padx=10, pady=10)
ramka_formularz.grid(row=0, column=0, sticky="nw")

ramka_mapa = tk.Frame(root, padx=10, pady=10)
ramka_mapa.grid(row=0, column=1, sticky="ne")

# --- Formularz dodawania placów zabaw ---

tk.Label(ramka_formularz, text="Dodaj plac zabaw", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

tk.Label(ramka_formularz, text="Nazwa placu:").grid(row=1, column=0, sticky=tk.W)
entry_name = tk.Entry(ramka_formularz)
entry_name.grid(row=1, column=1)

tk.Label(ramka_formularz, text="Szerokość (lat):").grid(row=2, column=0, sticky=tk.W)
entry_lat = tk.Entry(ramka_formularz)
entry_lat.grid(row=2, column=1)

tk.Label(ramka_formularz, text="Długość (lon):").grid(row=3, column=0, sticky=tk.W)
entry_lon = tk.Entry(ramka_formularz)
entry_lon.grid(row=3, column=1)

btn_dodaj = tk.Button(ramka_formularz, text="Dodaj plac", command=add_playground)
btn_dodaj.grid(row=4, column=0, columnspan=2, pady=10)

# --- Lista placów zabaw ---

tk.Label(ramka_formularz, text="Lista placów zabaw:").grid(row=5, column=0, columnspan=2, pady=(10, 0))
listbox = tk.Listbox(ramka_formularz, width=40, height=10)
listbox.grid(row=6, column=0, columnspan=2)

# --- Mapa ---

map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=800, height=600, corner_radius=0)
map_widget.pack()
map_widget.set_position(52.23, 21.01)  # Centrum Polski
map_widget.set_zoom(6)

# --- Uruchomienie ---

root.mainloop()
