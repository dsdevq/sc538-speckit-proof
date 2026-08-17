def truncate_words(text: str, max_words: int) -> str:
    """Return the first max_words words of text, appending … if truncated.

    Whitespace is normalised: any run of whitespace is collapsed to a single
    space. max_words <= 0 returns "".
    """
    if max_words <= 0:
        return ""
    words = text.split()
    if len(words) <= max_words:
        return " ".join(words)
    return " ".join(words[:max_words]) + "…"
