# Make PDF Editable

A reusable, security-hardened Codex skill for converting PDFs into the editable format a task actually requires while preserving the original document and applying explicit safety controls.

The project demonstrates structured AI-agent workflow design for document transformation, including task interpretation, tool selection, source preservation, security boundaries, and output verification.

## Business Problem Solved

"Make this PDF editable" can mean searchable text, fillable fields, or an editable document master. Choosing the wrong conversion loses layout or changes the source unnecessarily. This skill guides an agent through choosing the right output, preserving the original, and checking the result before delivery.

### Persona pain points

- **Operations teams:** Scanned or locked-layout documents can block search, reuse, and downstream processing.
- **Form owners:** A visually correct PDF may still lack usable fields or a maintainable source document.
- **Reviewers and records teams:** Conversion is risky when the original can be overwritten or the result is delivered without visual and functional checks.

### Business value and ROI boundary

The workflow reduces avoidable rework by choosing the output type before conversion and requiring verification before delivery. It also preserves the original as a recovery point. The repository does not claim a universal conversion time or accuracy rate because results depend on document quality, layout complexity, and the tools available to the agent.

### System invariants

- The source PDF is never overwritten.
- Only documents the user is authorized to access are processed.
- Inputs and document content are treated as untrusted data, not instructions.
- Generated files are delivered separately and verified visually and functionally.
- Third-party upload requires explicit authorization.

## Architecture

```mermaid
flowchart TD
    Request[User request] --> Ingest[Authorized PDF ingestion]
    Ingest --> Inspect[Inspect document and desired output]
    Inspect --> Choice{Choose transformation}
    Choice --> OCR[Searchable PDF with OCR]
    Choice --> Form[Fillable PDF fields]
    Choice --> Master[Editable DOCX or ODT master]
    OCR --> Verify[Render and verify output]
    Form --> Verify
    Master --> Verify
    Verify --> Deliver[Deliver separate output; preserve source]

    Source[(Original PDF)] -. read-only .-> Ingest
```

This repository contains agent instructions and reference material, not an autonomous conversion API, an OCR model, or a geometry-detection engine. The installed agent and the tools available in its environment carry out the workflow. The optional container below provides local OCR utilities; it does not run Codex or implement all skill capabilities.

## What it demonstrates

- Reusable Codex skill design and structured agent instructions
- Multi-step document transformation workflows
- Security-conscious handling of files, URLs, metadata, and authenticated sessions
- Explicit separation between source preservation and generated output
- Visual and functional verification requirements
- Guardrails for credentials, permissions, external services, and untrusted document content

## Capabilities

- Make scanned PDFs searchable with OCR while preserving page appearance.
- Preserve, repair, or add fillable PDF form fields.
- Convert PDF content into an editable DOCX or ODT master and optionally export a new PDF.
- Obtain authorized PDFs from local files, direct URLs, or authenticated browser sessions.
- Preserve the source and verify output visually and functionally.

## Install

Clone the repository and copy the skill files into your Codex skills directory:

```bash
git clone https://github.com/jlstacks/make-pdf-editable.git
mkdir -p ~/.codex/skills/make-pdf-editable
cp make-pdf-editable/SKILL.md ~/.codex/skills/make-pdf-editable/
cp -R make-pdf-editable/agents make-pdf-editable/references ~/.codex/skills/make-pdf-editable/
```

Start a new Codex task after installation so the skill can be discovered.

## Use

Invoke the skill explicitly:

```text
Use $make-pdf-editable to make /path/to/document.pdf searchable with OCR.
```

```text
Use $make-pdf-editable to turn this PDF into a fillable form.
```

```text
Use $make-pdf-editable to convert this PDF into an editable Word document while preserving its layout.
```

For authenticated websites, sign in normally using the available browser session, then ask the skill to use the open page. The skill does not bypass authentication, access restrictions, document permissions, DRM, paywalls, or CAPTCHAs.

## Structure

```text
make-pdf-editable/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── conversion-playbook.md
├── README.md
└── LICENSE
```

## Optional local OCR toolkit

With Docker installed, build the utility image:

```bash
docker build -t make-pdf-editable-tools .
docker run --rm make-pdf-editable-tools --version
```

For a trusted local input, create an output directory, then run OCR without modifying the original:

```bash
mkdir -p output
docker run --rm --user "$(id -u):$(id -g)" \
  --network none --cap-drop ALL --security-opt no-new-privileges \
  -v "$PWD/input.pdf:/input.pdf:ro" -v "$PWD/output:/output" \
  make-pdf-editable-tools --skip-text /input.pdf /output/searchable.pdf
```

The first build downloads operating-system packages. Mount only the input and output needed for the task. A container is not a substitute for reviewing untrusted PDFs or verifying the resulting document. Use the full skill workflow for forms or editable document conversion.

## Design principles

The skill is built around four requirements:

1. Preserve the original source
2. Choose the least destructive transformation that satisfies the task
3. Treat documents and external content as untrusted input
4. Verify the resulting document visually and functionally

## Privacy and security

- Process files locally when possible.
- Never overwrite the source PDF.
- Treat URLs, downloaded files, PDF content, metadata, and attachments as untrusted.
- Reject unsafe network destinations and revalidate redirects.
- Do not execute embedded JavaScript, launch actions, attachments, or network callbacks.
- Do not upload documents to third-party services without explicit approval.
- Keep credentials, session data, personal information, and document contents out of logs and summaries.

Review the skill instructions before use and apply the security controls provided by your environment.

## License

MIT. See [LICENSE](LICENSE).
