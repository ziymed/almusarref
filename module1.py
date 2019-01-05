from arabic_const import*
word=u"آجر"
if word.startswith(ALEF_MADDA):
    word=HAMZA+FATHA+HAMZA+SUKUN+word[1:];
print word;