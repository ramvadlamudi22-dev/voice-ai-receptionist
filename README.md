# Voice AI Receptionist

Prototype scaffold for a Voice AI receptionist and customer intake workflow.

## Status

MVP planning, documentation, sample intake data, prompt notes, and a local demo script are included.

## Why this exists

Small businesses often repeat the same front-desk tasks: collecting customer details, answering simple questions, routing requests, and preparing summaries. This repository explores a simple AI-assisted workflow for those tasks.

## Core Flow

```text
Customer Request -> Intake -> FAQ / Routing -> Review -> Owner Summary
```

## What it can support

- customer intake
- FAQ handling
- appointment request collection
- callback request collection
- support triage notes
- owner summary reports

## Human Review Policy

This project is designed as an assistant workflow. Important actions should be reviewed or confirmed by a human operator.

## Repository Structure

```text
.
├── README.md
├── TODO.md
├── docs/
│   ├── call-flow.md
│   ├── architecture.md
│   └── roadmap.md
├── prompts/
│   └── receptionist_prompt.md
├── sample/
│   ├── intake_form.json
│   └── faq_examples.json
├── reports/
│   └── sample_summary.md
└── src/
    └── main.py
```

## Roadmap

- [x] Add project overview
- [x] Add call flow notes
- [x] Add sample intake schema
- [x] Add FAQ examples
- [x] Add receptionist prompt
- [x] Add sample owner summary
- [ ] Add voice provider integration notes
- [ ] Add scheduling integration notes
- [ ] Add screenshots
- [ ] Add demo walkthrough

## Skills Demonstrated

AI Agents, AI Automation, Chatbots, Workflow Automation, Customer Support, Python

## Links

Portfolio: https://ramvadlamudi22-dev.github.io  
GitHub: https://github.com/ramvadlamudi22-dev
