# API Explorer Integration Plan

This document outlines how the automation pipeline integrates with the existing API Explorer architecture in API Dash.

---

## Current Architecture (from PR #837)

The current flow in API Explorer is:

JSON Templates (mock)
→ TemplatesService.loadTemplates()
→ templateListProvider (Riverpod)
→ Explorer UI (TemplateGrid, TemplateCard, DescriptionPage)

These templates are currently static and stored locally.

---

## Proposed Integration

The automation pipeline replaces mock JSON with dynamically generated templates.

### Updated Flow

OpenAPI / HTML / Markdown sources  
→ Python Pipeline (parsing + normalization + tagging)  
→ Generated ApiTemplate JSON  
→ Stored in GitHub (static JSON or dataset repo)  
→ TemplatesService.fetchTemplatesFromGitHub()  
→ templateListProvider  
→ Explorer UI  

---

## Role of Each Component

### 1. Pipeline (Python)
- Parses API specifications
- Extracts endpoints and metadata
- Performs category tagging
- Outputs standardized ApiTemplate JSON

---

### 2. GitHub (Data Layer)
- Stores generated templates
- Acts as a simple distribution layer (via raw URLs)
- Updated periodically via GitHub Actions

---

### 3. TemplatesService
- Fetches JSON templates from GitHub
- Parses into ApiTemplate objects
- Provides data to Riverpod providers

---

### 4. Riverpod Providers
- Manage state of template list
- Trigger UI updates when new data is fetched

---

### 5. Explorer UI
- Displays templates in grid form
- Allows user to explore API endpoints
- Enables one-click import into workspace

---

## Key Design Considerations

### Schema Alignment
Pipeline output must match `explorer_model.dart` exactly to ensure compatibility.

---

### Data Source Strategy
Two possible approaches:

1. Static JSON committed to API Dash repo
2. Separate data repository fetched via GitHub API

---

### Update Strategy
- Weekly GitHub Actions run
- Trigger on new API additions

---

### Error Handling
- Skip invalid specs
- Fallback to partial templates if parsing fails

---

## Future Extensions

- Advanced tagging using NLP models
- API popularity ranking
- Community-contributed templates
- Health monitoring of APIs

---

## Summary

The pipeline acts as the data generation layer, while API Dash consumes this data through TemplatesService, enabling a scalable and automated API discovery experience.