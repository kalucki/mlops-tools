import os
import json
import re
import sys

def main():
    try:
        cwd = os.getcwd()
        print(f"📂 Current working dir: {cwd}")
        print("📋 Files here:", os.listdir(cwd))
        if 'tools.json' not in os.listdir(cwd):
            print("❌ ERROR: 'tools.json' not found in this directory.")
            sys.exit(1)

        print("🔍 Loading tools.json…")
        with open('tools.json', 'r') as f:
            data = json.load(f)
        print(f"✅ Loaded {len(data)} tools.")

        # Clean up fields with list-of-strings entries
        for tool in data:
            # Clean supported_platforms
            if 'supported_platforms' in tool and isinstance(tool['supported_platforms'], list):
                cleaned = []
                for entry in tool['supported_platforms']:
                    cleaned.append(re.sub(r'\s*\(.*?\)', '', entry))
                tool['supported_platforms'] = list(dict.fromkeys(cleaned))

            # Clean integrations
            if 'integrations' in tool and isinstance(tool['integrations'], list):
                cleaned = []
                for entry in tool['integrations']:
                    cleaned.append(re.sub(r'\s*\(.*?\)', '', entry))
                tool['integrations'] = list(dict.fromkeys(cleaned))

        out_name = 'tools_clean.json'
        print(f"💾 Writing cleaned data to {out_name}…")
        with open(out_name, 'w') as f:
            json.dump(data, f, indent=2)
        print("🎉 Done! Check", out_name)

    except Exception as e:
        print("⚠️ An error occurred:", str(e))
        sys.exit(1)

if __name__ == '__main__':
    main()