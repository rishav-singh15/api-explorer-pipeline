# API Explorer Pipeline PoC

This repository demonstrates a Proof of Concept (PoC) for generating API templates for the API Explorer feature in API Dash.

---

## Overview

The goal of this project is to automate the generation of API templates from real-world API specifications (OpenAPI), replacing the current mock JSON-based approach used in the Explorer.

---

## Pipeline Flow

OpenAPI Spec  
→ Endpoint Extraction  
→ Metadata Normalization  
→ Rule-based Categorization  
→ ApiTemplate JSON Output  

---

## Repository Structure

- `prototype1.ipynb`  
  Initial exploratory work used to validate parsing, endpoint extraction, and category inference.

- `openapi_to_template.py`  
  Clean and modular implementation of the pipeline for generating templates.

- `sample_output.json`  
  Example generated output in ApiTemplate-like format.

---

## Features Implemented

- Parses OpenAPI specifications
- Extracts endpoints (path + method)
- Performs basic rule-based category inference
- Converts data into a structured template format compatible with API Dash
- Generates ready-to-use JSON output

---

## Example Output

See `sample_output.json`

---

## Why This Matters

Currently, API Explorer relies on manually created mock JSON templates.

This PoC demonstrates:
- How templates can be generated automatically
- How real APIs can be integrated into the Explorer
- A scalable path toward a fully automated pipeline

---

## Next Steps

- Align schema fully with `explorer_model.dart`
- Add support for HTML and Markdown parsing
- Improve tagging and categorization logic
- Implement validation against template schema
- Integrate with `TemplatesService.fetchTemplatesFromGitHub()`
- Add GitHub Actions for periodic updates

---

## Status

PoC complete for OpenAPI → ApiTemplate pipeline.  
Working toward deeper integration with API Dash architecture.

---

## Notes on Categorization

During development, an important issue was identified in naive keyword-based tagging:

- Substring matches (e.g., `"ai"` inside `"api"`) caused incorrect classification
- Metadata fields (like API title) introduced noise

### Improvements Made

- Switched to **word-level tokenization** to avoid substring false positives
- Introduced **weighted scoring**:
  - Endpoint paths → high weight (most reliable signal)
  - Tags → medium weight
  - API name → low weight (often noisy)
- Ensured category taxonomy completeness (e.g., added "Country & Geography")

### Result

More accurate domain-based classification driven by endpoint semantics rather than superficial keyword matches.