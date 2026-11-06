# Testes de unidade — US-08: Ver inscritos e confirmar pagamento

Primeiro código do repositório: os testes da história
[US-08](../docs/requisitos/historias/US-08-confirmar-pagamento.md),
escritos **antes** da implementação, como manda o
[passo 3](../docs/projeto/03-responsabilidades.md): *"cada linha vira pelo
menos um teste de unidade, com o critério no nome"*.

## Como rodar

```bash
pip install -r requirements.txt   # só o pytest
python -m pytest -v               # ou: pytest -v
```

## O estado atual (TDD: vermelho → verde)

`src/dominio/` contém **stubs**: os construtores guardam os dados do
[passo 2](../docs/projeto/02-classes.md), mas os métodos da US-08 (passo 3)
levantam `NotImplementedError` apontando o critério que lhes dá origem.

- **2 testes verdes** — critérios atendidos só com atributos (c1 e o início
  vazio de `acesso_enviado_em`): não há regra para implementar.
- **8 testes vermelhos** — a tarefa: implementar os quatro métodos de
  `Inscricao` até tudo ficar verde.

```text
esperado hoje: 2 passed, 8 failed (NotImplementedError com o critério)
```

## Matriz de rastreabilidade

história → critério → método → teste

| Critério | O que verifica | Dono da regra (passo 3) | Teste |
|---|---|---|---|
| US-08 c1 | Inscritos expõem nome, e-mail, data e status | atributo `Curso.inscricoes` | `test_us08_c1_inscritos_expoem_nome_email_data_e_status` |
| US-08 c2 | Confirmar muda o status para confirmado | `Inscricao.confirmar_pagamento()` | `test_us08_c2_confirmar_pagamento_muda_status_para_confirmado` |
| US-08 c2 | Acesso liberado só depois de confirmar (D-03) | `Inscricao.acesso_liberado()` | `test_us08_c2_confirmar_pagamento_libera_o_acesso` |
| US-08 c2 | Aguardando pagamento: sem acesso e sem links | `acesso_liberado()` · `links_liberados()` | `test_us08_c2_aguardando_pagamento_nao_tem_acesso_nem_links` |
| US-08 c2 | Links liberados = módulos do curso | `Inscricao.links_liberados()` | `test_us08_c2_links_liberados_mostra_os_modulos_do_curso` |
| US-08 c3 | Pagamento confirmado não confirma de novo | `confirmar_pagamento()` → `PagamentoJaConfirmado` | `test_us08_c3_pagamento_ja_confirmado_nao_confirma_de_novo` |
| US-08 c3 | Segunda confirmação não registra novo envio | `confirmar_pagamento()` + `acesso_enviado_em` | `test_us08_c3_segunda_confirmacao_nao_registra_novo_envio` |
| US-08 c4 | Registro de envio começa vazio | atributo `acesso_enviado_em` | `test_us08_c4_acesso_enviado_em_comeca_vazio` |
| US-08 c4 | Registrar o momento do envio (RN-02.5) | `Inscricao.registrar_envio_acesso(quando)` | `test_us08_c4_registrar_envio_acesso_guarda_o_momento` |
| US-09 c4 *(bônus)* | Links lidos do curso na hora, sem cópia | `links_liberados()` | `test_us09_c4_links_liberados_le_os_modulos_do_curso_na_hora` |

O teste da US-09 c4 entra de carona porque a regra ("links sempre
atualizados") mora no mesmo método `links_liberados()` definido junto com a
US-08 no passo 3.

## Fora do escopo destes testes

- **Envio do e-mail com os links (c2, decisão D-04):** é do serviço, que
  orquestra `confirmar_pagamento()` → envia → `registrar_envio_acesso(agora)`;
  será desenhado no passo 4 (diagrama de sequência).
- **"Só coordenador" vê e confirma:** depende de quem está logado — camada do
  FastAPI (passo 5).
- **US-08 c5 (desfazer confirmação):** *(a confirmar)* com o cliente; se for
  confirmada, vira método novo em `Inscricao` e teste novo aqui.

## Convenções

- Nome do teste = `test_usNN_cN_` + a regra em português (passo 3).
- Domínio em Python puro: nada aqui depende do FastAPI.
- Erros de domínio em `src/dominio/erros.py`; a tradução para HTTP fica na
  API (passo 5).
