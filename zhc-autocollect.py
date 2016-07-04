from zhihu_oauth import ZhihuClient
from zhihu_oauth import zhcls
from multiprocessing.dummy import Pool as ThreadPool
import argparse


def do_check(following):
    print("Follower ID: ", following.id)
    people = client.people(following.id)
    ActType = zhcls.activity.ActType
    for act in people.activities:
        answer = act.target
        if (act.type == ActType.CREATE_ANSWER) or (act.type == ActType.VOTEUP_ANSWER):
            answer_content = str(answer.content)
            for content in keyword_contents:
                # print("Searching for: ", content)
                if answer_content.find(content) != -1:
                    print("Found ", answer.author.name, "'s answer ID:", answer.id, ", with keyword ",
                          content)
                    me.collect(answer, collection, True)
                    answer_id = str(act.target.id)
                    answer.save(answer.author.name, answer_id)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--collection", "-c", help="Set collection ID, e.g. 99549491")
    parser.add_argument("--thread","-t", help="Set the threads, 3 to 7 is recommended, default value is 5.")

    client = ZhihuClient()
    client.login_in_terminal()

    me = client.me()

    args = parser.parse_args()
    if args.collection:
        print("Selected collection: ", str(args.collection))
        collection = client.collection(int(args.collection))
    else:
        print("YOU MUST TELL ME WHICH COLLECTION YOU WANT TO ADD IN!!")
        exit()

    if args.thread:
        print("Thread amount: ", str(args.thread))
        pool = ThreadPool(int(args.thread))
    else:
        print("Thread amount: 5 (DEFAULT)")
        pool = ThreadPool(5)

    keyword_file = 'keyword.txt'

    with open(keyword_file) as f:
        keyword_contents = f.read().splitlines()



    print("Name:", me.name)
    print("\n\n", "Keywords are:\n\n")
    print(keyword_contents)

    print("\n\n")

    pool.map(do_check, me.followings)
    pool.close()
    pool.join()
    print("All questions has been downloaded as HTML documents and added to collection.")
