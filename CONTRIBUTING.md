<!---
Copyright 2026 Sahíl Sharma. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Contribute to Gen Ai Mod App

Everyone is welcome to contribute, and we value every contribution. Code contributions are not the only way to support the project. Improving website content generation, image generation, language translation, text refinement, Google Cloud Run deployment, performance, architecture, security, testing, or documentation are all valuable ways to contribute to **Gen Ai Mod App**.

This project was developed as part of the Google Cloud learning experience using Gemini models, Imagen, and FastAPI. Contributions that improve the learning experience, reliability, maintainability, and practical application of modernized web applications are especially welcome.

If you find this project helpful, consider sharing it with others, referencing it in your blogs or projects, discussing it on social platforms, or simply giving the repository a ⭐️ to support the project and the community.

**However you choose to contribute, please be mindful and respect our [Code of Conduct](https://github.com/sahil-me/gen-ai-mod-app/blob/main/CODE_OF_CONDUCT.md).**

## Ways to contribute

There are several ways you can contribute to **Gen Ai Mod App**.

- **Website Content Generation:** Improve content generation quality, efficiency, and automated update workflows using generative AI.
- **Image Generation & Tuning:** Improve image generation using Vertex AI Imagen models, custom prompts, image editing features, and Cloud Storage integration.
- **Content Translation:** Improve inline text translation workflows into various target languages using generative language models.
- **Text Refinement:** Improve copy editing capabilities, style tuning (such as formal or impactful tones), and text replacement mechanisms on web pages.
- **Agent Search Integration:** Improve search integration using Agent Search on the Gemini Enterprise Agent Platform to handle unstructured data like blog posts.
- **FastAPI & Backend Improvements:** Improve backend API routers, data models, content caching, and application entrypoints.
- **Gemini Integration:** Improve model configuration, response quality, reliability, instruction following, and integration with Google AI services.
- **Cloud Run Deployment:** Improve containerization via Dockerfile, deployment reliability, environment configuration, and scaling on Cloud Run.
- **Logging & Observability:** Improve logging, debugging information, error reporting, and trace tracking using Google Cloud Logging and Logs Explorer.
- **Performance Optimization:** Improve application speed, container build times, response handling, and overall system efficiency.
- **Security Improvements:** Help identify and address issues involving credentials, environment variables, permissions, data handling, and configuration.
- **Testing:** Add or improve tests for website endpoints, generation logic, translation features, and error handling.
- **Documentation:** Improve the README, setup instructions, architecture documentation, usage examples, troubleshooting guidance, and contribution instructions.

> All contributions are valuable to the project and its learning community. 🥰

## Submitting a bug-related issue or feature request

Feel free to open an issue when you encounter a bug or have an idea for improving **Gen Ai Mod App**. Include relevant error logs, reproduction steps, Python and dependency versions, environment details, or Google Cloud service information when appropriate.

Please check the existing issues before creating a new one. This helps avoid duplicate reports and makes it easier to track existing problems.

### Did you find a bug?

**Gen Ai Mod App** becomes more reliable through community feedback, issue reporting, testing, and meaningful contributions.

Before reporting an issue, please make sure the bug has not already been reported under the repository's **Issues** section.

When submitting a bug report, please include the following information:

- Your **operating system** and version.
- Python version and relevant dependency versions.
- Steps to reproduce the issue.
- A short description of the expected behavior and what actually happened.
- Relevant error messages or application logs.
- The affected component, such as the FastAPI backend, image generation module, translation router, or Cloud Run service.
- Relevant configuration files, such as `config.toml` or `Dockerfile`.
- Google Cloud service or deployment information, if applicable.
- Screenshots or screen recordings, if applicable.
- Any other information that may help reproduce or understand the issue.

Please **do not include API keys, passwords, authentication tokens, service-account credentials, `.env` files, temporary Google Skills lab credentials, or other sensitive information** in an issue.

### Do you want a new feature?

If there is a new feature you'd like to see in **Gen Ai Mod App**, please open an issue and describe:

1. **Motivation**

   Explain the problem, limitation, or use case that the feature would address.

2. **Feature Description**

   Describe the proposed feature and how you would expect it to work.

3. **Generative AI Integration**

   If the feature affects AI capabilities, explain how it should influence model selection, prompt engineering, text refinement, or image creation.

4. **Web Application & UI Behavior**

   If the feature affects the frontend or FastAPI backend, describe the expected changes to routes, templates, or user interactions.

5. **Cloud Infrastructure**

   If the feature affects Cloud Run deployment, Cloud Storage buckets, or Artifact Registry, describe the infrastructure and configuration requirements.

6. **Implementation Details**

   If you have an implementation idea, architecture suggestion, or code example, feel free to include it.

7. **Additional References**

   If the feature is inspired by an external project, article, design, or technical reference, please include the relevant link.

A clear and well-written feature request makes it easier to evaluate and discuss the proposal.

## Do you want to improve generative AI content and image editing?

Generative AI tools are core to modernizing website text and visual assets.

You can contribute by:

- Improving prompt templates for text translation and refinement.
- Enhancing image generation workflows using Vertex AI Imagen.
- Improving error handling when generation APIs are unavailable or rate-limited.
- Adding support for new Gemini model versions and parameters.
- Improving how generated images are stored, retrieved, and linked via Cloud Storage.
- Improving documentation for generative configuration and prompt styling.
- Adding tests for content translation and copy refinement logic.

When modifying AI workflows, ensure that outputs remain clean, well-formatted, and aligned with project constraints (such as avoiding stray quotes or markdown formatting in raw outputs).

## Do you want to improve FastAPI and backend architecture?

The project relies on a FastAPI backend structured with routers, models, and utility handlers.

You can contribute by:

- Improving API route structure and request validation.
- Optimizing data models and content caching.
- Enhancing error handling and middleware configuration.
- Improving asynchronous execution and performance.
- Adding comprehensive unit and integration tests for backend routes.
- Simplifying dependency injection or code organization.

Changes to backend logic should be thoroughly tested to ensure stability across local development and Cloud Run environments.

## Do you want to improve Cloud Run and deployment reliability?

Cloud Run hosts the containerized web application.

You can contribute by:

- Optimizing the `Dockerfile` for faster builds and smaller image sizes.
- Improving environment variable management and configuration loading via `config.toml`.
- Enhancing deployment documentation and troubleshooting steps.
- Improving health checks, startup probes, and container lifecycle management.
- Securing application permissions and IAM service accounts.

Infrastructure and deployment adjustments should be validated in a live development environment before submission.

Do not include temporary Google Skills lab credentials, project-specific secrets, or private configuration files in your changes.

## Do you want to improve testing and reliability?

Testing is an important part of making **Gen Ai Mod App** easier to maintain and extend.

You can contribute by:

- Adding tests for individual FastAPI routes and backend handlers.
- Testing image generation and content translation utilities.
- Testing configuration parsing and environment setup.
- Testing error handling and unavailable service recovery.
- Improving test repeatability and documentation.

Tests should match the component being modified. Document any prerequisites or environment setups required for running integration tests.

## Do you want to improve documentation?

We're always looking for improvements that make **Gen Ai Mod App** clearer and easier to understand.

You can contribute by:

- Fixing typos or grammatical errors.
- Improving the README.
- Improving setup and local development instructions.
- Clarifying environment-variable and `config.toml` configuration.
- Documenting the project architecture and file structure.
- Documenting Google Cloud Run and Artifact Registry integration.
- Adding examples of supported website modernization workflows.
- Linking to relevant Google Skills course and lab resources.

Documentation contributions are especially appreciated when they help new contributors understand the project, set up their environment, and get started safely.

## Fixing outstanding issues

If you notice an existing issue and have a fix in mind, feel free to **[start contributing](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)** and open a Pull Request.

### Making code changes

<details>
<summary><strong>Step-by-step contribution workflow</strong></summary>

#### 1. Fork the repository

Go to the [Gen Ai Mod App repository](https://github.com/sahil-me/gen-ai-mod-app) on GitHub and click the **Fork** button.

#### 2. Clone your forked repository

Replace `<username>` with your GitHub username.

```bash
git clone https://github.com/<username>/gen-ai-mod-app.git
```

Navigate into the project directory:

```bash
cd gen-ai-mod-app
```

#### 3. Create a new branch

Create a separate branch for your feature or bug fix.

```bash
git checkout -b feature/your-feature-name
```

For a bug fix, you can use a name such as:

```bash
git checkout -b fix/issue-description
```

#### 4. Set up the Python environment

Make sure Python is installed. Create a virtual environment from the repository root:

```bash
python -m venv .venv
```

Activate the environment.

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

#### 5. Install dependencies

Install the listed dependencies from the requirements file:

```bash
python -m pip install -r requirements.txt
```

> Dependency installation commands may need to be adjusted if the repository's dependency files change.

#### 6. Configure Google Cloud and Gemini services

Configure the Google services, authentication, permissions, and other resources required by the component you are working on.

Follow the current project README, the relevant Google Skills lab instructions, and official Google documentation.

Workflows require authorized access to Vertex AI, Gemini models, Google Cloud Run, and Cloud Storage. Contributors are responsible for using an appropriately authorized development environment.

> Never commit API keys, service-account credentials, access tokens, temporary lab credentials, or other secrets to the repository.

#### 7. Configure environment variables and configuration files

Configure required environment variables and update `config.toml` according to the current project setup instructions.

Use your own authorized development resources and follow the applicable configuration guidance.

> Do not commit `.env` files or other files containing sensitive configuration. Keep secrets out of logs, screenshots, and Pull Request descriptions.

#### 8. Run the application locally

Launch the FastAPI application using Uvicorn or the project's entrypoint:

```bash
uvicorn main:app --reload --port 8080
```

Verify the working directory, installed dependencies, required environment variables, and service configuration before running the app.

Make sure the server starts successfully before making or testing changes.

#### 9. Make your changes

- Develop the feature or fix the issue.
- Follow the existing project structure and coding conventions.
- Keep changes focused and maintainable.
- Avoid unrelated modifications.
- Document important assumptions.
- Preserve existing functionality unless a change is intentional.
- Test your changes before submitting a Pull Request.

#### 10. Run and test functionality

If your changes affect the web application, test representative scenarios such as:

- Launching the FastAPI server locally and navigating through web pages.
- Testing text translation and refinement features.
- Testing image generation and tuning flows.
- Verifying search application integration.
- Checking container builds via Docker.

Verify that the application behaves as intended and that outputs are handled gracefully.

#### 11. Commit your changes

From the repository root, review the files you have changed and stage only the intended changes.

```bash
git status
git add <file-or-directory>
git commit -m "Describe your change"
```

Avoid committing credentials, local configuration files (`config.toml`), generated files, or unrelated modifications.

#### 12. Push to your fork

```bash
git push origin feature/your-feature-name
```

Replace the branch name if you used a different one.

#### 13. Create a Pull Request

Open your fork on GitHub and create a Pull Request targeting the original **Gen Ai Mod App** repository.

In your Pull Request description:

- Explain what you changed.
- Explain why the change was needed.
- Reference any related issue.
- Describe changes to application behavior or APIs.
- Include relevant screenshots or logs when appropriate.
- Describe the tests you performed.
- Mention Google Cloud configuration or integration changes, if applicable.
- Explain any setup requirements or limitations.

#### 14. Address feedback

If the project maintainer leaves comments or requests changes, address the feedback and push the required updates to your branch.

Thank you for taking the time to review and improve the project!

</details>

## Contribution Guidelines

To keep the project maintainable and welcoming:

- Keep Pull Requests focused on a single feature, fix, or improvement whenever possible.
- Avoid unnecessary changes to unrelated files.
- Follow the existing code style and project structure.
- Test changes before submitting a Pull Request.
- Test generative AI functionality when modifying model or prompt logic.
- Verify container and Cloud Run configurations before deployment.
- Avoid introducing unsupported facts or claims into application responses.
- Keep credentials and sensitive configuration out of the repository.
- Do not commit API keys, `.env` files, `config.toml`, service-account credentials, or other secrets.
- Do not make unverified claims about external services or deployment status.
- Provide clear commit messages and Pull Request descriptions.
- Include relevant screenshots, logs, or test results when appropriate.
- Be respectful and constructive when reviewing or discussing contributions.

## I want to become a maintainer of the project. How do I get there?

**Gen Ai Mod App** is a learning and demonstration project focused on modernizing legacy websites using Google Cloud Run, FastAPI, and Generative AI (Gemini and Imagen).

Contributors interested in improving content generation, image tools, translation workflows, FastAPI routing, Cloud Run deployments, testing, security, documentation, and Google Cloud integration are welcome.

If you are interested in contributing at a deeper level, consistently submitting meaningful improvements, reviewing Pull Requests, improving documentation, or helping maintain the project, feel free to get involved and collaborate.

Thank you for contributing to **Gen Ai Mod App**! 📲
