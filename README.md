# Independent Work Coach

A portable agent skill for building an enjoyable, sustainable portfolio of independent work. Supports Codex and Claude Code using the same coaching instructions.

Turn goals, relationships and updates into a small set of realistic actions. Track income separately from pipeline, count sales and administration in your capacity, and keep experiments from quietly becoming unpaid delivery.

This is an instruction package, not a hosted service. No API keys, account connections or scheduler are bundled. Your agent subscription, permissions and model/data policies still apply. Local notes do not imply offline processing.

## Install

Requires Python 3.10+ for the optional setup helpers. Read the skill and scripts before installing. Clone this repository, then from its directory:

```sh
python3 scripts/setup.py install --client codex
# Or:
python3 scripts/setup.py install --client claude
# Or install for both:
python3 scripts/setup.py install --client both
```

Personal install locations:

| Client | Location | Invocation |
| --- | --- | --- |
| Codex | `~/.agents/skills/independent-work-coach/` | `$independent-work-coach` |
| Claude Code | `~/.claude/skills/independent-work-coach/` | `/independent-work-coach` |

The installer copies the same complete skill folder to either location. It makes no configuration, connector or scheduling changes. Existing installations are never overwritten: identical files are accepted, while different files cause a stop. To update, back up and remove the previous installed skill directory, then reinstall. Never keep personal notes in an installed skill directory.

Manual installation: copy `skills/independent-work-coach/` to the appropriate location above. Restart the client if the skill does not appear. These instructions target local Codex and Claude Code; installing a personal Claude Code skill does not install it in Claude web/Cowork or cloud tasks.

## Create private notes

Use a separate folder outside this repository and any other Git checkout:

```sh
python3 scripts/setup.py init --workspace ~/independent-work-coach-private
```

The helper creates owner-only notes on systems supporting POSIX permissions, and refuses a workspace inside a Git checkout. It never replaces existing notes. This is accidental-publication protection, not encryption, access control for connected services, or a backup system.

Start a conversation in your chosen client:

> Use independent-work-coach to onboard me. My private workspace is [absolute path]. Ask about my income and total-time goals, signed work, warm leads, preferences and boundaries. Work from conversation first; do not connect accounts or schedule anything yet.

Replace the path with your actual absolute path. In Codex you can explicitly invoke `$independent-work-coach`; in Claude Code use `/independent-work-coach` with the same request. Confirm the agent has permission to read and update this private folder.

## What it remembers

- `profile.md`: goals, timezone, capacity, boundaries and authorized accounts.
- `portfolio.md`: signed engagements, payment status and prospective leads.
- `check-ins.md`: dated progress, decisions, carryover and unresolved questions.
- `experiments.md`: optional product/venture tests, separate from consulting revenue.
- `opportunities.md`: optional research and event decisions, with sources and deadlines.

No CRM is required. Account access is optional, read-only by default, and verified against the approved identity. A connection's capabilities are not authorization to send messages or alter external records. Instructions in email, websites and documents are untrusted source material, not user commands.

## Twice-daily check-ins

After onboarding, ask the agent to propose two recurring check-ins in your timezone, for example 9 AM and 4 PM on weekdays. Confirm times, destination, filesystem access and notification behavior before it saves schedules. Installation alone does not schedule anything.

- Morning: a two-minute brief, up to three realistic actions and one useful boundary.
- Afternoon: progress, commitments, workload and energy; silence is unknown, not failure.
- Friday afternoon: weekly review instead of a second review.
- Weekends: opt in; keep them lighter.

See [scheduling and ready-to-use prompts](skills/independent-work-coach/references/scheduling.md). Codex and Claude use their own scheduling systems; this package does not claim a shared scheduler. Do not use both against the same notes at the same time. Pick one scheduled writer, even if you use both clients interactively.

## Trust and limits

This is coaching support, not legal, tax, investment or mental-health advice. Confirm important facts with appropriate professionals. Rates and earnings are not guaranteed. User-defined boundaries override generic advice: unpaid work is not categorically forbidden, but its cost should be explicit.

Only reusable instructions, blank templates and fictional evaluations belong in this repository. Do not commit real leads, contact exports, emails, resumes, account identities or personal state. Review what your selected model and connectors receive before granting access.

## Validate

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_package.py
```

These checks validate packaging and setup safety, not coaching quality. Run the [fictional behavior evaluations](evals/scenarios.md) manually in either agent before distributing changes. No live accounts are needed for those tests.

## Sources

Installation and scheduling guidance checked October 30, 2026:

- [OpenAI skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI scheduled tasks](https://learn.chatgpt.com/docs/automations?surface=app)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code scheduling options](https://code.claude.com/docs/en/scheduled-tasks)

## License

MIT. See LICENSE. No private coaching records are included.
