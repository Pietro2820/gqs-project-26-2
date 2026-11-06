"""Fixtures dos testes (US-08 e futuras histórias).

Coloca `src/` no caminho de importação — assim o `pytest` roda sem instalar
nada além dele próprio.
"""
import sys
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parent.parent / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from dominio.curso import Curso  # noqa: E402
from dominio.enums import (  # noqa: E402
    Modalidade,
    Perfil,
    StatusCurso,
    StatusInscricao,
)
from dominio.inscricao import Inscricao  # noqa: E402
from dominio.modulo import Modulo  # noqa: E402
from dominio.periodo import Periodo  # noqa: E402
from dominio.usuario import Usuario  # noqa: E402


@pytest.fixture
def aluno() -> Usuario:
    """A aluna que se inscreve (US-04 criaria a conta de verdade)."""
    return Usuario(
        nome="Ana Souza",
        email="ana@exemplo.com",
        senha_hash="hash-ana",
        perfil=Perfil.ALUNO,
    )


@pytest.fixture
def curso_publicado() -> Curso:
    """Curso gravado, publicado, com dois módulos e inscrições abertas."""
    return Curso(
        nome="Excel para gerentes",
        descricao="Planilhas do básico ao avançado",
        cronograma="8 semanas",
        modalidade=Modalidade.GRAVADO,
        carga_horaria=20,
        datas=Periodo(date(2026, 11, 2), date(2026, 12, 18)),
        periodo_inscricao=Periodo(date(2026, 10, 1), date(2026, 10, 31)),
        vagas=30,
        valor_matricula=Decimal("199.90"),
        status=StatusCurso.PUBLICADO,
        modulos=[
            Modulo(titulo="Módulo 1 — Introdução", link="https://youtu.be/video-1"),
            Modulo(titulo="Módulo 2 — Tabelas dinâmicas", link="https://youtu.be/video-2"),
        ],
    )


@pytest.fixture
def inscricao_aguardando(aluno: Usuario, curso_publicado: Curso) -> Inscricao:
    """Inscrição recém-feita, ainda sem pagamento (US-07 c1)."""
    return Inscricao(
        aluno=aluno,
        curso=curso_publicado,
        data=datetime(2026, 10, 5, 14, 0),
        status=StatusInscricao.AGUARDANDO_PAGAMENTO,
    )


@pytest.fixture
def inscricao_confirmada(aluno: Usuario, curso_publicado: Curso) -> Inscricao:
    """Inscrição já paga, com o e-mail de acesso já registrado (US-08 c2 + c4)."""
    return Inscricao(
        aluno=aluno,
        curso=curso_publicado,
        data=datetime(2026, 10, 5, 14, 0),
        status=StatusInscricao.PAGAMENTO_CONFIRMADO,
        acesso_enviado_em=datetime(2026, 10, 21, 9, 30),
    )


@pytest.fixture
def curso_com_inscritos(
    curso_publicado: Curso, inscricao_aguardando: Inscricao
) -> Curso:
    """Curso com dois inscritos: um aguardando e outro já confirmado (US-08 c1)."""
    bruno = Usuario(
        nome="Bruno Lima",
        email="bruno@exemplo.com",
        senha_hash="hash-bruno",
        perfil=Perfil.ALUNO,
    )
    confirmada = Inscricao(
        aluno=bruno,
        curso=curso_publicado,
        data=datetime(2026, 10, 6, 9, 0),
        status=StatusInscricao.PAGAMENTO_CONFIRMADO,
    )
    curso_publicado.inscricoes = [inscricao_aguardando, confirmada]
    return curso_publicado
