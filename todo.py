todo_list: list[dict] = []

def ajoute_tache(nom:str, date:str, priorite:int,todo_list:list[dict])->list[dict]:
    """Ajoute une tâche à la liste des tâches.
    Crée un dictionnaire représentant la tâche avec les informations fournies et l'ajoute à la liste.
    :param nom: Le nom de la tâche.
    :type nom: str
    :param date: La date d'échéance de la tâche.
    :type date: str
    :param priorite: La priorité de la tâche .
    :type priorite: int
    :return: La liste des tâches mise à jour.
    :rtype: list[dict]"""
    etat: bool = False # par défaut, la tâche n'est pas terminée
    tache: dict = {"nom": nom, "date": date, "priorite": priorite, "etat": etat} # création d'un dictionnaire pour représenter la tâche
    todo_list.append(tache)
    return todo_list


def elimine_tache(nom: str,todo_list:list[dict]) -> list[dict]:
    """Élimine une tâche de la liste en fonction de son nom.
    Parcourt la liste des tâches et supprime celle qui correspond au nom donné.
    :param nom: Le nom de la tâche à éliminer.
    :type nom: str
    :return: la liste sans l'élément supprimé
    :rtype: list[dict]"""
    for i, tache in enumerate(todo_list):
        if tache["nom"] == nom:
            todo_list.pop(i)
            return todo_list
    return todo_list
       
def termine_tache(nom: str,todo_list:list[dict]) -> list[dict]:
    """Marque une tâche comme terminée en fonction de son nom.
    Parcourt la liste des tâches et modifie l'état de celle qui correspond au nom donné
    :param nom: Le nom de la tâche à terminer.
    :type nom: str
    :return: la todo list avec l'etat de la tache modifié
    :rtype: list[dict]"""
    for tache in todo_list:
        if tache["nom"] == nom:
            tache["etat"] = True
            return todo_list
    return todo_list

def tri_tache(todo_list:list[dict])->list[dict]:
    """Affiche les tâches triées par priorité (de la plus élevée à la plus basse).
    :param: liste des taches todo_list
    return: la liste des taches non trié par ordre de priorité décroissante
    rtype: list[dict]
    """
    n: int = len(todo_list)
    for droite in range(n-1,0,-1):
        for gauche in range(droite):
            if todo_list[gauche]["priorite"] < todo_list[gauche+1]["priorite"]:
                todo_list[gauche], todo_list[gauche+1] = todo_list[gauche+1], todo_list[gauche]
    return todo_list

def affiche_taches(todo_list: list[dict]) -> list[dict]:
    """Retourne uniquement les tâches non terminées, déjà triées.
    :param todo_list: La liste des tâches à afficher qui ne sont pas finis mais triées.
    :type todo_list: list[dict]
    :return: La liste des tâches non terminées triées .
    :rtype: list[dict]"""
    return [t for t in todo_list if t["etat"] == False]

def cherche_taches_noms(todo_list: list[dict], mot:str)-> list[dict]:
    """
    Recherche  et renvoie les tâches dans la todo list dont le nom contient un mot donné  par l'utilisateur
    param: la liste des taches todo et le mot recherché par l'utilisateur
    type: todo:list[dict]
           mot:str
    return: liste des taches correspondant au mot donnée
    rtype:list[dict]
    """
    resultat_nom: list[dict] = []
    for t in todo_list:
        if mot.lower() in t["nom"].lower():
            resultat_nom.append(t)
    return resultat_nom

def cherche_taches_priorite(todo_list: list[dict], p: int) -> list[dict]:
    """ recherche les taches ayant la priorité donnée par l'utilisateur et renvoie une liste des ces taches
    param:liste des taches todo et la priorité recherchée p
    type:list[dict] et p:int
    return:liste des taches correspondant à la priorité
    rtype: list[dict] """
    resultat_p: list[dict] = []
    for t in todo_list:
        if t["priorite"] == p:
            resultat_p.append(t)
    return resultat_p
