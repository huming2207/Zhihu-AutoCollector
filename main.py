from zhihu_oauth import ZhihuClient
from zhihu_oauth import zhcls
from multiprocessing.dummy import Pool as ThreadPool

keyword_file = 'keyword.txt'

with open(keyword_file) as f:
    keyword_contents = f.read().splitlines()
pool = ThreadPool(7)


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
    client = ZhihuClient()
    client.login_in_terminal()

    me = client.me()
    collection = client.collection(99549491)

    print("Name:", me.name)
    print("\n\n", "Keywords are:\n\n")
    print(keyword_contents)

    print("\n\n")

    pool.map(do_check, me.followings)
    pool.close()
    pool.join()
    print("All questions has been downloaded as HTML documents and added to collection.")
