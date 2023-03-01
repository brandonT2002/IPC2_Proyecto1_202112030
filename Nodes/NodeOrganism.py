from Nodes.Organism import Organism

class NodeOrganism:
    def __init__(self,organism):
        self.organism : Organism = organism
        self.next = None
        self.prev = None