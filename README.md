# Workflow Trigger Middleware for Slack and GitHub Actions

## Overview

This middleware API is designed to serve as a bridge between Slack and GitHub Actions, allowing you to trigger workflows with ease. By sending requests from Slack to your middleware, you can initiate GitHub Actions workflows, automating various tasks in your development process.

## Features

Slack Integration: Receive requests from Slack to trigger workflows.
GitHub Actions: Communicate with GitHub Actions API to start workflows.
Configurability: Easily configure and customize workflows to suit your needs.

## Setup
1 Clone the Repository:

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2 Install Dependencies:

```
pip install -r requirements.txt
```

3 Configure Slack and GitHub Tokens:

Obtain a Slack App token for your workspace.
Generate a GitHub Personal Access Token with the necessary permissions.

4 Update Configuration:

add a .env file with the following information

```
FLASK_DEBUG=
DB_USERNAME=
DB_PASSWORD=
DB_SERVER=
DB_DATABASE=
DB_DRIVER=
GITHUB_TOKEN=
SLACK_TOKEN=
```


```
python app.py
```

## Usage

1 Send a Request from Slack:

Use a Slack command or interactive message to send a request to your middleware.

2 Middleware Processes Request:

The middleware receives the request, validates it, and triggers the corresponding workflow in GitHub Actions.

3 GitHub Actions Executes Workflow:

GitHub Actions executes the specified workflow based on the request parameters.