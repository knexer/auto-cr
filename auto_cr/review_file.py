import openai
import os


def prompt(code):
    return f"""You are an experienced software engineer reviewing some code.
The code follows:

====== CODE BEGINS ======
{code}
====== CODE ENDS ======

Respond in sections:
1. What does it look like this code is for?
2. What technologies (language, key libraries, etc) does this code use? Are you
familiar with those libraries, given your training data only goes up to 2021?
3. What information is missing that would make the code easier to review?
4. What are some specific issues with the code?
5. What is your overall, big-picture feedback on the code?
6. Rate the code on a five star scale using the following rubric, highlighting
the factors from the rubric led to your decision.
★: Bad.
It's very hard to understand and is extremely brittle, if it even works at all.
★★: Mediocre.
The code has some structural problems, e.g. bad encapsulation, doing too many
very different things, being unnecessarily tightly coupled to other code, etc.
It may also, or instead, have extensive and obvious bugs and problems, or it
may be difficult to understand as a whole. It may have substantial performance
issues.
★★★: Suitable for a hobby project.
The code is reasonably well-structured and comprehensible, but has substantial
deficiencies, such as being poorly documented, not handling edge cases, not
considering localization (if applicable), has memory safety risks, poor
performance, etc. It may be somewhat difficult to modify, extend, or refactor
to accommodate new requirements. It probably works well for the developer who
wrote it, but might not be a good contribution to a larger project.
★★★★: Good enough.
The code is generally well-structured and readable, and is not likely to
present notable maintainability issues for projects that include it, and can be
modified to accommodate new requirements or fix issues. While it has room for
improvement, such as missing some edge cases, some undocumented complexity,
some technical debt, etc., it likely makes more sense to invest additional
effort elsewhere first.
★★★★★: Professional quality.
While still not perfect, the code is obviously well maintained and constructed
with care. It's easy to understand, despite potentially solving complex
problems, uses best practices to great effect, and nicely encapsulates a single
problem or domain. It can be easily modified to adapt to new requirements or
fix issues."""

def review_file(file):
    # read in the file
    contents = open(file).read()

    openai.api_key = os.environ["AUTOCR_OPENAI_API_KEY"]

    # rollout and return the result
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt(contents)},
        ]
    )

    print(response.choices[0].message.content)
