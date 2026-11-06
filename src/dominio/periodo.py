"""Periodo — início e fim (datas do curso, período de inscrição).

Stub: o construtor só guarda os dados. A regra "fim não antes do início"
(US-01 c3) pertence à criação do curso e será exigida pelos testes da US-01,
por isso não está aqui.
"""
from __future__ import annotations

from datetime import date


class Periodo:
    """Um intervalo de datas (US-01 c3)."""

    def __init__(self, inicio: date, fim: date) -> None:
        self.inicio = inicio
        self.fim = fim

    def contem(self, dia: date) -> bool:
        """US-03 c2 · US-07 c4 — o dia cai dentro do período?"""
        raise NotImplementedError(
            "US-03 c2 / US-07 c4: implemente Periodo.contem(dia)"
        )
