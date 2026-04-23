# AI Web Interaction Engine

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![AI](https://img.shields.io/badge/AI-Multimodal-green)
![Vision](https://img.shields.io/badge/Vision-YOLOv8-orange)
![Speech](https://img.shields.io/badge/Speech-Vosk-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A multi-modal automation system that combines computer vision and speech recognition to interact with complex web interfaces where traditional automation falls short.

This project demonstrates how AI can enhance browser automation by enabling systems to interpret visual and audio-based elements dynamically.

---

## 🚀 Overview

Traditional automation tools struggle with:
- Non-structured UI elements
- Dynamic visual components
- Audio-based interactions
- Human-like decision flows

This system integrates:
- **Computer Vision (YOLOv8)** for visual understanding
- **Speech-to-Text (Vosk)** for audio processing
- **Selenium-based automation** for execution
- **Decision logic layer** for intelligent interaction

---

## 🧠 Key Features

- 🔍 Vision-based UI element detection using YOLOv8
- 🎧 Audio processing via Vosk for speech-to-text conversion
- 🤖 Automated browser interaction with Selenium
- ⚙️ Intelligent task selection and execution logic
- 🔄 Repetitive workflow automation with adaptive behavior

---

## 🏗️ Architecture


Input (Web Page)
↓
Vision (YOLOv8) → Detect UI elements
↓
Audio (Vosk) → Process audio inputs
↓
Decision Layer → Select optimal action
↓
Execution Layer (Selenium)
↓
Repeat Loop


---

## 🧪 Technologies Used

- Python
- Selenium
- YOLOv8 (Ultralytics)
- Vosk (Offline Speech Recognition)
- OpenCV
- NumPy

---

## 🎯 Use Cases

- Automating complex web workflows
- AI-assisted UI interaction systems
- Accessibility tools for dynamic web interfaces
- Intelligent data extraction from non-structured pages

---

## ⚠️ Disclaimer

This project is intended for **educational and research purposes only**, demonstrating how AI can enhance automation systems.

It should be used in compliance with website terms of service and applicable laws.

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-web-interaction-engine.git
cd ai-web-interaction-engine
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the project
```bash
python main.py
📁 Project Structure (recommended)
.
├── main.py
├── vision/
│   └── yolo_detector.py
├── audio/
│   └── speech_to_text.py
├── automation/
│   └── browser_controller.py
├── models/
├── downloaded_files/
├── requirements.txt
└── README.md
```

---

### 💡 Future Improvements

- Real-time streaming pipeline
- Better decision intelligence using LLMs
- UI generalization across websites
- Integration with agent-based systems

### 👤 Author

Siddharth Lal
Backend & AI Systems Engineer
