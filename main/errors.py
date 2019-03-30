from attr import dataclass


@dataclass(frozen=True, cmp=True)
class BaseError(Exception):
    message: str


class InvalidInput(BaseError):
    """
    Raised when the input file cannot be parsed.
    """


class DeserializeError(BaseError):
    """
    Raised when the parse result cannot be deserialized to file structure models.
    """


class InternalError(BaseError):
    """
    Raised when something happens anomaly in the process of reformatting.
    """


class EquivalentError(InternalError):
    """
    Raised when the reformatted document is not equivalent to the original one.
    """


class StableError(InternalError):
    """
    Raised when we obtain a different document after reformatting the second time.
    """


@dataclass(frozen=True, cmp=True)
class BaseWarning(Warning):
    message: str


class MissingExamplesWarning(BaseWarning):
    """
    Raised when examples are missing in ScenarioOutline
    """


class EmptyExamplesWarning(BaseWarning):
    """
    Raised when an examples table is empty
    """


class NothingChanged(BaseWarning):
    """Raised when reformatted code is the same as source."""
