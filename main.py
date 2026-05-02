def main()-> None:
    """Fonction principale du programme.
    Affiche un menu pour interagir avec la todo list et exécute les actions correspondantes en fonction du choix de l'utilisateur.
    :param: rien
    :type: None
    :return: None
    :rtype: None"""
    todo_list: list[dict] = []
    while True:
        print("Menu:")
        print("1. Ajouter une tâche")
        print("2. Supprimer une tâche")
        print("3. Terminer une tâche")
        print("4. Afficher les tâches triées par priorité")
        print("5. Rechercher des tâches par nom")
        print("6. Rechercher des tâches par priorité")
        print("7. Sauvegarder les tâches")
        print("8. Charger les tâches")
        print("9. Quitter")

        choix : str = input("Entrez votre choix (1-9): ")

        if choix == "1":
            nom: str = input("Entrez le nom de la tâche: ")
            priorite: int = int(input("Entrez la priorité de la tâche (1-5): "))
            date: str = input("Entrez la date aaaammjj: ")
            ajoute_tache(nom, date, priorite, todo_list)
            todo_list: list[dict] = tri_tache(todo_list)
            print(f"Tâche '{nom}' ajoutée avec priorité {priorite} à la date {date}.")
            print(f"todo_list:{todo_list}")

        elif choix == "2":
            nom: str = input("Entrez le nom de la tâche à supprimer: ")
            todo_list: list[dict] = elimine_tache(nom,todo_list)
            print(f"Tâche '{nom}' supprimée.")
            print(f"todo_list:{todo_list}")

        elif choix == "3":
            nom: str = input("Entrez le nom de la tâche à terminer: ")
            todo_list: list[dict] = termine_tache(nom,todo_list)
            print(f"Tâche '{nom}' marquée comme terminée.")
            print(f"todo_list:{todo_list}")

        elif choix == "4":
            todo_list: list[dict] = tri_tache(todo_list)
            taches_triées: list[dict] = affiche_taches(todo_list)


            print(f"Tâches triées par priorité:{taches_triées}")
           

        elif choix == "5":
            mot: str = input("Entrez un mot à rechercher dans les noms des tâches: ")
            taches_trouvees: list[dict] = cherche_taches_noms(todo_list, mot)
            print(f"Tâches trouvées:{taches_trouvees}")
           

        elif choix == "6":
            p: int = int(input("Entrez la priorité à rechercher (1-5): "))
            taches_trouvee: list[dict] = cherche_taches_priorite(todo_list, p)
            print(f"Tâches trouvées:{taches_trouvee}")

        elif choix == "7":
            sauvegarde(todo_list)
            print("Tâches sauvegardées.")

        elif choix == "8":
            todo_list: list[dict] = charge()
            print("Tâches chargées.")
            print(f"todo_list: {todo_list}")


        elif choix == "9":
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 9.")
           

main()
