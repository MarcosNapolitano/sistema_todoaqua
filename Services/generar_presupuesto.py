from tkinter import messagebox
from BBDD.connect import get_single
from Models.Cliente import Cliente
from Models.Presupuesto import Presupuesto_Lamina
from Models.Presupuesto import Presupuesto_Repa
from Models.Presupuesto import Presupuesto_Fuga_Piscinas
from Models.Presupuesto import Presupuesto_Todo_Fugas

def generar_presupuesto(id_pres: int):

    presupuesto = get_single(
        "SELECT TIPO, ID_CLIENTE FROM PRESUPUESTOS WHERE ID_PRESUPUESTO = %s",
        (id_pres,),
    )

    cliente = Cliente()
    cliente = cliente.object_cliente(presupuesto["id_cliente"])

    match presupuesto["tipo"]:
        case "fuga piscinas":

            presupuesto = Presupuesto_Fuga_Piscinas()
            presupuesto = presupuesto.object_presupuesto_piscina(id_pres)

            try:
                presupuesto.generar_archivo_presupuesto(cliente, presupuesto)

            except:
                messagebox.showerror(
                    title="Sistema de Gestión Todo Aqua",
                    message=f"Error al generar presupuesto. Contacte al administrador.",
                )

                return

            del cliente
            del presupuesto

        case "todo fugas":

            presupuesto = Presupuesto_Todo_Fugas()
            presupuesto = presupuesto.object_presupuesto_fuga(id_pres)
            try:
                presupuesto.generar_archivo_presupuesto(cliente, presupuesto)

            except:
                messagebox.showerror(
                    title="Sistema de Gestión Todo Aqua",
                    message=f"Error al generar presupuesto. Contacte al administrador.",
                )

                return

            del cliente
            del presupuesto

        case "reparación":

            presupuesto = Presupuesto_Repa()
            presupuesto = presupuesto.object_presupuesto_repa(id_pres)
            try:
                presupuesto.generar_archivo_presupuesto(cliente, presupuesto)

            except:
                messagebox.showerror(
                    title="Sistema de Gestión Todo Aqua",
                    message=f"Error al generar presupuesto. Contacte al administrador.",
                )

                return

            del cliente
            del presupuesto

        case "lámina armada":

            presupuesto = Presupuesto_Lamina()
            presupuesto = presupuesto.object_presupuesto_lamina(id_pres)
            try:
                presupuesto.generar_archivo_presupuesto(cliente, presupuesto)

            except:
                messagebox.showerror(
                    title="Sistema de Gestión Todo Aqua",
                    message=f"Error al generar presupuesto. Contacte al administrador.",
                )

                return

            del cliente
            del presupuesto

    messagebox.showinfo(
        title="Sistema de Gestión Todo Aqua",
        message=f"Presupuesto generado correctamente.",
    )

    return
