class MyString:
    def __init__(self, value=""):
        self.value = value  # Uses the setter to validate input

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")  # Print instead of raising an error

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re
        sentences = re.split(r"[.!?]+", self.value.strip())
        return len([s for s in sentences if s.strip()])

# Test case simulation
string = MyString()
string.value = 123  # Should print: "The value must be a string."
