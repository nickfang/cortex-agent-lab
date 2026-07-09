from pathlib import Path

VAULT_ROOT = Path("/Users/nfang/Cortex").resolve()

def _safe_path(rel: str) -> Path:
   """Resolve a vault-relative path and refuse anything that escapes the vault."""
   p = (VAULT_ROOT / rel).resolve()
   if not p.is_relative_to(VAULT_ROOT):
      raise ValueError(f"Path escapes the vault: {rel!r}")
   return p

def read_file(path:str) -> str:
   p = _safe_path(path)
   if not p.is_file():
      return f"Error: no file at {path!r}"
   return p.read_text(encoding="utf-8")

READ_FILE_TOOL = {
   "name": "read_file",
   "description": (
      "Read a UTF-8 text file from the Cortex vault. "
      "Path is relative to the vault root, e.g. 'codex/ai/Prompt Engineering.md'."
   ),
   "input_schema": {
      "type": "object",
      "properties": {
         "path": {"type": "string", "description": "Vault-relative file path"},
      },
      "required": ["path"],
   },
}
