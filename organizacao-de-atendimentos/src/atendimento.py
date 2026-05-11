class Atendimento:
    def __init__(
        self,
        nome,
        inicio,
        fim,
        expresso=False
    ):
        self.nome = nome
        self.inicio = inicio
        self.fim = fim
        self.expresso = expresso

    def __repr__(self):

        tipo = (
            "EXPRESSO"
            if self.expresso
            else "NORMAL"
        )

        return (
            f"{self.nome} "
            f"({self.inicio}-{self.fim}) "
            f"[{tipo}]"
        )