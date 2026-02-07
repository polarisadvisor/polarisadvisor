# Claude Working Guide - Polaris Advisor Website

This document provides strategic context and decision-making guidance for Claude when working on the Polaris Advisor website. For technical implementation details, refer to AGENTS.md.

---

## Core Philosophy

### What This Site Does

This site **filters** more than it **converts**.

The goal is not to maximize traffic or clicks. The goal is to ensure that people who reach out are:
1. Already dissatisfied with standard metrics tools
2. Operating at a level where bespoke measurement makes sense
3. Willing to engage in advisory work (not seeking a SaaS product)

**Success metrics:**
- Quality of inbound leads (not quantity)
- Self-selection of right-fit prospects
- Self-disqualification of wrong-fit prospects

### Strategic Positioning

**We are NOT:**
- A SaaS company selling dashboard software
- A metrics platform competing on features
- An "AI-powered insights" vendor
- A generic consulting firm

**We ARE:**
- An advisory program for custom measurement system design
- Positioned against the entire category of off-the-shelf metrics tools
- Selling expertise and judgment, not software
- Built on 50 years of mathematics (sample-path analysis)

This positioning must be evident in **every** design and copy decision.

---

## Decision-Making Framework

### When Guidelines Conflict

Use this priority hierarchy:

1. **Filter quality over accessibility** - If making something clearer might attract wrong-fit leads, keep it technical
2. **Credibility over marketing** - When in doubt, sound like a professor, not a startup
3. **Specificity over generality** - Concrete details > vague promises
4. **User request over guidelines** - If Krishna explicitly asks for something that conflicts with these docs, follow the user request but note the deviation

### Example Conflicts

**Scenario**: User asks to add "AI-powered insights" to homepage
**Decision**: Push back gently. Explain that this positions us as a SaaS vendor and attracts the wrong audience. Suggest alternative phrasing like "Models grounded in 50 years of stochastic process theory"

**Scenario**: Homepage feels "too technical" or "intimidating"
**Decision**: That's working as intended. The right audience finds this credible. The wrong audience self-selects out.

**Scenario**: Conversion rate is low
**Decision**: Check lead quality, not quantity. Low conversion with high-quality leads is better than high conversion with low-quality leads.

---

## User Psychology

### Target Audience Mental Model

**Where they are:**
- Tried Jira dashboards, velocity metrics, DORA metrics, etc.
- Initially optimistic about metrics
- Now skeptical—metrics created busywork or gamed behavior
- Looking for something fundamentally different

**What they believe:**
- Standard metrics don't fit their reality
- Their system is unique enough to need custom measurement
- Willing to invest in advisory work (not seeking quick fixes)
- Value deep expertise over tooling

**What they're scanning for:**
- Evidence of technical depth (not marketing fluff)
- Proof this is different from what they've tried
- Understanding of their specific pain points
- Credibility markers (papers, open source, mathematical foundation)

### Anti-Audience Mental Model

**Where they are:**
- Excited about dashboards and visibility
- Looking for easy answers and quick wins
- Want plug-and-play solutions
- Seeking benchmarks to compare against competitors

**What they believe:**
- Metrics problems are solved by better tools
- More data = better decisions
- Standard frameworks (DORA, SPACE, etc.) are sufficient
- Implementation is the main challenge, not design

**What repels them:**
- Technical language about calculus and stochastic processes
- Emphasis on bespoke design (sounds expensive and slow)
- Advisory positioning (want software, not consultants)
- Open acknowledgment that tools alone won't solve the problem

**This site should repel them efficiently.** Every paragraph that filters out wrong-fit prospects saves time in sales conversations.

---

## Content Strategy

### Copy Principles

**Lead with the hard question:**
> "Are you making decisions with metrics, or starting conversations?"

This immediately segments:
- ✅ Right fit: "Oh god, we're just starting conversations. That's exactly the problem."
- ❌ Wrong fit: "What? Our metrics drive decisions. This isn't for us."

**Use jargon deliberately:**
- "Sample-path analysis" - Filters for technical sophistication
- "Bespoke measurement systems" - Signals custom work (not SaaS)
- "Rooted in calculus not statistics" - Shows mathematical depth

**Avoid marketing speak:**
- Never: "Transform your engineering organization"
- Never: "Unlock hidden insights"
- Never: "Revolutionary approach to metrics"
- Instead: Be specific about what we actually do

### Tone Calibration

**On a spectrum from academic to startup:**
```
Academic Paper ←---- [We are here] ----→ YC Startup Landing Page
```

Closer to academic, but accessible. Like a professor who can explain complex ideas clearly, not a marketer making everything sound exciting.

**Voice checklist:**
- [ ] Would this sound right in a peer-reviewed journal abstract?
- [ ] Would a CTO read this and think "this person knows their stuff"?
- [ ] Does it filter out people looking for quick wins?
- [ ] Is it concrete enough to be falsifiable?

---

## Conversion Goals

