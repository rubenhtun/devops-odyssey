## Shorthand Notes

### 1. Building Jenkins Workspace
- enter new item
- select project type and ok
- select Githud project and git
- paste github repo link
- branch is main
- add some shells echo "--- Current Directory ---"
pwd
echo "--- Files in Workspace ---"
ls -la
echo "--- Testing Docker Access ---"
docker --version in build steps and save

finally build now
