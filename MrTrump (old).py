import praw
#get_reddit_agent links to my script on reddit
def get_reddit_agent(user_agent, client_id, client_secret, redirect='https://127.0.0.1'):
    reddit_agent = praw.Reddit(user_agent = "Trump's World", client_id = client_id, client_secret = client_secret)
    reddit_agent.set_oauth_app_info(client_id = client_id,
                            client_secret = client_secret,
                            redirect_uri = redirect)
    
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
    client_id = 'IswqHyud5J7X7g'
    client_secret = 'bCp0DAF1-alofK6plKe1AEwhRYUQ'
    reddit_agent = get_reddit_agent("Trump's World", client_id, client_secret)
    #list of political subreddits
    trump_subreddits = ['The_Donald', 'EnoughtTrumpSpam', 'politics', 'news', 'hillaryclinton', 'worldpolitics']
    #keep track of comments containing Trump
    trump_comments = []
    for subreddit in trump_subreddits:
        get_sub_comments(reddit_agent, subreddit, trump_comments, count = (1000 / len(trump_reddits)))
    trumpsub_trump, trumpsub_words = trump_count(trump_comments)
    #global sample
    world_comments = []
    get_subreddit_comments(reddit_agent, 'all', world_comments, count = 1000)
    world_trump, world_words = trump_count(world_coments)
    print("Trump subreddits: {} / {} = {} \n World: {} / {} = {}".format(trumpsub_trump, trumpsub_words, ((float(trumpsub_trump) / trumpsub_Words) * 100), world_trump, world_words, ((float(world_trump) / world_words) * 100)))
