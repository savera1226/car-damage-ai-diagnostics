🚗 AI Vehicle Damage Diagnostic Engine

📝 Project Overview
This end-to-end Computer Vision application automates the assessment of vehicle damage for insurance and repair industries. By utilizing a fine-tuned ResNet-50 architecture, the engine identifies both the location (Front/Rear) and the severity (Normal/Breakage/Crushed) of damage from 3/4 view images.

🚀 Key Features
Real-time Diagnostics: Instant classification across 6 specialized damage categories.

Confidence Scoring: Visualized certainty metrics for every prediction to ensure diagnostic reliability.

Automated Reporting: Generates a formal PDF/TXT diagnostic report for insurance claims.

Safety Logic: Built-in warning system for low-confidence predictions requiring manual inspection.

🧠 Technical Architecture
The Model
Backbone: ResNet-50 (Transfer Learning).

Optimization: Unfrozen layer4 and custom Fully Connected (FC) head for domain-specific feature extraction.

Dataset: 2,378 proprietary images (Balanced across 6 classes).

Training Specs: CrossEntropyLoss with Adam Optimizer and weight decay regularization.

Performance Metrics
Validation Accuracy: 78.49%.

Inference Speed: ~0.5s per image on CPU.

🛠️ Installation & Setup
Clone the Repository

Bash
git clone https://github.com/your-username/car-damage-detection.git
cd car-damage-detection

Install Dependencies

Bash
pip install -r requirements.txt
Launch the App

Bash
streamlit run app.py

📊 Future Roadmap
[ ] Integration of Grad-CAM for damage localization (Heatmaps).

[ ] Support for side-impact and roof damage detection.

[ ] Mobile-optimized interface for on-site insurance adjusters.