"""Modulo — parte de um curso (composição), com título, link e data opcional.

Stub: guardador de dados. A regra "link precisa ser uma URL" (US-02 c4)
entra junto com os testes da US-02. `data` só existe na modalidade síncrona
(docs/projeto/02-classes.md, "opcionais").
"""
from __future__ import annotations

from datetime import date


class Modulo:
    """Um módulo de curso: 1 vídeo não listado ou 1 reunião do Meet (RN-02.2/02.3)."""

    def __init__(self, titulo: str, link: str, data: date | None = None) -> None:
        self.titulo = titulo
        self.link = link
        self.data = data
