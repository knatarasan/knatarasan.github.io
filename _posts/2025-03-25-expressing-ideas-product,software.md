## Expressing ideas, product design, software design and software document ? : Documentation for Software Product - my perspectives
_most of us hate to create sometimes to read, but is it really worth the effort_

---

&nbsp; &nbsp; Recently , when I am about to take over a new module , I was talking to the     subject matter expert. In response to a query about a business logic, he has asked me to check the current code. which surprised me why he doesn't have idea about the business logic. It is complex module, where I found that there isn't a common place where the knowledge is maintained , which could be referred by SME[^1], PM[^2] Product Manager and the SWE[^3] can refer. which triggered me to think around documentation for a Software Product. Well not many like to write or create document, not many like to read it, not many able to create right document , then is it worth thinking, creating and reading a document ?


&nbsp; &nbsp; A right document bridges how a SME[^3] thinks through a business problem, how a PM[^2] imagine a Software Product which can be used by customer for money and how a SWE[^3] builds software for the problem. A live document can make scaling the team easier by on boarding new team members faster. A well understood problem makes other functional teams like testing (Unit,GUI, Integration), Sales and Marketing work transparent.

&nbsp; &nbsp; A right document opens with good overview and expands into layers which can be followable by the audience, it helps the follower gets the context and able to delve into the detail without loosing the context. It uses right form factor, possibly easier to prepare and maintain. Ideally synchronized with software changes ( if code changes document must be updated) and easy maintain version. A right document is relied by a SWE[^3] without fear of it is out of sync. Audience  finds it is comprehensible ( it is not too technical for an SME[^1] or not too business domain for a SWE[^3]). It is not to abstract without details or opposite ( too much details not able to follow or get context). The document doesn't repeat same thing more than once, exception same concept could be expressed in more than one form factor.

&nbsp; &nbsp; Most common form factor of a document is combination of text and Diagram. Using multi media especially video could provide  different dimensions in expressing content. A diagram varies in different formats, 1. mermaid  markdown (diagram as code) stays close to code, so favorite of engineers. easy to build collaborate and maintained in git. 2. Lucid - favorite of Architects easy to make , collaborate, but there is possibility not in synch with code. 3. Figma - too good for UI design and brainstorming 4. Paper & pencil - easy to express ideas, since it is free form, enables to mind to express ideas easily, suggested during ideation and product discovery. 5. Infographic , little harder to make and powerful in expressing ideas with clarity.   Documentation in text form could be expressed in 1. Essay - need lingustic skills to create but good for communicating details and persuading. 2. Article - good for analysis of pros and cons in detail. 3. white paper - comprehensive in nature. 4. cheat sheet - very easy for reference.  Another variety of text document is code embedded documentation some of them to mention here, `docstring` by _python_ leveraged by `pydoc` , `document comments` by _Java_ leveraged by `javadoc` and for API side `swagger`. Videos can provide expressions in action, especially in product walk through. 


&nbsp; &nbsp; The direction of documentation could be , PM2E ( PM to SWE), S2E ( SME to SWE) and E2E ( SWE to SWE)
  

_Improvements to work on_
* Bring form factor in detail
* Give a chronological order on Form factor
  * Product Discovery
  * MVP
  * Prod version for first 10 customers
  * Established prodct

## Notes
SME[^1]: Subject Matter Expert
PM[^2]: Product Manager 
SWE[^3]: Software Engineer