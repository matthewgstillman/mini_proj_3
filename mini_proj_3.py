#Mini Project #3 (BONUS. Up to 3 points)
#Due Date: 11/29
#Your program will read in an article called article.txt.
#It will perform the following tasks
#It will read an article and build a dictionary such as the word_count dictionary below:
#word_count = {
#"the": 50,
#"a": 20,
#...
#...
#}
#Use a function build_dict, which takes in an article and returns a dictionary
#def build_dict (my_dict, article):
def build_dict (article):
    article = open('article.txt', "r")

    with open("article.txt") as oa:
        # article_dict = {
        # }
        # my_dict = article_dict
        word_count = 0
        character_count = 0
        most_frequent = 0
        lines = oa.readlines()
        for i in lines:
            words = i.split()
            for i in words:
                i = i.lower()

                if '"' in i:
                    quotation_index = i.index('"')
                    print("Quotation Index: {}".format(quotation_index))
                    i = i.strip('"')
                    print("i IS NOW EQUAL TO: {}".format(i))
                    if i not in article_dict.keys():
                        article_dict[i] = 1
                        if 'quotation_marks' not in article_dict.keys():
                            article_dict['quotation_marks'] = 1
                        else:
                            article_dict['quotation_marks'] += 1
                    else:
                        article_dict[i] += 1
                        if 'quotation_marks' not in article_dict.keys():
                            article_dict['quotation_marks'] = 1
                        else:
                            article_dict['quotation_marks'] += 1

                elif "," in i:
                    comma_index = i.index(",")
                    print("Comma Index: {}".format(comma_index))
                    i = i.strip(',')
                    print("i IS NOW EQUAL TO: {}".format(i))
                    if i not in article_dict.keys():
                        article_dict[i] = 1
                        if 'commas' not in article_dict.keys():
                            article_dict['commas'] = 1
                        else:
                            article_dict['commas'] += 1
                    else:
                        article_dict[i] += 1
                        if 'commas' not in article_dict.keys():
                            article_dict['commas'] = 1
                        else:
                            article_dict['commas'] += 1

                elif "." in i:
                    print("i = {}".format(i))
                    period_index = i.index(".")
                    print("Period Index: {}".format(period_index))
                    i = i.strip('.')
                    print("i IS NOW EQUAL TO: {}".format(i))
                    if i not in article_dict.keys():
                        article_dict[i] = 1
                        if 'periods' not in article_dict.keys():
                            article_dict['periods'] = 1
                        else:
                            article_dict['periods'] += 1
                    else:
                        article_dict[i] += 1
                        if 'periods' not in article_dict.keys():
                            article_dict['periods'] = 1
                        else:
                            article_dict['periods'] += 1


                elif ',"' in i:
                    comma_index = i.index(",")
                    print("Comma Index: {}".format(comma_index))
                    i = i.strip(',')
                    print("i IS NOW EQUAL TO: {}".format(i))
                    if i not in article_dict.keys():
                        article_dict[i] = 1
                        if 'commas' not in article_dict.keys():
                            article_dict['commas'] = 1
                        else:
                            article_dict['commas'] += 1
                    else:
                        article_dict[i] += 1
                        if 'commas' not in article_dict.keys():
                            article_dict['commas'] = 1
                        else:
                            article_dict['commas'] += 1
                    
                    i = i.strip('"')
                    print("i IS NOW EQUAL TO: {}".format(i))
                    if i not in article_dict.keys():
                        article_dict[i] = 1
                        if 'quotation_marks' not in article_dict.keys():
                            article_dict['quotation_marks'] = 1
                        else:
                            article_dict['quotation_marks'] += 1
                    else:
                        article_dict[i] += 1
                        if 'quotation_marks' not in article_dict.keys():
                            article_dict['quotation_marks'] = 1
                        else:
                            article_dict['quotation_marks'] += 1
                
                else:
                    print("i = {}".format(i))
                    if i not in article_dict.keys():
                        article_dict[i] = 1
                        if i not in article_dict.keys():
                            article_dict[i] = 1
                        else:
                            article_dict[i] += 1
                    else:
                        article_dict[i] += 1
                        if 'periods' not in article_dict.keys():
                            article_dict[i] = 1
                        else:
                            article_dict[i] += 1
        
        # for key, value in article_dict.items():
        #     print("Key: {} - Value: {}".format(key.title(), value))

        for key, value in article_dict.items():
            key_length = len(key)
            print("Key: {}, Key Length: {}".format(key.title(), key_length))
            word_count += 1
            character_count += int(key_length) * value
            print(value)
            average_length = int(character_count) / int(word_count)

        print(article_dict.items())
        print("Character Count: {}".format(character_count))
        print("Word Count: {}".format(word_count))
        print("Average Length: {}".format(average_length))
        my_dict = article_dict
        print("my_dict: {}".format(my_dict))
        return article_dict

                
build_dict("article.txt")



