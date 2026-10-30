# Consulting Portfolio Coach

Build a consulting practice that fits the life you want, not just a calendar full of work.

Consulting Portfolio Coach helps you keep track of leads, follow up with people, scope projects, and make room for work you actually enjoy. It remembers what you tell it, helps you choose a few useful next steps, and checks in on how things are going.

It works with **Codex or Claude Code**. You bring your own AI account. There is no separate coaching app or subscription from this project.

> **Your notes live on your computer, under your control.** Your goals, leads and check-in history are saved as readable files in a private folder you choose, not in a database hosted by this project. You can inspect, edit, back up or delete them yourself. This project runs no server that collects your coaching data. 

## What it can help with

- Set an income goal alongside a realistic weekly time budget.
- Keep promising leads from getting lost, without treating every conversation as a commitment.
- Prepare follow-up messages, project scopes and questions for potential clients.
- Spot work that looks attractive but comes with too many meetings, unclear responsibilities or ongoing support.
- Keep paid work, unpaid favors and side-project experiments separate.
- Notice what feels energizing or draining, and use that to make better choices next time.

You set the goals and boundaries. The coach should help you follow your own priorities, not push you to work more or say yes to everything.

## What using it looks like

You can start with ordinary updates:

> A former client wants to work together again. Last time it paid well, but the meetings took over my week. Help me figure out what to offer this time.

Or:

> I sent the proposal. Please mark that done, and help me decide what deserves my attention next.

The coach keeps private notes so you don't have to explain the whole situation every time. It distinguishes interest from a signed contract, a team's project budget from your personal fee, and a good idea from something you've agreed to build.

## Getting started

You'll need Codex or Claude Code with access to a folder on your computer. You do **not** need to connect email, a calendar or a CRM. A CRM is a contact-and-sales tracking system; this coach can start with simple notes instead.

### Prefer to ask your AI assistant?

Share the repository link with Codex or Claude Code and say:

> Help me install Consulting Portfolio Coach from https://github.com/mathemagica/consulting-portfolio-coach. Read its instructions and setup script first. Use the installation for this app, and create a separate private folder for my notes outside any shared code repository. Don't overwrite an existing skill or notes. Then ask me about my goals and current work. Don't connect accounts or schedule anything yet.

Your assistant may need your permission to download files or create the folders. If it cannot install the skill directly, it should walk you through the steps below rather than claim it is installed.

### Prefer the terminal?

These commands require Git and Python 3.10 or later. Download the repository and enter its folder:

```sh
git clone https://github.com/mathemagica/consulting-portfolio-coach.git
cd consulting-portfolio-coach
```

If the repository is private, you will need GitHub access first. Read the included skill and setup script, then choose your app:

```sh
python3 scripts/setup.py install --client codex
# For Claude Code instead:
python3 scripts/setup.py install --client claude
# Or install for both:
python3 scripts/setup.py install --client both
```

Create a separate folder for your personal notes:

```sh
python3 scripts/setup.py init --workspace ~/consulting-portfolio-coach-private
```

The setup script never overwrites existing notes or a different installed version of the skill. It does not connect accounts, create schedules or change your other settings.

### Start your first conversation

In Codex, invoke `$consulting-portfolio-coach`. In Claude Code, use `/consulting-portfolio-coach`. Then say:

> Help me set up my portfolio coach. My private notes are in [full path to my private folder]. Ask about my income goal, total time available, existing work, potential clients and the kind of work I want more or less of.

Replace the bracketed text with your actual folder path; your assistant can help find it. It may need permission to read and update that folder. Restart your app if the new skill does not appear.

## Morning and afternoon check-ins

Once the coach understands your situation, you can ask:

> Set up a morning brief at 9 AM and an afternoon review at 4 PM on weekdays in my timezone. Show me the times and where the check-ins will appear before saving them. Use Friday afternoon for a weekly review instead. Leave weekends off.

- **Morning:** a short reminder of your goals, what changed, and up to three realistic next actions.
- **Afternoon:** what moved, anything new you committed to, and what felt energizing or draining.
- **Friday:** a look at income, workload, opportunities and next week's priorities.

You can choose different times, include lighter weekend check-ins, or use the coach only when you ask. Missing a check-in isn't a failure and shouldn't produce a pile of catch-up assignments.

**Installing the skill does not turn on reminders.** Your assistant must set them up separately using the scheduling features available in your app and confirm they were saved. For check-ins that use local notes, your computer needs to be on; app-running requirements depend on the scheduler. Claude Code's `/loop` is not the recommended durable twice-daily setup.

See the [scheduling guide](skills/consulting-portfolio-coach/references/scheduling.md) for prompts and app-specific details. If you use both apps, choose just one to run scheduled check-ins so they don't write to your notes at the same time.

## Your notes and privacy

Your notes stay separate from the shareable skill. They include your goals, work, leads, decisions and check-in history. Optional files track product experiments, research and events. No personal information is included with this project.

You can use the coach without account connections. If you choose to add email or documents later, start with relevant read-only access and confirm the correct account. The coach should not send messages, edit external records, buy anything or make commitments without your explicit approval.

The private-folder setup restricts file access on systems that support it and helps prevent accidentally adding notes to Git. **It is not encryption or a backup.** Your AI provider may still process information you ask the assistant to read; local storage does not mean offline AI. Check your provider's data settings before sharing sensitive material.

Never put passwords, API keys, client correspondence or your personal notes in this repository. This is coaching support, not legal, tax, investment or mental-health advice, and it cannot guarantee income.

## For people who want to customize it

Both apps use the same `SKILL.md` and supporting files. The installer copies them to:

| App | Personal skill folder |
| --- | --- |
| Codex | `~/.agents/skills/consulting-portfolio-coach/` |
| Claude Code | `~/.claude/skills/consulting-portfolio-coach/` |

You can copy `skills/consulting-portfolio-coach/` there manually instead. Personal Claude Code installation does not automatically install the skill in Claude web, Cowork or cloud tasks.

To update an installation, back up the existing skill folder, remove that installed copy and reinstall. Leave your private notes alone. If you installed this project's previous name, `independent-work-coach`, back up and remove that old installed copy too so both versions don't appear. Review any existing task paths before switching; this rename does not migrate schedules. An unrelated skill with the same name will not be overwritten by the installer.

To check a change:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_package.py
```

These tests check packaging and setup safety, not whether the coaching is useful. The [fictional evaluation scenarios](evals/scenarios.md) help you test behavior in either app without using real personal information.

## Documentation and license

Setup guidance checked October 30, 2026: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Codex scheduling](https://learn.chatgpt.com/docs/automations?surface=app), [Claude Code skills](https://code.claude.com/docs/en/skills), and [Claude Code scheduling](https://code.claude.com/docs/en/scheduled-tasks).

MIT license. See [LICENSE](LICENSE).
