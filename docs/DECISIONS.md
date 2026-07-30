# Registro de decisões

Este arquivo registra decisões confirmadas e pendências que podem alterar o
escopo ou a arquitetura do VetRegula RJ.

## Decisões confirmadas

| ID      | Data       | Decisão                                                                     | Motivo                                            |
| ------- | ---------- | --------------------------------------------------------------------------- | ------------------------------------------------- |
| DEC-001 | 29/07/2026 | Nome do projeto: VetRegula RJ                                               | Identificação clara do tema e da jurisdição       |
| DEC-002 | 29/07/2026 | VS Code como IDE principal                                                  | Centraliza Python, Git, testes, notebooks e Codex |
| DEC-003 | 29/07/2026 | Google Colab somente como contingência                                      | Evita fragmentar o ambiente e o repositório       |
| DEC-004 | 29/07/2026 | Python 3.12                                                                 | Compatibilidade entre bibliotecas, Windows e OCI  |
| DEC-005 | 29/07/2026 | Ambiente virtual local `.venv`                                              | Isolamento das dependências                       |
| DEC-006 | 29/07/2026 | Branch principal `main`                                                     | Fluxo Git simples                                 |
| DEC-007 | 29/07/2026 | ChatGPT Project + Codex como ambiente principal de IA                       | Planejamento e execução coordenados               |
| DEC-008 | 29/07/2026 | Ruff, pytest e pip-tools como ferramentas de desenvolvimento                | Qualidade, testes e reprodutibilidade             |
| DEC-009 | 29/07/2026 | Pip fixado temporariamente em 26.1.2                                        | Compatibilidade com pip-tools 7.6.0               |
| DEC-010 | 29/07/2026 | Sem Docker, LangChain ou banco vetorial no início                           | Redução de complexidade e risco                   |
| DEC-011 | 29/07/2026 | Documentos brutos e materiais privados não serão publicados automaticamente | Segurança, privacidade e direitos autorais        |

## Decisões pendentes antes da implementação

| ID       | Decisão necessária                                                | Recomendação atual                                              |
| -------- | ----------------------------------------------------------------- | --------------------------------------------------------------- |
| PEND-001 | Estabelecimento como pessoa jurídica ou consultório em CPF        | Pessoa jurídica                                                 |
| PEND-002 | Inclusão de vacinação no MVP                                      | Incluir                                                         |
| PEND-003 | Tenancy, região, shape e orçamento de contingência da OCI         | Testar antes do código principal                                |
| PEND-004 | Chave e política de uso da Gemini API                             | Usar somente documentos públicos e perguntas sem dados pessoais |
| PEND-005 | Horas semanais e dias indisponíveis                               | Ajustar cronograma antes da implementação                       |
| PEND-006 | Política de redistribuição dos PDFs oficiais                      | Verificar antes de versionar                                    |
| PEND-007 | Pessoa responsável pela revisão de clareza das respostas críticas | Definir antes da avaliação final                                |

## Regra de atualização

Uma decisão pendente somente muda para confirmada depois de aprovação explícita
do responsável pelo projeto. Toda mudança de arquitetura ou escopo deve registrar
data, motivo e impacto.
