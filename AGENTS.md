# AGENTS.md

## Objetivo

Construir o VetRegula RJ conforme o planejamento em
`docs/Planejamento_Challenge_ONE_G10_VetRegula_RJ.md`.

A solução será um assistente documental sobre abertura e regularização inicial
de consultório veterinário no Município do Rio de Janeiro.

## Fonte de verdade

- Leia o planejamento antes de propor arquitetura ou implementação.
- Use o repositório e os documentos versionados como fonte de verdade.
- Não considere memória de chat como decisão permanente.
- Registre decisões importantes em `docs/DECISIONS.md`.
- Não amplie o escopo sem confirmação explícita do usuário.

## Forma de trabalho

- Trabalhe em uma tarefa pequena e verificável por vez.
- Explique o motivo de cada escolha de ferramenta ou arquitetura.
- Antes de adicionar dependência, informe finalidade, licença, custo, alternativa
  e necessidade no MVP.
- Faça perguntas quando faltar uma decisão que altere materialmente o resultado.
- Preserve mudanças existentes e revise o diff antes de concluir.
- Não use agentes paralelos sem solicitação explícita.
- Comunique-se em português do Brasil.

## Ambiente

- Python suportado: `>=3.12,<3.13`.
- Versão local validada: Python 3.12.10.
- Ambiente virtual: `.venv`.
- Use `python -m pip` para instalar pacotes.
- Instale dependências somente a partir dos arquivos versionados.
- Não atualize o pip acima de 26.1.2 enquanto a compatibilidade com
  `pip-tools 7.6.0` não estiver confirmada.
- Não adote Docker, LangChain, LlamaIndex ou banco vetorial sem nova decisão.

## Qualidade

Antes de considerar uma tarefa concluída, execute quando aplicável:

```powershell
python -m pip check
python -m ruff check .
python -m ruff format --check .
python -m pytest
```
