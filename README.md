Deployment Log Generator

Overview

This GitHub repository contains a GitHub Actions workflow that automates the generation of a PDF log file based on the job's log output. The PDF log file serves as a record of the deployment process, capturing important information such as timestamps and status updates.

Workflow Steps
Checkout Repository: The workflow starts by checking out the repository code to the GitHub Actions runner environment.
Set up Python 3.10: Python 3.10 is set up as the runtime environment for the workflow.
Install Dependencies: Necessary Python dependencies (fpdf, pandas, regex, pyyaml) are installed using pip.
Generate PDF Log: The job's log output is processed and converted into a PDF file using a Python script (PDFlogs.py). The script includes functionality to parse variables and include them at the top of the PDF file.
Upload Artifact: The generated PDF log file is uploaded as an artifact named "deployment-log" to GitHub. This allows easy access and retrieval of the log file for future reference.
Accessing the PDF Log
To access the generated PDF log file:

Go to the "Actions" tab of this GitHub repository.
Select the workflow run where the log was generated.
Locate the "deployment-log" artifact and download it to your local machine.
Open the PDF file using a PDF viewer to view the deployment log.
Usage
To use this GitHub Actions workflow for your deployments:

Ensure that your deployment process generates log output in a format that can be parsed by the provided Python script (PDFlogs.py).
Customize the workflow to suit your specific deployment requirements, such as adjusting input variables and dependencies as needed.
Run the workflow manually or trigger it automatically based on your desired events (e.g., push to the main branch).
Feedback and Support
If you encounter any issues or have feedback regarding this GitHub Actions workflow, please feel free to open an issue in this repository. We're here to help and improve the workflow to better meet your needs.
