"""Curso — o centro do domínio.

Stub: guardador de dados com os atributos do diagrama em
docs/projeto/02-classes.md. Os métodos do passo 3 (`editar`,
`adicionar_modulo`, `publicar`, `aceita_inscricoes`, `situacao`, `inscrever`…)
ainda não existem: entram junto com os testes das histórias que os exigem
(US-01, US-02, US-03, US-06, US-07).

Para a US-08, apenas os atributos `inscricoes` e `modulos` são usados.
"""
from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING

from dominio.enums import Modalidade, StatusCurso
from dominio.modulo import Modulo
from dominio.periodo import Periodo

if TYPE_CHECKING:  # só para anotações; evita import circular com Inscricao
    from dominio.inscricao import Inscricao


class Curso:
    """Um curso online, em rascunho ou publicado."""

    def __init__(
        self,
        nome: str,
        descricao: str,
        cronograma: str | None,
        modalidade: Modalidade,
        carga_horaria: int,
        datas: Periodo,
        periodo_inscricao: Periodo,
        vagas: int,
        valor_matricula: Decimal,
        status: StatusCurso,
        modulos: list[Modulo] | None = None,
        inscricoes: list[Inscricao] | None = None,
    ) -> None:
        self.nome = nome
        self.descricao = descricao
        self.cronograma = cronograma
        self.modalidade = modalidade
        self.carga_horaria = carga_horaria
        self.datas = datas
        self.periodo_inscricao = periodo_inscricao
        self.vagas = vagas
        self.valor_matricula = valor_matricula
        self.status = status
        self.modulos = modulos if modulos is not None else []
        self.inscricoes = inscricoes if inscricoes is not None else []
