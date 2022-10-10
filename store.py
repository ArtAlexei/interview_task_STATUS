class TreeStore:
    def __init__(self, items):
        self.storage = {}
        for item in items:
            id = item.pop("id")
            item["children"] = []
            self.storage[id] = item

            perent = item["parent"]
            if perent != "root":
                self.storage[perent]["children"].append(id)

    def getItem(self, id):
        item = self.storage[id].copy()
        item["id"] = id
        del item["children"]
        return item

    def getAll(self):
        items = []
        for item in self.storage:
            items.append(self.getItem(item))
        return items

    def getChildren(self, id):
        items = []
        for item in self.storage[id]["children"]:
            items.append(self.getItem(item))
        return items

    def getAllParents(self, id):
        items = []
        item = self.getItem(id)
        while item["parent"] != "root":
            id = item["parent"]
            item = self.getItem(id)
            items.append(item)
        return items
