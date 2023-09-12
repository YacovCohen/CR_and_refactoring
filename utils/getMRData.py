from github import Github
import getpass

def fetch_pull_request_data(repo_url, mr_number):
    # Parse the repository URL to extract the owner and repo name
    # Example URL: https://github.com/owner/repo
    parts = repo_url.strip('/').split('/')
    owner = parts[-2]
    repo_name = parts[-1]

    # Create a GitHub instance (you may need to provide your GitHub credentials)
    username = input("Enter your GitHub username: ")
    password = getpass.getpass("Enter your GitHub password or access token: ")
    g = Github(username, password)

    try:
        # Get the repository
        repo = g.get_repo(f"{owner}/{repo_name}")

        # Get the pull request by number
        pull_request = repo.get_pull(int(mr_number))

        # Print pull request details
        print(f"Title: {pull_request.title}")
        print(f"Author: {pull_request.user.login}")
        print(f"Created at: {pull_request.created_at}")
        print(f"Updated at: {pull_request.updated_at}")
        print(f"URL: {pull_request.html_url}")
        print(f"Description:\n{pull_request.body}")
        print(f"List of changed files:\n{pull_request.get_files}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    repo_url = input("Enter the GitHub repository URL: ")
    mr_number = input("Enter the pull request (MR) number: ")

    fetch_pull_request_data(repo_url, mr_number)
