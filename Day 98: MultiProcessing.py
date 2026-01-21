import multiprocessing
import requests
import concurrent.futures


def downloadFile(url, name):
    print(f"Started downloading{name}")
    resoponse = requests.get(url)
    open(f"photo/photo{name}.jpg", "wb").write(resoponse.content)
    print(f"Finished downloading{name}")


if __name__ == "__main__":
    url = "https://picsum.photos/200/300"
    # process = []
    # for i in range(50):
    #     # downloadFile(url, i)
    #     p = multiprocessing.Process(target=downloadFile, args=[url, i])
    #     p.start()
    #     process.append(p)

    # for p in process:
    #     p.join()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        l1 = [url for i in range(60)]
        l2 = [i for i in range(60)]
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            print(r)
