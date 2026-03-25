# API Explorer Pipeline PoC

This repository demonstrates a Proof of Concept (PoC) for generating API templates for API Explorer in API Dash.

## What this does

Converts an OpenAPI specification into an ApiTemplate-like JSON structure.

## Pipeline Flow

OpenAPI → Endpoint Extraction → Normalization → ApiTemplate JSON

## Features

- Extracts endpoints from OpenAPI specs
- Converts into API Dash compatible structure
- Basic rule-based tagging
- Handles simple failure cases

## Example Output

See `sample_output.json`

## Why this matters

Currently, API Explorer uses mock JSON templates. This PoC demonstrates how those templates can be automatically generated from real APIs.

## Next Steps

- Align schema fully with `explorer_model.dart`
- Add HTML/Markdown parsing
- Improve tagging logic
- Integrate with TemplatesService
- Add GitHub Actions for periodic updates