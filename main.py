word = 'lesson'
word_ch = list(word)
ans = []
put = ''
while word != ''.join(ans):
    put = input()
    if len(ans) == len(word):
         for i in range(len(word)):
            if word_ch[i] == put:
                 ans[i] = word_ch[i]
            else:
                pass
    elif len(ans) != len(word):
        for i in range(len(word)):
            if word_ch[i] == put:
                ans.insert(i,word_ch[i])
            else:
                ans.insert(i,'*')
    print(''.join(ans))
print('win')
