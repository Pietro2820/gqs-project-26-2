"""Testes de unidade da US-08 — Ver inscritos e confirmar pagamento.

- História: docs/requisitos/historias/US-08-confirmar-pagamento.md
- Projeto (dono de cada regra): docs/projeto/03-responsabilidades.md
- Convenção do passo 3: cada teste leva o critério de aceitação no nome —
  história → critério → método → teste.

Os métodos de `Inscricao` são stubs: os testes vermelhos são a lista de
tarefas (TDD). Ver tests/README.md para a matriz completa.
"""
from datetime import datetime

import pytest

from dominio.enums import StatusInscricao
from dominio.erros import PagamentoJaConfirmado
from dominio.modulo import Modulo


# ---------------------------------------------------------------------------
# US-08 c1 — Dado um curso, quando abro seus inscritos, então vejo nome,
#            e-mail, data da inscrição e status.
# Passo 3: atendido pelo atributo `Curso.inscricoes` — não há regra a
# implementar, então este teste já nasce verde.
# ---------------------------------------------------------------------------


def test_us08_c1_inscritos_expoem_nome_email_data_e_status(curso_com_inscritos):
    ana, bruno = curso_com_inscritos.inscricoes

    assert ana.aluno.nome == "Ana Souza"
    assert ana.aluno.email == "ana@exemplo.com"
    assert ana.data == datetime(2026, 10, 5, 14, 0)
    assert ana.status == StatusInscricao.AGUARDANDO_PAGAMENTO

    assert bruno.aluno.nome == "Bruno Lima"
    assert bruno.aluno.email == "bruno@exemplo.com"
    assert bruno.data == datetime(2026, 10, 6, 9, 0)
    assert bruno.status == StatusInscricao.PAGAMENTO_CONFIRMADO


# ---------------------------------------------------------------------------
# US-08 c2 — Dado um inscrito aguardando pagamento, quando confirmo o
#            pagamento, então o status muda para "pagamento confirmado" e o
#            acesso aos links é liberado na área do aluno.
# (O envio do e-mail é do serviço, passo 4 — ver tests/README.md.)
# ---------------------------------------------------------------------------


def test_us08_c2_confirmar_pagamento_muda_status_para_confirmado(
    inscricao_aguardando,
):
    inscricao_aguardando.confirmar_pagamento()

    assert inscricao_aguardando.status == StatusInscricao.PAGAMENTO_CONFIRMADO


def test_us08_c2_confirmar_pagamento_libera_o_acesso(inscricao_aguardando):
    assert not inscricao_aguardando.acesso_liberado()  # antes: sem acesso

    inscricao_aguardando.confirmar_pagamento()

    assert inscricao_aguardando.acesso_liberado()  # depois: liberado (D-03)


def test_us08_c2_aguardando_pagamento_nao_tem_acesso_nem_links(
    inscricao_aguardando,
):
    assert not inscricao_aguardando.acesso_liberado()
    assert inscricao_aguardando.links_liberados() == []


def test_us08_c2_links_liberados_mostra_os_modulos_do_curso(
    inscricao_confirmada, curso_publicado
):
    liberados = inscricao_confirmada.links_liberados()

    assert liberados == curso_publicado.modulos


# ---------------------------------------------------------------------------
# US-08 c3 — Dado um inscrito com pagamento já confirmado, então não é
#            possível confirmar de novo, e o e-mail de acesso não é
#            reenviado automaticamente.
# ---------------------------------------------------------------------------


def test_us08_c3_pagamento_ja_confirmado_nao_confirma_de_novo(
    inscricao_confirmada,
):
    with pytest.raises(PagamentoJaConfirmado):
        inscricao_confirmada.confirmar_pagamento()


def test_us08_c3_segunda_confirmacao_nao_registra_novo_envio(
    inscricao_confirmada,
):
    enviado_antes = inscricao_confirmada.acesso_enviado_em

    with pytest.raises(PagamentoJaConfirmado):
        inscricao_confirmada.confirmar_pagamento()

    assert inscricao_confirmada.acesso_enviado_em == enviado_antes


# ---------------------------------------------------------------------------
# US-08 c4 — Dado um inscrito, então o sistema registra se o e-mail de
#            acesso foi enviado e quando (RN-02.5).
# ---------------------------------------------------------------------------


def test_us08_c4_acesso_enviado_em_comeca_vazio(inscricao_aguardando):
    # antes: sem registro — hoje a evidência seria a caixa "Enviados" do Gmail
    assert inscricao_aguardando.acesso_enviado_em is None


def test_us08_c4_registrar_envio_acesso_guarda_o_momento(inscricao_confirmada):
    quando = datetime(2026, 10, 22, 10, 15)

    inscricao_confirmada.registrar_envio_acesso(quando)

    assert inscricao_confirmada.acesso_enviado_em == quando


# ---------------------------------------------------------------------------
# Bônus — US-09 c4 (mesmo método da US-08): os links são lidos do curso na
# hora, então um módulo cadastrado depois aparece sem reconfirmar nada.
# ---------------------------------------------------------------------------


def test_us09_c4_links_liberados_le_os_modulos_do_curso_na_hora(
    inscricao_confirmada, curso_publicado
):
    modulo_novo = Modulo(
        titulo="Módulo 3 — Encerramento", link="https://youtu.be/video-3"
    )
    curso_publicado.modulos.append(modulo_novo)

    assert modulo_novo in inscricao_confirmada.links_liberados()
