# a copy

text = "X-DSPAM-Confidence:    0.8475"
pos= text.find(':')
host= text[pos+5:]
value= float(host)
print(host)