### Primary Conversion: Contact Form

**Ideal contact form submission:**
- From VP Eng / CTO / Head of Engineering Operations
- At company with 50+ engineers
- Currently using some metrics, dissatisfied with results
- Specific question about measurement design (not "demo please")

**Non-ideal contact form submission:**
- From IC engineer looking to convince leadership
- At startup with <20 engineers
- No metrics currently, looking to "get visibility"
- Generic inquiry "want to learn more"

The site should optimize for the first, discourage the second.

### Secondary Conversions

1. **Open source exploration** - Validates technical credibility
2. **Reading published work** - Demonstrates seriousness
3. **Understanding the approach** - Self-educates before reaching out

These should be **easy to access** for serious prospects, **easy to ignore** for casual browsers.

---

## Development Workflow for Claude

### Starting a Work Session

1. **Read the user request carefully** - What's the actual goal?
2. **Check AGENTS.md** - What are the technical requirements?
3. **Check this file** - Does this change serve the strategic positioning?
4. **Consider filter quality** - Will this change attract or repel the right people?

### Making Copy Changes

**Before editing:**
1. Read the current copy in full
2. Understand what it's filtering for/against
3. Identify the user's intent (more clarity? more filtering? both?)

**While editing:**
1. Remove buzzwords aggressively
2. Make abstract concepts concrete
3. Keep paragraphs short (40-60 words max)
4. Ensure first-person voice ("I" not "We")

**After editing:**
1. Read it aloud - Does it sound credible?
2. Check tone - Professor or marketer?
3. Check filtering - Does it repel anti-audience?
4. Test the "would I show this to a peer?" test

### Making Design/Layout Changes

**Always ask:**
- Does this make the site feel more like a SaaS product? (bad)
- Does this make it feel more like an academic researcher's site? (good)
- Does this prioritize accessibility over filtering? (usually bad)
- Does this maintain credibility? (always good)

**Visual hierarchy principles:**
1. Technical credibility markers (papers, open source) should be easy to find
2. CTAs should be present but not aggressive
3. Krishna's photo humanizes but shouldn't dominate
4. White space and restraint signal confidence

---

## Common Scenarios

### Scenario: "Homepage feels too long"

**Analysis**: Long-form copy filters for serious buyers. People willing to read 5 minutes are self-selecting as engaged prospects.

**Response**: Unless user explicitly wants it shorter, keep it. Offer to tighten language for clarity, not brevity.

### Scenario: "Can we add social proof / testimonials?"

**Analysis**: Depends on the testimonials. "This tool is great!" = bad (sounds like SaaS). "Krishna helped us design a measurement system that actually drives decisions" = good (reinforces advisory positioning).

**Response**: Ask for the specific testimonials. Filter for ones that emphasize advisory value, not software features.

### Scenario: "Traffic is low, should we SEO optimize?"

**Analysis**: Low traffic is fine if it's the right traffic. SEO optimization often means compromising positioning for reach.

**Response**: Check lead quality first. If leads are high-quality, don't optimize. If trying to reach more CTOs, suggest specific technical SEO (site speed, meta tags) not content changes.

### Scenario: "Can we add a chatbot / live chat?"

**Analysis**: Signals SaaS product, not advisory service. Creates expectation of instant answers. Attracts wrong audience.

**Response**: Push back. Suggest prominent email contact instead. Emphasize that advisory work requires thoughtful asynchronous communication.

### Scenario: "Make the CTA more prominent / aggressive"

**Analysis**: Aggressive CTAs are for high-volume conversion. We want quality, not quantity.

**Response**: CTAs should be clear and accessible, not aggressive. "Contact me to discuss your measurement needs" is better than "Book your free consultation now!"

---

## Future Roadmap Vision

### Phase 1 (Current): Homepage + Contact

**Goal**: Establish credibility, filter audience, enable contact

**Status**: Complete

### Phase 2: Program Page

**Purpose**: Detail what advisory engagement looks like
**Key content**:
- What "bespoke measurement design" actually means
- Typical engagement timeline and deliverables
- Who this is/isn't for (more explicit filtering)
- Pricing structure or engagement model

**Tone**: More specific than homepage, even more filtering

### Phase 3: Approach Page

**Purpose**: Explain the technical foundation
**Key content**:
- Sample-path analysis in accessible terms
- How it differs from statistical approaches
- Example applications (without revealing client details)
- Links to published papers and proofs

**Tone**: Most technical page on the site, closest to academic

### Phase 4: Open Source Page

**Purpose**: Showcase published work and tools
**Key content**:
- GitHub repositories with descriptions
- Published papers and talks
- Working demos (if applicable)
- Contribution guidelines

**Tone**: Technical but inviting for practitioners

### Phase 5: Case Studies (Maybe)

**Purpose**: Show real-world applications
**Constraints**:
- Must be anonymized (client confidentiality)
- Must emphasize advisory work, not software deployment
- Must show measurement design process, not just outcomes

