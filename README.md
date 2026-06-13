# treasury-ai-label-verification

## Executive Summary

This repository contains a standalone proof-of-concept (PoC) for an AI-powered alcohol label verification system, designed to modernize the Department of the Treasury's legacy review workflows.  

The Alcohol and Tobacco Tax and Trade Bureau (TTB) operates as a critical federal revenue generator, collecting billions annually in excise taxes. This project addresses the operational challenge of transitioning from manual, paper-based legacy verification processes—originally digitized in 2003 [1]—to an automated, AI-assisted architecture. By implementing a human-in-the-loop design, this prototype demonstrates how AI can enhance processing throughput and support compliance agents without compromising the accuracy or regulatory nuance required for federal market oversight.  

## Getting Started

This project requires a Python 3.10+ environment. Follow these steps to set up your local development environment:

**1. Clone and Initialize**

git clone https://github.com/your-username/treasury-ai-label-verification.git
cd treasury-ai-label-verification

**2. Environment Setup**

## Create and activate virtual environment
python -m venv venv
## On Windows:
venv\Scripts\activate
## On macOS/Linux:
source venv/bin/activate

**3. Dependencies & Configuration**

Install the required packages and configure your credentials:

pip install -r requirements.txt
pip install python-dotenv

Create a .env file in the root directory and add your credentials:

VISION_API_KEY=your_key_here
PROXY_URL=http://your-proxy-address:port

Note: The .env file is ignored by Git to ensure security.

**4. Usage**

To process label images, run the following command:

python main.py --input-folder ./data/labels

Ensure sample images are placed in the ./data/labels directory before running.

## Project Structure

**main.py:** The entry point that manages user arguments and input/output flow.

**processor.py:** Contains the core logic for image analysis and label verification.

**requirements.txt:** Lists all Python dependencies required to run the environment.

**/data/labels/:** Reserved directory for batch processing of label images.

## Troubleshooting

**ModuleNotFoundError:** Ensure your virtual environment is activated before installing dependencies.

**Execution Policy Errors (Windows):** If PowerShell prevents script execution, run Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process before activating the environment.

**Permission Errors:** Ensure your IDE has appropriate disk write permissions for the project directory.

## Technical Approach

**Architecture:** Modular design facilitating future cloud integration.

**Security:** Employs environment variables to prevent credential leakage.

**Assumptions:** The system supports standard input formats (JPG/PDF) and assumes a modular pipeline for future OCR engine upgrades.

## Project Roadmap & Next Steps

**[ ] Engine Integration:** Connect the modular processor to a production-grade Vision Engine (Azure/Google Cloud).

**[ ] Human-in-the-loop Interface:** Develop a UI for compliance agents to verify AI suggestions.

**[ ] Advanced Processing:** Expand capability to support multi-page PDF documents and batch analysis.

## License

This project is for assessment purposes. All rights reserved.

## References

[1] TTB Discovery Session Notes (Internal Project Documentation)
