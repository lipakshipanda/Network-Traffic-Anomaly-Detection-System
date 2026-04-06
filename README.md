# 🛡️ Network Traffic Anomaly Detection System (NTADS)

**NTADS** is a high-performance security framework designed to identify and mitigate malicious network activities in real-time. By combining **Machine Learning (Random Forest & XGBoost)** with live data processing, it detects anomalies such as DoS, Probes, and unauthorized access attempts with high precision.

![Main Dashboard Screenshot](screenshots\Screenshot 2026-04-06 214420.png)
*Figure 1: Real-time SOC Dashboard Monitoring Live Traffic*

---

## 🌟 Key Features
* **Ensemble ML Engine**: Utilizes a hybrid model (Random Forest + XGBoost) trained on the **NSL-KDD dataset**.
* **Dual-Mode Data Ingestion**: Supports **Live Packet Sniffing** (via Scapy) and a **High-Fidelity Simulation Engine**.
* **Interactive SOC Dashboard**: A professional "Security Operations Center" interface with live traffic feeds and threat distribution charts.
* **Active Mitigation (IPS)**: Integrated "Block IP" functionality to simulate immediate firewall responses.
* **High Accuracy**: Achieves a balanced detection rate of **98.4%** on benchmark tests.

---

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.11 |
| **Backend** | Flask, Flask-CORS |
| **Machine Learning** | Scikit-Learn, XGBoost, Pandas, Numpy |
| **Networking** | Scapy (Packet Analysis) |
| **Frontend** | HTML5, CSS3, JavaScript, Chart.js |

---

## 📁 Project Structure
```text
Network_IDS/
├── data/               # NSL-KDD Dataset files (KDDTrain+.txt)
├── models/             # Serialized ML models (.pkl) and Scalers
├── static/             # Frontend assets (index.html)
├── app.py              # Backend API & Detection Logic
├── requirements.txt    # Dependency list
└── README.md           # Documentation
🚀 Getting Started
1. Prerequisites
Python 3.9+

Npcap: Required for live sniffing on Windows. Download here (Ensure "WinPcap API-compatible Mode" is checked).

2. Installation
Clone the repository and install the required dependencies:

PowerShell
pip install -r requirements.txt
3. Execution
Note: To capture real traffic, you must run your terminal as an Administrator.

PowerShell
python app.py
Access the dashboard at: http://127.0.0.1:5000

Figure 2: Backend initialization and AI model loading

🔬 Methodology
The system processes raw network data through a multi-stage pipeline:

Ingestion: Captures packets at Layer 2 (Data Link) using Scapy.

Feature Mapping: Normalizes packet headers into the 41-feature format of the NSL-KDD dataset.

Inference: The Ensemble Model calculates the probability of an anomaly.

Visualization: Results are pushed to the dashboard via a RESTful API.

Figure 3: Threat classification and confidence scoring

🎓 Academic Context
Developed by Lipakshi, a 3rd-year CSE-AIML student at Odisha University of Technology and Research (OUTR). This project serves as a practical implementation of Computer Networks and Artificial Intelligence, aligning with core concepts.

