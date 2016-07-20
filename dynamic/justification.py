"""
Text justification

Solution we want:
~~ ~~ ~~~~ ~~~~
~~~ ~~~ ~~~ ~~~
~~~ ~~ ~~~ ~~~~

Other notes:
Word uses greedy strategy
LaTeX uses dynamic programming strategy

badiness(i, j) = how bad the line is
words[i:j]

Exponential Algo ->
    For each word check if a newline should be created
"""

# passed list instead of indexes, don't want to rewrite
# but throw in a memoizer and it'll go
def justification(words):
    if not words:
        return None, 0

    least_bad = 999999999999
    other_lines = None
    end_index = 0

    for i in range(1, len(words)):
        possible_other_lines, bad = justification(words[i:])
        bad += badness(words[:i])
        if bad < least_bad:
            least_bad = bad
            end_index = i
            other_lines = possible_other_lines

    if not other_lines:
        return [words], badness(words)

    return [words[:end_index]] + other_lines, least_bad


def badness(words, max_column_length=20):
    val = len(" ".join(words))
    if val > max_column_length:
        return 999999999999

    return (max_column_length - val)**3

results = justification(["hello", "how", "how", "how", "how", "how", "how", "how", "how", "how", "how", "how", "how", "how", "how", "how", "how", "how", "how", "how"])[0]
for result in results:

    print(" ".join(result))
