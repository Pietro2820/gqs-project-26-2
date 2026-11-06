"""Usuario — aluno ou coordenador (US-04, US-05).

Stub: o construtor só guarda os dados. As validações de e-mail (US-04 c3),
a senha e a sessão (US-05) ficam nas camadas de aplicação ou nos testes das
próprias histórias.
"""
from __future__ import annotations

from dominio.enums import Perfil


class Usuario:
    """Pessoa com conta no sistema (US-04)."""

    def __init__(self, nome: str, email: str, senha_hash: str, perfil: Perfil) -> None:
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash
        self.perfil = perfil

    def eh_coordenador(self) -> bool:
        """US-05 c1 — este usuário tem perfil de coordenador?"""
        raise NotImplementedError("US-05 c1: implemente Usuario.eh_coordenador()")
