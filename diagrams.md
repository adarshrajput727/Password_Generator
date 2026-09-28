# Design Diagrams

## System Architecture

```mermaid
flowchart LR
    U[User] --> M[main.py]
    M --> C[cli.py]
    C --> V[validator.py]
    C --> G[generator.py]
    C --> S[strength.py]
    C --> F[formatter.py]
    G --> R[secrets / SystemRandom]
    V --> C
    S --> F
    F --> U
```

## Use Case Diagram

```mermaid
flowchart LR
    U((User))
    U --> UC1([Generate by counts])
    U --> UC2([Generate by length])
    U --> UC3([Generate multiple passwords])
    U --> UC4([Analyse password])
    U --> UC5([Exit])
```

## Sequence Diagram

```mermaid
sequenceDiagram
    actor User
    participant CLI
    participant Validator
    participant Generator
    participant Analyzer

    User->>CLI: Select generation option
    CLI->>Validator: Validate inputs
    Validator-->>CLI: Valid input
    CLI->>Generator: Request password
    Generator-->>CLI: Generated password
    CLI->>Analyzer: Analyze password
    Analyzer-->>CLI: Strength metrics
    CLI-->>User: Display result
```

## Component / Class View

```mermaid
classDiagram
    class CLI {
        +run()
        +generate_by_counts()
        +generate_by_length()
        +generate_batch()
        +analyse_existing()
    }

    class Validator {
        +validate_count()
        +validate_password_length()
        +validate_composition()
    }

    class Generator {
        +generate_password()
        +generate_from_length()
        +generate_multiple()
    }

    class Strength {
        +analyze_password()
        +strength_message()
    }

    class Formatter {
        +print_banner()
        +print_password()
        +print_help()
    }

    CLI --> Validator
    CLI --> Generator
    CLI --> Strength
    CLI --> Formatter
```

No ER diagram is required because this version does not use persistent database storage.
