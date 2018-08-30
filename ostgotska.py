line = input()
list_words = line.split()
number_of_words = len(list_words)
count = 0
#number of words that contain 'ae':
for word in list_words:
    if 'ae' in word:
        count += 1
#ratio of words that contain 'ae':
ratio = count / number_of_words
if ratio >= 0.4:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')