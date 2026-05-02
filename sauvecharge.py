import pandas as pd
from todo import *

def sauvegarde(todo_list: list[dict]) -> None:
    """Sauvegarde la todo list dans un fichier csv.
    :param: liste des taches todo
    :type: list[dict]
    :return: rien
    :rtype: None"""
    df = pd.DataFrame(todo_list)
    df.to_csv("todo_list.csv", index=False)

def charge() -> list[dict]:
    """charge les taches depuis un fichier csv et reconstruit la liste des taches.
    :param: rien
    :type: None
    :return: liste des taches chargées depuis le fichier
    :rtype: list[dict]"""
    df = pd.read_csv("todo_list.csv")
    todo2: list[dict] = []
    for i in range(len(df)):
        tache: dict = {
            "nom": str(df.iloc[i, 0]),
            "date": str(df.iloc[i, 1]),
            "priorite": int(df.iloc[i, 2]),
            "etat": bool(df.iloc[i, 3] == True)
        }
        todo2.append(tache)
    return todo2
