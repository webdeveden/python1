#field service report

text= 'Field servcice report'
print(text.upper())

def report():
    date= input('Date:')
    hour= input('Hours:')
    pl= input('Placement:')
    vd= input('Videos:')
    vt= input('Visits:')
    cmt= input('Comments:')
    print('-----------------------')
    print(hour,'|',pl,'|',vd,'|',vt)
report()

text = "X-DSPAM-Confidence:    0.8475"
pos= text.find('C')
rt= text[pos+5:]
print(rt)
