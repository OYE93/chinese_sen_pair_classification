from bert_serving.client import BertClient
from sklearn.metrics.pairwise import cosine_similarity

# start the bert_as_service client
bc = BertClient()


def bert_embedding_cos_similarity(sen_pair):
    embedding_pair = bc.encode(sen_pair)
    cos_similarity = cosine_similarity([embedding_pair[0]], [embedding_pair[1]])
    return cos_similarity


def main():
    sen_pair = ['糖尿病吃什么？',
                '糖尿病的食谱？']
    sen_pair = ['乙肝小三阳的危害？',
                '乙肝大三阳的危害？']
    print(bert_embedding_cos_similarity(sen_pair))


if __name__ == '__main__':
    main()