from store import TreeStore

items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None},
]
ts = TreeStore(items)


assert ts.getItem(7) == {"id": 7, "parent": 4, "type": None}
assert ts.getAll() == [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None},
]
assert ts.getChildren(4) == [
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None},
]

assert ts.getAllParents(7) == [
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 1, "parent": "root"},
]
