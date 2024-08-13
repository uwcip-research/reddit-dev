# reddit-dev

**NOTE:** The script will have `TODO` snippets to help assist you with this exercise.

1. Obtain access to the [Reddit API](https://www.reddit.com/r/reddit.com/wiki/api/).
2. In the script `reddit_dev/apis.py`, update the `create_client` function using those credentials.  Note, the API and PRAW property names do not match, so here's a stackoverflow comment to explain it [https://stackoverflow.com/questions/74174099/how-to-login-in-to-reddit-with-praw](https://stackoverflow.com/questions/74174099/how-to-login-in-to-reddit-with-praw)
3. In the script `reddit_dev/apis.py`, update `get_submissions` and `get_toplevel_comments` to implement the reddit API using the [PRAW library](https://praw.readthedocs.io/en/stable/). **NOTE:** please update the call arguments to your preferred subreddit and comment, do not use the defaults.
4. Data will be saved to `outputs/comments.json` and `outputs/submissions.json` respectively.  The `dat/` directory serves as an example of what format we are looking for.
5. Prepare to talk about your code and your solutions in the interview.
