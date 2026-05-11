from consultorio import Consultorio


def organizar_atendimentos(
    atendimentos
):

    atendimentos.sort(
        key=lambda a: (
            not a.expresso,
            a.inicio
        )
    )

    consultorios = []

    for atendimento in atendimentos:

        alocado = False

        for consultorio in consultorios:

            if consultorio.pode_adicionar(
                atendimento
            ):

                consultorio.adicionar(
                    atendimento
                )

                alocado = True

                break

        if not alocado:

            novo = Consultorio(
                len(consultorios) + 1
            )

            novo.adicionar(
                atendimento
            )

            consultorios.append(
                novo
            )

    return consultorios