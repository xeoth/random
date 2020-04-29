from random import randint

copypasta = 'put the text here'

spongebobed_copypasta = ''

# generating the sPongEboB spEEcH
for i in range(len(copypasta)):
    if randint(0, 1) == 0:
        spongebobed_copypasta += copypasta[i].upper()
    else:
        spongebobed_copypasta += copypasta[i].lower()

# adding several !/1 for extra dramatism
for i in range(randint(2, 8)):
    if randint(0, 1) == 0:
        spongebobed_copypasta += '!'
    else:
        spongebobed_copypasta += '1'


print(spongebobed_copypasta)
