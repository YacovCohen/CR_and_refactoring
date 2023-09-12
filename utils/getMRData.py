from argparse import ArgumentParser
import requests

DEFAULT_REPO = "CR_and_refactoring"
DEFAULT_OWNER = "YacovCohen"

def fetch_pull_request_data(repo_name, owner, mr_number):
	token = "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"
	# Make an authenticated GET request to retrieve the MR details
	url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls/{mr_number}/files"
	headers = {"Authorization": f"token {token}"}

	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		changes = response.json()
		for change in changes:
			print(f"File: {change['filename']}")
			print(f"Status: {change['status']}")
			print(f"Additions: {change['additions']}")
			print(f"Deletions: {change['deletions']}")
			print(f"Changes: {change['changes']}")
			print("\n")
	else:
		print(
			f"Failed to fetch MR changes. Status code: {response.status_code}")


if __name__ == "__main__":
    parser = ArgumentParser(description="Util: get MR data")
    parser.add_argument("--repo_name", "-r", help="Repository name", default=DEFAULT_REPO)
    parser.add_argument("--owner", "-o", help="Repository owner", default=DEFAULT_OWNER)
    parser.add_argument("--mr_number", "-n", help="MR number.", default=None)
    args = parser.parse_args()

    fetch_pull_request_data(args.repo_name, args.owner, args.mr_number)