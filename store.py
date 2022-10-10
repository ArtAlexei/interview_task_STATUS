from collections import defaultdict


class TreeStore:
    def __init__(self, items):
        self.items = {}
        self.children = defaultdict(list)

        for item in items:
            id = item.pop("id")
            self.items[id] = item
            perent = item["parent"]
            if perent != "root":
                self.children[perent].append(id)
        pass

    def getItem(self, id):
        item = self.items[id].copy()
        item["id"] = id
        return item

    def getAll(self):
        return [self.getItem(item) for item in self.items]

    def getChildren(self, id):
        return [self.getItem(item) for item in self.children[id]]

    def getAllParents(self, id):
        items = []
        item = self.getItem(id)
        while item["parent"] != "root":
            id = item["parent"]
            item = self.getItem(id)
            items.append(item)
        return items
