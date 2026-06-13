# treasury-ai-label-verification

## Executive Summary

This repository contains a standalone proof-of-concept (PoC) for an AI-powered alcohol label verification system, designed to modernize the Department of the Treasury's legacy review workflows.  

The Alcohol and Tobacco Tax and Trade Bureau (TTB) operates as a critical federal revenue generator, collecting billions annually in excise taxes. This project addresses the operational challenge of transitioning from manual, paper-based legacy verification processes—originally digitized in 2003 [1]—to an automated, AI-assisted architecture. By implementing a human-in-the-loop design, this prototype demonstrates how AI can enhance processing throughput and support compliance agents without compromising the accuracy or regulatory nuance required for federal market oversight.  

## Technical Approach & Assumptions
**Architecture**: A standalone proof-of-concept utilizing a modular design to allow for future .NET or Azure integration.

**Security**: Designed for prototype usage; utilizes environment variables for all API keys to ensure no credentials are stored in source code.

**Assumptions**: The system assumes standard input formats (PDF/JPG) and acknowledges that image-based label verification remains an evolving computer vision challenge.

## Project Structure
The repository is organized to maintain a clean separation between command-line orchestration and AI processing logic:

- `main.py`: The entry point that manages user arguments and input/output flow.
- `processor.py`: Contains the core logic for image analysis and label verification.
- `requirements.txt`: Lists all Python dependencies required to run the environment.
- `/data/labels/`: Reserved directory for batch processing of label images.

## Setup and Installation

This project requires a Python 3.10+ environment. Follow these steps to configure your local development environment:

## Prerequisites

Python 3.10+

Git

API Access: Ensure your network environment permits outbound traffic to required ML endpoints.  

## Local Installation

**1. Clone the Repository:**  

   git clone https://github.com/your-username/treasury-ai-label-verification.git
   cd treasury-ai-label-verification

**2. Create a virtual environment:**  

   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate

**3. Install dependencies:**  

   pip install -r requirements.txt

## Usage

**To run the verification prototype locally:**

python main.py --input-folder ./data/labels

**Note:** The system is designed to handle batch uploads for label applications. Ensure your sample images are placed in the           ./data/labels directory before running.  

## Configuration

**1. Create a copy of the template file:** 
   cp .env.example .env

**2. Open the .env file and input your credentials:** 

   AI_MODEL_API_KEY=your_key_here
   PROXY_URL=http://your-proxy-address:port
   
## References

1. TTB Discovery Session Notes (Internal Project Documentation)
