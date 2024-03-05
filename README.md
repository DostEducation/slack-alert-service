# Slack-Alert-Service

This repository supports a generic Slack alert service. We use a trigger pub/sub to send budget alert notifications and an HTTP trigger to alert the team about Exotel call permissions on the Slack channel.

## Installation

### Prerequisite

1. pyenv
2. python 3.11

### Steps

1. Clone the repository
   ```sh
   git clone https://github.com/DostEducation/slack-alert-service.git
   ```
2. Switch to project folder and setup the virtual environment
   ```sh
   cd slack-alert-service
   python -m venv venv
   ```
3. Activate the virtual environment
   ```sh
   source ./venv/bin/activate
   ```
4. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Set up your .env file by copying .env.example
   ```sh
   cp .env.example .env
   ```
6. Add/update variables in your `.env` file for your environment.
7. Run the following command to get started with pre-commit
   ```sh
   pre-commit install
   ```
8. Start the server by following command:

   ```sh
   functions_framework --target=handle_alerts --debug
   ```
