from model.editora import Editora
from typing import List


class EditoraDAO:


    def __init__(self):
        self.__editoras: list[Editora] = list()


    def listar(self) -> List[Editora]:
        return self.__editoras


    def adicionar(self, editora: Editora) -> None:
        self.__editoras.append(editora)


    def remover(self, editora_id: int) -> bool:
        encontrado = False
        for c in self.__editoras:
            if (c.id == editora_id):
                index = self.__editoras.index(c)
                self.__editoras.pop(index)
                encontrado = True
                break
        return encontrado


    def buscar_por_id(self, editora_id) -> Editora:
        cat = None
        for c in self.__editoras:
            if (c.id == editora_id):
                cat = c
                break
        return cat
   
    def ultimo_id(self) -> int:
        
        # i = 0
        # id = 0
        # for index in (0, range(len(self.__editoras)), 1):
        #     print(index, self.__editoras[index].id-1)
        #     if (self.__editoras[index].id -1) == i:
        #         i+=1
        #         id = i

        #     else:
        #         id = i
        #         break
        
        # return id
            
        index = len(self.__editoras) -1
        if (index == -1):
            id = 0
        else:
            id = self.__editoras[index].id
        return id
   

    