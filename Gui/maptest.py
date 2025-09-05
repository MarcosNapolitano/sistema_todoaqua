import tkinter
import tkintermapview

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("map_view_example.py")

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

map_widget.set_position(37.3530005, -6.1411663)
map_widget.set_zoom(14)

map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

marker_1 = map_widget.set_address("Av. Camas 20, Bollullos de la Mitación, Spain", marker=True)

marker_2 = map_widget.set_address("Calle Castilla 38, Triana, Sevilla", marker=True)

path_1 = map_widget.set_path([marker_1.position, marker_2.position])
print(path_1)
root_tk.mainloop()