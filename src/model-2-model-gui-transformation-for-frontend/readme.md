# Digital Twin OT Advanced

Advanced dissertation-oriented scaffold for a hybrid OT cybersecurity Digital Twin based on Mininet + Docker.

## What is included
- Hybrid architecture: Mininet for network emulation, Docker for services
- OT/DMZ/IT segmented topology
- OT protocol service stubs (Modbus, DNP3, IEC 104, IEC 61850)
- Monitoring stack (Zeek, Suricata, OpenSearch, Grafana)
- Attack modules (replay, spoofing, fuzzing, MITM)
- Compliance mapper aligned with IEC 62443 / NIS2
- Experiment scenarios and result folders
- Dissertation assets (LaTeX section + architecture notes)

## Status
This project is a strong implementation scaffold rather than a production-ready ICS lab. Some protocol services are simplified stubs intended for extension.

## High-level execution flow
1. Build and start containers with Docker Compose.
2. Start the Mininet topology.
3. Attach selected containers to Mininet switches using veth pairs.
4. Apply netem rules to selected links.
5. Run baseline traffic.
6. Execute attack scenarios.
7. Collect pcaps, alerts, logs, metrics.
8. Run the compliance mapper.

## Prerequisites
- Linux host
- Docker + Docker Compose plugin
- Python 3.10+
- Mininet + Open vSwitch installed on host
- Root privileges for Mininet / veth / tc operations

## Quick start
```bash
cd orchestration
docker compose up -d --build
cd ../network/topology
sudo python3 full_topology.py
```

In another terminal:
```bash
cd orchestration
sudo ./connect_all.sh
sudo ../network/scripts/apply_netem.sh
```

## Suggested phased validation
1. Validate Docker services alone.
2. Validate Mininet topology alone.
3. Connect one OT node and one HMI.
4. Add Zeek and Suricata on span switch.
5. Execute replay and spoofing scenarios.
6. Map alerts to IEC 62443 requirements.

## Main folders
- `orchestration/`: compose and lifecycle scripts
- `network/`: Mininet topology and traffic control scripts
- `containers/`: Dockerfiles and service code
- `experiments/`: scenarios, metrics, and outputs
- `analysis/`: notebooks and post-processing scripts
- `docs/`: architecture, dissertation sections, figures

## Notes
- Containers are attached to Mininet externally through veth pairs.
- Monitoring sensors use `network_mode: none` to allow manual attachment to the span switch.
- Replace the simplified protocol servers with full implementations as your dissertation evolves.
