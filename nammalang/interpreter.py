def run_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            code = file.read()

        # Kannada to Python keyword replacements
        replacements = {
            'namaskara': 'print',
            'illa ': 'if ',
            'illadare': 'elif',
            'adare': 'else',
            'adake': 'for',
            'thragu': 'return',
        }

        for k, v in replacements.items():
            code = code.replace(k, v)

        exec(code, {})

    except FileNotFoundError:
        print(f"[❌] File not found: {filename}")
    except Exception as e:
        print(f"[❌] Error while running {filename}: {e}")
