import praw
#get_reddit_agent links to my script on reddit
def get_reddit_agent(user_agent, client_id, client_secret, redirect='https://127.0.0.1'):
    reddit_agent = praw.Reddit(client_id = client_id, client_secret = client_secret, user_agent = "Trump's World", username = 'redditbot333', password = 'hotbot333')
    return reddit_agent


def get_sub_comments(reddit_agent, subreddit, commments = [], count = 200):
    #extract comments from specific subreddits
    try:
        sub = reddit_agent.get_subreddit(subreddit)
        comments_raw = sub.get_comments(sub, limit=count)
        comments_flat = praw.helpers.flatten_tree(comments_raw)
        for comment in comments_flat:
            #try catches any null comments
            try:
                #check if there are any replies to the comment
                if hasattr(comment, 'comments'):
                    for reply in comment.comments:
                        comments_out.append(reply.body)
                else:
                    commnts_out.append(comment.body)
            except:
                pass
    except:
        pass

def trump_count(comment_list):
    trump_count = 0
    word_count = 0
    #count total words and times trump is mentioned
    for comments in comment_list:
        words = comment.split(' ')
        for i in words:
            if i.lower() == 'donald' or 'trump':
                trump_count += 1
            word_count += 1
    return trump_count, word_count

if __name__ == '__main__':
    client_id = 'gpVF2dKDnikxrA'
    client_secret = 'mQjr46anmuO48UsuXFr-lb4WyPE'
    reddit_agent = get_reddit_agent("Trump's World", client_id, client_secret)
    #list of political subreddits
    trump_subreddits = ['The_Donald', 'EnoughtTrumpSpam', 'politics', 'news', 'hillaryclinton', 'worldpolitics']
    #keep track of comments containing Trump
    trump_comments = []
    for subreddit in trump_subreddits:
            for comment in reddit_agent.subreddit(subreddit).stream.comments():
                trump_comments.append(comment)
    trumpsub_trump, trumpsub_words = trump_count(trump_comments)
    print(trumpsub_trump)
    #global sample
    world_comments = []
    get_sub_comments(reddit_agent, 'all', world_comments, count = 1000)
    world_trump, world_words = trump_count(world_comments)
    print("Trump subreddits: {} / {} = {} \n World: {} / {} = {}".format(trumpsub_trump, trumpsub_words,
    ((float(trumpsub_trump) / trumpsub_words) * 100), world_trump, world_words, ((float(world_trump) / world_words) * 100)))
