## Documentation by / for Software Engineer 
_most of us hate to create sometimes to read, but is it really worth the effort_

---


### Intro
  - Only talks about SWE[^1] product documentation
  - not many like to document 
  - not many like to read document 
  - not many makes right document
  - then why should we worry

### Why should we worry about it, SWE's documentation
  - A right document does the following 
    - new SWE picks up fast, enhance fast ==> scale Engineering team faster
    - Better unit, integration and GUI test automation can be built to test all scenarios
    - new SWE understands the module without flaw
    - Brings SWE, SME and PM in line, thus SME can validate the logic and PM can follow it
  
### What is too much documentation
  - comments embedded into code (for only E2E) when code expresses itself without ambiguity 
  - Any form of repetition, i.e, same message expressed more than once . ( exceptions : expressing in more than one form) - Repetition reduces clarity , clutteredness makes the follower difficult to understand.

### What is right document
  - Starts with right overview and expand layers followable by audience (in other way) Followers get the context and able to follow the details, while following details they don't loose context.
  - Uses right form
  - Easy to prepare 
  - Easy to maintain
  - sync locked ( if code changes doc must be updated)
  - version preserved 

### What is too much documentation
  - comments embedded into code (for only E2E) when code expresses itself without ambiguity 
  - Any form of repetition, i.e, same message expressed more than once . ( exceptions : expressing in more than one form) - Repetition reduces clarity , clutteredness makes the follower difficult to understand.


### What is wrong/unused document
  - SWE thinks he can't rely , i.e, not in sync with code
  - SME finds it is not comprehensible ( too technical, too abstract too detailed )

### Audience
  - E2E ( SWE to SWE)
  - S2E (SME to SWE)
  - PM2E (PM to SWE)
  
### Form factor
  - Diagram
    - mermaid
    - Lucid
    - Paper & pencil
    - Infographic
  - Text
    - Essay
    - Article
    - White paper     
    - cheat sheet
  - Code embeded
    - thoughts 
      - pros and cons
      - what it serves  and what it doesn't
      - why mermaid is superior to this
      - e.g:
        - docstring (_python_) `pydoc`
        - document comments (_Java_ ) `javadoc` 
  - Multimedia
    - Video
    - Audio ( not common )
  - Mix
    - A mix of above all 

### Diagram vs Prose

| Diagram                                            | Prose                                                           |
| -------------------------------------------------- | --------------------------------------------------------------- |
| A picture                                          | 1000 lines                                                      |
| Easy observe and comprehend                        | Read get context and move forward                               |
| Great in providing overview :grinning: big picture | Great in detailing out , which couldn't be expressed by picture |
| Hard to create and edit                            | Easy to write and edit, but not many are good in language       |

### Reverse ( or reverse engineering)
White paper to Hadoop , Mapreduce , Cassandra

### Reach
Why a document unused, mis guides , stops progress

## Notes
[^1]: Software Engineer