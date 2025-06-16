# ☸️ Kubernetes Deployment Manifests

This folder contains the Kubernetes manifests required to simulate a production-grade deployment of the Enterprise Airflow Platform, designed for scalable orchestration and data engineering pipelines.

> ⚠️ **Note:** While this project runs locally via Docker Compose, these manifests demonstrate how it would be deployed in a Kubernetes environment within a real organization.

---

## 📦 Components

### 1. `postgres-deployment.yaml`

Deploys the **PostgreSQL** backend used by Airflow for metadata storage.

- Defines a single pod with persistent storage (simulated via `emptyDir`).
- Exposes PostgreSQL via a `ClusterIP` service.
- Environment variables define DB name, user, and password.

### 2. `airflow-deployment.yaml`

Deploys the **Airflow Webserver** and **Scheduler** in a single container (for simulation).

- Uses `LocalExecutor` for simplicity (can be replaced with `CeleryExecutor` or `KubernetesExecutor` in production).
- Mounts simulated volumes for DAGs, logs, and plugins.
- Connects to the PostgreSQL service internally.

> In a real environment, Airflow components would be separated into individual deployments (webserver, scheduler, workers, etc.)

### 3. `airflow-service.yaml`

Exposes the Airflow webserver internally and externally via `NodePort`.

- Port `8080` inside the cluster is mapped to `30001` on the host.
- Allows accessing Airflow UI at `http://localhost:30001`.

### 4. `airflow-ingress.yaml` *(Optional)*

Simulates an **Ingress Controller** setup for routing via domain.

- Routes traffic from `airflow.local` to the Airflow service.
- Useful in environments with NGINX or cloud-native ingress controllers (e.g., AWS ALB, GCP Ingress).

---

## 📁 Folder Structure

```bash
kubernetes/
├── airflow-deployment.yaml     # Airflow pod and volumes
├── airflow-service.yaml        # Expose Airflow externally
├── postgres-deployment.yaml    # Postgres deployment and service
└── airflow-ingress.yaml        # Optional domain routing (Ingress)

🚀 Enterprise Notes
Designed for educational/demo purposes with simulated volumes and simplified configs.

Can be scaled to real cloud-native platforms like GKE, EKS, or AKS with minor adjustments.

Demonstrates best practices in modular infrastructure, with clear separation of concerns.

💡When to Use Kubernetes
If this were a real-world system, Kubernetes would help with:

Scalability: Run distributed Airflow tasks via KubernetesExecutor or CeleryExecutor.

Resilience: Auto-restart failed pods and ensure uptime.

CI/CD Integration: Integrate with GitHub Actions to auto-deploy DAG changes.

Observability: Connect with Prometheus + Grafana for system metrics.

✅ Deployment Simulated Only
This project does not require actual Kubernetes deployment — instead, this structure helps demonstrate how an enterprise would provision and manage Airflow at scale, giving recruiters and reviewers an insight into platform-thinking.
