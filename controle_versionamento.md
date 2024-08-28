# Fluxo de versionamento

## Explicação inicial:
Cada desenvolvedor mantém uma cópia completa do repositório, com todo o histórico de commits e branches.


## Estrutura de Branches

- **`main`**: Código estável e pronto para produção. Não receber merges diretos.
- **`desenv`**: Integração de funcionalidades. Base para novas branches.

- **Feature Branches** (`feature/nome-da-funcionalidade`):
  - Criação: `git checkout desenv` -> `git checkout -b feature/nome-da-funcionalidade`
  - Exemplo: `feature/autenticacao`, `feature/dashboard`

## Fluxo de Trabalho

1. **Desenvolvimento**:
   - Será realizado commits pequenos e frequentes na branch de funcionalidade, no mínimo uma vez por semana de cada membro da equipe.
   - Padrão de Commit: `[Tipo]: Descrição`
     - Tipos: `feat`, `fix`, `refactor`, `docs`, `style`, `test`

2. **Pull Request**:
   - Será aberto um Pull Request da branch de funcionalidade para a `desenv`.
   - As mudanças serão descritas de forma clara.
   - Revisão: Pelo menos uma aprovação será necessária, que poderá ser realizada por qualquer membro da equipe.

3. **Merge na desenv**:
   - Após aprovação do Pull Request, será feito o merge na `desenv`.
   - Se necessário, os conflitos terão que ser resolvidos.


## Resumindo

- **Branches**: `main`, `desenv`, `feature/nome-da-funcionalidade`
- **Commits**: `[Tipo]: Descrição`
- **PRs**: Revisão obrigatória antes do merge.