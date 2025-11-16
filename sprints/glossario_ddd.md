# Glossário DDD (Opcional)

- Entidade (Entity): objeto com identidade persistente (ex.: `Project`, `Task`).
- Agregado (Aggregate): cluster de entidades com regras e invariantes, tendo um agregado raiz.
- Valor (Value Object): objeto sem identidade, definido por seus atributos (ex.: `ProjectName`).
- Repositório (Repository): abstração de persistência para agregados/entidades.
- Caso de Uso (Application Service): orquestra operações do domínio para atender um objetivo.
- Port (Interface): contrato exposto/consumido entre camadas ou subdomínios.
- Adapter (Implementação): componente que cumpre um port (ex.: `Repository` com ORM).
- Bounded Context: limite de um modelo consistente de domínio (ex.: `tasks`, `notes`).
- ACL (Anti-Corruption Layer): camada para integrar sistemas externos sem poluir o domínio.
- Evento de Domínio: fato importante do domínio (ex.: `ProjectArchived`).
- Saga/Process Manager: coordenação de processos distribuídos entre agregados/subdomínios.