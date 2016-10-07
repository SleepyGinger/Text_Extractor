Use the below commands to make use of the core code

#reads urls in current.csv
df=pd.read_csv('current.csv')

#appends text to csv
text_list=[]
for link in df['url']:

    text=get_content(link)
    
        text_list.append(text)

df['text'] = text_list

#finds words of interest and counts frequencies
count_list=[]
for words in df['text']:

    word_count=freq_count('TEXT', words)

count_list.append(word_count)

df['frequency count'] = count_list

#finds words of interests and surrounding words
abridged=short_text(df,'TEXT')

df['abridged']=abridged

#puts it all into a csv
df.to_csv('current_text.csv')
