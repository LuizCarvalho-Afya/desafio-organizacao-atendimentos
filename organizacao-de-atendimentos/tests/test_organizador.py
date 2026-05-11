import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../src"
        )
    )
)

from atendimento import Atendimento
from organizador import organizar_atendimentos


def test_criacao_consultorios():

    atendimentos = [
        Atendimento("João", 8, 10),
        Atendimento("Maria", 8, 9),
        Atendimento("Pedro", 9, 10),
    ]

    consultorios = organizar_atendimentos(
        atendimentos
    )

    assert len(consultorios) == 2


def test_atendimento_expresso():

    atendimentos = [
        Atendimento(
            "Normal",
            8,
            9,
            False
        ),

        Atendimento(
            "Expresso",
            8,
            9,
            True
        )
    ]

    consultorios = organizar_atendimentos(
        atendimentos
    )

    primeiro = (
        consultorios[0]
        .atendimentos[0]
        .nome
    )

    assert primeiro == "Expresso"