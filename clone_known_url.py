from git import Repo


def clone_repository():
    # Vervang de URL hieronder door de URL van de repository die je wilt klonen
    repository_url = "https://github.com/gebruiker/voorbeeld-repo.git"

    # Vervang ook de padnaam hieronder door de gewenste doelmap op je machine
    destination_path = "pad/naar/doelmap"

    try:
        # Git clone-commando uitvoeren met GitPython
        Repo.clone_from(repository_url, destination_path)
        print(f"Repository gekloond naar {destination_path}")
    except Exception as e:
        print(f"Fout bij het klonen van de repository: {e}")


if __name__ == "__main__":
    clone_repository()
