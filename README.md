# 🚆 Train Control System Requirements Tracing Tool

A modular Python-based tool that simulates a systems engineering requirements traceability workflow—similar to IBM Rational DOORS—tailored for safety-critical railway environments. It maps hierarchical requirements between customers, system-level, and subsystem-level modules, enabling better alignment and compliance tracking for rail control systems.

---

## 📌 Features

- 🔄 Parses hierarchical requirement datasets from CSV files.
- 📊 Builds a traceability matrix between customer and system/subsystem requirements.
- 📁 Outputs data in structured JSON format for further processing or visualization.
- 🧩 Supports modular extension for additional layers (e.g., subsystems, test cases).
- 💡 Inspired by Communication-Based Train Control (CBTC) workflows.

---

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Libraries**: `csv`, `json`, `dataclasses`
- **Structure**: Object-oriented with modular file organization
