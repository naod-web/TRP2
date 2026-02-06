# Skill: Persona-Consistent Content Generation

## Purpose
Generate text, image, or short video that perfectly matches the agent's SOUL.md persona.

## Input Contract
```
{
  "skill": "persona-consistent-content-generation",
  "prompt_seed": "string",                        // goal or hook
  "content_type": "string",                       // "caption", "thread", "image", "video"
  "character_reference_id": "string",             // for image/video consistency
  "generation_tier": "string"                     // "daily" | "hero"
}
```

## Output Contract
```
{
  "reply_text": "string",
  "confidence_score": "number",
  "needs_hitl": "boolean",
  "disclosure_flag": "boolean"                    // whether to set AI label
}
```

## Dependencies
MCP Tools: twitter.reply_tweet, instagram.reply, etc.
Memory retrieval (Weaviate + Redis)
Judge validation step (mandatory)
