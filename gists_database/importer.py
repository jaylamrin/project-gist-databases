import requests

def import_gists_to_database(db, username, commit=True):
    api_url = 'https://api.github.com/users/{u}/gists'.format(u=username)
    api_response = requests.get(api_url)
    if api_response.status_code != requests.codes.ok:
        api_response.raise_for_status()
        return

    query = """
    INSERT into gists('github_id', 'html_url', 'git_pull_url', 'git_push_url', 'commits_url', 'forks_url','public', 
            'created_at', 'updated_at', 'comments', 'comments_url')
            VALUES
            (:github_id, :html_url, :git_pull_url, :git_push_url, :commits_url, :forks_url, :public,
            :created_at, :updated_at, :comments, :comments_url)
    """
    for gist in api_response.json():
        params = {
            'github_id': gist['id'],
            'html_url': gist['html_url'],
            'git_pull_url': gist['git_pull_url'],
            'git_push_url': gist['git_push_url'],
            'commits_url': gist['commits_url'],
            'forks_url': gist['forks_url'],
            'public': gist['public'],
            'created_at': gist['created_at'],
            'updated_at': gist['updated_at'],
            'comments': gist['comments'],
            'comments_url': gist['comments_url']
        }
        db.execute(query,params)
    if commit:
        db.commit()
    return
