import git
import tempfile
import os
import shutil

def clone_repository(repo_url):
    temp_dir = tempfile.mkdtemp()
    try:
        git.Repo.clone_from(repo_url, temp_dir)
        print(f"🛸 Repository cloned to {temp_dir}")
        return temp_dir
    except Exception as e:
        print(f"Error cloning repository: {e}")
        return None

def on_rm_error(func, path, exc_info):
    # Handle read-only files on Windows by setting write permissions and retrying
    import stat
    os.chmod(path, stat.S_IWRITE)
    func(path)

def cleanup_repository(directory):
    if directory and os.path.exists(directory):
        shutil.rmtree(directory, onerror=on_rm_error)
        print(f"🧹 Cleaned up directory: {directory}")
