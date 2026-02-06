# Skill: Social Listening & Trend Spotting

## Purpose
Enable the agent to detect relevant trends, mentions, and conversations to stay contextually relevant.

## Input Contract
```
{
  "skill": "social-listening-trend-spotting",
  "niche_keywords": ["array", "string"],          // e.g. ["Ethiopian fashion", "sneakers"]
  "platforms": ["array", "string"],               // ["twitter", "instagram"]
  "time_window_hours": "number",                  // default: 24
  "min_relevance_threshold": "number"             // default: 0.75
}
```

## Output Contract
```
{
  "trends_detected": [
    {
      "topic": "string",
      "relevance_score": "number",
      "source_platform": "string",
      "sample_posts": ["array", "object"],        // lightweight snippets
      "volume_trend": "string"                    // "rising", "stable", "peak"
    }
  ],
  "new_mentions_count": "number",
  "action_recommendation": "string"               // "create_content", "reply", "monitor"
}
```

## Dependencies
MCP servers: mcp-server-twitter, mcp-server-instagram (or equivalents)
Internal: Semantic Filter (Gemini Flash / Haiku)
