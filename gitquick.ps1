#This is a powershell script for easily running the git commands to update your repo

param ([string]$msg = "")

if ($msg -eq "") {
    $msg = "Updated on $(Get-Date -Format 'yyyy-MM-dd')"
}

git add .
git commit -m "$msg"
git push origin main
