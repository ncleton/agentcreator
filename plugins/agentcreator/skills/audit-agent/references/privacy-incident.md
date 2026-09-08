# Privacy incident

## Local or staged detection

Block commit and push. Move the data into private storage, then remove it from the index with `git rm --cached` without deleting the local copy. Replace it in shareable files with a neutral variable.

## Data already pushed

Treat the data as exposed even when the repository is private. In order:

1. revoke or rotate every affected secret;
2. suspend publication;
3. identify affected commits and people who may have retrieved the data;
4. prepare history cleanup;
5. obtain explicit confirmation before coordinated history rewriting and force pushing.

Never display the detected value. Report only the file, risk category, and required action.
