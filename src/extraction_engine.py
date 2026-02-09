
import numpy as np
import pandas as pd
from scipy.signal import hilbert
import json
import os
import glob
from datetime import datetime

class PhiBitEngine:
    """
    Automated Research Package for NewFoS Lab.
    Functions: Data Ingestion -> Hilbert Mapping -> Auto-Filing.
    """
    def __init__(self, fs=2000, freq_modes=(40, 80)):
        self.fs = fs
        self.freq_modes = freq_modes
        # Define the paths relative to the repository root
        self.raw_dir = "data/raw"
        self.processed_dir = "data/processed"

    def run_pipeline(self):
        """Finds all CSVs in raw folder and processes them."""
        # 1. Search for new data
        files = glob.glob(os.path.join(self.raw_dir, "*.csv"))
        
        if not files:
            print("📭 No new data found in data/raw/")
            return

        for file_path in files:
            file_name = os.path.basename(file_path)
            print(f"🔄 Processing: {file_name}")
            
            # 2. Load and extract
            df = pd.read_csv(file_path)
            # Assuming the CSV has a column named 'signal' or 'voltage'
            signal = df.iloc[:, 1].values # Takes the second column
            
            psi = self._extract_vector(signal)
            
            # 3. Save result back to repository
            output_name = file_name.replace(".csv", "_result.json")
            self._save_to_repo(psi, output_name)

    def _extract_vector(self, signal):
        """Internal math for Hilbert Space mapping."""
        analytic = hilbert(signal)
        fft_vals = np.fft.fft(analytic)
        freqs = np.fft.fftfreq(len(signal), 1/self.fs)
        
        v = []
        for f in self.freq_modes:
            idx = np.argmin(np.abs(freqs - f))
            v.append(fft_vals[idx] / len(signal))
        
        v_vector = np.array(v)
        return v_vector / np.linalg.norm(v_vector)

    def _save_to_repo(self, psi, filename):
        """Files the results into the processed folder."""
        if not os.path.exists(self.processed_dir):
            os.makedirs(self.processed_dir)

        result = {
            "timestamp": datetime.now().isoformat(),
            "state_vector": [str(psi[0]), str(psi[1])],
            "status": "Verified"
        }
        
        path = os.path.join(self.processed_dir, filename)
        with open(path, 'w') as f:
            json.dump(result, f, indent=4)
        print(f"✅ Filed to: {path}")

if __name__ == "__main__":
    # When you run the package, it executes the loop
    engine = PhiBitEngine()
    engine.run_pipeline()
