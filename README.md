## Introduction

This project is designed to handle API calls for an organization using Python. It includes setting up the necessary development environment, including emulators, and configuring the project for local development and testing.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Development Workflow](#development-workflow)
- [Setting Up Emulators](#setting-up-emulators)
- [Azure Functions](#azure-functions)
- [Committing and Pushing Changes](#committing-and-pushing-changes)
- [Pull Requests](#pull-requests)
- [Contributors](#contributors)
- [License](#license)

## Installation

### Step 1: Install GitHub Desktop
1. Download and install GitHub Desktop from [here](https://desktop.github.com/).

### Step 2: Clone the Repository
1. Open GitHub Desktop.
2. Click on `File` > `Clone repository`.
3. Select the repository URL and clone it to your local machine.

### Step 3: Install Azure Functions Core Tools
1. Download and install Azure Functions Core Tools from [this link](https://go.microsoft.com/fwlink/?linkid=2174087).

### Step 4: Install Required Python Packages
1. Open a terminal and navigate to the project directory.
2. Run the following command to install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Step 5: Install Visual Studio Code
1. Download and install Visual Studio Code from [here](https://code.visualstudio.com/).

### Step 6: Install Recommended VSCode Extensions
1. Open VSCode.
2. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
3. Install the recommended extensions listed in the `.vscode/extensions.json` file.

## Development Workflow

### Branching Model
- **Master Branch**: The production-ready code is stored here.
- **Development Branch**: The latest development code is stored here.
- **Feature Branches**: Use the format `wijzigingstype/wijziging` to create your own branch (e.g., `feature/new-api-call`).

## Setting Up Emulators

### Step 1: Install Docker Desktop
1. Download and install Docker Desktop from [this link](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module).
2. Run Docker Desktop as an administrator.
3. Ensure Docker is running by checking the Docker icon in your system tray.

### Step 2: Install .NET 6
1. Download and install .NET 6 from [this link](https://dotnet.microsoft.com/download/dotnet/6.0).
2. Follow the installation instructions specific to your operating system.
3. Verify the installation by opening a terminal or command prompt and running dotnet --version.

### Step 3: Set Up Database Emulator
1. Open VSCode.
2. Go to the Database Projects tab.
3. Select the database found and click on "Build database" and then "Publish to Emulator".
4. Make sure there is a `local.settings.json` file in your main direactory of the project with the needed environment variables to connect to the emulator.
5. Test your project with the emulator connection.

### Step 4: Set Up Azurite
1. In VSCode, press `F1` and type `Azurite: Start Blob`.
2. This will start the local blob emulator.

### Step 5: Install Azure Storage Explorer
1. Download and install Azure Storage Explorer from [this link](https://go.microsoft.com/fwlink/?linkid=2216182&clcid=0x409).

## Azure Functions

### Adding Azure Functions
1. Create a new folder for your function inside the `functies` directory.
2. Implement the function logic in a Python file.

### Project Structure
```plaintext
.
├── .vscode
│   ├── extensions.json            (Specifies recommended VS Code extensions for the project)
│   ├── launch.json                (Configures debugging settings for the project)
│   ├── settings.json              (Project-specific settings for VS Code)
│   ├── tasks.json                 (Defines tasks for automating workflows in VS Code)
├── .github
│   ├── workflows
│   │   ├── python-app.yml         (GitHub Actions workflow configuration for CI/CD pipeline)
│   ├── pull_request_template.md   (Template for pull request descriptions)
├── functies
│   ├── my_function_name
│   │   ├── __init__.py            (Initializes the Python module for the function)
├── blob_connection
│   ├── __init__.py                (Initializes the Python module for blob storage connection)
├── get_secret
│   ├── __init__.py                (Initializes the Python module for retrieving secrets)
├── pyodbc_connection
│   ├── __init__.py                (Initializes the Python module for pyodbc connection)
├── tests
│   ├── __init__.py                (Initializes the Python module for tests)
└── .gitignore                     (Specifies files and directories for Git to ignore)
└── .funcignore                    (Specifies files and directories for Azure Functions to ignore)
└── README.md                      (Provides an overview and description of the project)
├── requirements.txt               (Lists the project's Python dependencies)
└── function_app.py                (Main entry point for initializing functions)
└── utils.py                       (Library of utility functions for reuse throughout the project)
└── host.json                      (Configuration settings for hosting the project)

```

## Committing and Pushing Changes

### Committing Changes
1. Ensure your commit messages are descriptive and follow the format: `[ChangeType] Description of change`.
2. Example: `[Feature] Add new endpoint for user data`.

### Pushing Changes
1. Push your changes to your feature branch:
    ```bash
    git push origin your-branch-name
    ```

## Pull Requests

### Creating a Pull Request
1. Go to the GitHub repository.
2. Click on `New pull request`.
3. Select your feature branch as the source and the `development` branch as the destination.
4. Fill in the required fields in the pull request template.
5. Request a reviewer to review your code.

### Merging Changes
1. Once your code is reviewed and feedback is addressed, merge your pull request into the `development` branch.
2. For a new release, create a pull request from the `development` branch to the `master` branch.

## Contributors

- [Bram Teunis](https://github.com/BramTeunisCumlaude)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
