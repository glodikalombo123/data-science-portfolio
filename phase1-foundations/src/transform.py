from extract import extract_events

def filter_valid_events(events : list[dict]) -> list[dict]:
    """
    Cette fonction filtre et ne garde que les événements où user_id n'est pas NULL ou vide et retourne une liste nettoyée

    Args:
        events (list[dict]): argument de la liste des événements que l'on importe à partir du fichier extract.py

    Returns:
        list[dict]: liste des événements filtrés, sans les événements qui avaient des 'users_id' NULL ou vide
    """

    valid_event = [event for event in events if event['user_id'] not in ('NULL', '')]
    return valid_event

def convert_types(events : list[dict]) -> list[dict]:
    """
    Converti les types des données là où c'est necessaire

    Args:
        events (list[dict]): la liste que nous avons importé en CSV

    Returns:
        list[dict]: Liste que nous retournons où nous avons modifiés les types des certaines données
    """
    for event in events:
        event['event_id'] = int(event['event_id'])
        event['session_duration_sec'] = int(event['session_duration_sec'])

    return events

def add_event_date(events: list[dict]) -> list[dict]:
    """ Ajout de la date dans la liste des événements """
    for event in events:
        event['event_date'] = event['timestamp'].split(" ")[0]
    return events

def main():
    my_data = extract_events("phase1-foundations/data/raw/events.csv")

    filtered_data = filter_valid_events(my_data)
    type_converted = convert_types(filtered_data)
    transformed_data = add_event_date(type_converted)

    print(f"Le nombre d'événement avant filtrage est de : {len(my_data)}")
    print(f"Le nombre d'événement après filtrage est de : {len(filtered_data)}")
    print(f"Les 3 premiers événements avec les types corrects sont : {type_converted[0:3]}")


if __name__ == "__main__":
    main()
