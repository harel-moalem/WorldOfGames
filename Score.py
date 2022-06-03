from Utils import SCORES_FILE_NAME


def add_score(difficulty):
    score = difficulty * 3 + 5
    with open(SCORES_FILE_NAME, 'r+') as file:
        score_str = file.read()
        if score_str.isnumeric():
            score += int(score_str)
        # back to the start of file
        file.seek(0)
        file.write(str(score))


