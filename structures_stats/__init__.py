from visitor import Visitor

class DictKeyCounter(Visitor):
    def __init__(self, key_to_count):
        self._what_to_count = key_to_count
        self._count = 0

    def visit_dict(self, node):
        for k,v in node.items():
            if k == self._what_to_count:
                self._count += 1
            self.visit(v)

    def visit_list(self, node):
        for e in node:
            self.visit(e)

    def visit_tuple(self, node):
        for e in node:
            self.visit(e)

    def visit(self, node):
        try:
            super().visit(node)
        except NotImplementedError:
            pass

    def count(self, obj):
        self._count = 0
        self.visit(obj)
        return self._count


class DictValueCollector(Visitor):
    def __init__(self, key_to_collect):
        self._what_to_collect = key_to_collect
        self._collection = []

    def visit_dict(self, node):
        for k,v in node.items():
            if k == self._what_to_collect:
                self._collection.append(v)
            self.visit(v)

    def visit_list(self, node):
        for e in node:
            self.visit(e)

    def visit_tuple(self, node):
        for e in node:
            self.visit(e)

    def visit(self, node):
        try:
            super().visit(node)
        except NotImplementedError:
            pass

    def collect(self, obj):
        self._collection = []
        self.visit(obj)
        return self._collection

