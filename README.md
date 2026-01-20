## Pytorch-Image-Classification


### Dependencies

* Python3
* Pytorch

```python
pip instal pytorch       # pytorch library
pip install torchsummary # summary
pip install torchvision  # pytorch for vision
```

⬇️⬇️**Download**: [Dataset](https://drive.google.com/file/d/1Rv82F7CjPveyONdy1YbRHh05emCb6_Eu/view)


### Results
| Model   | Accuracy | Precision (Normal) | Precision (DME)| Precision (AMD) |
|----|----|----|----|-----|
| **ResNet50 Finetuning** | 98.5% | 97.6%   |  98%  |  99%  |


### Authors

Van Thiep

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <repository-name>
```

### 2. Environment Setup

Ensure you have **Python 3.8+** installed. Then install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## 📖 Usage Guide

### 1. Quick Start

Run the tool with default settings (**Color mode**, **Save action**, **Device 0**):

```bash
python main.py
```

---

### 2. Command Line Arguments

You can customize the execution by passing the following arguments.

#### 🔹 Basic Settings

| Argument   | Type  | Default | Choices / Description                             |
| ---------- | ----- | ------- | ------------------------------------------------- |
| `--mode`   | int   | 8       | Image Mode: `2` (Depth), `8` (Color), `12` (Mono) |
| `--action` | int   | 2       | Action: `1` (Stream), `2` (Save), `3` (Both)      |
| `--output` | str   | Output  | Root directory for file storage                   |
| `--fps`    | float | 50.0    | Desired acquisition frame rate                    |
| `--device` | int   | 0       | Camera device index                               |

#### 🔹 Advanced Hardware Settings

| Argument           | Type | Default | Choices / Description                       |
| ------------------ | ---- | ------- | ------------------------------------------- |
| `--working-mode`   | int  | 4       | `0` (Calibration), `2` (Debug), `4` (Depth) |
| `--exposure-mode`  | int  | 2       | `0` (Single), `2` (Multiple)                |
| `--color-exposure` | int  | 1       | `0` (Single), `1` (Dynamic)                 |

---

## 💡 Examples

### A. Stream Live Depth Data

```bash
python main.py --mode 2 --action 1
```

### B. Save Mono Images at 30 FPS to a Specific Folder

```bash
python main.py --mode 12 --action 2 --fps 30.0 --output ./Recordings
```

### C. High-Speed Capture (Stream & Save) with Device 1

```bash
python main.py --device 1 --action 3 --fps 60.0
```

### D. Calibration Setup (Single Exposure & Calibration Mode)

```bash
python main.py --working-mode 0 --exposure-mode 0 --color-exposure 0
```

---

## ❓ Getting Help

To view all available options and descriptions directly in your terminal, run:

```bash
python main.py --help
```

---

## 📝 Requirements

* Compatible **MVS Camera** hardware.
* Properly installed **MVS Camera drivers / SDK** on your operating system.
* Sufficient disk space if `--action` is set to `2` (Save) or `3` (Both).
