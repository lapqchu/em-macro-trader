# Ebook / Source Material Ingestion Protocol

When the user uploads a new book, paper, or research document for integration into the EM macro knowledge base, follow this protocol exactly.

## Step 1: Convert and Read

- Use the `markitdown` skill or `Read` tool to extract full text from the uploaded file.
- For large PDFs (>10 pages), process in chunks using the `pages` parameter.
- For ebooks (.epub, .mobi), convert to readable format first.

## Step 2: Create a Structured Digest

Create a new file in `references/` named after the source (e.g., `references/em-fx-handbook-digest.md`).

The digest must contain these sections:

### Metadata
```
Title: [full title]
Author(s): [names]
Publication date: [if known]
Scope: [what markets/topics does this cover]
Ingested: [date of ingestion]
```

### Core Thesis
What is the central argument or framework of this source? State it in 2-3 sentences that a trader could act on.

### Analytical Framework
How does the author reason about problems? What do they look at first? What is their hierarchy of importance? This is the most valuable section — it transfers the author's method, not just their conclusions.

Document:
- Decision hierarchy (what factors does the author prioritize?)
- Causal model (what drives what, in the author's view?)
- Key distinctions the author insists on (e.g., flow vs. stock, nominal vs. real)
- What the author considers noise vs. signal

### Key Concepts and Definitions
Extract precise definitions for any terms the author defines carefully. Many EM macro disagreements are definitional. Capture the author's definitions exactly, especially where they differ from common usage.

### Tradeable Frameworks
Translate the author's insights into frameworks a macro trader can use:
- If the author describes a model, what are the inputs and what trades does it suggest?
- If the author describes a historical pattern, what are the conditions for it to repeat?
- If the author describes a policy dynamic, what are the observable signals that confirm or deny it?

### Contrarian or Non-Consensus Views
Flag any claims that contradict conventional market wisdom or other ingested sources. These are especially valuable — they either represent alpha or errors, and the user needs to know about them.

### Limitations and Blind Spots
No source is perfect. Note:
- What markets or time periods does this source NOT cover?
- Where is the author's expertise weakest?
- What has changed since publication that might invalidate some conclusions?
- What biases (institutional, regional, methodological) are visible?

### Cross-References
How does this source connect to other materials already in the knowledge base? Where does it agree, disagree, or extend existing frameworks?

## Step 3: Extract Reusable Artifacts

If the source contains any of the following, extract them as standalone sections or files:
- Checklists (e.g., "10 signs of an EM crisis")
- Decision trees (e.g., "how to assess central bank credibility")
- Quantitative models or formulas
- Historical case studies with clear lessons
- Data sources or indicators the author recommends monitoring

## Step 4: Integration Test

After creating the digest, test integration by asking yourself:
- If the user asked about [topic covered by this source], would I reference this material and apply its framework?
- Can I distinguish between what this source says and what other sources say?
- Have I captured the method or just the conclusions?

If the answer to any of these is "no," the digest is incomplete. Revise.

## Step 5: Update the Knowledge Base Index

After ingestion, update `references/em-macro-foundations.md` to note the new source and what it contributes to the overall knowledge base.
