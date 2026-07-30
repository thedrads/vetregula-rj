# VetRegula RJ

Assistente documental em desenvolvimento para apoiar a consulta inicial de
informações oficiais sobre abertura e regularização de consultório veterinário
no Município do Rio de Janeiro.

> Status: preparação do ambiente. A aplicação ainda não foi implementada.

## Objetivo

Construir o MVP do Challenge ONE G10 — Agente de IA com:

- processamento de documentos PDF ou CSV;
- perguntas em linguagem natural;
- respostas baseadas na documentação;
- indicação das fontes;
- execução local;
- deploy na Oracle Cloud Infrastructure;
- repositório público e documentação reproduzível.

## Ambiente de desenvolvimento

- Windows 10 x64;
- Python 3.12;
- ambiente virtual `.venv`;
- Visual Studio Code;
- Git e GitHub;
- Ruff;
- pytest;
- pip-tools.

## Preparação local

Criar o ambiente:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar a versão compatível do pip e as ferramentas:

```powershell
python -m pip install "pip==26.1.2"
python -m pip install -r requirements-dev.txt
```

Verificar o ambiente:

```powershell
python -m pip check
python -m ruff check .
```

## Documentação

- [Planejamento completo](docs/Planejamento_Challenge_ONE_G10_VetRegula_RJ.md)
- [Registro de decisões](docs/DECISIONS.md)
- [Estado do projeto](docs/PROJECT_STATUS.md)
- [Instruções para o Codex](AGENTS.md)

## Segurança e privacidade

- credenciais e arquivos `.env` não são versionados;
- o relatório de hardware original não pode ser publicado;
- materiais privados do MBA e TECH AI BUILDER não fazem parte do repositório;
- a aplicação inicial não armazenará perguntas nem dados pessoais.

## Situação da implementação

A arquitetura funcional, as fontes e as funcionalidades serão implementadas
somente depois da confirmação das decisões pendentes registradas em
`docs/DECISIONS.md`.
