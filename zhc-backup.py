from zhihu_oauth import ZhihuClient
from zhihu_oauth import zhcls
from multiprocessing.dummy import Pool as ThreadPool
import argparse
import os


def do_download(answer):
    name = answer.question.title + ' - ' + answer.author.name
    print('Now backing up: ' + name)
    answer.save(collection_id, str(answer.id))


def do_upload(answer_id):
    print("Now restoring: " + answer_id + " to " + collection_id)
    answer = client.answer(int(answer_id))
    me.collect(answer, collection, True)


def get_collections():
    return os.listdir()


def get_answers():
    return os.listdir(collection_id)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--collection", "-c", help="Set collection ID, e.g. 99549491")
    parser.add_argument("--thread", "-t", help="(Optional) Set the threads, 3 to 7 is recommended, default value is 5.")
    parser.add_argument("--upload", "-u", action='store_true', help="Upload the answers to Zhihu.")
    parser.add_argument("--download", "-d", action='store_true', help="Download the answers from Zhihu.")

    global client
    client = ZhihuClient()
    client.login_in_terminal()
    me = client.me()

    args = parser.parse_args()

    if args.collection:
        print("Selected collection: ", str(args.collection))
        collection = client.collection(int(args.collection))
        global collection_id
        collection_id = str(collection.id)
    else:
        print("YOU MUST TELL ME WHICH COLLECTION YOU WANT TO ADD IN!!")
        exit()

    if args.thread:
        print("Thread amount: ", str(args.thread))
        pool = ThreadPool(int(args.thread))
    else:
        print("Thread amount: 5 (DEFAULT)")
        pool = ThreadPool(5)

    if args.upload:
        pool.map(do_upload, get_answers)
        pool.close()
        pool.join()

    if args.download:
        print("Mode: Download (Backup)")
        answers = collection.answers
        print("Initializing...")
        pool.map(do_download, answers)
        pool.close()
        pool.join()
