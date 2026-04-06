Network Traffic Anomaly Detection System (NTADS)

NTADS is a high-performance security framework designed to identify and mitigate malicious network activities in real-time. By combining Machine Learning (Random Forest & XGBoost) with live data processing, it detects anomalies such as DoS, Probes, and unauthorized access attempts with high precision.

🌟 Key Features

Hybrid ML Engine: Utilizes an ensemble of Random Forest and XGBoost trained on the NSL-KDD dataset for robust classification.

Dual-Mode Data Ingestion: Supports Live Packet Sniffing via Scapy and a High-Fidelity Simulation Engine for environments without specialized drivers.

Interactive SOC Dashboard: A professional "Security Operations Center" interface featuring live traffic feeds and threat distribution charts.

Active Mitigation (IPS): Integrated "Block IP" functionality to simulate immediate firewall response against detected threats.

High Accuracy: Achieves a balanced detection rate of over 98% on standard benchmark tests.

🛠️ Tech Stack

Language: Python 3.11

Frameworks: Flask, Flask-CORS

ML Libraries: Scikit-Learn, XGBoost, Pandas, Numpy

Networking: Scapy (for packet analysis)

Frontend: HTML5, CSS3, JavaScript, Chart.js

📁 Project Structure


Network_IDS/
├── data/               # NSL-KDD Dataset files
├── models/             # Serialized ML models (.pkl)
├── static/             # Frontend assets (index.html)
├── app.py              # Backend API & Detection Logic
├── requirements.txt    # Dependency list
└── README.md           # Documentation

🚀 Getting Started

1. Installation

Clone the repository and install the required dependencies:
pip install -r requirements.txt

2. Configuration
Live Mode: To capture real traffic, ensure Npcap is installed in "WinPcap API-compatible Mode" and run VS Code as Administrator.

Simulation Mode: Use the built-in traffic generator if hardware-level sniffing is not required.

3. Execution
Start the detection engine:

Bash
python app.py
Access the dashboard at http://127.0.0.1:5000.

🔬 Methodology
The system processes raw network data through a multi-stage pipeline:

Ingestion: Captures packets at Layer 2 (Data Link) using Scapy.

Feature Mapping: Normalizes packet headers into the 41-feature format of the NSL-KDD dataset.

Inference: The Ensemble Model calculates the probability of an anomaly.

Visualization: Results are pushed to the dashboard via a RESTful API.
