"""Enumerações do domínio (docs/projeto/02-classes.md).

Herdam de `str` para que os valores apareçam legíveis nas mensagens de erro
e nas respostas da API (ex.: `StatusInscricao.AGUARDANDO_PAGAMENTO` é
"aguardando pagamento").
"""
from enum import Enum


class Modalidade(str, Enum):
    """Modalidade do curso (RN-01.x)."""

    GRAVADO = "gravado"
    SINCRONO = "síncrono"


class StatusCurso(str, Enum):
    """Estados do curso (US-01 c1, US-03 c1)."""

    RASCUNHO = "rascunho"
    PUBLICADO = "publicado"


class StatusInscricao(str, Enum):
    """Estados da inscrição (US-07 c1, US-08 c2)."""

    AGUARDANDO_PAGAMENTO = "aguardando pagamento"
    PAGAMENTO_CONFIRMADO = "pagamento confirmado"


class Perfil(str, Enum):
    """Papéis de usuário (US-05)."""

    ALUNO = "aluno"
    COORDENADOR = "coordenador"
