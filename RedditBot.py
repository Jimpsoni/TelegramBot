from praw import Reddit
from prawcore import exceptions
import requests as r


class RedditBot:
    def __init__(self):
        # Read log info from text file
        with open("login_info.txt", "r") as log:
            info = log.readlines()
            # Read all needed info from text file
            self.login_info = list(map(lambda x: x.split(":")[1][1:].replace("\n", ""), info))

        self.client = None

    def log_in(self):
        try:
            # Initialize reddit client and use all the predefined variables
            self.client = Reddit(
                    username=self.login_info[0],
                    password=self.login_info[1],
                    user_agent=self.login_info[2],
                    client_secret=self.login_info[3],
                    client_id=self.login_info[4],
                                )

            self.client.user.me()
            return self.client

        except exceptions.OAuthException:
            raise ValueError("Something went wrong with logging into reddit engine \nCredentials not right...")

    def get_top_post(self, limit=1):
        top_posts = self.client.subreddit("ProgrammerHumor").top(time_filter="week", limit=limit)

        posts = []
        for post in top_posts:
            posts.append((post.title, post.url))

        return posts

    @staticmethod
    def download_image(url, name):
        if url.endswith(("jpg", "png", "jpeg")):
            req = r.get(url, allow_redirects=False)
            open(name, 'wb').write(req.content)
        else:
            print("Unknown filetype")


if __name__ == "__main__":
    client = RedditBot()
    client.log_in()
    submissions = client.get_top_post()
    post_url = submissions[0][1]
    client.download_image(post_url, "Test1.png")
