# Voice AI Receptionist

A prototype repository for a Voice AI receptionist and customer intake workflow.

## Status

MVP planning and documentation scaffold.

## Goal

Create a simple AI-assisted front-desk workflow for small businesses.

## What it can support

- customer intake
- FAQ handling
- appointment request collection
- callback request collection
- support triage notes
- daily owner summary

## Workflow

```text
Customer Message -> Intake -> FAQ / Routing -> Appointment Request -> Owner Summary
```

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── call-flow.md
│   └── implementation-plan.md
├── prompts/
│   └── receptionist_prompt.md
├── sample/
│   └── intake_form.json
├── src/
│   └── main.py
├── .env.example
└── requirements.txt
```

## Human Review Policy

This project is designed as an assistant workflow. Important actions should be reviewed or confirmed by a human operator.

## Roadmap

- [x] Add project overview
- [x] Add call flow notes
- [x] Add sample intake schema
- [x] Add receptionist prompt
- [ ] Add voice provider integration notes
- [ ] Add scheduling integration
- [ ] Add reporting template
- [ ] Build a small demo

## Links

Portfolio: https://ramvadlamudi22-dev.github.io  
GitHub: https://github.com/ramvadlamudi22-dev
