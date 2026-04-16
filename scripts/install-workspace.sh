#!/usr/bin/env sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO_ROOT=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
TARGET=""
DEST=""
FORCE=0

usage() {
  cat <<'EOF'
Usage:
  ./scripts/install-workspace.sh --target openclaw [--dest PATH] [--force]
  ./scripts/install-workspace.sh --target claude --dest PATH [--force]
  ./scripts/install-workspace.sh --target hermes [--dest PATH] [--force]
  ./scripts/install-workspace.sh --target all --dest PATH [--force]

Targets:
  openclaw  Install the workspace files into ~/.openclaw/workspace by default
  claude    Install an AGENTS.md launcher plus .sowork-workspace/ into a Claude Code project root (requires --dest)
  hermes    Install a Hermes skill pack into ~/.hermes/skills/openclaw-imports/openclaw-workspace-sowork by default
  all       Install claude + openclaw + hermes (requires --dest for the Claude target)

Options:
  --target TARGET   One of: openclaw, claude, hermes, all
  --dest PATH       Destination path (required for claude, optional otherwise)
  --force           Overwrite existing files instead of creating timestamped backups
  -h, --help        Show this help message
EOF
}

log() {
  printf '%s\n' "$*"
}

fail() {
  printf 'Error: %s\n' "$*" >&2
  exit 1
}

normalize_path() {
  python3 - "$1" <<'PY'
import os
import sys
print(os.path.realpath(os.path.expanduser(sys.argv[1])))
PY
}

ensure_safe_destination() {
  candidate=$(normalize_path "$1")
  source_root=$(normalize_path "$REPO_ROOT")

  case "$candidate" in
    "$source_root"|"$source_root"/*)
      fail "Destination $candidate overlaps the source repository $source_root. Choose a different --dest outside the cloned repo."
      ;;
  esac
}

backup_or_remove() {
  path=$1
  if [ ! -e "$path" ]; then
    return 0
  fi

  if [ "$FORCE" -eq 1 ]; then
    rm -rf "$path"
    return 0
  fi

  stamp=$(date +%Y%m%d-%H%M%S)
  mv "$path" "$path.bak.$stamp"
  log "Backed up existing $(basename "$path") -> $path.bak.$stamp"
}

copy_item() {
  src=$1
  dest_dir=$2
  [ -e "$src" ] || return 0
  base=$(basename "$src")
  mkdir -p "$dest_dir"
  backup_or_remove "$dest_dir/$base"
  cp -R "$src" "$dest_dir/$base"
}

copy_workspace_bundle() {
  bundle_dest=$1
  mkdir -p "$bundle_dest"

  for item in \
    AGENTS.md \
    HEARTBEAT.md \
    IDENTITY.md \
    MEMORY.md \
    README.md \
    SKILL.md \
    SOUL.md \
    TOOLS.md \
    USER.md \
    CONTRIBUTING.md \
    LICENSE \
    docs \
    examples \
    memory \
    outputs \
    scripts \
    skills
  do
    copy_item "$REPO_ROOT/$item" "$bundle_dest"
  done
}

write_claude_launcher() {
  launcher_root=$1
  launcher_path="$launcher_root/AGENTS.md"
  backup_or_remove "$launcher_path"
  cat > "$launcher_path" <<'EOF'
# AGENTS.md — Claude Code bootstrap for openclaw-workspace-sowork

At the start of each session, load and follow these workspace files:

- `./.sowork-workspace/AGENTS.md`
- `./.sowork-workspace/SOUL.md`
- `./.sowork-workspace/TOOLS.md`
- `./.sowork-workspace/USER.md`
- `./.sowork-workspace/IDENTITY.md`
- `./.sowork-workspace/HEARTBEAT.md`
- `./.sowork-workspace/MEMORY.md` for direct owner sessions only

Use the reusable skill prompts from `./.sowork-workspace/skills/` when the task matches.
Treat `./.sowork-workspace/` as agent context, not application source code, unless the user explicitly asks you to edit it.
EOF
}

install_openclaw() {
  openclaw_dest=${1:-"$HOME/.openclaw/workspace"}
  ensure_safe_destination "$openclaw_dest"
  log "Installing OpenClaw workspace -> $openclaw_dest"
  copy_workspace_bundle "$openclaw_dest"
  log "OpenClaw install complete."
}

install_claude() {
  project_root=$1
  [ -n "$project_root" ] || fail "Claude target requires --dest /path/to/project"
  ensure_safe_destination "$project_root"
  mkdir -p "$project_root"

  if [ -e "$project_root/AGENTS.md" ] && [ "$FORCE" -ne 1 ]; then
    fail "Refusing to overwrite $project_root/AGENTS.md. Move it, merge it manually, or rerun with --force."
  fi

  claude_workspace="$project_root/.sowork-workspace"
  log "Installing Claude Code workspace context -> $claude_workspace"
  copy_workspace_bundle "$claude_workspace"
  write_claude_launcher "$project_root"
  log "Claude install complete. Claude Code will pick up AGENTS.md and load ./.sowork-workspace/."
}

install_hermes() {
  hermes_dest=${1:-"$HOME/.hermes/skills/openclaw-imports/openclaw-workspace-sowork"}
  ensure_safe_destination "$hermes_dest"
  log "Installing Hermes skill pack -> $hermes_dest"
  mkdir -p "$hermes_dest"

  backup_or_remove "$hermes_dest/SKILL.md"
  mkdir -p "$hermes_dest/templates/workspace" "$hermes_dest/references" "$hermes_dest/assets"
  cp "$REPO_ROOT/SKILL.md" "$hermes_dest/SKILL.md"

  for item in AGENTS.md HEARTBEAT.md IDENTITY.md MEMORY.md SOUL.md TOOLS.md USER.md; do
    backup_or_remove "$hermes_dest/templates/workspace/$item"
    cp "$REPO_ROOT/$item" "$hermes_dest/templates/workspace/$item"
  done

  backup_or_remove "$hermes_dest/references/README.md"
  cp "$REPO_ROOT/README.md" "$hermes_dest/references/README.md"

  backup_or_remove "$hermes_dest/references/workspace-deep-dive.md"
  cp "$REPO_ROOT/docs/workspace-deep-dive.md" "$hermes_dest/references/workspace-deep-dive.md"

  backup_or_remove "$hermes_dest/assets/skills"
  cp -R "$REPO_ROOT/skills" "$hermes_dest/assets/skills"

  log "Hermes install complete. Load the skill: openclaw-workspace-sowork"
}

while [ $# -gt 0 ]; do
  case "$1" in
    --target)
      [ $# -ge 2 ] || fail "--target requires a value"
      TARGET=$2
      shift 2
      ;;
    --dest)
      [ $# -ge 2 ] || fail "--dest requires a value"
      DEST=$2
      shift 2
      ;;
    --force)
      FORCE=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      fail "Unknown argument: $1"
      ;;
  esac
done

[ -n "$TARGET" ] || {
  usage
  fail "--target is required"
}

command -v python3 >/dev/null 2>&1 || fail "python3 is required for path normalization"

case "$TARGET" in
  openclaw)
    install_openclaw "$DEST"
    ;;
  claude)
    install_claude "$DEST"
    ;;
  hermes)
    install_hermes "$DEST"
    ;;
  all)
    [ -n "$DEST" ] || fail "--target all requires --dest for the Claude project"
    install_openclaw
    install_claude "$DEST"
    install_hermes
    ;;
  *)
    fail "Unsupported target: $TARGET"
    ;;
esac
