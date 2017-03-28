''''

Hacker rank question to find answers given questions
url:-https://www.hackerrank.com/challenges/matching-questions-answers
'''

import fileinput
import string
import re
import sys
import os

stop_words = [u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own', u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now']

question_words = ['which','what','who','how']
stop_words.extend(question_words)

#### Find the ratio of count of common words between 2 sentences
def similarity(sentence1,sentence2):
    sentence1_set = set(sentence1.split(" "))
    sentence2_set = set(sentence2.split(" "))
    score = float(len(sentence1_set.intersection(sentence2_set)))/len(sentence2_set)
    return score


def parse_input():
    ### Extract paragraph , questions and  answers
    file_path = os.getcwd()
    print(file_path)
    file_name = '\data\MatchingQuestions.txt'
    f = open( file_path + file_name, 'r')
    i = -1
    questions = list()
    for lines in f:
        if i == -1 :
            sentences = [x.replace("\n" , "").lower() for x in lines.split(".")]
            i += 1
        else:
            questions.append(lines.replace("\n" , "").lower())
    answers =  questions[-1] # answer list
    questions.remove(answers) # Quations List
    answers_set = answers.split(";")
    #print(answers_set)

    ## Process Questions and Answers : remove stop words
    processed_questions = list()
    processed_answers = list()
    for question in questions:
        temp_string = " ".join([x.lower() for x in question.split(" ") if x.lower() not in stop_words])
        processed_questions.append(re.sub("[^a-zA-Z]"," ",temp_string))

    for answer in answers_set:
        temp_string = " ".join([x.lower() for x in answer.split(" ") if x.lower() not in stop_words])
        processed_answers.append(re.sub("[^a-zA-Z]"," ",temp_string))

    return(processed_questions , processed_answers , sentences , questions , answers_set)



def main():
    processed_questions , processed_answers , sentences , questions , answers_set = parse_input()
    # find similar matching pair of question and answers
    match = {}
    for each_question in range(len(processed_questions)):
        max_similarity = 0
        for each_answer in range(len(processed_answers)):
            for each_sentence in sentences:
                # calculate similarity
                similarity_temp = similarity(each_sentence , processed_questions[each_question]) * similarity(each_sentence , processed_answers[each_answer])
                if similarity_temp > max_similarity:
                    max_similarity = similarity_temp
                    match[each_question] = each_answer
                    #print(max_similarity)
    print(questions)
    ##### print the  matching Pair
    for i in range(len(questions)):
        print(answers_set[match[i]])

if __name__ == '__main__':
    main()