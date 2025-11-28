# Hardware Construction Guide: Low-Cost CMOS Muon Detector

## 1. Overview
This document details the engineering and construction of a portable cosmic ray muon detector using a standard commercial CMOS sensor. The device operates on the principle that high-energy charged particles (muons) passing through the silicon die generate localized ionization, creating measurable electron-hole pairs that manifest as "hot pixels" in the sensor readout.

**Target Cost:** < $50 USD
**Sensor Type:** CMOS (Complementary Metal-Oxide-Semiconductor)
**Primary Application:** High-altitude vertical transect analysis.

---

## 2. Bill of Materials (BOM)

| Component | Specifications | Notes |
| :--- | :--- | :--- |
| **CMOS Webcam** | USB 2.0, 720p or 1080p | Older models (e.g., Logitech C270) are easier to disassemble. |
| **Shielding A** | Aluminum Foil | Heavy-duty preferred. Acts as a Faraday cage. |
| **Shielding B** | Black Vinyl Electrical Tape | High opacity. Blocks visible/UV photons. |
| **Housing** | Plastic Container (Tupperware) | Weatherproofing and structural support. |
| **Interface** | USB-A to USB-C Adapter | For connecting to modern laptops (MacBook/ThinkPad). |

---

## 3. Theory of Operation
Unlike standard photography, where the goal is to focus visible light (photons, $E \approx 2-3$ eV) onto the sensor, particle detection requires blocking **all** ambient light.

When a cosmic ray muon ($E \approx 4$ GeV) traverses the silicon lattice of the CMOS chip, it deposits energy via ionization (Bethe-Bloch formula). This liberates thousands of electrons along the particle track. These electrons collect in the potential wells of the pixels, registering as a bright signal (value > 0) in an otherwise pitch-black frame.

---

## 4. Construction Steps

### **Step 1: Sensor Extraction**
1.  **Disassemble the Webcam:** Remove the outer plastic casing to expose the PCB (Printed Circuit Board).
2.  **Remove the Lens Assembly:** Unscrew the focusing lens.
3.  **Remove the IR Cut Filter:** Most webcams have a reddish/glassy square filter over the sensor. Carefully pry this off or unscrew the mount. **The bare silicon die must be exposed.**
    * *Warning:* Do not touch the gold wire bonds connecting the sensor to the PCB. They are extremely fragile.

### **Step 2: Optical Isolation (Light Proofing)**
1.  **Primary Shield (Tape):** Place a piece of black electrical tape directly over the lens mount opening (not touching the sensor wire bonds, but covering the aperture).
2.  **Secondary Shield (Foil):** Wrap the entire PCB module in aluminum foil. This serves two purposes:
    * **Light Blocking:** Fills gaps in the tape.
    * **EMI Shielding:** Acts as a Faraday cage to reduce electromagnetic noise from the laptop/environment.
3.  **Final Seal:** Wrap the foil layer entirely in black electrical tape. Ensure no metal foil touches the USB contacts (short circuit risk).

### **Step 3: Enclosure**
1.  Place the taped sensor unit inside a rigid plastic container.
2.  Drill a small hole for the USB cable.
3.  Seal the cable entry with hot glue or tape to prevent light leaks and moisture ingress (crucial for high-altitude snow conditions).

---

## 5. Calibration & Verification

Before deployment, the detector must be calibrated to define the "Noise Floor."

1.  **Connect to Laptop:** Run `src/detector.py`.
2.  **Dark Room Test:** Place the detector in a dark room or cover with a thick blanket.
3.  **Run Noise Analysis:**
    * Observe the feed. It should be completely black (Pixel values $\approx 0$).
    * If you see static "snow" or flickering, the sensor is overheating or there is a light leak.
    * **Threshold Setting:** Determine the maximum brightness of thermal noise (usually values 0-10). Set the software threshold to **25-30** to safely ignore this noise while catching the brighter muon events (often values > 50).

### **Reference Images**
*(See `results/photos/` for actual assembly photos)*

* **Fig 1:** Exposed CMOS Die.
* **Fig 2:** Taped and Shielded Sensor Unit.
* **Fig 3:** Final deployment at Annapurna Base Camp.
