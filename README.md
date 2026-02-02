AI Coding Agent Rules - Documentation
1. What I Did

Reviewed and improved the AI coding agent rules file.
Incorporated best practices from Boris Cherny’s workflow (Claude Code) and the AI coding community.
Added the following key updates to the rules:
Role definition: Clearly defined the agent as a senior developer who asks questions if requirements are unclear.
Planning requirement: The agent must create and get approval for a multi-step plan before coding.
Boundaries and safety: Defined “Ask First” tasks and “Never” tasks to prevent unsafe or undesired actions.
Code style enforcement: Rules for linting, formatting, and consistent project conventions.
Verification & testing: Require test generation or updates and verification before completing tasks.
Documentation & memory: Persistent rule file for learning from past mistakes.
Optional automation: Slash commands and subagents for repeated tasks.
Implemented a Python mock agent to simulate the rules' behavior and tested it in VS Code.

2. What Worked

Defining a clear role and boundaries improved the AI agent’s adherence to rules.
Requiring planning before coding ensured the agent produced structured, step-by-step outputs.
Verification steps (simulated test generation) helped ensure changes were safe and predictable.
Persistent memory/documentation rules helped capture recurring mistakes and avoid them in future tasks.
Mock testing in Python successfully demonstrated that the rules were enforceable and consistent.

3. What Didn’t Work

Some complex tasks still required human clarification despite the rules.
Initially, the agent could attempt tasks restricted under “Ask First” before plan approval — needed adjustment in mock Python logic.
Implementing subagents or slash commands fully would require IDE-specific integration, which wasn’t tested in Python.
Context management for large projects caused occasional irrelevant suggestions, which needed careful simulation.

4. Insights Gained

Rules directly influence the agent’s behavior: clear, specific, and actionable instructions result in more predictable and accurate outputs.
Planning and verification requirements significantly improve alignment with intent and thought process.
Persistent project memory allows the agent to learn from mistakes and follow established patterns.
Explicit boundaries and safety rules reduce the risk of undesirable actions and maintain project integrity.
Testing rules in a mock Python environment is a safe way to validate agent behavior before using it in real coding environments like VS Code, Copilot, or Claude Code.
Structured rules help the AI adopt a logical, stepwise problem-solving approach, aligning outputs with human expectations.
