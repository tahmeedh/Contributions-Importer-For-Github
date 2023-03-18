# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo('https://stash.globalrelay.net/scm/portal/jsat-message-web.git')
# Your mock repo
mock_repo = git.Repo('https://github.com/tahmeedh/MockServiceTest.git')
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['tahmeedhossain@gmail.com', 'tahmeed.hossain@globalrelay.net'])
importer.import_repository()
