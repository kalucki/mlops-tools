import json

def dedupe_tools(input_file='tools.json', output_file='tools_deduped.json'):
    """
    Reads a JSON file containing a list of tool objects, removes duplicates based on the 'name' field,
    and writes the deduplicated list to a new JSON file.
    """
    with open(input_file, 'r') as f:
        tools = json.load(f)

    seen = set()
    unique_tools = []
    for tool in tools:
        name = tool.get('name')
        if name and name not in seen:
            seen.add(name)
            unique_tools.append(tool)

    with open(output_file, 'w') as f:
        json.dump(unique_tools, f, indent=2)

    removed = len(tools) - len(unique_tools)
    print(f"Removed {removed} duplicate entries. {len(unique_tools)} unique tools remain and were written to '{output_file}'.")

if __name__ == '__main__':
    dedupe_tools()