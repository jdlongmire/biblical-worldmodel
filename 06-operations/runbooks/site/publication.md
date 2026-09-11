# Publish and recover the site

Edit the product repository on an isolated branch, run the documented site checks and publish an authorized change to main. `.github/workflows/pages.yml` owns the GitHub-hosted build/deploy path. Check the Actions run and live URL before reporting deployment.

If a build fails, diagnose its logs; do not bypass checks. The deploy job requires the build job. A workflow dispatch with negative_control enabled is a deliberate failure test, not a production incident.

Recover a bad published page with a reviewed forward corrective commit, or a new revert commit targeting the specific product change, under the operator's applicable authorization. Do not rewrite history, change Home services, or rotate shared credentials. GitHub Pages uses its default domain; custom DNS is not configured.
