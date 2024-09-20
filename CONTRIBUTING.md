# Contributing to lion-openai

We welcome contributions to the lion-openai project! By contributing, you can help improve the project and make it more useful for everyone. Please take a moment to review this document to understand the process and guidelines for contributing.

## Process for Contributing

1. **Fork the repository**: Start by forking the lion-openai repository to your GitHub account.

2. **Clone the repository**: Clone the forked repository to your local machine.

   ```bash
   git clone https://github.com/your-username/lion-openai.git
   cd lion-openai
   ```

3. **Create a new branch**: Create a new branch for your changes.

   ```bash
   git checkout -b my-feature-branch
   ```

4. **Make your changes**: Implement your changes in the new branch.

5. **Commit your changes**: Commit your changes with a descriptive commit message.

   ```bash
   git add .
   git commit -m "Add new feature"
   ```

6. **Push your changes**: Push your changes to your forked repository.

   ```bash
   git push origin my-feature-branch
   ```

7. **Create a pull request**: Open a pull request from your forked repository to the main repository.

## Development Setup

To set up the development environment, follow these steps:

1. **Install dependencies**: Install the required dependencies using Poetry.

   ```bash
   poetry install
   ```

2. **Activate the virtual environment**: Activate the virtual environment created by Poetry.

   ```bash
   poetry shell
   ```

3. **Run tests**: Run the tests to ensure everything is working correctly.

   ```bash
   poetry run pytest
   ```

## Testing and Code Style

We use the following tools to ensure code quality and consistency:

- **pytest**: For running tests.
- **black**: For code formatting.
- **flake8**: For linting.
- **isort**: For sorting imports.

Before submitting your changes, make sure to run the following commands to check code style and run tests:

```bash
poetry run black .
poetry run isort .
poetry run flake8 .
poetry run pytest
```

## Code Style Requirements

- Follow the PEP 8 style guide for Python code.
- Use type hints for all functions and methods.
- Write docstrings for all public functions and methods.
- Ensure that your code is well-documented and easy to understand.

Thank you for contributing to lion-openai!