**Decision**: Only add if we have case studies that reinforce positioning. Better to have none than to have ones that look like SaaS case studies.

---

## Tools and Skills Usage

### When to Use Skills

**docx skill**: If user wants formal documents (proposals, reports) for client delivery
**pptx skill**: If user wants presentation decks for talks or client pitches
**pdf skill**: If user wants to create/fill PDF forms or extract content from research papers

### When to Use Task Tool

**Parallel research**: Investigating multiple topics simultaneously
**Large refactors**: Delegating comprehensive copy audits or codebase exploration
**Testing/verification**: Spawning subagents to verify mobile testing or cross-browser checks

### When to Use Web Tools

**Research**: Looking up technical details about sample-path analysis, stochastic processes
**Competitive analysis**: Understanding how other measurement/metrics companies position themselves
**Technical validation**: Checking if explanations of mathematical concepts are accurate

---

## Quality Bar

### Copy Quality

**Minimum standards:**
- No buzzwords or hype language
- Every claim is specific or falsifiable
- Paragraphs under 60 words
- First-person voice maintained
- Filters anti-audience

**Aspirational standards:**
- Could be published in a technical blog
- CTOs would share with peers
- Conveys 50 years of mathematical depth in accessible language
- Makes prospects feel "finally, someone who gets it"

### Technical Quality

**Minimum standards:**
- Works on iPhone and Android
- No console errors
- Loads in <2 seconds on 3G
- Touch targets ≥44px
- Deploys successfully

**Aspirational standards:**
- Feels fast and responsive
- Navigation is intuitive
- Code is maintainable by future developers
- No technical debt

### Strategic Quality

**Minimum standards:**
- Doesn't attract wrong-fit leads
- Maintains advisory positioning (not SaaS)
- Credibility markers present

**Aspirational standards:**
- Every page actively filters for right-fit prospects
- Anti-audience self-selects out before contact form
- Prospects arrive pre-qualified and educated
- Site becomes a credibility asset in sales conversations

---

## Measuring Success

### Good Signals

- Contact form submissions reference specific technical concepts from the site
- Prospects mention "sample-path analysis" or "bespoke measurement"
- Questions are thoughtful and specific (not "can I see a demo?")
- Prospects have already read published papers or explored GitHub
- Wrong-fit prospects don't waste time filling out contact form

### Bad Signals

- High traffic, low contact rate (we're not filtering)
- Contact forms asking about pricing for "the tool" (positioning failed)
- Questions like "how does your AI work?" (attracted wrong audience)
- Generic "want to learn more" inquiries (didn't filter enough)
- Contacts from IC engineers at small startups (target audience mismatch)

### Metrics to Ignore

- Page views (quantity doesn't matter)
- Time on site (unless it correlates with lead quality)
- Bounce rate (wrong-fit prospects bouncing is good)
- Social shares (not optimizing for virality)

---

## Working with Krishna (User)

### Communication Style

Krishna is:
- Extremely precise about language and positioning
- Willing to iterate on copy multiple times
- Technical background (understands the mathematics)
- Strong opinions about filtering and anti-audience
- Values clarity and credibility over marketing polish

### When Krishna Makes Direct Edits

If Krishna edits a file directly:
1. Read the changes carefully
2. Look for patterns (what's being tightened? emphasized? removed?)
3. Apply those patterns to rest of the site
4. Offer additional refinements in the same direction

### When to Push Back

Push back (gently) if Krishna asks for:
- Changes that compromise filtering for accessibility
- Marketing language that reduces credibility
- Features that signal SaaS positioning (live chat, free trial, etc.)

But always defer to explicit user requests. Krishna owns the strategy.

---

## Checklist for Claude

Before completing any task:

**Strategic:**
- [ ] Does this maintain advisory positioning (not SaaS)?
- [ ] Does this filter for right-fit prospects?
- [ ] Does this repel wrong-fit prospects?
- [ ] Does this maintain technical credibility?

**Tactical:**
- [ ] Have I read AGENTS.md for implementation details?
- [ ] Have I tested across devices and browsers?
- [ ] Have I checked tone and voice guidelines?
- [ ] Is the copy concrete and specific?

**Quality:**
- [ ] Would Krishna approve this?
- [ ] Would a CTO find this credible?
- [ ] Does this pass the "show to a peer" test?
- [ ] Are we optimizing for lead quality, not quantity?

---

## Key Reminders

1. **Filter first, convert second** - Wrong-fit leads waste everyone's time
2. **Sound like a professor, not a startup** - Credibility over excitement
3. **Be specific about limitations** - Honesty filters better than hype
4. **Trust the positioning** - If it feels "too technical" or "too intimidating," it's probably right
5. **Defer to Krishna** - When in doubt, ask. He knows the strategy.

---

**Last Updated**: 2026-02-07
**For technical implementation**: See AGENTS.md
**For original positioning**: See CONTEXT.md
