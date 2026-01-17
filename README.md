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
Hikrobot_mv_dls600p/
├── Camera_implement/
│   ├── __init__.py
│   └── Camera.py               
├── output/                      
│   ├── color_images/             
│   └── depth_images/            
├── tests/
│   ├── hikrobot_camera_rgb.py    
│   └── hikrobot_camera_depth.py  
├── utils/
│   ├── __init__.py
│   └── utils.py               
├── main.py                    
├── README.md                    
├── requirements.txt           
```

---

## Usage Instructions

### 1. Set up the environment
```bash
pip install -r requirements.txt
```

### 2. Get image

```bash
python main.py   
```
