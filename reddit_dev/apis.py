# praw documentation: https://praw.readthedocs.io/en/stable/
import praw
import json
import os


def create_client():
    # TODO Create Secrets in your REPLIT (under Tools) and replace the strings with your new environemnt variables
    reddit = praw.Reddit(
        client_id="my client id",
        client_secret="my client secret",
        user_agent="my user agent",
    )
    return reddit


def get_submissions(subreddit_name, order, limit):
    """
    :param subreddit_name: the name of the subreddit
    :type subreddit_name: string
    :param order: 'hot', 'top', 'new', 'rising', 'gilded', 'controversial'
    :type order: string
    :param limit: number of submissions to return
    :type limit: integer
    :return: list of submissions
    :rtype: list of json objects
    """
    # TODO, given the subreddit_name, return X (where X=limit) number of submissions for the subreddit, ordered according to the 'order' parameter
    pass


def get_toplevel_comments(submission_id, order, limit):
    """
    :param submission_id:
    :type submission_id: string
    :param order: "confidence", "controversial", "new", "old", "q&a", and "top"
    :type order: string
    :param limit: number of comments to return
    :type limit: integer
    :return: list of comments
    :rtype: list of json
    """
    # TODO, given the submission_id, return X (where X=limit) number of top level comments for the matching submission, ordered according to the 'order' parameter
    pass


def json2file(file_name, jobjs):
    with open(file_name, 'wt') as f:
        for jobj in jobjs:
            f.write(json.dumps(jobj, ensure_ascii=False, default=str) + "\n")
    pass


def run_sample_submission():
    subreddit_name = "news"
    order = "new"
    limit = 10
    submissions = get_submissions(subreddit_name, order, limit)
    file_name = os.path.join(os.getcwd(), "outputs/submissions.json")
    json2file(file_name, submissions)


def run_sample_comments():
    submission_id = "1b6o9l4"
    order = "confidence"
    limit = 50
    comments = get_toplevel_comments(submission_id, order, limit)
    file_name = os.path.join(os.getcwd(), "outputs/comments.json")
    json2file(file_name, comments)


def main():
    run_sample_submission()
    run_sample_comments()


if __name__ == '__main__':
    main()
