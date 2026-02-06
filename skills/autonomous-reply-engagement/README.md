# Skill: Autonomous Reply & Engagement

## Purpose
Enable the agent to autonomously reply to incoming content and engage with users or other agents, maintaining persona consistency and safety.

## Input Contract
```
{
  "skill": "autonomous-reply-engagement",
  "incoming_content": {"object"},
  "context_window": ["array", "object"],
  "max_length_chars": "number"
}
```

## Output Contract
```
{
  "reply_text": "string",
  "confidence_score": "number",
  "needs_hitl": "boolean",
  "disclosure_flag": "boolean"
}
```

## Dependencies
MCP Tools: platform.reply, semantic filter, persona memory
Judge validation step (mandatory)
