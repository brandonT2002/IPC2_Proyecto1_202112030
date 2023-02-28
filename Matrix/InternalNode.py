class InternalNode:
    def __init__(self,row,column,value):
        self.value = value
        self.row = row
        self.column = column
        self.right : InternalNode = None
        self.left : InternalNode = None
        self.up : InternalNode = None
        self.down : InternalNode = None
    
    def toString(self,tab) -> str:
        cadena = ("\t" * tab) + f"-----NODO ({self.row}, {self.column})---\n"
        cadena += ("\t" * tab) + f"Valor: {self.value}\n"
        if self.right != None:
            cadena += self.right.toString(tab + 1)
        return cadena;