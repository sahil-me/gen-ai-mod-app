# 🌐 Gen Ai Mod App 📲

https://github.com/user-attachments/assets/44119e2f-ad16-4612-ac6c-6da97987a7cc

> 🎥 Watch **Gen Ai Mod App** in action!

> [!CAUTION]
> The Cloud Run deployment is currently unavailable because the Google Cloud project has exhausted its available credits. The project was previously deployed and tested successfully on Google Cloud Run.

---

## Table of Contents

- [Introduction](#introduction)
- [Architecture Diagram](#architecture-diagram)
- [Project Structure](#project-structure)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Application Workflow](#application-workflow)
- [Screenshots](#screenshots)
- [Generative AI Capabilities & Integration](#generative-ai-capabilities--integration)
- [AI-Assisted Development](#ai-assisted-development)
- [Google Skills Challenge Lab Reference](#google-skills-challenge-lab-reference)
- [Future Enhancements](#future-enhancements)
- [Resources](#resources)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## Introduction

**Gen Ai Mod App** is a modernized web application project developed as part of my hands-on learning with Google Cloud's Generative AI tools, including Gemini models, Vertex AI Imagen, Agent Search (Gemini Enterprise Agent Platform), and Cloud Run.

The project explores how to modernize a traditional legacy website into a dynamic, AI-powered platform by integrating automated content generation, image editing and creation, instant language translation, text copy refinement, and conversational search capabilities over unstructured data like blog posts.

The repository includes a backend API built using FastAPI, Jinja templates for frontend rendering, modular routers for different AI functionalities, and containerization setup for seamless deployment on Google Cloud Run.

The project demonstrates practical concepts in website modernization, prompt engineering, multi-model AI integration, and cloud-native application deployment.

This repository documents my implementation and learning with Google Cloud Generative AI, including the application structure, supporting modules, dependencies, and related learning resources.

---

## Architecture Diagram

The following diagram illustrates the architecture of the application deployed on Google Cloud:

```mermaid
flowchart TD
    U["User / Web Browser"] --> C["Cloud Run Service (FastAPI App)"]
    
    C --> V["Vertex AI / Gemini LLM API<br>(Text Refinement & Translation)"]
    C --> I["Vertex AI Imagen API<br>(Image Generation & Tuning)"]
    C --> S["Agent Search / Discovery Engine<br>(Gemini Enterprise Agent Platform)"]
    C --> B["Cloud Storage<br>(Blog Posts & Image Assets)"]

    classDef user fill:#e8f0fe,stroke:#4285f4,color:#202124
    classDef app fill:#e6f4ea,stroke:#34a853,color:#202124
    classDef gcp fill:#fef7e0,stroke:#f9ab00,color:#202124

    class U user
    class C app
    class V,I,S,B gcp
```

> [!NOTE]
> This diagram provides a high-level overview of the application components and their interactions across Google Cloud managed services.

### Architecture Overview

1. **Cloud Run Service (FastAPI App)**
   - Hosts the containerized Python FastAPI web application.
   - Manages HTTP routing, view dispatching, and API integrations.
  
2. **Vertex AI / Gemini LLM API**
   - Powers the text editing, translation, and copy refinement features.
   - Utilizes advanced Gemini models for contextual content transformation.
  
3. **Vertex AI Imagen API**
   - Handles image generation and tuning requests.
   - Allows users to generate and substitute visuals directly from the website UI.
  
4. **Agent Search (Gemini Enterprise Agent Platform)**
   - Provides semantic search and RAG capabilities over unstructured blog data imported from Cloud Storage.
  
5. **Cloud Storage**
   - Stores raw HTML/JSON blog post documents, static assets, and generated images.
  
---

## Project Structure

The repository organizes the source code into separate modules, templates, and backend routers.

```text
gen-ai-mod-app/
├── genai-website-mod-app/
│   ├── models/
│   │   └── data models used by the website application
│   ├── routers/
│   │   ├── hello.py
│   │   ├── vertex_imagen.py
│   │   ├── vertex_llm.py
│   │   ├── vertex_search.py
│   │   └── page_content_dispatch.py
│   ├── static/
│   │   ├── css, images, and JS assets
│   ├── templates/
│   │   └── Jinja templates for website pages
│   ├── utils/
│   │   ├── content_utils.py
│   │   ├── imagen.py
│   │   └── vertex_llm_utils.py
│   ├── views/
│   │   └── view implementations
│   │ 
│   ├── config.toml
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
│
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

> [!NOTE]
> This tree represents the main source files identified in the project. Refer to the repository for the complete file structure.

### Key Components

- **`main.py`** — Main FastAPI entrypoint to the website application.
- **`config.toml`** — Configuration file for application variables, project IDs, and model settings.
- **`Dockerfile`** — Configuration to build the website application container for Cloud Run.
- **`routers/`** — FastAPI API routers handling search, image generation, text translation, and refinement functionality.
- **`utils/`** — Utility modules implementing SDK calls for Gemini, Imagen, and content management.
- **`static/`** & **`templates/`** — Frontend assets and Jinja HTML templates powering the Cymbal Investments website UI.
- **`.gitignore`** — Excludes configured local, generated, and sensitive files from version control.
- **`CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `SECURITY.md`** — Describe contribution, community conduct, and security-reporting guidelines.

---

## Features

- **FastAPI Backend:** Built with a high-performance Python web framework for robust API and web page handling.
- **Cloud Run Deployment:** Fully containerized and deployed on Google Cloud's serverless container platform.
- **Agent Search Integration:** Embedded semantic search powered by the Gemini Enterprise Agent Platform to query unstructured blog documents.
- **AI-Powered Image Generation:** Integrated Vertex AI Imagen model allowing users to tune and generate new visual assets on the fly.
- **Inline Text Translation:** Instant webpage text translation into multiple languages using generative language models.
- **Copy Refinement:** Tone and style adjustments (e.g., formal and impactful) to improve website text content instantly.
- **Cloud Storage Persistence:** Stores and retrieves content and generated images dynamically using Google Cloud Storage buckets.
- **Logging & Observability:** Uses Google Cloud Logging and Logs Explorer to audit prompt executions and API requests.

> [!NOTE]
> The actual capabilities and execution behavior depend on valid GCP credentials, API enablement, and configuration settings.

---

## Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Primary programming language |
| **FastAPI** | Web framework for building APIs and handling application routes |
| **Google Cloud Run** | Scalable serverless container hosting platform |
| **Gemini Models & Vertex AI** | Text translation, content refinement, and generation |
| **Vertex AI Imagen** | AI-based image generation and tuning |
| **Agent Search / Discovery Engine** | Conversational search over unstructured data |
| **Google Cloud Storage** | Storing website content, blog posts, and generated images |
| **Docker** | Containerization of the web application |
| **Jinja / HTML / CSS / JS** | Frontend templates and static web assets |
| **Git & GitHub** | Version control and source code hosting |

> [!NOTE]
> The table describes the technologies and concepts reflected in the project implementation.

---

## Application Workflow

**Gen Ai Mod App** is structured around modern web routes and AI utility handlers.

### 1️⃣ Environment & Config Setup

- Configure project IDs, region settings, and data store identifiers in `config.toml`.
- Enable required GCP services including the Agent Platform API and Vertex AI.

### 2️⃣ Containerization & Deployment

- Build the container image using the provided `Dockerfile`.
- Deploy the service to Google Cloud Run with environment variables set for Vertex AI usage.

### 3️⃣ Conversational Search Integration

- Ingest blog post HTML data from Cloud Storage into a data store.
- Query unstructured knowledge using the Agent Search API to return AI summaries alongside source references.

### 4️⃣ Content Generation & Editing

- Access edit mode on website blog pages to modify text or visual assets.
- Trigger Imagen prompts to replace stock images with newly generated graphics.

### 5️⃣ Translation & Copy Refinement

- Select text paragraphs to translate into languages like French.
- Apply style prompts such as "formal impactful" to refine copywriting and replace text inline.

--- 

## Screenshots

This section showcases the **Gen Ai Mod App** user interface, search functionality, content editing, and Google Cloud configurations.

### GCP Console Dashboard

<img width="1366" height="768" alt="GCP Console Dashboard" src="https://github.com/user-attachments/assets/43a98ef1-5418-4c1b-9f32-49b249807d62" />

### Cloud Shell Terminal

<img width="1366" height="768" alt="Cloud Shell Terminal - 1" src="https://github.com/user-attachments/assets/03cd32df-ce7b-4d1e-b3f8-ab77e7c9cc48" />
<img width="1366" height="768" alt="Cloud Shell Terminal - 2" src="https://github.com/user-attachments/assets/8a7f60de-6ad6-44ba-a67f-8bb2823a23f5" />
<img width="1366" height="767" alt="Cloud Shell Config Editor (Nano)" src="https://github.com/user-attachments/assets/33c1b126-6f9c-442b-9712-1777979e5ffc" />
<img width="1366" height="768" alt="Cloud Shell Terminal - 3" src="https://github.com/user-attachments/assets/1d6ae958-bfc9-4783-9948-f51e2c888582" />

### Google Cloud AI Applications Dashboard

<img width="1366" height="768" alt="AI Applications Dashboard - Apps List" src="https://github.com/user-attachments/assets/a0132d46-4a8d-4339-809c-d5b447fa377c" />
<img width="1366" height="768" alt="Agent Search App Overview and Pipeline Configuration" src="https://github.com/user-attachments/assets/54a7dd87-3c10-4ec4-9e58-9d9c50286399" />
<img width="1366" height="768" alt="Agent Search Data Store Ingestion and Documents - 1" src="https://github.com/user-attachments/assets/e432bc41-a7ac-43b9-86a1-706cb7e59fef" />
<img width="1366" height="768" alt="Agent Search Data Store Ingestion and Documents - 2" src="https://github.com/user-attachments/assets/6f507cc7-50a2-45e3-ad97-32906c7f6823" />
<img width="1366" height="768" alt="Agent Search Data Store Ingestion and Documents - 3" src="https://github.com/user-attachments/assets/484038dd-d93d-4d39-aace-35b2e7a3e7f5" />

### Agent Search Preview & Query Testing

<img width="1366" height="768" alt="Agent Search Preview and Query Testing - 1" src="https://github.com/user-attachments/assets/973e933b-feed-477a-9ebd-5ec419be98b3" />
<img width="1366" height="768" alt="Agent Search Preview and Query Testing - 2" src="https://github.com/user-attachments/assets/aaad7cb4-f43a-43ed-91f4-44e3daccfcc9" />
<img width="1366" height="768" alt="Agent Search Preview and Query Testing - 3" src="https://github.com/user-attachments/assets/7268167f-0965-4f46-a02a-f12bfb41f32d" />
<img width="1366" height="768" alt="Agent Search Preview and Query Testing - 4" src="https://github.com/user-attachments/assets/a72fce56-a646-49b0-8d63-760ba97492cd" />

### Modernized Website UI & Pages

<img width="1366" height="768" alt="Website Home Page - Cymbal Investments" src="https://github.com/user-attachments/assets/810fefb5-220f-4359-808d-ae94d7948f72" />
<img width="1366" height="768" alt="Website Section - Our Approach to Investing" src="https://github.com/user-attachments/assets/ac062ade-75f0-4279-ad6c-e918903d9093" />
<img width="1366" height="768" alt="Website Section - Our Services" src="https://github.com/user-attachments/assets/a2cc0384-349b-431e-a2cd-4c9be46b1334" />
<img width="1366" height="768" alt="Website Section - Our Products" src="https://github.com/user-attachments/assets/747d2937-4f56-455a-b624-883f854af8c9" />
<img width="1366" height="768" alt="Website Section - Why Choose Us" src="https://github.com/user-attachments/assets/6ceddbd6-363a-4189-8a06-d66aeeb0c1d6" />
<img width="1366" height="768" alt="Website Section - Partner With Us" src="https://github.com/user-attachments/assets/908e32b7-f310-48bb-a5b2-07f7bcfd61e1" />
<img width="1366" height="768" alt="Website Footer and Weekly Newsletter" src="https://github.com/user-attachments/assets/4a95f14a-55b5-4671-b3e2-3500825bf673" />
<img width="1366" height="768" alt="Website FAQ Page" src="https://github.com/user-attachments/assets/157ae479-efd0-4563-bf44-a754698f963a" />
<img width="1366" height="768" alt="All Blogs Gallery Page" src="https://github.com/user-attachments/assets/f0e8ac56-57ff-4d74-a8d3-e6f5073d580b" />

### Blog Editor and AI Content Generation

<img width="1366" height="768" alt="Blog Editor and AI Content Generation Toolbar - 1" src="https://github.com/user-attachments/assets/48731993-21b2-4df4-af5e-587eabbe5540" />
<img width="1366" height="768" alt="Blog Editor and AI Content Generation Toolbar - 2" src="https://github.com/user-attachments/assets/c5b530a6-0b2a-41c6-a418-8a88a2552068" />
<img width="1366" height="768" alt="Blog Editor and AI Content Generation Toolbar - 3" src="https://github.com/user-attachments/assets/ea1bccc4-4a2f-4a65-bd88-d5ab7bef1d11" />
<img width="1366" height="767" alt="Blog Editor and AI Content Generation Toolbar - 4" src="https://github.com/user-attachments/assets/ba483faf-bb33-4854-ab9d-0a7aab5a00b1" />
<img width="1366" height="768" alt="Blog Editor and AI Content Generation Toolbar - 5" src="https://github.com/user-attachments/assets/539febdf-f49b-4959-9c99-8653a675c7f8" />
<img width="2607" height="1536" alt="An image of a man gone fishing" src="https://github.com/user-attachments/assets/54429ab9-d162-49d1-8821-8165ffba15fb" />

### Project Source Code

<img width="1366" height="768" alt="Project Configuration - config.toml" src="https://github.com/user-attachments/assets/7364f7b4-29ec-477f-af11-a9dae0c849a9" />
<img width="1366" height="768" alt="FastAPI Main Entrypoint - main.py" src="https://github.com/user-attachments/assets/180d3b43-4448-460c-a62c-927a61fcafd4" />
<img width="1366" height="768" alt="Backend Logic & UI Routes - main.py" src="https://github.com/user-attachments/assets/79a94a31-6b68-40b2-8f7e-8ca0825ee58b" />

### Google Cloud Monitoring & Logging

<img width="1366" height="768" alt="Cloud Monitoring Overview and Logs Dashboard" src="https://github.com/user-attachments/assets/7dedb4c3-6e18-450a-9c7a-a6f91818d380" />
<img width="1366" height="768" alt="Cloud Monitoring - CPU and Memory Utilization Metrics" src="https://github.com/user-attachments/assets/074f7166-3751-4372-9260-2da6f3c54ed6" />
<img width="1366" height="768" alt="Cloud Monitoring - Fleet and Zone Metrics" src="https://github.com/user-attachments/assets/91d184c1-23f6-4ee1-bd2d-660a7bd6c64a" />
<img width="1366" height="768" alt="Google Cloud Logs Explorer" src="https://github.com/user-attachments/assets/b0b09e48-0b7e-46b2-a876-00ef52e9a229" />

### Cloud Run Observability & Deployment Management

<img width="1366" height="768" alt="Google Cloud Run Services Overview" src="https://github.com/user-attachments/assets/c1a2b505-bf61-4713-a0a4-5f1530074af2" />
<img width="1366" height="768" alt="Cloud Run Observability - Request Metrics and Latencies" src="https://github.com/user-attachments/assets/d573da0e-de54-487a-91d8-ee489a55decd" />
<img width="1366" height="768" alt="Cloud Run Observability - Container Instance and Resource Utilization" src="https://github.com/user-attachments/assets/199da542-a368-4cf0-a6db-685929979e03" />
<img width="1366" height="768" alt="Cloud Run Observability - Network and Concurrency Metrics" src="https://github.com/user-attachments/assets/dba3852b-a42b-4cb8-b8a1-543cef4f8060" />
<img width="1366" height="768" alt="Cloud Run Observability - Startup Latency and Health Checks" src="https://github.com/user-attachments/assets/d1544455-4e94-4726-8c7b-ddf0b7218a0b" />
<img width="1366" height="768" alt="Cloud Run Service Logs" src="https://github.com/user-attachments/assets/70bca81c-197a-4dbd-abc4-48a476fbc9e4" />

---

## Generative AI Capabilities & Integration

### Agent Search App

- Created via AI Applications / Discovery Engine.
- Indexes unstructured HTML documents from Cloud Storage to power semantic RAG search.

### Image Generation (Vertex AI Imagen)

- Invokes generative image models through the Vertex AI SDK.
- Translates descriptive user prompts into high-resolution visuals embedded directly into website pages.

### Text Translation & Refinement

- Uses Gemini models with structured prompt templates (`ai_translate_inline` and `ai_refine_text`).
- Returns clean, unquoted string outputs to ensure seamless inline website updates.

---

## AI-Assisted Development

AI tools can support the development and exploration of modernized web applications by helping explain unfamiliar code, investigate implementation issues, understand cloud architectures, and improve technical documentation.

During the development and learning process for Gen Ai Mod App, AI assistance may be used to support activities such as:

- Understanding FastAPI routing principles and Jinja template integration.
- Exploring Vertex AI SDK implementations for Gemini and Imagen.
- Configuring Discovery Engine data stores and Agent Search integrations.
- Investigating containerization best practices with Docker and Cloud Run.
- Reviewing cloud logging structures and prompt execution logs.
- Improving project documentation, code readability, and repository presentation.

AI-generated suggestions and code should be reviewed critically, verified against the actual implementation, and tested before being adopted.

---

## Google Skills Challenge Lab Reference

This project was developed after completing the following Google Cloud learning resources.

### Challenge Lab

**Modernize your Website with Generative AI on Google Cloud**

[Open the Google Skills lab](https://www.skills.google/paths/1282/course_templates/1097/labs/686300)

### Learning Context

The repository serves as a personal source-code project associated with this learning experience.

It provides a place to explore and document:

- Website modernization techniques using Generative AI.
- FastAPI backend development and routing.
- Google Cloud Run serverless deployment.
- Gemini Enterprise Agent Platform and Agent Search.
- Vertex AI Imagen image generation.
- Inline content translation and text copy refinement.

For official learning objectives, instructions, and environment setup requirements, refer to the Google Skills lab page linked above.

---

## Future Enhancements

The following ideas could be considered for future versions of **Gen Ai Mod App**:

- **Advanced Multi-Modal Editing:** Expand image tuning capabilities to support image-to-image style transfers.
- **User Authentication:** Add secure login workflows for content editors and administrators.
- **Automated Workflow Approvals:** Implement robust draft submission and review pipelines.
- **Multi-Language Expansion:** Support dynamic full-page translation for a wider array of global languages.
- **Enhanced Analytics:** Integrate Vertex AI Search analytics to track popular user queries.
- **Automated Testing:** Add comprehensive unit and integration tests for FastAPI routes and AI helper utilities.

> [!IMPORTANT]
> These are potential improvements, not claims that the features are already fully implemented.

---

## Resources

[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Documentation-4285F4?logo=googlecloud)](https://cloud.google.com/docs)
[![Cloud Run](https://img.shields.io/badge/Cloud%20Run-Documentation-4285F4?logo=googlecloudrun)](https://cloud.google.com/run/docs)
[![Vertex AI](https://img.shields.io/badge/Vertex%20AI-Documentation-4285F4?logo=google)](https://cloud.google.com/vertex-ai/docs)
[![Gemini](https://img.shields.io/badge/Gemini-Documentation-8E75B2?logo=google)](https://ai.google.dev/gemini-api/docs)
[![FastAPI](https://img.shields.io/badge/FastAPI-Documentation-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Documentation-2496ED?logo=docker&logoColor=white)](https://docs.docker.com/)
[![Python](https://img.shields.io/badge/Python-Documentation-3776AB?logo=python)](https://docs.python.org/3/)
[![Git](https://img.shields.io/badge/Git-Documentation-F05032?logo=git&logoColor=white)](https://git-scm.com/doc)
[![GitHub](https://img.shields.io/badge/GitHub-Documentation-181717?logo=github)](https://docs.github.com/)

---

## Disclaimer

**Gen Ai Mod App** is a learning and demonstration project associated with Google Cloud training.

The project utilizes third-party technologies and services, including Google Cloud Run, Vertex AI, Gemini, and Imagen. The availability, functionality, pricing, and policies of external cloud services are subject to their respective providers' terms.

Access to Google Skills lab environments and temporary GCP projects expires after completion. A completed lab does not imply permanent public availability of the deployed web application.

This repository is intended for educational and demonstration purposes. Do not commit API keys, access tokens, service-account credentials, or private configuration files to source control.

---

## Contributing

Contributions are welcome! If you would like to improve **Gen Ai Mod App**, fix a bug, add tests, or improve the documentation, please review the following guidelines:

- [Contributing Guide](./CONTRIBUTING.md)
- [Code of Conduct](./CODE_OF_CONDUCT.md)
- [Security Policy](./SECURITY.md)

Please ensure that contributions are focused, documented, and tested where appropriate. Never include secrets or private configuration in issues, commits, or Pull Requests.

---

## License

This project is licensed under the **Apache License 2.0**.

See the [LICENSE](./LICENSE) file for details.

---

## Author

[**Sahil Sharma**](https://github.com/sahil-me)

Thank you for exploring **Gen Ai Mod App**! If you find the project useful, consider giving the repository a ⭐ to show your support.
