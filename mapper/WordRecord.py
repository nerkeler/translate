class WordRecord:
    def __init__(self, word, definition, example, pronunciation, category, source, progress, occurrence, familiar, created_at, updated_at):
        self.word = word
        self.definition = definition
        self.example = example
        self.pronunciation = pronunciation
        self.category = category
        self.source = source
        self.progress = progress
        self.occurrence = occurrence
        self.familiar = familiar
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"Word: {self.word}\nDefinition: {self.definition}\nExample: {self.example}\nPronunciation: {self.pronunciation}\nCategory: {self.category}\nSource: {self.source}\nProgress: {self.progress}\nOccurrence: {self.occurrence}\nFamiliar: {self.familiar}\nCreated At: {self.created_at}\nUpdated At: {self.updated_at}"

