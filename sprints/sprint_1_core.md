# Sprint 1 — Core/Project

## Objetivo
- Implementar o agregado `Project` com invariantes e casos de uso básicos, disponibilizando endpoints essenciais para criação, listagem, detalhamento e transições de status.

## Por que
- `Project` é a raiz de composição dos subdomínios (`tasks`, `notes`, `task_notes`) e define regras transversais (ex.: ativo/arquivado) que impactam operações em outras áreas.

## Escopo
- Dentro: entidade `Project`, repositório (port + adapter), casos de uso (`create/list/get/archive/unarchive`) e API correspondente.
- Fora: autenticação, autorização avançada e integrações externas (serão tratadas depois).

## Entregáveis
- `projects/domain/core`: `Project` + `ProjectRepositoryInterface`.
- `projects/infrastructure/core`: `ProjectModel`, mappers e `ProjectRepository` (Django ORM).
- `projects/application/core`: casos de uso e orquestração de regras.
- `projects/interfaces/api/core`: views HTTP e serialização.
- Testes unitários e de integração cobrindo invariantes e repositório.

## Endpoints
- `GET /projects/` — lista projetos do usuário.
- `GET /projects/{id}/` — detalhe de projeto.
- `POST /projects/` — cria projeto (`owner_id`, `name`, `description?`).
- `POST /projects/{id}/archive` — arquiva projeto (bloqueia operações nos subdomínios).
- `POST /projects/{id}/unarchive` — reativa projeto.

## Estrutura
- Domain
  - `core/Project` com campos: `id`, `owner_id`, `name`, `description`, `status`, `created_at`, `updated_at`.
  - Invariantes: `name` único por `owner_id`; edição restrita se `status=archived`.
  - `ProjectRepositoryInterface` com métodos `get`, `list`, `create`, `update_status`.
- Application
  - `create_project`, `list_projects`, `get_project`, `archive_project`, `unarchive_project`.
- Infrastructure
  - `ProjectModel` (ORM), mappers entity↔model e `ProjectRepository`.
- Interfaces
  - Views para cada endpoint e conversão entity→JSON.

## Testes
- Domínio: invariantes (`name` único, transições válidas de status).
- Infra: persistência correta e mapeamento entity↔model.
- API: smoke para rotas, respostas e códigos HTTP.

## Critérios de Aceite
- Casos de uso e endpoints funcionalmente corretos com validações ativas.
- Nenhum acoplamento do domínio com ORM ou views.

## Riscos/Dependências
- Risco: acoplamento entre subdomínios. Mitigação: `ProjectId` e ports na `application/core`.
- Dependência: `Project` deve existir para sprints seguintes.

## Métricas
- Tempo: 1–2 dias.
- Cobertura mínima: 70% em domínio; smoke em API.