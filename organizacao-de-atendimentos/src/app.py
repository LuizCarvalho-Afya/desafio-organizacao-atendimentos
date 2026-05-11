import tkinter as tk

from atendimento import Atendimento
from organizador import organizar_atendimentos


horarios = [
    "08:00",
    "09:00",
    "10:00",
    "11:00",
    "14:00",
    "15:00",
    "16:00"
]

atendimentos = []


def hora_para_int(hora):

    return int(
        hora.split(":")[0]
    )


def agendar(hora):

    nome = entry_nome.get().strip()

    if not nome:
        return

    inicio = hora_para_int(hora)

    fim = inicio + 1

    expresso = var_expresso.get()

    novo = Atendimento(
        nome,
        inicio,
        fim,
        expresso
    )

    atendimentos.append(novo)

    atualizar_interface()

    entry_nome.delete(
        0,
        tk.END
    )

    var_expresso.set(False)


def atualizar_interface():

    for widget in frame_horarios.winfo_children():

        widget.destroy()

    horas_ocupadas = []

    for atendimento in atendimentos:

        horas_ocupadas.append(
            f"{atendimento.inicio:02d}:00"
        )

    for hora in horarios:

        ocupado = (
            hora in horas_ocupadas
        )

        cor = (
            "#F33939"
            if ocupado
            else "#28a745"
        )

        texto = (
            f"{hora} - INDISPONÍVEL"
            if ocupado
            else f"{hora} - DISPONÍVEL"
        )

        botao = tk.Button(
            frame_horarios,
            text=texto,
            bg=cor,
            fg="white",
            width=25,
            state=(
                "disabled"
                if ocupado
                else "normal"
            ),
            command=lambda h=hora:
            agendar(h)
        )

        botao.pack(pady=3)

    resultado.delete(
        "1.0",
        tk.END
    )

    consultorios = (
        organizar_atendimentos(
            atendimentos
        )
    )

    for consultorio in consultorios:

        resultado.insert(
            tk.END,
            f"{consultorio}\n"
        )


janela = tk.Tk()

janela.title(
    "Organização de Atendimentos"
)

janela.geometry("700x650")

janela.configure(
    bg="#102542"
)

titulo = tk.Label(
    janela,
    text="ORGANIZAÇÃO DE ATENDIMENTOS",
    bg="#102542",
    fg="white",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=15)

tk.Label(
    janela,
    text="Nome do Paciente",
    bg="#102542",
    fg="white"
).pack()

entry_nome = tk.Entry(
    janela,
    width=30,
    font=("Arial", 12)
)

entry_nome.pack(pady=5)

var_expresso = tk.BooleanVar()

check = tk.Checkbutton(
    janela,
    text="Atendimento Expresso",
    variable=var_expresso,
    bg="#102542",
    fg="white",
    selectcolor="#102542"
)

check.pack(pady=10)

frame_horarios = tk.Frame(
    janela,
    bg="#102542"
)

frame_horarios.pack(pady=10)

resultado = tk.Text(
    janela,
    width=70,
    height=18,
    font=("Arial", 10)
)

resultado.pack(pady=15)

atualizar_interface()

janela.mainloop()