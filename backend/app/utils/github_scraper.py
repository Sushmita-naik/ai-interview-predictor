import requests
from datetime import datetime


def get_github_profile(username):
    """
    Fetch GitHub profile information
    """

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code != 200:
        return {
            "error": "GitHub user not found"
        }

    data = response.json()

    return {
        "username": data.get("login"),
        "name": data.get("name"),
        "bio": data.get("bio"),
        "followers": data.get("followers"),
        "following": data.get("following"),
        "public_repos": data.get("public_repos"),
        "profile_url": data.get("html_url")
    }


def get_repositories(username):
    """
    Fetch public repositories
    """

    url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    repos = response.json()

    repository_list = []

    for repo in repos:

        repository_list.append({
            "name": repo.get("name"),
            "language": repo.get("language"),
            "stars": repo.get("stargazers_count"),
            "forks": repo.get("forks_count"),
            "created_at": repo.get("created_at")
        })

    return repository_list


def calculate_github_score(username):
    """
    Generate GitHub score
    """

    repos = get_repositories(username)

    if not repos:
        return 0

    total_stars = sum(
        repo["stars"] or 0
        for repo in repos
    )

    total_forks = sum(
        repo["forks"] or 0
        for repo in repos
    )

    repo_count = len(repos)

    score = (
        repo_count * 5 +
        total_stars * 2 +
        total_forks
    )

    return min(score, 100)


def analyze_github(username):

    profile = get_github_profile(
        username
    )

    repos = get_repositories(
        username
    )

    score = calculate_github_score(
        username
    )

    return {
        "profile": profile,
        "repository_count": len(repos),
        "github_score": score,
        "repositories": repos[:10]
    }


if __name__ == "__main__":

    username = "octocat"

    result = analyze_github(
        username
    )

    print(result)