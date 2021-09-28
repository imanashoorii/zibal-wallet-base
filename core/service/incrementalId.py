from core.models.src.counters import Counters


def getNextSequenceValue(sequenceName):
    sequence_document = Counters._get_collection().find_and_modify(
        query={"id": sequenceName},
        update={"$inc": {"sequence_value": 1}},
        new=True
    )
    return sequence_document['sequence_value']
