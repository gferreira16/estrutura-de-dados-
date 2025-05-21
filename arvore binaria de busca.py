class Nodo:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (
            self.esquerda and self.esquerda.chave,
            self.chave,
            self.direita and self.direita.chave
        )


class BinaryTree:
    def __init__(self):
        self.raiz = None

def insert(root, key):
    if root is None:
        return Nodo(key)
    if key < root.chave:
        root.esquerda = insert(root.esquerda, key)
    else:
        root.direita = insert(root.direita, key)
    return root


def search(root, key):
    if root is None:
        return False
    if key == root.chave:
        return True
    elif key < root.chave:
        return search(root.esquerda, key)
    else:
        return search(root.direita, key)


def remove(root, key):
    if root is None:
        return None

    if key < root.chave:
        root.esquerda = remove(root.esquerda, key)
    elif key > root.chave:
        root.direita = remove(root.direita, key)
    else:
        if root.esquerda is None and root.direita is None:
            return None
        elif root.esquerda is None:
            return root.direita
        elif root.direita is None:
            return root.esquerda
        else:
            aux = root.direita
            while aux.esquerda:
                aux = aux.esquerda
            root.chave = aux.chave
            root.direita = remove(root.direita, aux.chave)

    return root


def em_ordem(root):
    if root:
        em_ordem(root.esquerda)
        print(root.chave, end=' ')
        em_ordem(root.direita)


def pre_ordem(root):
    if root:
        print(root.chave, end=' ')
        pre_ordem(root.esquerda)
        pre_ordem(root.direita)


def pos_ordem(root):
    if root:
        pos_ordem(root.esquerda)
        pos_ordem(root.direita)
        print(root.chave, end=' ')


# Exemplo de uso:
if __name__ == "__main__":
    arvore = BinaryTree()
    elementos = [6, 2, 1, 4, 3, 8]
    for el in elementos:
        arvore.raiz = insert(arvore.raiz, el)

    print("Árvore atual:")
    print(arvore.raiz)

    print("\nEm ordem:")
    em_ordem(arvore.raiz)

    print("\nPré-ordem:")
    pre_ordem(arvore.raiz)

    print("\nPós-ordem:")
    pos_ordem(arvore.raiz)

    print("\n\nBusca por 4:", search(arvore.raiz))
