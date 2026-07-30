# Estado do projeto

**Projeto:** VetRegula RJ
**Atualizado em:** 29/07/2026
**Fase atual:** preparação do ambiente
**Implementação da aplicação:** não iniciada

## Concluído

- pastas pública e privada separadas;
- Python 3.12.10 instalado;
- ambiente virtual `.venv` criado e validado;
- pip 26.1.2 configurado;
- Git 2.54 inicializado na branch `main`;
- identidade Git local configurada com endereço privado;
- VS Code 1.131.0 configurado;
- extensões Python, Pylance, Jupyter, Ruff e Codex disponíveis;
- pytest 9.1.1 instalado;
- Ruff 0.16.0 instalado;
- pip-tools 7.6.0 instalado;
- dependências de desenvolvimento fixadas;
- `.gitignore` e `.gitattributes` configurados;
- planejamento adicionado em `docs/`;
- `AGENTS.md` criado;
- registro de decisões criado;
- verificações `pip check` e `ruff check` aprovadas.
- documentação inicial do repositório concluída;
- teste de sanidade aprovado;
- primeiro commit criado;
- repositório público criado e conectado ao GitHub;
- conteúdo publicado auditado, sem arquivos privados ou credenciais.

## Em preparação

- validação operacional do Codex no VS Code;
- verificação das contas Gemini API e OCI.

## Bloqueios antes da implementação

As pendências registradas em `docs/DECISIONS.md` devem ser resolvidas antes do
desenvolvimento das funcionalidades regulatórias.

## Restrição técnica conhecida

Não atualizar o pip acima da versão 26.1.2 enquanto a compatibilidade com
pip-tools 7.6.0 não estiver confirmada.

## Próximo marco

Validar o Codex no VS Code, verificar o acesso ao Gemini API e à OCI e concluir
a preparação do ambiente antes da implementação.
