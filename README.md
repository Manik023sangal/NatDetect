## 📌 Project Overview
This project is a demonstration of a **Nationality & Emotion Detection GUI** using Tkinter and placeholder logic.

The system takes an input image and predicts:
- **Nationality**
- **Emotion**

Based on nationality:
- **Indian** → Predicts Age, Dress Colour, Emotion  
- **US** → Predicts Age, Emotion  
- **African** → Predicts Dress Colour, Emotion  
- **Others** → Predicts Nationality, Emotion 

## 🚀 How to Run
1. Download this project.  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the GUI:  
   ```bash
   python app.py
   ```

---

## 📂 Files
- `app.py` → Tkinter GUI Application  
- `requirements.txt` → Required dependencies  
- `README.md` → Documentation  

---

## 🛠️ Future Improvements
- Integrate a **deep learning model** for nationality & emotion detection.  
- Extend dataset for **age & dress colour classification**.  
- Deploy on **web interface (Streamlit/Flask)**.  

---

## 📌 Requirements
- Python 3.8+  
- Tkinter
- Pillow  
