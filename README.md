# deploy-log-artifact


# deployment-log-generator

This repository contains files to automate the generation of a deployment log in PDF format using GitHub Actions and Python.
 Below is a brief overview of the files provided and how to use them:

Files Included:
pdfArtifact.yml: This YAML file defines a GitHub Actions workflow that triggers on pushes to the main branch. It runs a Python script to generate a deployment log in PDF format and uploads it as an artifact.

PDFlogs.py: This Python script generates the deployment log in PDF format. It includes sample log content and variables like deployment date, deployed by, and environment.

Usage:

After each deployment, access the deployment log PDF from the Actions tab of your GitHub repository.
Customize the PDFlogs.py script to include your actual deployment log content and variables.

Ensure Python and the required libraries (like fpdf) are installed on your system to run the script.
Workflow Steps:

Checkout Repository: Fetches the latest code from your repository.

Generate PDF: Runs the Python script to create the deployment log.

Upload Artifact: Uploads the generated PDF file as an artifact named deployment-log.

Customization:
Edit the PDFlogs.py script to modify the deployment log content or variables as needed.

Support:
For assistance or questions, please reach out to [Your Name/Your Company].
Thank you for using our services!# deploy-log-artifact
# deploy-log-artifact
