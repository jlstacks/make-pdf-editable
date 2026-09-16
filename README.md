# Make PDF Editable

A reusable, security-hardened Codex skill for converting PDFs into the editable format a task actually requires while preserving the original document and applying explicit safety controls.

The project demonstrates structured AI-agent workflow design for document transformation, including task interpretation, tool selection, source preservation, security boundaries, and output verification.

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
