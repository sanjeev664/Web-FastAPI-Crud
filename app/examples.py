"""Examples for endpoints."""
examples = {
    "one": {
        "summary": "one sentence",
        "description": "given a sentence return a score",
        "value": {
            "sentence": "I love you",
        },
    },
    "many": {
        "summary": "many sentences",
        "description": "given a batch of setences return scores",
        "value": {
            "sentence": ["You sound stupid", "Be nice to me"]
        },
    },
}