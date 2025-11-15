# Agent Insta - Python Full Project

This package contains the full Python-only project for **Agent Insta**:
- automation/       : Instagram Graph API wrapper (dry-run) and scheduler
- mas/              : Multi-Agent System simulation (asyncio)
- orchestrator/     : FastAPI orchestration API to control agents (dry-run)
- sdk/              : Python SDK (InstaAgent)
- scripts/          : helper scripts to run components

IMPORTANT: The automation Graph API client defaults to dry-run for safety.
To enable real posting, set environment variables `IG_ACCESS_TOKEN` and `IG_ACCOUNT_ID`
and instantiate clients with `dry_run=False`.
