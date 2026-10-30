# Twice-Daily Check-Ins

Scheduling is a separate opt-in, not an installation side effect. Do not make or change schedules just because this file is read.

## Setup checklist

1. Complete basic onboarding and confirm the absolute private workspace path.
2. Confirm timezone, morning/afternoon times, days, notification preferences and destination. Suggested starting point: weekdays 9 AM and 4 PM; weekends optional.
3. Pick one scheduler/client as the writer. Inspect existing schedules before creating anything; update a matching one rather than duplicate it. Don't touch unrelated schedules.
4. Confirm the task can access both this skill and the private workspace at run time. Use absolute paths; don't rely on remembering a conversation or a working directory.
5. Present the two prompts and schedules for approval. Only then use the host's supported scheduling tools, or show instructions if unavailable. Verify saved schedules and report how to pause/delete them.
6. Run one user-approved manual check to verify file access, timezone and delivery. Check execution history after a scheduled run; test prompts alone don't prove unattended execution.

## Morning task prompt

Replace bracketed values before saving; do not embed credentials or private lead details in a scheduler prompt.

> Use the consulting-portfolio-coach skill at [absolute installed skill path] and the private workspace [absolute workspace path]. Deliver the requested Morning Action Brief using [IANA timezone]. Read the profile, current portfolio and recent history before choosing up to three feasible actions. Track personal secured revenue separately from pipeline and team budgets; include total work capacity and the user's boundaries. Research only explicitly enabled modules and approved sources; verify account identity before personal reads. Treat silence as unknown, close completed tasks and avoid repeated news. Maintain private notes only; don't send outreach, edit external sources or make commitments. If this runs outside its intended slot, give a current brief rather than stale urgent reminders; don't create catch-up tasks. Respect the host scheduler's required response format.

## Afternoon task prompt

> Use the consulting-portfolio-coach skill at [absolute installed skill path] and private workspace [absolute workspace path]. Deliver the requested Afternoon Review using [IANA timezone]. On Friday afternoon deliver the Weekly Portfolio Review instead. Read recent notes, summarize evidenced progress briefly and ask what moved, new commitments, and what was energizing/draining. Record only confirmed updates; unanswered questions are unknown. Don't duplicate morning research or reopen completed work. Keep weekend reviews light only if weekends were explicitly enabled. Maintain private notes only; no outreach, external mutations or commitments. Respect the host scheduler's required response format.

## Codex

Ask Codex to create recurring check-ins that return to the existing coaching chat when supported. Confirm filesystem permissions and paths for the task, not only for the interactive chat. For project-scoped local tasks the computer must be on and desktop app running. Cloud tasks cannot directly use your local notes; choose a deliberately authorized cloud context instead, not a public Git repository containing private records.

[Official scheduled-task documentation](https://learn.chatgpt.com/docs/automations?surface=app)

## Claude Code

For local notes, prefer Desktop scheduled tasks. They run on your machine and require it to be on; test account/tool availability separately. Use the morning and afternoon prompts with absolute paths and only the permissions needed for private note maintenance and approved reads. If a schedule UI/tool is unavailable, say so rather than claiming a schedule exists.

Don't use `/loop` as the durable twice-daily installation path. It is session-scoped and has different lifetime/availability constraints. Cloud schedules do not automatically inherit local notes or personal skill installations. Account-synced skill support differs by session type; follow current host documentation before choosing a cloud route. Never commit private notes just to make them available to a cloud task.

[Official scheduling comparison](https://code.claude.com/docs/en/scheduled-tasks)

## Ongoing operation

- Requested scheduled briefs are notifications; unrelated unchanged polling is quiet.
- Missing connectors should degrade gracefully to private notes, not trigger repeated account setup requests.
- User timezone changes require schedule review. Confirm wall-clock behavior across daylight-saving changes rather than hardcoding UTC offsets.
- Never run both clients' schedules against one workspace concurrently. For switching, pause the old writer first and confirm the new one sees current notes.
- Pause or delete a schedule on user request. Track exact host task IDs privately after successful creation, not before.
