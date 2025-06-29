def generate_outreach_messages(candidates, jd_context):
    messages = []

    for c in candidates:
        msg = (
            f"Hi {c['name']},\n\n"
            f"I came across your profile while sourcing for a role at {jd_context.get('company', 'our company')}.\n"
            f"Your experience with {', '.join(jd_context['skills'])} and background at {c.get('company', 'your company')} "
            f"stood out in relation to our ML Research position focused on LLMs and developer productivity.\n\n"
            f"Would love to share more if you’re open to exploring this exciting opportunity!"
        )
        messages.append(msg)

    return messages
