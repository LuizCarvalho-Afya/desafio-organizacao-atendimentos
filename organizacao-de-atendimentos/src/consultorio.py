class Consultorio:

    def __init__(self, numero):

        self.numero = numero

        self.atendimentos = []

    def pode_adicionar(
        self,
        atendimento
    ):

        if not self.atendimentos:
            return True

        ultimo = self.atendimentos[-1]

        return (
            atendimento.inicio
            >=
            ultimo.fim
        )

    def adicionar(
        self,
        atendimento
    ):

        self.atendimentos.append(
            atendimento
        )

    def __repr__(self):

        texto = (
            f"CONSULTÓRIO "
            f"{self.numero}\n"
        )

        for atendimento in self.atendimentos:

            texto += (
                f" - "
                f"{atendimento}\n"
            )

        return texto