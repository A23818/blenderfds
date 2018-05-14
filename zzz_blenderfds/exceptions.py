"""BlenderFDS, exceptions."""


class BFException(Exception):
    """Exception raised by all methods in case of an error."""

    def __init__(self, sender, msg, errors=None):
        self.sender = sender
        self.msg = msg
        self.errors = list()
        if errors:
            self.errors.extend(errors)

    def __str__(self):
        return "\n".join(self.labels)

    def draw(self, context, layout) -> "layout":
        """Draw self msgs user interface."""
        layout.label(icon="ERROR", text=self.msg)

    @property
    def my_label(self) -> "str":
        """Get my label."""
        return self.sender and ": ".join((str(self.sender), self.msg)) \
            or self.msg

    @property
    def labels(self) -> "List":
        """Get my label and all errors labels."""
        labels = list()
        labels.append(self.my_label)
        for err in self.errors:
            labels.extend(err.labels)
        return labels

    @property
    def free_texts(self) -> "list":
        """Return labels in free_text format."""
        return ["# ERROR: {}".format(label) for label in self.labels]
