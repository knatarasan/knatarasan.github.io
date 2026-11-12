---
layout: post
title: "Prompt caching"
tags: [tech]
---

{% if page.tags contains "wip" %}

<div style="background:#ffeeba; border-left:4px solid #f0ad4e; padding:1em; margin-bottom:2em;">
  🚧 This post is a Work In Progress — feel free to share feedback.
</div>
{% endif %}

![image info]({{ site.image_base }}/2026-11-08/prompt_caching_linkedin_cover.png)


---

## Prompt caching


Prompt Caching can save your cost but also quietly add some

Are you under-using it ?
  
Or over-using it  ?


An Agent calls LLM with `context` + `Query 1` and LLM produces two inferences , 
1) _processed `context`_
2) _Inference for  `Query 1`_
 
the context and processed context   are cached as key value pair  with TTL of 5 min or 60 min. During next call with Query 2 with the same context , it is cache hit so LLM will do inference only for Query 2,  user pays only `0.1x $`on most models; Opus 5.5 is even cheaper at 0.05x  , for the inference of context , without caching they might pay `1x $`.  This is more useful especially when you have 
1. Long System prompt
2. Tool definitions
3. Reference Document

LLM is called for the first time with context + Query 1 and cache enabled. After inference LLM cache stores the  inference out of context ( note not inference from Query 1) by keeping context as key. Now when the model  called with same context and Query 2 within 5 min , inference is made only for Query 2 and the model reuses its processed context and only processes Query 2. 

 
When LLM is frequently cached for 5 min  but not read at least once or cached for an hour but not read at least twice  is extra expense than without using prompt caching.

### For the builders

```python
response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    system=[
        {"type": "text", "text": "You are a support agent for Acme."},
        {
            "type": "text",
            "text": REFUND_HANDBOOK,  # long, stable reference doc
            "cache_control": {"type": "ephemeral"},  # cache everything up to here
        },
    ],
    messages=[{"role": "user", "content": query}],  # changes every call
)
```

If cache hit happens within 5 min the user pays only `0.1x $` on most models; Opus 5.5 is even cheaper at 0.05x , instead of `1x $` . However with context  they  pay  `1.25x $` for the  cache write. If the cache TTL is 1 hour they pay  `2x $`. Every cache read costs `0.1x $`. 
The user saves money if the agent makes at least 2 calls within 5 min or 3 calls within  60 min cache.

#### 5 min cache 
```python
cache_control={"type": "ephemeral"}
```

| Call to LLM                    | Cache Write | Cache Read | Running total with Prompt Cache | Running total without Prompt Cache |
| :----------------------------- | :---------: | ---------: | ------------------------------: | ---------------------------------: |
| first call  context + Query 1  |  `$1.25x`   |          0 |                        `$1.25x` |                              `$1x` |
| second call  context + Query 2 |      0      |    `$0.1x` |                        `$1.35x` |                              `$2x` |
| Third call  context + Query 3  |      0      |    `$0.1x` |                        `$1.45x` |                              `$3x` |
 
For 3 calls with prompt caching         `$1.45x`
For 3 calls with no prompt caching    `$3.00x`



#### 60 min cache 
```python
cache_control={"type": "ephemeral","ttl": "1h"}
```

| Call to LLM                    | Cache Write | Cache Read | Running total with Prompt Cache | Running total without Prompt Cache |
| :----------------------------- | :---------: | ---------: | ------------------------------: | ---------------------------------: |
| first call  context + Query 1  |   `$2.0x`   |          0 |                         `$2.0x` |                              `$1x` |
| second call  context + Query 2 |      0      |    `$0.1x` |                         `$2.1x` |                              `$2x` |
| Third call  context + Query 3  |      0      |    `$0.1x` |                         `$2.2x` |                              `$3x` |
| Fourth call  context + Query 4 |      0      |    `$0.1x` |                         `$2.3x` |                              `$4x` |
 
For 4 calls with prompt caching         `$2.3x`
For 4 calls with no prompt caching    `$4.0x`


Question
    Have you explored from your tracing the LLM calls with heavy context  called more than once within 5 min ?



[https://platform.claude.com/docs/en/build-with-claude/prompt-caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)