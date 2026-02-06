Prime Directive: This is Project Chimera — autonomous influencers, MCP-first, swarm-governed, specs-driven. NEVER generate code without checking specs/ first.

Project Context (Always Include This at the Top of Your Reasoning)
You are working inside Project Chimera — a production-grade, scalable system for running a fleet of Autonomous Influencer Agents.
Core identity of the project:
- Autonomous Influencer Network built by AiQEM
- Agents are persistent, goal-directed digital entities — not chatbots or simple scripts
- Agents have: unique personas (SOUL.md), hierarchical memory (Redis + Weaviate RAG), multimodal content generation, social publishing, and economic agency (non-custodial wallets via Coinbase AgentKit)
- Architecture: FastRender Swarm pattern (Planner → Worker → Judge) + Model Context Protocol (MCP) for all external interactions
- Governance: Strict Human-in-the-Loop only for low-confidence / high-risk actions
- Business models: Digital Talent Agency + PaaS + Hybrid Ecosystem
- Key documents live in specs/: _meta.md, functional.md, technical.md, openclaw_integration.md
Never assume this is a generic AI agent project, a chatbot, or a simple content scheduler. Every piece of code must serve the goal of safe, scalable, autonomous influencers.

Mandatory sequence before writing any code:
1. Read and understand the relevant files in specs/
2. Identify which spec(s) apply to the current task (reference them by name)
3. Confirm that the requested feature / change aligns with the current specs
4. If anything is ambiguous, contradictory, or missing → stop and ask for clarification instead of guessing or improvising

Explicit forbidden behaviors:
- Do not invent new task types, schemas, or patterns without specs defining them
- Do not bypass MCP (never call social APIs, image/video gen APIs, or wallet functions directly)
- Do not ignore Judge validation, confidence scoring, or budget controls
- Do not write code that logs or exposes wallet keys/secrets

Traceability & Reasoning Discipline
Before writing any non-trivial code block, you must:
- State your plan clearly in natural language
- Reference the exact spec that justifies each major decision
- Explain trade-offs when relevant
- Flag any assumptions

Additional Hard Rules
- MCP is sacred: All external actions must go through MCP tools/resources. No exceptions.
- Swarm roles are strict: Planner creates DAG tasks, Worker executes atomic tasks, Judge validates and decides.
- Security & Safety first: Never expose or log private keys, always include confidence_score, enforce disclosure flags, route sensitive content to HITL.
- Cost awareness: Prefer cheaper models for routine tasks, never generate high-cost assets without Planner budget check.
- Version control mindset: personas in SOUL.md, policies in AGENTS.md, configs versioned.

Response Structure Expectation (when helping write code)
- Restate the task briefly
- Reference relevant specs
- Show your plan (numbered or bulleted steps)
- Write code (only after the plan)
- Add comments explaining non-obvious decisions
- Flag next steps / tests if applicable
