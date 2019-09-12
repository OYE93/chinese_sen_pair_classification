import jieba

word_list_file = "./knowledge/THUOCL_medical.txt"
jieba.load_userdict(word_list_file)
word_list = jieba.cut("洋地黄毒苷注射液中心吃什么？糖尿病的食谱？问句1：乙肝小三阳的危害？问句2：乙肝大三阳的危害？")
print("/".join(word_list))
