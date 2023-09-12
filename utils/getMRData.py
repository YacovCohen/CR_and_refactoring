from argparse import ArgumentParser
import requests
from github import Github


DEFAULT_REPO = "CR_and_refactoring"
DEFAULT_OWNER = "YacovCohen"
TOKEN = "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"

def fetch_pull_request_data(repo_name, owner, mr_number):
	# Make an authenticated GET request to retrieve the MR details
	headers = {"Authorization": f"token {TOKEN}"}
 
	g = Github(owner, TOKEN)
	repo = g.get_repo(f"{owner}/{repo_name}")
	pull_request = repo.get_pull(int(mr_number))
	print_repo_data(pull_request)
 
	for file in pull_request.get_files():
    	# Get the file content
		file_content = getContent(url_file=file.raw_url, headers=headers)
		
		if file_content is not None:
			print(f"File Name: {file.filename}")
			print("File Content:")
			print(file_content)
			print("\n" + "-" * 40 + "\n")

def print_repo_data(pull_request):
	print(f"Title: {pull_request.title}")
	print(f"Author: {pull_request.user.login}")
	print(f"Created at: {pull_request.created_at}")
	print(f"Updated at: {pull_request.updated_at}")
	print(f"URL: {pull_request.html_url}")
	print(f"Description:\n{pull_request.body}")

def getContent(url_file, headers):
	response = requests.get(url_file, headers)

	if response.status_code == 200:
		return response.text

	print(f"Failed to fetch file content. Status code: {response.status_code}")
	return None
	

if __name__ == "__main__":
	parser = ArgumentParser(description="Util: get MR data")
	parser.add_argument("--repo_name", "-r", help="Repository name", default=DEFAULT_REPO)
	parser.add_argument("--owner", "-o", help="Repository owner", default=DEFAULT_OWNER)
	parser.add_argument("--mr_number", "-n", help="MR number.", default=None)
	args = parser.parse_args()

	fetch_pull_request_data(args.repo_name, args.owner, args.mr_number)