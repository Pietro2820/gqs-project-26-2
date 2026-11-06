"""Erros de domínio — quando uma regra é violada, o método recusa.

Convenção (docs/projeto/03-responsabilidades.md): a classe lança um erro do
domínio; quem o traduz numa resposta HTTP é a camada do FastAPI (passo 5),
nunca a classe.
"""


class ErroDeDominio(Exception):
    """Classe base dos erros de regra de negócio."""


class PagamentoJaConfirmado(ErroDeDominio):
    """US-08 c3 — não é possível confirmar um pagamento já confirmado."""
