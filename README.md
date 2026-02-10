# Automated-Hilbert-Space-Mapping-for-Topological-Acoustic-Computing 🪇
This repository provides the required software to run the extraction_engine package for digital signal analysis for topological acoustics.
By implementing a modular "Extraction Engine" this package is able to automate the transformation of time-series acoustic data into high-dimensional Hilbert space vectors. This allows for the real-time mapping of state transitions—or "Phi-bits"—onto a Bloch Sphere representation, facilitating the rapid verification of non-linear logic gates. Built with a focus on reproducibility and data integrity, the repository integrates modern CI/CD principles to ensure that every experimental iteration is version-controlled, structured, and ready for advanced cryptographic research

## Install instructions
This project is built using Python 3.x. To ensure a reproducible research environment and avoid dependency conflicts, please follow these steps:

### 1. Clone the Repository

Open your terminal or command prompt and run:

'''Bash
git clone https://github.com/yourusername/Acoustic-Encryption-Automation.git
cd Acoustic-Encryption-Automation
'''
### 2. Create a Virtual Environment

This isolates the project dependencies specifically for this lab work:

Windows:

Bash
python -m venv venv
.\venv\Scripts\activate
macOS/Linux:

Bash
python3 -m venv venv
source venv/bin/activate

### 3. Install Required Dependencies

Install the specific versions of the libraries used in the extraction engine:

Bash
pip install -r requirements.txt

### 4. Verify the Engine

Run the self-test built into the core logic to ensure the Hilbert Transform and mapping functions are active:

Bash
python src/extraction_engine.py
If successful, you will see a message: "Test Successful. State Vector extracted."
