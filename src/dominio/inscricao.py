"""Inscricao — liga um aluno a um curso (docs/projeto/02-classes.md).

Dono das regras da US-08 (docs/projeto/03-responsabilidades.md). O construtor
só guarda dados: nascer em "aguardando pagamento" é regra de
`Curso.inscrever()` (US-07 c1), não daqui.
"""
from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from dominio.enums import StatusInscricao

if TYPE_CHECKING:  # só para anotações; evita import circular com Curso
    from dominio.curso import Curso
    from dominio.modulo import Modulo
    from dominio.usuario import Usuario


class Inscricao:
    """A inscrição de um aluno num curso, com seu status e seu registro de envio."""

    def __init__(
        self,
        aluno: Usuario,
        curso: Curso,
        data: datetime,
        status: StatusInscricao,
        acesso_enviado_em: datetime | None = None,
    ) -> None:
        self.aluno = aluno
        self.curso = curso
        self.data = data
        self.status = status
        self.acesso_enviado_em = acesso_enviado_em

    # ---- US-08: métodos a implementar -------------------------------------

    def confirmar_pagamento(self) -> None:
        """US-08 c2 — muda o status para "pagamento confirmado" e libera o acesso.

        US-08 c3 — pagamento já confirmado: recusa, lançando
        `PagamentoJaConfirmado` (o e-mail de acesso não é reenviado).
        Quem envia o e-mail é o serviço, desenhado no passo 4.
        """
        raise NotImplementedError(
            "US-08 c2/c3: implemente Inscricao.confirmar_pagamento()"
        )

    def registrar_envio_acesso(self, quando: datetime) -> None:
        """US-08 c4 — registra se e quando o e-mail de acesso saiu (RN-02.5)."""
        raise NotImplementedError(
            "US-08 c4: implemente Inscricao.registrar_envio_acesso(quando)"
        )

    def acesso_liberado(self) -> bool:
        """US-08 c2 · US-09 c2/c3 — o aluno já pode ver os links?"""
        raise NotImplementedError("US-08 c2: implemente Inscricao.acesso_liberado()")

    def links_liberados(self) -> list[Modulo]:
        """US-08 c2 · US-09 c2–c4 — os módulos do curso, lidos na hora (sem cópia)."""
        raise NotImplementedError("US-08 c2: implemente Inscricao.links_liberados()")
