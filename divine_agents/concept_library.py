class ConceptLibrary:
    """Base class for truth libraries."""

    def get_truth(self) -> str:
        raise NotImplementedError


class AbsoluteTruthLibrary(ConceptLibrary):
    """Library for absolute truths."""

    def get_truth(self) -> str:
        return "Resnica je absolutna in neodvisna od drugih."


class RelativeTruthLibrary(ConceptLibrary):
    """Library for relative truths."""

    def get_truth(self) -> str:
        return "Resnica je relativna, oblikovana z našimi odnosi."


class UnityOfGreedLibrary(ConceptLibrary):
    """Library for unified truths (unity of greed)."""

    def get_truth(self) -> str:
        return "Vse resnice so eno, medsebojno povezane."
