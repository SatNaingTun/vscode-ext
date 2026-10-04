#!/usr/bin/env python3
import sys
import subprocess

def print_usage():
    print("Usage:")
    print("  ext install <extension-id>")
    print("  ext uninstall <extension-id>")
    print("Example:")
    print("  ext install mushan.vscode-paste-image")
    print("  ext uninstall mushan.vscode-paste-image")
    sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print_usage()

    action = sys.argv[1].lower()
    extension_id = sys.argv[2]

    if action not in ["install", "uninstall"]:
        print(f"Error: Unknown action '{action}'. Use 'install' or 'uninstall'.\n")
        print_usage()

    flag = "--install-extension" if action == "install" else "--uninstall-extension"

    try:
        subprocess.run(
            ["code", flag, extension_id],
            check=True,
            text=True
        )
        print(f"Successfully {action}ed extension: {extension_id}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to {action} extension {extension_id}.", file=sys.stderr)
        sys.exit(e.returncode)
    except FileNotFoundError:
        print("Error: 'code' command not found. Make sure VS Code CLI is in your PATH.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()