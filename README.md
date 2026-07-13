# Codex Skills

Reusable skills for Codex.

## Included skill

### acquire-editable-pdf

Obtain a PDF from an authorized website, browser session, direct URL, or local computer and create the appropriate editable derivative while preserving the source.

Supported outcomes:

- Searchable PDFs with an OCR text layer
- Fillable PDFs with interactive form fields
- Content-editable DOCX or ODT masters, with optional PDF export

The workflow includes source preservation, output verification, URL and redirect validation, sandboxed processing of untrusted PDFs, and safeguards against active PDF content.

## Install

Copy the skill directory into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/acquire-editable-pdf ~/.codex/skills/
```

Start a new Codex task after installation so the skill can be discovered.

## Use

Invoke the skill explicitly:

```text
Use $acquire-editable-pdf to make /path/to/document.pdf searchable with OCR.
```

```text
Use $acquire-editable-pdf to turn this PDF into a fillable form.
```

```text
Use $acquire-editable-pdf to convert this PDF into an editable Word document while preserving its layout.
```

For authenticated websites, sign in normally using the available browser session, then ask the skill to use the open page. The skill does not bypass authentication, access restrictions, document permissions, DRM, paywalls, or CAPTCHAs.

## Structure

```text
skills/acquire-editable-pdf/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    └── conversion-playbook.md
```

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
