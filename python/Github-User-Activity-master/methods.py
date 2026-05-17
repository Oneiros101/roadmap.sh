import requests
from rich import print as rich_print

API_URL = "https://api.github.com"
TOKEN_FILE = "github_token.txt"


def _authenticate():
    # read token from github_token file
    with open(TOKEN_FILE, "r") as file:
        GITHUB_TOKEN = file.read().strip("\n")

    if not GITHUB_TOKEN:
        raise ValueError("Github PAT (personal access token) is missing")
    return {"Authorization": f"token {GITHUB_TOKEN}"}


def get_user_events(username: str):
    BASE_URL = f"{API_URL}/users/{username}/events"
    headers = _authenticate()
    response_events = requests.get(BASE_URL, headers=headers)

    if response_events.status_code == 200:
        # a visual confirmation that we got a 200 response
        rich_print(
            f"\n[bold green]Status code {response_events.status_code}: {response_events.reason}\n[/bold green]"
        )
        events = response_events.json()
        _display_user_events(events, username)
    else:
        # If we get 401 Unauthorized error code
        if response_events.status_code == 401:
            return rich_print(
                f"[bold red]\nStatus code {response_events.status_code} is {response_events.reason}\n[/bold red]"
                f"A new GitHub token will need to be generated from your account.\n"
            )
        # To know which non 200 status code hit us
        return rich_print(
            f"[bold red]\nStatus code {response_events.status_code} is {response_events.reason}\n[/bold red]")


def get_user_repositories(username: str):
    BASE_URL = f"{API_URL}/users/{username}/repos"
    headers = _authenticate()
    response_repos = requests.get(BASE_URL, headers=headers)

    if response_repos.status_code == 200:
        # A visual confirmation that we got a 200 response
        rich_print(
            f"[bold green]\nStatus code {response_repos.status_code}: {response_repos.reason}\n[/bold green]"
        )
        repository = response_repos.json()
        _display_user_repositories(repository, username)
    else:
        # If we get 401 Unauthorized error code
        if response_repos.status_code == 401:
            return rich_print(
                f"[bold red]\nStatus code {response_repos.status_code} is {response_repos.reason}\n[/bold red]"
                f"A new GitHub token will need to be generated from your account.\n"
            )
        # To know which non 200 status code hit us
        return rich_print(
            f"[bold red]\nStatus code {response_repos.status_code} is {response_repos.reason}\n[/bold red]")


def _display_user_repositories(repo_list, username):
    if not repo_list:
        raise ValueError("Could not get repos\n")
    else:
        rich_print(
            f"Public Repositor{'ies' if len(repo_list) > 1 else 'y'} of [bold white]{username}[/bold white]:"
        )
        for repo in repo_list:
            print(f"- {repo["name"]}")
        print(f"\nNumber of repos: {len(repo_list)}\n")


def _display_user_events(events_list, username):
    if not events_list:
        raise ValueError("Could not get events\n")
    else:
        print(f"Event{'s' if len(events_list) > 1 else ''} of {username}:")

        for event in events_list:
            if event["type"] == "PushEvent":
                # 'size' has been removed from Github documentation
                # commit_count = event["payload"]["size"]
                # commits = event["payload"].get("commits", [])
                # commit_count = len(commits)
                #print(
                #    f"- Pushed {commit_count} commit{'s' if commit_count > 1 else ''} to {event['repo']['name']} at"
                #    f" {event['created_at']}"
                #)
                repo_name = event['repo']['name']
                commit_creation_time = event['created_at']
                print(f"- Pushed commit to {repo_name} at {commit_creation_time}")

            if event["type"] == "CreateEvent":
                repo_name = event['repo']['name']
                branch = event['payload']['ref']
                commit_creation_time = event['created_at']
                print(f"- {branch} created in {repo_name} at {commit_creation_time}")

            if event["type"] == "WatchEvent":
                repo_name = event['repo']['name']
                star_creation_time = event['created_at']
                print(f"- Starred {repo_name} at {star_creation_time}")
        print()
