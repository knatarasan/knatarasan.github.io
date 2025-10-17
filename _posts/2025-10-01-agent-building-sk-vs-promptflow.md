---
layout: post
title: "Agent Building: Semantic Kernel vs Promptflow"
tags: [wip]
permalink: /2025/10/01/agent-building-sk-promptflow.html
---

{% if page.tags contains "wip" %}

<div style="background:#ffeeba; border-left:4px solid #f0ad4e; padding:1em; margin-bottom:2em;">
  🚧 This post is a Work In Progress — feel free to share feedback.
</div>
{% endif %}

### Semantic Kernel vs Prompt Flow

- As Semantic Kernel and PromptFlow are important libraries to build agents 
- As we (myself and my buddy ) are building [A personal finance app with Agents In-Built]({% link _posts/2025-10-02-how-to-design-an-app-with-agents.md %})
- I' pondering to understand where to use Semantic Kernel and where to use PromptFlow



| Scenario                                                                         | Semantic Kernel | Prompt Flow                        | Notes                                                                                                      |
| -------------------------------------------------------------------------------- | --------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| request                                                                          | Yes             | No                                 | notes                                                                                                      |
| Evaluation, testing, metrics, deploying generative App                           | No              | Yes                                | Use prompt Flow to evaluate & benchmark your SK planners plugins                                           |
| You want a visual flow/ DAG, modular nodes, team visibility                      | No              | Yes                                | PromptFlow to structure and visualize your Sk-based logic                                                  |
| heavy integration needed with existing code,libraries, APIs , business logic     | Yes             | No                                 | Use SK for heavy lifting but wrap or invoke parts via PromptFlow when you want orchestration at flow level |
| Simpler and linear prompt pipeline (eg: prompt-> model -> output -> postprocess) | No              | Yes                                | You may use SK funcitons/skills but flow is main driver                                                    |
| You anticipate the logic evolving, branching , growing more complex              | Yes             | No - Constrained for dynamic logic | Mix them : flows + planner nodes                                                                           |


