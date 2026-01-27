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

# Hikrobot MV-DLS600P

## Device Overview
The **MV-DLS600P** is a binocular structured light stereo camera from Hikrobot, designed to deliver high-precision measurements in industrial environments.

### Key Technical Specifications:
| Parameter | Value |
| :--- | :--- |
| **Measuring Range** | 1000 mm |
| **Working Distance (WD)** | 1200 mm |
| **Field of View (FOV)** | From 580 × 520 mm to 1220 × 960 mm |
| **XY Accuracy** | Up to 0.5 mm (at 1.2 m) |
| **Z Accuracy** | Up to 0.2 mm (at 1.2 m) |
| **Scan Speed** | 1 fps |
| **Laser Safety** | Class 2 |

---

## 🛠 Software & SDK Installation

To operate the camera, you need to install Hikrobot software tools according to your operating system.

### 1. Download Control Software
- **Windows:** Use **HiViewer**
- **Linux:** Use **Machine Vision Software (MVS)**
- **Official download link:** https://www.hikrobotics.com/en/machinevision/service/download/

---

### 2. SDK Configuration (Linux Only)

After installing MVS, all SDK resources are located at:

```
/opt/MVS
```
- **SDK Documentation:** `/opt/MVS/doc  
- **Sample Source Code:** `/opt/MVS/doc/samples`
---

### 3. Reference Documentation
- Product documentation [link](https://www.ztec.dk/shop/hikrobot-306400345-hikrobot-mv-dls600p-12-52392)
- **MV-DLS600P-12 Galvanometer Laser 3D.pdf** – Detailed specifications
- **UD44176B_Binocular Structured Light Stereo Camera User Manual** – Instructions for using camera features in **HiViewer (Windows only)**
- **User_Manual_of_Client_Software_English.pdf** – Instructions for using **MVS on Ubuntu (Linux)** located at:`/opt/MVS/bin/`

---



## 📂 Project Directory Structure

```
mv_dls600p/
├── Camera_implement/
│   ├── __init__.py
│   └── Camera.py               
├── Output/                      
│   ├── color_images/             
│   └── depth_images/            
├── tests/
│   ├── get_color_image.py    
│   └── get_depth_image.py  
├── utils/
│   ├── __init__.py
│   └── camera_setup.py 
    └── config.py  
    └── io_utils.py                  
├── main.py                    
├── README.md                    
├── requirements.txt
├── setup.py            
```

---

## 🛠 Installation

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone git@bitbucket.org:vinrobotics/mv_dls600p.git
cd mv_dls600p/Hikrobot_mv_dls600p

### 📌 Notes
- `pip install -r requirements.txt` installs all required dependencies.
- `pip install -e .` installs the project as a local editable package, allowing code changes without reinstallation.

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

| Argument   | Type  | Default | Choices / Description                                              |
| ---------- | ----- | ------- | ------------------------------------------------------------------ |
| `--mode`   | int   | 8       | Image Mode: `2` (Pointcloud) `2` (Depth), `8` (Color), `12` (Mono) |
| `--action` | int   | 2       | Action: `1` (Stream), `2` (Save), `3` (Both)                       |
| `--output` | str   | Output  | Root directory for file storage                                    |
| `--fps`    | float | 50.0    | Desired acquisition frame rate                                     |
| `--device` | int   | 0       | Camera device index                                                |

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


### C. Calibration Setup (Single Exposure & Calibration Mode)

```bash
python main.py --working-mode 0 --exposure-mode 0 --color-exposure 0
```


### D. Capture Color Point Clouds (Save Only)

```bash 
python main.py --mode 1 --action 2 
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


