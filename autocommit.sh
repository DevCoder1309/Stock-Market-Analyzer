while true; do
    # Check for changes
    if ! git diff --quiet; then
        git add .
        git commit -m "Process of AutoCommit in the Project"
        git push
    fi
    sleep 10
done