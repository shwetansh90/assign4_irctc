# CASHGUARD 🛡️
> **“Predict the Cash-Out Before It Happens.”**  
> *A Proactive Cybercrime Intelligence Platform for Law Enforcement Agencies (LEAs) & Financial Institutions.*  
> **Smart India Hackathon 2026 — Problem Statement SIH26184**

---

## 📌 Executive Summary
**CASHGUARD** is an actionable predictive analytics framework that forecasts likely physical cash withdrawal locations and extraction time windows from anomalous transaction streams. 

### 🌟 Core Innovation: Proactive Without Complaints
Unlike conventional reactive systems that require a victim to file an FIR or call the 1930 helpline hours after funds have already been liquidated at ATMs, **CASHGUARD operates proactively**:
1. It ingests live high-velocity transaction streams.
2. Extracts 11 real-time behavioral features (velocity, amount deviation, fan-in senders).
3. Executes **Isolation Forest** unsupervised anomaly detection.
4. Matches against a **Historical Fraud Pattern Library** using high-dimensional cosine similarity.
5. Reconstructs the multi-hop money flow graph using **NetworkX** to identify mule accounts and shared synthetic device footprints.
6. Computes an ensemble Risk Score combining supervised Random Forest and unsupervised anomaly scores.
7. Forecasts the **Top 3 Geographic Cash-Out Zones** and **Expected Time Windows** (e.g. *Next 30–60 minutes*).
8. Pins the high-risk perimeter on an interactive **GIS Hotspot Map** with nearby ATM kiosks for timely field interception.
9. Emits a real-time **LEA Intelligence Alert** equipped with transparent explainability bullets.
10. Supports **optional retroactive victim complaint enrichment**.

---

## ⚡ Quickstart (Run in 30 Seconds)

### Prerequisites
- Python 3.10+ (FastAPI, Uvicorn, Pandas, NumPy, Scikit-Learn, NetworkX are used)

### 1. Launch Server
In your terminal, run:
```bash
python3 run.py
```

### 2. Open Dashboard in Browser
Open your browser and navigate to:
```
http://localhost:8000
```

---

## 🎬 12-Step Judge Presentation Guide

Follow this exact story to demonstrate the core value proposition:

1. **Step 1:** Open `http://localhost:8000`. Point to the top banner: *"Notice that no victim complaint has been filed yet."*
2. **Step 2:** Click the red **`[SIMULATE SUSPICIOUS ACTIVITY — NO COMPLAINT]`** button in the top control deck.
3. **Step 3:** The **Live Simulation HUD** opens, executing each pipeline stage in real time:
   - **Live Inflow Ingestion:** Multiple unrelated UPI senders deposit round sums into a newly activated account.
   - **Feature Extraction:** 11 live behavioral dimensions computed on the fly.
   - **Anomaly Detection (Isolation Forest):** High anomaly flag triggered.
   - **Historical Pattern Matching:** 89.5% cosine match with *Pattern 01: Multi-Source → Mule → Cash-Out*.
   - **NetworkX Graph Traversal:** Multi-hop layering chain mapped; shared synthetic device `DEV-1042` correlated.
   - **Ensemble Risk Score:** 93.4 / 100 (*CRITICAL*).
   - **Cash-Out Zone Classifier:** *Sector 14 ATM & Cyber Cluster (84.2% Confidence)*.
   - **Time Window Forecast:** *Next 60–120 minutes*.
   - **GIS Hotspot Updated:** Map automatically zooms to Sector 14 with high-risk pulsing perimeter and 8 ATM markers.
   - **LEA Alert Emitted:** Proactive alert `#CG-1042` generated with 6 explainability reasons.
4. **Step 4:** Click **`2. Live Alerts`** tab to inspect the detailed intelligence dossier.
5. **Step 5:** Click **`3. Transaction Network`** tab to explore the interactive NetworkX graph (click any node to see its role, device ID, and forecasted next action).
6. **Step 6:** Click **`4. Historical Patterns`** tab to view the 5 canonical fraud topology profiles.
7. **Step 7:** Click **`5. Predictive Hotspots`** tab to view the ranked geographic extraction clusters.
8. **Step 8 (Negative Test):** Click **`[Simulate Normal Activity]`** to prove the system stays quiet on ordinary transactions without false alarms.
9. **Step 9 (Enrichment):** Click **`[Optional Complaint Mode]`** to demonstrate retroactive linking when a citizen files an FIR.

---

## 🏗️ Technical Architecture

| Layer | Technologies Used |
|---|---|
| **Frontend UI** | HTML5, Tailwind CSS, Leaflet.js (GIS Map), Vis.js (NetworkX Graph), Chart.js (Trends), Lucide Icons |
| **Backend API** | Python 3, FastAPI, Uvicorn, SQLite3 (WAL mode) |
| **Machine Learning** | Scikit-Learn (`IsolationForest`, `RandomForestClassifier`), NumPy, Pandas, Cosine Similarity |
| **Graph Intelligence** | NetworkX (directed multigraph, in/out degree, hop traversal, mule identification) |
| **Data Engine** | 10,000 synthetic accounts, 50,000 baseline transactions, 9 Delhi NCR geographic zones, 45+ ATM kiosks |

---

## 🏛️ Legal & Ethical Framing
- **Prototype Mode:** Operates strictly on synthetic data for demonstration safety.
- **Ethical Language:** The system never labels individuals as "criminals"; it surfaces *"Suspicious activity"*, *"High-risk account"*, and *"Actionable investigative leads"* for authorized law enforcement agencies.
- **Production Roadmap:** Outlines institutional data integration pathways with RBI-regulated banking CBS, NPCI switches, and I4C (1930 Helpline).

---

Developed for **Smart India Hackathon 2026**.
# SIH_PROJECT
# SIH_PROJECT
