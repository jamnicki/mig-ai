import re
from typing import List

# This pattern must not contain capturing parentheses; Use non-capturing parentheses, e.g. (?:…), instead
GLOSA_TOKENIZER_PATTERN = re.compile(
    # TODO: inspect glosa annotations and improve this pattern
    r"""
        \S+  # non-whitespace characters
    """,
    flags=re.VERBOSE,
)


class GlosaTokenizer:
    def __init__(self, pattern: re.Pattern = GLOSA_TOKENIZER_PATTERN):
        self.pattern = pattern

    def tokenize(self, text: str) -> List[str]:
        return self.pattern.findall(text)
