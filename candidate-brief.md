# Practical Assessment — Authentication Log Analyzer

**Time:** ~2 hours · **Language:** Python 3 · **You may use:** the official Python
and Git/GitHub documentation, your own notes, and the internet for reference.
Please write the code yourself rather than having it generated for you.

You will need a free **GitHub account** for this task. If you don't have one yet,
create one at https://github.com/signup before you start.

---

## Background

You work on a support team. A switch using **802.1X / RADIUS** authentication has
produced a log file, `auth_log.txt`. Each line records one authentication attempt
— either `ACCEPT` (the device was allowed onto the network) or `REJECT` (it was
refused).

A colleague has asked you to turn this raw log into something queryable and to
answer a few questions about what happened. This is the kind of task you would do
when investigating a ticket. You will deliver your work the same way we work
day-to-day: through Git and a **pull request** on GitHub.

---

## Step 0 — Get the code from GitHub

The starter repository and the log file live here:

**https://github.com/ondernemersschoolnl/coding-test**

1. **Fork** the repository to your own GitHub account (the "Fork" button, top
   right of the repo page). This gives you your own copy to work in.
2. **Clone** your fork to your computer:
   ```
   git clone https://github.com/<your-username>/coding-test.git
   cd coding-test
   ```
3. **Create a new branch** to work in (don't work directly on `main`):
   ```
   git checkout -b solution-<your-name>
   ```

You'll find `auth_log.txt` inside the repository — that's your input data.

> Note: a "pull request" on GitHub is the same thing GitLab calls a "merge
> request". If you've used GitLab before, it's the same idea.

---

## The log format

Every line of `auth_log.txt` looks like this:

```
2025-06-02T09:00:05 host=switch-01 port=Gi1/0/22 mac=00:1A:2B:DE:AD:01 user=admin vlan=- result=REJECT reason=bad-credentials
```

Fields:

| field    | meaning                                            |
|----------|----------------------------------------------------|
| timestamp| when it happened (ISO format)                      |
| host     | which switch                                       |
| port     | which switch port                                  |
| mac      | the device's MAC address                           |
| user     | the username presented                             |
| vlan     | assigned VLAN (`-` if the attempt was rejected)    |
| result   | `ACCEPT` or `REJECT`                               |
| reason   | only present on `REJECT` lines                     |

---

## What to build

A single Python script (standard library only — you do **not** need to install
anything; `sqlite3` is built in).

**Step 1 — Parse.** Read `auth_log.txt` line by line and extract the fields above.

**Step 2 — Store.** Insert each record into an **SQLite** database, into a table
you design (one row per log line). Choose sensible column names and types.

**Step 3 — Answer these questions using SQL queries** (not by counting in Python)
and print the answers clearly:

1. How many `ACCEPT` results and how many `REJECT` results are there in total?
2. The **top 5 usernames** with the most `REJECT` results, with their counts.
3. Every **MAC address that was rejected 3 or more times**, with its count,
   most-rejected first.
4. The number of events per switch (`host`).

**Step 4 — Short written note.** At the bottom of your script (as a comment) or in
a separate text file, write 2–4 sentences: looking at your results, is there
anything that looks suspicious or worth raising with a colleague? Why?

---

## Step 5 — Commit and open a pull request

Work the way we do on the team:

1. **Commit** your work as you go, with clear messages:
   ```
   git add .
   git commit -m "Parse auth log into SQLite and answer questions"
   ```
   (Several small commits are perfectly fine — better than one giant one.)
2. **Push** your branch to your fork:
   ```
   git push origin solution-<your-name>
   ```
3. On GitHub, **open a pull request** from your branch back to the
   `ondernemersschoolnl/coding-test` repository. Give it a short title and, in the
   description, briefly say what you did and note anything you didn't finish.

That pull request is your hand-in. We'll review it there.

---

## What "done" looks like (acceptance criteria)

- [ ] You forked the repo, cloned it, and worked on your own branch.
- [ ] Running `python3 your_script.py` parses the log and builds the database with
      no errors.
- [ ] The script prints clear answers to all four questions.
- [ ] The answers come from SQL queries against the database.
- [ ] You included your short written note for Step 4.
- [ ] Your work is committed and submitted as a pull request to the repository.

---

## Optional (only if you finish early — not required)

- Add a query: which users had a `REJECT` and later (by timestamp) an `ACCEPT`?
- Make the log filename a command-line argument instead of hard-coding it.
- Count how many lines (if any) did not match the expected format.

---

## A note from us

If you get stuck on any part — Git, the parsing, the SQL — leave a comment in your
code or in the pull request explaining what you tried and what you'd do next. That
is genuinely useful to us, not a negative. It is also completely fine to ask
clarifying questions before or during the task. Knowing when to ask is a strength.
