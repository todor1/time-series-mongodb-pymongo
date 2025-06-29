### TODO: enhance the script to get ALL public repos by the user, not only on the first page, perhaps connected with the gihub api functionality

import requests
import os


def download_github_repos(username, output_dir="github_repos"):
    os.makedirs(output_dir, exist_ok=True)
    api_url = f"https://api.github.com/users/{username}/repos"

    response = requests.get(api_url)
    if response.status_code != 200:
        print(
            f"Failed to fetch repositories for user '{username}'. Status code: {response.status_code}"
        )
        return

    repos = response.json()

    for repo in repos:
        repo_name = repo["name"]
        default_branch = repo["default_branch"]
        zip_url = f"https://github.com/{username}/{repo_name}/archive/refs/heads/{default_branch}.zip"
        zip_path = os.path.join(output_dir, f"{repo_name}.zip")

        print(f"Downloading {repo_name}...")
        zip_response = requests.get(zip_url)
        if zip_response.status_code == 200:
            with open(zip_path, "wb") as f:
                f.write(zip_response.content)
            print(f"Saved to {zip_path}")
        else:
            print(
                f"Failed to download {repo_name}. Status code: {zip_response.status_code}"
            )


# Example usage
if __name__ == "__main__":
    # Change GitHub username
    download_github_repos("codingforentrepreneurs")
