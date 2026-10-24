# Robot code time machine

The robot-lab folder is a starter project, not a Git repository yet. Use a fresh copy for each pair. The Python program only prints a pretend mission, so no robot is needed.

## Local lab (everyone)

1. In VS Code, choose File > Open Folder and open the robot-lab folder inside this package.
2. Choose Terminal > New Terminal. Check that the terminal is inside robot-lab.
3. Type `git init -b main`. If Git requests an identity when committing, ask your coach to configure a suitable repository-local name and email.
4. Type `git status`, then `git add mission.py`, then `git diff --cached`.
5. Type `git commit -m "Add our first mission"`.
6. In `mission.py`, change `turn_speed = 60` to `turn_speed = 40`. Save the file.
7. Type `git diff`. Explain the minus and plus lines to your partner.
8. Type `git add mission.py`, then `git diff --cached`, then `git commit -m "Lower turn speed to 40"`.
9. Type `git log --oneline`. You should see two commits.
10. Type `git switch -c turn-test`.
11. Change `turn_angle = 90` to `turn_angle = 45`. Save, review, stage, and commit with message `Try a 45 degree turn`.
12. With no uncommitted changes, type `git switch main`. Read the angle in the editor. It should be 90.
13. Type `git switch turn-test`. Read the angle again. It should be 45.

Optional: run `python mission.py` or `python3 mission.py`, depending on your computer. The console output is a simulation, not a physical robot test.

## Recovery mini-lab

On `turn-test`, make an unwanted edit to `turn_speed`, save it, and do NOT stage it. Review it with `git diff`. If you agree to lose this edit, use `git restore -- mission.py`. This replaces unstaged edits with the staged version. With nothing staged, that is the current committed version. Ask your coach before discarding a change you want to keep.

## GitHub demonstration

Your coach supplies a separate practice repository, permissions, and sign-in where appropriate. Its `main` branch must contain the starting mission before the branch push/PR demonstration. This local starter has no remote configured.

- `git clone REPO_URL` makes a separate local copy of a coach-supplied repository. Replace `REPO_URL` with its actual URL. Run the command from a parent folder, not inside this initialized lab.
- `git push -u origin turn-test` uploads the committed practice branch once the remote and access are prepared.
- On GitHub, open a pull request with base `main` and compare `turn-test`. Explain your change and the output you checked.
- After review and merge, use `git switch main` and `git pull --ff-only` from a clean working tree. This requires `main` to track the remote main branch. If Git refuses, ask the coach to inspect instead of forcing it.

## Team habits

Save before reviewing changes. Stage the files you intend. Review the staged snapshot. Write a helpful commit message. Check your current branch. Explain and test a proposed change before merging.
