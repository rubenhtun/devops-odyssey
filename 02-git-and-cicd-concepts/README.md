flowchart LR
    subgraph CI_CD_Pipeline[DevOps CI/CD Pipeline]
        direction LR
        S[Git Repository<br/>📦 Source] -->|Commit/Push| B[Docker Build<br/>🐳 Image]
        B --> T[Automated Tests<br/>✅ Unit & Integration]
        T --> D[Deploy to Production<br/>🚀 Kubernetes]
    end