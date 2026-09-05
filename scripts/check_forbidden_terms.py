import sys

forbidden_terms = [
    'суверенітет', 'sovereignty',
    'автономія', 'autonomy',
    'федерація', 'federation',
    'конфедерація', 'confederation',
    'конституція', 'constitution',
    'громадян', 'citizen',
    'права людини', 'human rights',
    'право власності', 'property rights',
    'кримінальн', 'criminal',
    'цивільн', 'civil',
    'штраф', 'fine',
    'держав', 'state',
    'монарх', 'monarch',
    'сегрегація', 'segregation',
    'корупція', 'corruption',
    'демократія', 'democracy',
    'бюджет', 'budget'
]

def check_text(text):
    text_lower = text.lower()
    found = []
    for term in forbidden_terms:
        if term in text_lower:
            found.append(term)
    return found

print("Linter loaded successfully.")
